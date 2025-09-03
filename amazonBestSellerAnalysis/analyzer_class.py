# Importing the Pandas library
import pandas as pd

# Creating the Analyzer Class
class Analyzer:

    # Initializing the Class and DataFrame
    def __init__(self, file_path):
        # Loading the CSV File
        self.df = pd.read_csv(file_path)

    # This method returns the First 5 Rows of the Spreadsheet
    def get_header(self):
        return self.df.head()

    # This method returns the Columns in the Spreadsheet
    def get_columns(self):
        return self.df.columns

    # This method returns the Shape of the Spreadsheet
    def get_shape(self):
        return self.df.shape
    
    # This method gets a Summary statistics for each column
    def get_description(self):
        return self.df.describe()
    
    # This method drops all the duplicate data from the DataFrame
    def drop_duplicate_data(self):
        self.df.drop_duplicates(inplace=True)

    # This method renames the Columns of the DataFrame
    def rename_columns(self, renamed_columns):
        self.df.rename(columns=renamed_columns, inplace=True)

    # This method converts datatypes from int to float
    def convertDataType(self):
        self.df["Price"] = self.df["Price"].astype(float)

# Runs the Program if it this Program is Ran
if __name__ == "__main__":
    an = Analyzer("bestsellers.csv")
    
    # Testing Each Get Methods

    ## Using the Get Header Method
    print("\n", an.get_header(), "\n")

    ## Using the Get Shape Method
    print("\n", an.get_shape(), "\n")

    ## Using the Get Columns Method
    print("\n", an.get_columns(), "\n")

    ## Using the Get Columns Method
    print("\n", an.get_description(), "\n")

    ## Duplicate Cleansing
    an.drop_duplicate_data()
    print("\n", an.get_description(), "\n")

    # Renaming the Column Names
    an.rename_columns({"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"})
    print("\n", an.get_columns(), "\n")

    # Changing the Datatype to Float
    an.convertDataType()
    print("\n", an.get_header(), "\n")
