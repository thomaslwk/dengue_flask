import pandas
import requests
from bs4 import BeautifulSoup

'''Calculating average dengue cases and rainfall
 def filter_months(dataset):
    Input: CSV file(Sorted by weeks)
    Output: Dataframe (Data sorted by months)
 
 def averagerainfall(month):
    Input: A number representing the month
    Output: The average of rainfall in the list with the same month
    Calculates average rainfall in each month

 def avgrainfalllist():
    Output: Average rainfall given by averagerainfall(x) in a list
    Append each month average rainfall into a list
    
 def averagedenguecases(month):
    Input: The variable month filtered by filter_months(dataset)
    Output: The average dengue cases for that month
    Calculate average dengue cases in each month
 
 def avgdenguelist():
    Output: The average dengue cases calculated by averagedenguecases listed in a list
    Append each month average dengue cases into a list
 
 '''
# To filter and get all 12 months
def filter_months(dataset):  
    # to remove any duplicate after identifying the first month
    total_months = dataset.drop_duplicates(subset="Month", keep="first")
    return total_months.loc[:, ["Month"]]

#function to calculate the average rainfall per month
def averagerainfalls(x):
    a = 0
    # read csv file
    rainfall = pandas.read_csv("source/dengue_data/RainfallData.csv")
    # check if the month in csv is same as the variable month
    is_month = rainfall["Month"] == x
    # check for the whole csv file using the check
    monthlist = rainfall[is_month]
    # list out the total rainfall based on the filtered list
    monthlist = monthlist.Total_Rainfall.to_list()
    # sum all the elements in the list
    for b in monthlist:
        a += b
    #returning the avg of the list
    return (a / len(monthlist))

#function list the average rainfall
def avgrainfalllist():
    avgrainlist = []
    # loop 12 times sinces there is 12 months in a year
    for i in range(1, 13):
        # calculating the average rainfall in 1 specfic month
        avgrain = averagerainfalls(i)
        # appending the average of each month to a list
        avgrainlist.append(avgrain)
    # return the list of average rainfall
    return avgrainlist

#function to get the average dengue cases sorted by month
def averagedenguecases(month):
    k = 0
    # read csv file
    denguecases = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
    # checking each line if the Month column matches the variable
    is_month = denguecases["Month"] == month
    # adding each variable that matches to a list
    monthlist = denguecases[is_month]
    # removing any empty set as csv file is sorted by weeks not months
    monthlist = monthlist.dropna(subset=["Case per Month"])
    # adding the final results to a list
    monthlist = monthlist["Case per Month"].to_list()
    # finding the average of the list
    for j in monthlist:
        k += j
    avg = k/ len(monthlist)
    # return month average
    return avg

#function list the average dengue cases
def avgdenguelist():
    avglist = []
    # read csv file
    dataset = pandas.read_csv("source/dengue_data/hist_data_dengue.csv")
    # remove any duplicated months using filter_months
    dataset = filter_months(dataset)
    # adding the months to a list
    dataset = dataset['Month'].astype(str).values.tolist()
    # appending each month average list into a list
    for i in dataset:
        avg = averagedenguecases(i)
        avglist.append(avg)
    # return the avg list
    return avglist


"""
    Function Name: nea_data_big_c(), nea_data_small_c()
    Variable: NILL
    Description: Web scrape function to get html data from NEA's site to get most updated active cluster.
    Wasn't able to figure out in time how to input condition to separate the functions. 
"""
# -- Function to return Largest Active Cluster -- #
def nea_data_big_c():
    # -- Using beautiful soup to borrow data from NEA because no api provided -- #
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []

    # -- Get table element with this classname on NEA's site. -- #
    # -- This is the start of the table, where the information we want to crawl begins. -- #
    table = soup.find('table', attrs={'class': 'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # -- Format output to get first set of element as it reflects the largest cluster -- #
    biggest_active_cluster = " ".join(data[3][1].split('/'))
    return biggest_active_cluster
   
# -- Function to return Smallest Active Cluster -- #
def nea_data_small_c():
    # -- Using beautiful soup to borrow data from NEA because no api provided -- #
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []

    # -- Get table element with this classname on NEA's site. -- # 
    # -- This is the start of the table, where the information we want to crawl begins.  -- #
    table = soup.find('table', attrs={'class': 'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])

    # -- Format output to get last set as it reflects the smallest cluster -- #
    smallest_active_cluster = " ".join(data[-1][1].split('/'))
    return smallest_active_cluster
  
    