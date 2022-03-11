import pandas as pd 
import os
import typer
from DataCleaning import clean_data, generate_csv_file


# function that will run when 
# python terminal_app.py is run in the terminal
def main(input_file_name,output_file_name):
    # raw data path
    json_data_file = input_file_name
    # json full file path
    file_path = os.path.abspath(json_data_file)
    # read json data
    data = pd.read_json(file_path)

    # add additional fields required in the csv file
    data["branchCountry"] = ""
    data["accountNumberType"] = ""
    data["name1AndName2"] = ""
    data["comments"] = ""
    data[""] = ""
    # clean the data
    cleaned_data = clean_data(data)

    # generate and display the csv data
    csv_data = generate_csv_file(cleaned_data, output_file_name)
    csv_data.head(30)


if __name__ == "__main__":
    typer.run(main)