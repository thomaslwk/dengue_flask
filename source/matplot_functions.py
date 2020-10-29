import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression


def import_csv(filename):  # import csv filetype and assign to a dataframe
    filename = "source/dengue_data/"
    overall_dataset = pd.read_csv(filename, index_col=None)
    return overall_dataset
# def total_case_per_month(dataset):  # check for hte
#     cases_per_month = pd.notnull(dataset["Case per Month"])
#     return dataset[cases_per_month].drop(["Week", "Case per Week", "Case per Year"], axis=


def total_case_per_month(dataset):  # check for hte
    cases_per_month = pd.notnull(dataset["Case per Month"])
    return dataset[cases_per_month]


# def months(dataset):
#     total_months = dataset.drop_duplicates(subset="Month", keep="first")
#     total_months = total_months.Month
#     return total_months
def cases_each_months(dataset):
    total_months = dataset.drop_duplicates(subset="Month", keep="first")
    return total_months.loc[:, ["Case per Month"]]


def cases_per_month_for_choice_year(dataset, year_choice):
    months_year = dataset[dataset["Year"] == int(year_choice)]
    total_months = months_year.drop_duplicates(subset="Month", keep="first")
    return total_months.loc[:, ["Case per Month"]]


def df_to_list(dataset):
    return dataset.values.tolist()


def rainfall_per_month_for_choice_year(dataset, year_choice):
    months_year = dataset[dataset["Year"] == int(year_choice)]
    return months_year.loc[:, "Total_Rainfall"]


def dengue_cases_2016_chart():
    dengue_data = import_csv("Historical Data Dengue.csv")
    dcases_2016 = cases_per_month_for_choice_year(dengue_data, 2016)
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_dcases_2016 = df_to_list(dcases_2016)
    plt.plot(year, no_dcases_2016, color='red')
    plt.xlabel('Yearly Data')
    plt.ylabel('Number of Cases')
    plt.title('Total Number of Dengue Cases In Singapore, 2016')
    red_patch = mpatches.Patch(color='red', label='2016')
    plt.legend(handles=[red_patch])
    plt.savefig('Dengue_Cases_2016.png', bbox_inches="tight")
    return plt.show()


def dengue_cases_2017_chart():
    dengue_data = pandas.read_csv("source/dengue_data/hist_data_dengue.csv") 
    dcases_2017 = cases_per_month_for_choice_year(dengue_data, 2017)
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_dcases_2017 = df_to_list(dcases_2017)
    plt.plot(year, no_dcases_2017, color='red')
    plt.xlabel('Yearly Data')
    plt.ylabel('Number of Cases')
    plt.title('Total Number of Dengue Cases In Singapore, 2017')
    red_patch = mpatches.Patch(color='red', label='2017')
    plt.legend(handles=[red_patch])
    plt.savefig('Dengue_Cases_2017.png', bbox_inches="tight")
    return plt.show()


def dengue_cases_2018_chart():
    dengue_data = import_csv("Historical Data Dengue.csv")
    dcases = cases_per_month_for_choice_year(dengue_data, 2018)
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_dcases = df_to_list(dcases)
    plt.plot(year, no_dcases, color='red')
    plt.xlabel('Yearly Data')
    plt.ylabel('Number of Cases')
    plt.title('Total Number of Dengue Cases In Singapore, 2018')
    red_patch = mpatches.Patch(color='red', label='2018')
    plt.legend(handles=[red_patch])
    plt.savefig('Dengue_Cases_2018.png', bbox_inches="tight")
    return plt.show()


def dengue_cases_2019_chart():
    dengue_data = import_csv("Historical Data Dengue.csv")
    dcases = cases_per_month_for_choice_year(dengue_data, 2019)
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_dcases = df_to_list(dcases)
    plt.plot(year, no_dcases, color='red')
    plt.xlabel('Yearly Data')
    plt.ylabel('Number of Cases')
    plt.title('Total Number of Dengue Cases In Singapore, 2019')
    red_patch = mpatches.Patch(color='red', label='2019')
    plt.legend(handles=[red_patch])
    plt.savefig('Dengue_Cases_2019.png', bbox_inches="tight")
    return plt.show()


def overall_dengue_cases_chart():
    dengue_data = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
    rainfall_data = import_csv("RainfallData.csv")
    dcases_2016 = cases_per_month_for_choice_year(dengue_data, 2016)
    dcases_2017 = cases_per_month_for_choice_year(dengue_data, 2017)
    dcases_2018 = cases_per_month_for_choice_year(dengue_data, 2018)
    dcases_2019 = cases_per_month_for_choice_year(dengue_data, 2019)

    # rcases_2016 = rainfall_per_month_for_choice_year(rainfall_data, 2016)
    # rcases_2017 = rainfall_per_month_for_choice_year(rainfall_data, 2017)
    # rcases_2018 = rainfall_per_month_for_choice_year(rainfall_data, 2018)
    # rcases_2019 = rainfall_per_month_for_choice_year(rainfall_data, 2019)

    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_dcases_2016 = df_to_list(dcases_2016)
    no_dcases_2017 = df_to_list(dcases_2017)
    no_dcases_2018 = df_to_list(dcases_2018)
    no_dcases_2019 = df_to_list(dcases_2019)

    # no_rcases_2017 = df_to_list(rcases_2017)
    # no_rcases_2018 = df_to_list(rcases_2018)
    # no_rcases_2019 = df_to_list(rcases_2019)
    plt.plot(year, no_dcases_2016, color='violet')
    plt.plot(year, no_dcases_2017, color='blue')
    plt.plot(year, no_dcases_2018, color='red')
    plt.plot(year, no_dcases_2019, color='green')
    plt.xlabel('Yearly Data')
    plt.ylabel('Number of Cases')
    plt.title('Total Number of Dengue Cases In Singapore 2016 - 2019')
    violet_patch = mpatches.Patch(color='violet', label='2016')
    blue_patch = mpatches.Patch(color='blue', label='2017')
    red_patch = mpatches.Patch(color='red', label='2018')
    green_patch = mpatches.Patch(color='green', label='2019')
    plt.legend(handles=[violet_patch, blue_patch, red_patch, green_patch])
    plt.savefig('Dengue_Cases_2016-2019.png', bbox_inches="tight")
    return plt.show()


def rainfall_chart():
    rainfall_data = pandas.read_csv("source/dengue_data/RainfallData.csv")
    rcases_2016 = rainfall_per_month_for_choice_year(rainfall_data, 2016)
    rcases_2017 = rainfall_per_month_for_choice_year(rainfall_data, 2017)
    rcases_2018 = rainfall_per_month_for_choice_year(rainfall_data, 2018)
    rcases_2019 = rainfall_per_month_for_choice_year(rainfall_data, 2019)
    year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    no_rcases_2016 = df_to_list(rcases_2016)
    no_rcases_2017 = df_to_list(rcases_2017)
    no_rcases_2018 = df_to_list(rcases_2018)
    no_rcases_2019 = df_to_list(rcases_2019)
    plt.plot(year, no_rcases_2016, color='blue')
    plt.plot(year, no_rcases_2017, color='violet')
    plt.plot(year, no_rcases_2018, color='black')
    plt.plot(year, no_rcases_2019, color='purple')
    plt.xlabel('Monthly Data')
    plt.ylabel("Monthly Rainfall in 'mm'")
    plt.title('Total Amount of Rainfall In Singapore')
    blue_patch = mpatches.Patch(color='blue', label='2016')
    violet_patch = mpatches.Patch(color='violet', label='2017')
    black_patch = mpatches.Patch(color='black', label='2018')
    purple_patch = mpatches.Patch(color='purple', label='2019')
    plt.legend(handles=[blue_patch, violet_patch, black_patch, purple_patch])
    plt.savefig('Rainfall_Amount_2016-2019.png', bbox_inches="tight")
    return plt()


def linear_reg_chart():
    dengue_title = "Dengue Linear Regression Analysis"
    denguedata = pd.read_csv("source/dengue_data/hist_data_dengue.csv")
    denguecases = total_case_per_month(denguedata)
    raindata = pd.read_csv("source/dengue_data/RainfallData.csv")
    raincases = raindata.Total_Rainfall
    x = raincases.values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
    y = denguecases["Case per Month"].values.reshape(-1, 1)  # values converts it into a numpy array
    linear_regressor = LinearRegression()
    linear_regressor.fit(x, y)
    y_pred = linear_regressor.predict(x)
    plt.xlabel("Monthly Rainfall in (mm)")
    plt.ylabel('Dengue Cases')
    plt.title('Dengue Cases vs Rainfall 2016 - 2019')
    plt.scatter(x, y)
    plt.plot(x, y_pred, color='red')
    plt.savefig('flaskr/static/images/Linear_Regression_DvR.svg', bbox_inches="tight")
    return(dengue_title)


# def dengue_v_rainfall():
#     denguedata = import_csv("Historical Data Dengue.csv")
#     denguecases = total_case_per_month(denguedata)
#     raindata = import_csv("RainfallData.csv")
#     raincases = raindata.Total_Rainfall
#
#     year = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     plt.plot(year, denguecases["Case per Month"], color='red')
#     plt.plot(year, raincases, color='blue')
#     plt.xlabel('Yearly Data')
#     plt.ylabel('Number of Cases')
#     plt.title('Total Number of Dengue Cases In Singapore')
#     blue_patch = mpatches.Patch(color='blue', label='2017')
#     red_patch = mpatches.Patch(color='red', label='2018')
#     plt.legend(handles=[blue_patch, red_patch])
#     plt.savefig('dengue_v_rainfall.png', bbox_inches="tight")
#     return plt.show()




# overall_dengue_cases_chart()
# rainfall_chart()
# linear_reg_chart()
# 
# dengue_cases_2016_chart()
# dengue_cases_2017_chart()
# dengue_cases_2018_chart()
# dengue_cases_2019_chart()



