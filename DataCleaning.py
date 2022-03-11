# clean the data
# cleaning the data involves determining if the data is valid or not
# removing the whitespace in the bank name
# and generating a new table with the valid data and updated fields that will be in the csv file


def clean_data(data):
    # loop through the data to clean the data
    for current_row in range(len(data)):
        # get name1 and name2 of the acount
        name1 = data["name1"][current_row]
        name2 = data["name2"][current_row]

        # get the notes
        notes = data["notes"][current_row]

        # get the bank name
        bank_name = data['bankName'][current_row]

        # get fieds required to determine if the record is valid or not
        iban_number = data["ibanNumber"][current_row]
        sort_code = data["sortCode"][current_row]
        account_number = data["accountNumber"][current_row]
        unstructured_account_number = data["unstructuredAccountNumber"][current_row]

        # set variable to check if the record is valid or not
        # and check if record is valid or not
        valid_record = False
        iban_number_is_provided = len(iban_number) > 0
        sort_code_is_provided = len(sort_code) > 0
        account_number_is_provided = len(account_number) > 0
        unstructured_account_number_is_provided = len(unstructured_account_number) > 0

        if iban_number_is_provided or (sort_code_is_provided and account_number_is_provided) or unstructured_account_number_is_provided:
            valid_record = True
        

        # if the record is invalid, remove it from the data
        if valid_record == False:
            print("Removing invalid record: " + str(current_row))
            data = data.drop(data.index[current_row])
            
        # split the bank name into an array containing 
        # the bank name and the country code, i.e [bank_name, country_code]
        bank_name_array = bank_name.split('-')
        # get the bank name and remove the whitespace
        bank_name = bank_name_array[0].strip()
        # get the country code
        country_code = bank_name_array[1]
        # update the bank name in the data
        data["bankName"][current_row] = bank_name
        data["branchCountry"][current_row] =  country_code

        
        # set the account number type and update the account_number field
        if iban_number_is_provided:
            data["accountNumberType"][current_row] = "iban"
            data["accountNumber"][current_row] = iban_number
        elif sort_code_is_provided and account_number_is_provided:
            data["accountNumberType"][current_row] = "gbDomestic"
            data["accountNumber"][current_row] = sort_code + account_number
        elif unstructured_account_number_is_provided:
            data["accountNumberType"][current_row] = "unstructured"
            data["accountNumber"][current_row] = unstructured_account_number

        
        # set the value of the name1AndName2 field
        data["name1AndName2"][current_row] = name1[0:30] + " " + name2[0:20]

        # set the value of the comments field 
        # and remove the non ascii characters
        data["comments"][current_row] = notes[0:30].encode('ascii', 'ignore')
        

    # return cleaned data
    return data



def generate_csv_file(data,output_file_name):
    # remove fields that are not required to be in the csv file
    data = data.drop(columns=["ibanNumber", "sortCode", "unstructuredAccountNumber", "name1", "name2", "notes"])
    # generate a csv file with the cleaned data
    data.to_csv(output_file_name, index=False)

    # return data with the fields that are required to be in the csv file
    return data