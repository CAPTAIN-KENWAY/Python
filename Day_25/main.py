import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_colors = data["Primary Fur Color"].unique()
count_list = []

for color in fur_colors:
    fur_color = data[data["Primary Fur Color"] == color]
    count_list.append(len(fur_color["Unique Squirrel ID"]))

count_list.remove(0)
data_dict={
    "Fur Color": ["Gray","Red","Black"],
    "Count": count_list
}
df=pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")