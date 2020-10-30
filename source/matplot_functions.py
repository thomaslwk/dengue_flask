import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import pandas
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def import_csv(filename):
    """
    The function to import csv files and be accessed by the developer through this program.

    Parameters:
        filename(str): The file that needs to be read.

    Returns:
        overall_dataset (DataFrame): A dataframe type data that can be transformed into
        tables / charts depending on the user, through the use of pandas library.
    """
    # pointing to the file location
    filename = "source/dengue_data"
    # This will perform the reading of the file and assigning the data inside to a variable
    overall_dataset = pd.read_csv(filename)
    # returns the data in the file as a DataFrame type
    return overall_dataset


def total_case_per_month(dataset):
    """
    This function will filter the dataset and return all the values when the column "Case per Month"
    is not null.

    Parameters:
    dataset (DataFrame): This will be the output after using import csv.

    Returns:
        dataset[cases_per_month] (DataFrame): This is the filtered data which consists of the entire dataset when
        the Case per Month column is not empty.
    """
    # this will remove all the rows where the values are empty
    cases_per_month = pd.notnull(dataset["Case per Month"])
    # returns the first row of each month for every month
    return dataset[cases_per_month]


def cases_per_month_for_choice_year(dataset, year_choice):
    """
        This function will filter the dataset input and

        Parameters:
            dataset (DataFrame): This will be the output after using import csv.
            year_choice (int): The chosen year to filter the dataset

        Returns:
            total_months.loc[:, ["Case per Month"]] (DataFrame):
                Returns the number of cases each month for the chosen year.
    """
    # Choosing all the data from a specific year
    months_year = dataset[dataset["Year"] == int(year_choice)]
    # Remove the duplicate months that contains no data in "Case per Month" column
    total_months = months_year.drop_duplicates(subset="Month", keep="first")
    # Returns the entire data set without the rows that have been dropped
    return total_months.loc[:, ["Case per Month"]]


def df_to_list(dataset):
    """
        This function will convert the datatype of the input to a list.

        Parameter:
            dataset (DataFrame): This is a filtered data.

        Returns:
                dataset.values.tolist() (list): Returns a list of values that were passed through.
    """
    # Converts the input into a list
    return dataset.values.tolist()


def weeks(dataset):
    """
    This function is to filter and retrieve the total number of unique weeks in the data set.

    Parameters:
        dataset (DataFrame): This is a filtered data set after reading the CSV

    Returns:
        total_months.loc[:, ["Week"]] (DataFrame): This will return all unique weeks there are in the column "Week"
    """
    # To filter and get all 12 months to remove any duplicate after identifying the first month
    total_months = dataset.drop_duplicates(subset="Week", keep="first")
    # print(total_months)
    return total_months.loc[:, ["Week"]]


def months(dataset):
    """
        This function is to filter and retrieve the total number of unique months in the data set.

        Parameters:
            dataset (DataFrame): This is a filtered data set after reading the CSV

        Returns:
            total_months.loc[:, ["Month"]] (DataFrame): This will return all unique years there are in the column "Month"
    """
    # To filter and get all 12 months while removing any duplicate after identifying the first month
    total_months = dataset.drop_duplicates(subset="Month", keep="first")
    # Returns only the Month column
    return total_months.loc[:, ["Month"]]


def years(dataset):
    """
        This function is to filter and retrieve the total number of unique years in the data set.

        Parameters:
            dataset (DataFrame): This is a filtered data set after reading the CSV

        Returns:
            total_months.loc[:, ["Year"]] (DataFrame): This will return all unique years there are in the column "Year"
    """

    # To remove any duplicate years and only keeping the first identified value
    total_months = dataset.drop_duplicates(subset="Year", keep="first")
    # Returns only the Year column
    return total_months.loc[:, ["Year"]]


def rainfall_per_month_for_choice_year(dataset, year_choice):
    """
        This function will filter the dataset input and return the
        amount of rainfall  for the chosen year

        Parameters:
            dataset (DataFrame): This will be the output after using import csv.
            year_choice (int): The chosen year to filter the dataset

        Returns:
            months_year.loc[:, "Total_Rainfall"] (DataFrame):
                Returns the amount of rainfall each month for the chosen year.
    """
    # Reads the CSV and assigning its data to a variable
    rainfall_data = pandas.read_csv("source/dengue_data/RainfallData.csv")
    # Getting the all the rainfall amount for each month from selected year
    rcases = cases_per_month_for_choice_year(rainfall_data, year_choice)
    # Choosing all the data from a specific year
    months_year = dataset[dataset["Year"] == int(year_choice)]
    # Converting the filtered data set to a list
    no_dcases = df_to_list(rcases)
    # Plotting the dataset into the graph
    plt.plot(months, no_dcases, color='red')
    # Indicating the label for the X Axis
    plt.xlabel('Yearly Data')
    # Indicating the label for the Y Axis
    plt.ylabel('Number of Cases')
    # Indicating the Title of the chart
    plt.title('Total Number of Dengue Cases In Singapore, %s' % str(year_choice))
    # A legend for the chart
    red_patch = mpatches.Patch(color='red', label=str(year_choice))
    # Inserting the legend into the chart
    plt.legend(handles=[red_patch])
    # Save the chart as a svg
    plt.savefig('flaskr/static/images/Dengue_Cases_%s.svg' % str(year_choice), bbox_inches="tight")
    # Save the chart as a png
    plt.savefig('flaskr/static/images/Dengue_Cases_%s.png' % str(year_choice), bbox_inches="tight")
    return months_year.loc[:, "Total_Rainfall"]


def dengue_cases_chart(year_choice):
    """
        This function will produce a chart that shows the number of cases in a given year

        Parameter:
            year_choice (int): This will be the year that the will determine what data is being filtered for the chart

        Returns:
            Chart: This will display a chart and save it as a png in the local folder.
    """
    # Reads the CSV and assigning its data to a variable
    dengue_data = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
    # Getting the all the dengue cases for each month from selected year
    dcases = cases_per_month_for_choice_year(dengue_data, year_choice)
    # A list of the months in a year used as the X axis label
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Converting the filtered data set to a list
    no_dcases = df_to_list(dcases)
    # Plotting the dataset into the graph
    plt.plot(months, no_dcases, color='red')
    # Indicating the label for the X Axis
    plt.xlabel('Yearly Data')
    # Indicating the label for the Y Axis
    plt.ylabel('Number of Cases')
    # Indicating the Title of the chart
    plt.title('Total Number of Dengue Cases In Singapore, %s' % str(year_choice))
    # A legend for the chart
    red_patch = mpatches.Patch(color='red', label=str(year_choice))
    # Inserting the legend into the chart
    plt.legend(handles=[red_patch])
    # Save the chart as a svg
    plt.savefig('flaskr/static/images/Dengue_Cases_%s.svg' % str(year_choice), bbox_inches="tight")
    # Save the chart as a png
    plt.savefig('flaskr/static/images/Dengue_Cases_%s.png' % str(year_choice), bbox_inches="tight")


def overall_dengue_cases_chart():
    """
        This function will display all the data into a chart and saves it as a png and svg file.
    """
    # Reads the csv file and saves its data into a variable
    dengue_data = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
    # Getting the number of cases for each month by selected year
    dcases_2014 = cases_per_month_for_choice_year(dengue_data, 2014)
    dcases_2015 = cases_per_month_for_choice_year(dengue_data, 2015)
    dcases_2016 = cases_per_month_for_choice_year(dengue_data, 2016)
    dcases_2017 = cases_per_month_for_choice_year(dengue_data, 2017)
    dcases_2018 = cases_per_month_for_choice_year(dengue_data, 2018)
    dcases_2019 = cases_per_month_for_choice_year(dengue_data, 2019)
    # Creating the list that will be displayed as the X axis ticker
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Converting the filtered data into a list
    no_dcases_2014 = df_to_list(dcases_2014)
    no_dcases_2015 = df_to_list(dcases_2015)
    no_dcases_2016 = df_to_list(dcases_2016)
    no_dcases_2017 = df_to_list(dcases_2017)
    no_dcases_2018 = df_to_list(dcases_2018)
    no_dcases_2019 = df_to_list(dcases_2019)
    # Plotting the filtered list into the graph with their oen colour
    plt.plot(months, no_dcases_2014, color='purple')
    plt.plot(months, no_dcases_2015, color='black')
    plt.plot(months, no_dcases_2016, color='violet')
    plt.plot(months, no_dcases_2017, color='blue')
    plt.plot(months, no_dcases_2018, color='red')
    plt.plot(months, no_dcases_2019, color='green')
    # Setting the X axis label
    plt.xlabel('Yearly Data')
    # Setting the Y axis label
    plt.ylabel('Number of Cases')
    # Setting the Title for the chart
    plt.title('Total Number of Dengue Cases In Singapore 2014 - 2019')
    # Creating the legend for the chart
    purple_patch = mpatches.Patch(color='purple', label='2014')
    black_patch = mpatches.Patch(color='black', label='2015')
    violet_patch = mpatches.Patch(color='violet', label='2016')
    blue_patch = mpatches.Patch(color='blue', label='2017')
    red_patch = mpatches.Patch(color='red', label='2018')
    green_patch = mpatches.Patch(color='green', label='2019')
    # Inserting the legend for the chart
    plt.legend(handles=[purple_patch, black_patch, violet_patch, blue_patch, red_patch, green_patch])
    # Saving the images as png and svg format
    plt.savefig('flaskr/static/images/Dengue_Cases_2014-2019.svg', bbox_inches="tight")
    plt.savefig('flaskr/static/images/Dengue_Cases_2014-2019.png', bbox_inches="tight")


def rainfall_chart():
    """
        This function will display all the data into a chart and saves it as a png and svg file.
    """
    # Reads the csv file and saves its data into a variable
    rainfall_data = pandas.read_csv("source/dengue_data/RainfallData_G.csv")
    # Getting the number of cases for each month by selected year
    rcases_2014 = rainfall_per_month_for_choice_year(rainfall_data, 2014)
    rcases_2015 = rainfall_per_month_for_choice_year(rainfall_data, 2015)
    rcases_2016 = rainfall_per_month_for_choice_year(rainfall_data, 2016)
    rcases_2017 = rainfall_per_month_for_choice_year(rainfall_data, 2017)
    rcases_2018 = rainfall_per_month_for_choice_year(rainfall_data, 2018)
    rcases_2019 = rainfall_per_month_for_choice_year(rainfall_data, 2019)
    # Creating the list that will be displayed as the X axis ticker
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Converting the filtered data into a list
    no_rcases_2014 = df_to_list(rcases_2014)
    no_rcases_2015 = df_to_list(rcases_2015)
    no_rcases_2016 = df_to_list(rcases_2016)
    no_rcases_2017 = df_to_list(rcases_2017)
    no_rcases_2018 = df_to_list(rcases_2018)
    no_rcases_2019 = df_to_list(rcases_2019)
    # Plotting the filtered list into the graph with their oen colour
    plt.plot(year, no_rcases_2014, color='green')
    plt.plot(year, no_rcases_2015, color='red')
    plt.plot(year, no_rcases_2016, color='blue')
    plt.plot(year, no_rcases_2017, color='violet')
    plt.plot(year, no_rcases_2018, color='black')
    plt.plot(year, no_rcases_2019, color='purple')
    # Setting the X axis label
    plt.xlabel('Monthly Data')
    # Setting the Y axis label
    plt.ylabel("Monthly Rainfall in 'mm'")
    # Setting the Title for the chart
    plt.title('Total Amount of Rainfall In Singapore')
    # Creating the legend for the chart
    green_patch = mpatches.Patch(color='green', label='2014')
    red_patch = mpatches.Patch(color='red', label='2015')
    blue_patch = mpatches.Patch(color='blue', label='2016')
    violet_patch = mpatches.Patch(color='violet', label='2017')
    black_patch = mpatches.Patch(color='black', label='2018')
    purple_patch = mpatches.Patch(color='purple', label='2019')
    # Inserting the legend for the chart
    plt.legend(handles=[green_patch, red_patch, blue_patch, violet_patch, black_patch, purple_patch])
    # Saving the images as png and svg format
    plt.savefig('flaskr/static/images/Rainfall_Amount_2014-2019.png', bbox_inches="tight")
    plt.savefig('flaskr/static/images/Rainfall_Amount_2014-2019.svg', bbox_inches="tight")


def linear_reg_chart():
    """
        This function will create a chart and saves it as a png and svg file. It will also calculate and make sense
        of the inputs and find the correlation between rainfall amount and dengue cases through finding the coefficient,
        mean square error and r-squared value.

        Returns:
            dengue_title (str): Returns a string
    """
    # Setting a string to be displayed later
    dengue_title = "Dengue Linear Regression Analysis"
    # Calling the csv and reading from it
    denguedata = pd.read_csv("source/dengue_data/hist_data_dengue.csv")
    raindata = pd.read_csv("source/dengue_data/RainfallData.csv")
    # Getting filtering the data to get only the monthly data for both
    denguecases = total_case_per_month(denguedata)
    raincases = raindata.Total_Rainfall
    # -1 means that calculate the dimension of rows, but have 1 column, the values are converted into a numpy array
    x = raincases.values.reshape(-1, 1)
    y = denguecases["Case per Month"].values.reshape(-1, 1)
    # Creating the linear regression object
    linear_regressor = LinearRegression()
    # Train the model with the filtered data sets
    linear_regressor.fit(x, y)
    # Making a prediction with the data set
    y_pred = linear_regressor.predict(x)
    # The coefficient of the linear regression
    correlation = linear_regressor.coef_[0]
    # The mean squared error
    mse = mean_squared_error(y, y_pred)
    # The R-squared value
    rsquare = r2_score(y, y_pred)

    plt.xlabel("Monthly Rainfall in (mm)\nCorrelation : %.2f\nMean Square Error: %.2f\nR-squared: %.2f" %
               (correlation, mse, rsquare))
    # Setting the X axis label
    plt.ylabel('Dengue Cases')
    plt.title('Dengue Cases vs Rainfall 2014 - 2019')
    # Plotting the data
    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red')
    # Saving the data as a png and svg
    plt.savefig('flaskr/static/images/Linear_Regression_DvR.svg', bbox_inches="tight")
    plt.savefig('flaskr/static/images/Linear_Regression_DvR.png', bbox_inches="tight")
    # Returns a string that can be printed later
    return dengue_title

# -- (PENDING) Function -- # 
# def dengue_cases_table():
#     """
#         FOR FUTURE UPDATES
#
#         This function will produce a table that will display all the cases for each week for all the years.
#
#         Parameter:()
#
#         Returns:
#             print(dengue_cases_table) (DataFrame): This will return a DataFrame that will be displayed.
#     """
#     # Importing of dataset
#     dengue_data = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
#     # Getting the unique years and weeks
#     year = years(dengue_data)
#     week = weeks(dengue_data)
#     # Converting the Dataframe to a list of integers
#     years_list = year["Year"].astype(int).values.tolist()
#     weeks_list = week["Week"].astype(int).values.tolist()
#     # Setting the header for the table
#     header = pd.MultiIndex.from_product([years_list, ['Dengue Cases']])
#     # Creating an empty list to store the different rows to be printed
#     total_weeks_list = []
#     # This for loop checks if the first week is the same as i and then appends it to a list.
#     for i in weeks_list:
#         is_week = dengue_data["Week"] == i
#         weeklist = dengue_data[is_week]
#         weeklist = weeklist['Case per Week'].to_list()
#         total_weeks_list.append(weeklist)
#     # This will fill the table with the data from the list row by row
#     dengue_cases_table = pd.DataFrame(total_weeks_list, index=weeks_list, columns=header)
#     # Returns a printed table
#     return print(dengue_cases_table)

