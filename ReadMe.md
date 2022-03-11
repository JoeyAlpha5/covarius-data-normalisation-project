# Covarius data normalisation project

This documentation provides a breakdown of the Covarius data normalisation app. This is a Python cli application that takes json data and then processes the data to generate a csv file.

Use [this Jupyter notebook](https://github.com/JoeyAlpha5/covarius-data-normalisation-project/blob/development/Data%20Normalisation%20App.ipynb) to view the format of the input and output data along with the steps taken to generate the required output file.

Use the sections listed below to get started with running the application on your machine. 


## Documentation sections
- [Setting up the app](#setting-up-the-app)
- [Third party libraries and packages used](#third-party-libraries)
- [Application preview](#application-preview)
- [Future improvements](#future-improvement)


### Setting up the app

1. To get started, clone this repository using the following git command
```
git clone https://github.com/JoeyAlpha5/covarius-data-normalisation-project.git
```

2. Once the repo has been cloned, in your terminal cd into the project folder, make sure you're working in the development branch and have python installed on your machine. Run the command below to install all the required packages and libraries

```
pip install -r requirements.txt
```

3. You can then run the application by running the following command in the terminal passing along the following two parameters: 

- json_input_file.json. Name of the json file that contains the input data. This file must be in the parent directory of this project.

- output_csv_file.csv. The name of the csv file to contain the output data. The file can be found in the parent directory of this project once it has been generated.


```
python terminal_app.py json_input_file.json output_csv_file.csv
```

### Third party libraries

This section lists all the third party libraries and dependencies that have been used and the reasons for including them. All the required third party libararies have been listed in [this requirements.txt](https://github.com/JoeyAlpha5/covarius-data-normalisation-project/blob/development/requirements.txt) file.

1. [Pandas](https://pandas.pydata.org/). Pandas provides a quick and easy way to analyse & manipulate the data and  visualise the data in the Jupyter notebook.
2. [typer](https://typer.tiangolo.com/). This python library has been used to build the cli application.


### Future Improvements

The current application is far from perfect. The [clean_data](https://github.com/JoeyAlpha5/covarius-data-normalisation-project/blob/development/DataCleaning.py) function could be broken up into smaller functions which would make the code more readable and easier to maintain as the application gets more complex, for example determining whether a record is valid or not could be a function.

Running the current application on a different machine might present a few issues especially if python is not installed on the machine. Containerising the application using Docker would solve this issue, however I'm not too familiar with Docker yet to set that up, alternatively python can be downloaded and installed on the machine from [this](https://www.python.org/downloads/) site.