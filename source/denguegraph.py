import pandas


# test = pandas.read_csv("C:\\SIT\\1002\\Project\\DengueData.csv")
# test2 = pandas.read_csv("C:\\SIT\\1002\\Project\\rainfall-monthly-total.csv")
# print(test)
# print(test2)

# def denguecases():
#     denguecase = pandas.read_csv("C:\\SIT\\1002\\Project\\DengueMonthlyData.csv")
#
#     return denguecase.Monthly_Cases.to_list(), denguecase.Monthly.to_list()
#
# def rainfalls():
#     rainfall = pandas.read_csv("C:\\SIT\\1002\\Project\\RainfallData.csv")
#     return rainfall.Total_Rainfall.to_list(), rainfall.Month.to_list()

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


# rainfall1 = pandas.read_csv("C:\\SIT\\1002\\Project\\RainfallData.csv")
# print(rainfall1.Total_Rainfall.to_list())
# print(rainfall1.Month.to_list())


# # print(denguecases()[0], denguecases()[1])
# #
# # def testcase():
# list1 = []
# list2 = []
# testcase = pandas.read_csv("C:\\SIT\\1002\\Project\\TestCase.csv")
# list1 = testcase.Year.to_list()
# list2 = testcase.Cases.to_list()
# print(list1)
# print(list2)
# # return list1, list2



