from order import Order
from item import Item
from home_page import HomePage
import pandas as pd
FONT = ("Angsana New", 16)

list_item = []
data = pd.read_csv("./item.csv")
dict_data = data.to_dict(orient="records")
for _ in dict_data:
    item = Item(_["id"], _["name"], _["cost"], _["amount"])
    list_item.append(item)
# print(list_item)
order = Order(list_item)
home_page = HomePage()
