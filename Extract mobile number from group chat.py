


# check directory to change to your desired location
#import os
#os.getcwd()


# function to extract numbers below

def whatsapp_number_extraction(fileName) : 
    import numpy as np
    import pandas as pd
    
    dataframe_input = pd.read_excel(fileName)
#    print(dataframe_input.shape)
#    dataframe_input.head()
    
    
    # Taking only relevent chat column which is first column
    
    df = dataframe_input.iloc[:, 0].to_frame()
    df.columns = ["Chat Data"]
        
    
    # dropping rows that are blank
    
    df.dropna(inplace = True)
    
   
    # converting dataset to string format so that we can do splitting on the basis of "+91"
    
    df["Chat Data"] = df["Chat Data"].apply(str)
    
    # checking the information for datatype
    #df.info()
       
    
    # funtion to get mobile number digits column 
    
    def get_digits(rowValue):
        digits_taken = ""
        if "+91" in rowValue : 
            split_with_plus_sign = rowValue.split("+")
    
            for c in split_with_plus_sign[1] : 
                if not(c.isalpha()) :
                    digits_taken += c
                else :
                    break
        else : 
            digits_taken = ""
        
        return digits_taken
    
    df["digit col"] = df['Chat Data'].apply(get_digits)
    
    # after getting sepearte mobile number digits column, it was found that it 
    # containes non - alphanumerics so a seperate function is created to remove them. 
    
    
    
    # function to remove non - alphanumerics
    
    def get_number(rowValue):
        mobile_number = ""
        for c in rowValue : 
            if c.isdigit() :
                mobile_number += c
            elif c.isspace() : 
                mobile_number += c
            else :
                break
        return mobile_number.strip()
    
    df['digit col'] = df['digit col'].apply(get_number)

    
    # creating a function to convert mobile numbers greater than 10 to Indian mobile numbers with '+' sign,
    # else put a NaN value so that we can drop it
    
    for r in range(df.shape[0]) : 
        if len(df.iloc[r, 1]) < 10 : 
            df.iloc[r, 1] = np.nan
        else : 
            df.iloc[r, 1].strip()
            df.iloc[r, 1] = "+" + df.iloc[r, 1] 
    
    
    # dropping NaN values, which were rows having length less than 10 digits
    df_final = df["digit col"]
    
    df_final.dropna(inplace = True)
    
    # checking shape and head for only mobile number dataFrame
    
    mobile_dataframe = df_final.to_frame()   
    mobile_dataframe.drop_duplicates(inplace = True)     
    mobile_dataframe.to_csv("mobileNumbers.csv")
    



######### Run below code ###########

# taking the excel file after converting text email file to excel

fileName = "Extract mobile number from group chat"
fileName = fileName + ".xlsx"

whatsapp_number_extraction(fileName)

