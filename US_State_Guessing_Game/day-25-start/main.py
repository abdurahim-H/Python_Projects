import pandas


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

g_s = len(data[data["Primary Fur Color"] == "Gray"])
c_s = len(data[data["Primary Fur Color"] == "Cinnamon"])
b_s = len(data[data["Primary Fur Color"] == "Black"])


s_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [g_s, c_s, b_s]
}
data = pandas.DataFrame(s_dict)

data.to_csv("test.csv")