# Day 25 - Pandas Practice + Squirrel Census Project
# Topics: read_csv, DataFrame, filtering rows, to_csv




#import csv
#import pandas


#with open("./weather_data.csv") as data:
   # data_set = csv.reader(data)
   # temperatures = []
   # condition = []
  #  for row in data_set:
     #   if row[1] != "temp" and row[2] != "condition":
    #        temperatures.append(int(row[1]))
   #         condition.append(row[2])


#import pandas
#data = pandas.read_csv("weather_data.csv")
#print(type(data["temp"]))
#print(data)

#print(type(data))
#conversion to dict - 
#data_dict = data.to_dict()
#conversion to list -
#temp_list = data["temp"].to_list()
#print(len(temp_list))

#temp_list_p = data["condition"].to_list()
#print(temp_list_p)
#print(temperatures)
#print(condition)

#average temp-
#average = sum(temp_list) / len(temp_list)
#print(average)

#average temp by mean method-
#print (data["temp"].mean())




#for data_P in data_set:
 #   data_P = data_P.strip()
#    list.append(data_P)


#get data in row
#Can it be convert to objetct type

#get data in row
#print(data[data.day == "Sunday"])
#print(data[data.temp == data.temp.max()])

#monday = data[data.day == "Monday"]
#monday.condition

#monday_temp = monday.temp[0]
#monday_temp_F = monday_temp * 9/5 + 32
#monday_temp_F

#CREATE DATAFRAME FROM SCRATCH
#data_dict = {
  #  "students": ["Any" , "James", "Angela"],
 #   "score": [76, 56, 65] 

#}

#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260512.csv")


Gray_Squirrels = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_Squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_Squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_squirrels_color = {
    "color_of_squirrels": ["Gray", "Cinanamon", "Black"],
    "Number_of_squirrels": [ Gray_Squirrels, Cinnamon_Squirrels, Black_Squirrels]
}

data_dict = pandas.DataFrame(data_squirrels_color)
data_dict.to_csv("squirrel_count.csv")
