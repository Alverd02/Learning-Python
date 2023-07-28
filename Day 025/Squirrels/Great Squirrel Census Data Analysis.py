import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# fur_color_list = data["Primary Fur Color"].to_list()

# gray = []
# cinnamon = []
# black = []

# for i in fur_color_list:
#     if i == "Gray":
#         gray.append(i)
#     elif i == "Black":
#         black.append(i)
#     elif i == "Cinnamon":
#         cinnamon.append(i)
#
# squirrel_count = {"Fur color": ["Gray", "Cinnamon", "Black"], "Count": [len(gray), len(cinnamon), len(black)]}
#
# squirrel_count_dataFrame = pandas.DataFrame(squirrel_count)
# squirrel_count_dataFrame.to_csv("Squirrel_Count")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

squirrel_count = {"Fur color": ["Gray", "Cinnamon", "Black"], "Count": [gray_count, cinnamon_count, black_count]}

squirrel_count_dataFrame = pandas.DataFrame(squirrel_count)
squirrel_count_dataFrame.to_csv("Squirrel_Count.csv")
