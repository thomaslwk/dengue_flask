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


def nea_data_big_c():
   # Using beautiful soup to borrow data from NEA because no api provided 
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = [] 
    table = soup.find('table', attrs={'class':'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols] 
        data.append([ele for ele in cols if ele])
    
    biggest_active_cluster = " ".join(data[3][1].split('/'))
   
    return biggest_active_cluster 
    # return requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters").json()

def nea_data_small_c():
   # Using beautiful soup to borrow data from NEA because no api provided 
    page = requests.get("https://www.nea.gov.sg/dengue-zika/dengue/dengue-clusters")
    soup = BeautifulSoup(page.content, 'html.parser')

    data = [] 
    table = soup.find('table', attrs={'class':'table surveillance-table two-row-head dengue-fixed-table'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols] 
        data.append([ele for ele in cols if ele])
    smallest_active_cluster = " ".join(data[-1][1].split('/'))
    # biggest_active_cluster = " ".join(data[3][1].split('/'))
   
    return smallest_active_cluster 
    # return requests.get("https://www.nea.gov.sg/dengue-zika/dengue/de
 
