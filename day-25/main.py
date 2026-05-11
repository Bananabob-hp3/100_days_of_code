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


import pandas
data = pandas.read_csv("weather_data.csv")
#print(type(data["temp"]))
#print(data)

#print(type(data))
#conversion to dict - 
data_dict = data.to_dict()
#conversion to list -
temp_list = data["temp"].to_list()
#print(len(temp_list))

temp_list_p = data["condition"].to_list()
#print(temp_list_p)
#print(temperatures)
#print(condition)

#average temp-
average = sum(temp_list) / len(temp_list)
#print(average)

#average temp by mean method-
#print (data["temp"].mean())



#max value method-
#print(data["temp"].max())

#NOTE- PROS AND CONS 
#print(data["condition"])
#print(data.condition)

#for data_P in data_set:
 #   data_P = data_P.strip()
#    list.append(data_P)


#get data in row
#Can it be convert to objetct type

#get data in row
#print(data[data.day == "Sunday"])
#print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

