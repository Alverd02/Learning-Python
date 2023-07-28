with open("weather_data.csv") as file:
     data = file.readlines()

import csv

with open("weather_data.csv") as file:
    data = csv.reader(file)
    data_list = [i for i in data]
    temperature = []
    for line in data_list[1:]:
        temperature.append(int(line[1]))

import pandas

data = pandas.read_csv("weather_data.csv")
column = data["temp"]

data_dict = data.to_dict()

temp_list = data["temp"].to_list()
average_temp = sum(temp_list)/len(temp_list)
mean = data["temp"].mean()

max_temp = data["temp"].max()

row = data[data["day"] == "Monday"]

row_max_temp = data[data["temp"] == data["temp"].max()]

monday = data[data.day == "Monday"]
fahrenheit_temp = int(monday.temp)*9/5+32

data_dict = {"Students": ["Amy", "Josh", "Sean"], "scores": [78, 57, 94]}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("new_data.csv")