import pandas
import requests
from bs4 import BeautifulSoup

def averagerainfalls(x):
    a = 0
    rainfall = pandas.read_csv("source/dengue_data/RainfallData.csv")
    is_jan = rainfall["Month"] == x
    monthlist = rainfall[is_jan]
    monthlist = monthlist.Total_Rainfall.to_list()
    for b in monthlist:
        a += b
    return (a / len(monthlist))

def avgrainfalllist():

    avgrainlist = []
    for i in range(1, 13):
        avgrain = averagerainfalls(i)
        avgrainlist.append(avgrain)
    return avgrainlist


def averagedenguecases(Month):
    k = 0
    denguecases = pandas.read_csv("source/dengue_data/DengueMonthlyData.csv")
    is_jan = denguecases["Monthly"] == Month
    monthlist = denguecases[is_jan]
    monthlist = monthlist.Monthly_Cases.to_list()
    for j in monthlist:
        k += j
    return (k/len(monthlist))

def avgdenguelist():
    avglist = []
    for i in range(1, 13):

        avg = averagedenguecases(i)
        avglist.append(avg)
    return avglist

''' Webscraping with BeautifulSoup.'''
# Function to return largest Active Cluster.
def nea_data_big_c():
   # Using beautiful soup to borrow data from NEA because no api provided 
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    
    # Get table element with this classname on NEA's site.
    # This is the start of the table, where the information we want to crawl begins.  
    table = soup.find('table', attrs={'class':'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols] 
        data.append([ele for ele in cols if ele])

    # Format output to get first set of element as it reflects the largest cluster
    biggest_active_cluster = " ".join(data[3][1].split('/'))
    return biggest_active_cluster 

def nea_data_small_c():
   # Using beautiful soup to borrow data from NEA because no api provided 
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')
    data = [] 

    # Get table element with this classname on NEA's site.
    # This is the start of the table, where the information we want to crawl begins.  
    table = soup.find('table', attrs={'class':'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols] 
        data.append([ele for ele in cols if ele])

    # Format output to get last set as it reflects the smallest cluster
    smallest_active_cluster = " ".join(data[-1][1].split('/'))
    return smallest_active_cluster 

#  def nea_data(x):
#    # Using beautiful soup to borrow data from NEA because no api provided 
#     page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
#     soup = BeautifulSoup(page.content, 'html.parser')

#     data = []
#     # Get table element with this classname from NEA's site 
#     table = soup.find('table', attrs={'class':'table surveillance-table two-row-head dengue-fixed-table'})
#     table_body = table.find('tbody')
#     rows = table_body.find_all('tr')
#     for row in rows:
#         cols = row.find_all('td')
#         cols = [ele.text.strip() for ele in cols] 
#         data.append([ele for ele in cols if ele])
#     # Format output to get first set of element as it reflects the largest cluster
#     if x == "big":
#         biggest_active_cluster = " ".join(data[3][1].split('/'))
#         return biggest_active_cluster 
#     elif x == "small":
#         smallest_active_cluster = " ".join(data[-1][1].split('/'))
#         return smallest_active_cluster 

