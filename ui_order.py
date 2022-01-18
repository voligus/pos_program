from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
import home_page
from order import Order
from item import Item
import pandas as pd
FONT = ("Angsana New", 20)
COST = 0

list_stock = []
data = pd.read_csv("./item.csv")
dict_data = data.to_dict(orient="records")
for _ in dict_data:
    item = Item(_["id"], _["name"], _["cost"], _["amount"])
    list_stock.append(item)
order = Order(list_stock)
print(len(order.list_stock))


class OderInterface:
    def __init__(self):
        self.list_stock = []
        self.order = Order(self.list_stock)
        self.messagebox = messagebox
        self.window = Tk()
        self.window.configure(padx=30, pady=30)
        self.tv = Treeview(show="headings")
        self.style = Style()
        self.style.configure(
            "Treeview",
            rowheight=40,
            font=FONT
        )
        self.style.configure(
            "Treeview.Heading",
            font=FONT
        )

        self.label_receipt = Label(text="ใบเสร็จ", font=("Angsana New", 24, "bold"))
        self.label_receipt.grid(row=0, column=0, columnspan=4)

        self.tv['columns'] = ('id', 'name', 'cost', 'amount')
        self.tv.column('id', anchor=CENTER, width=150)
        self.tv.column('name', anchor=CENTER, width=150)
        self.tv.column('cost', anchor=CENTER, width=150)
        self.tv.column('amount', anchor=CENTER, width=150)

        self.tv.heading('id', text='ID', anchor=CENTER)
        self.tv.heading('name', text='NAME', anchor=CENTER)
        self.tv.heading('cost', text='COST', anchor=CENTER)
        self.tv.heading('amount', text='AMOUNT', anchor=CENTER)
        self.tv.grid(row=1, column=0, columnspan=4)

        self.scrollbar = Scrollbar(orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=5, sticky="ns")

        self.label_cost = Label(text="ราคารวม", font=FONT)
        self.label_cost.grid(row=2, column=2)
        self.label_num_cost = Label(text="0", font=FONT)
        self.label_num_cost.grid(row=2, column=3)

        self.label_id = Label(text="ID", font=FONT)
        self.label_id.grid(row=3, column=0)
        self.entry_id = Entry()
        self.entry_id.grid(row=3, column=1)

        self.label_name = Label(text="NAME", font=FONT)
        self.label_name.grid(row=3, column=2)
        self.entry_name = Entry()
        self.entry_name.grid(row=3, column=3)

        self.label_cost = Label(text="COST", font=FONT)
        self.label_cost.grid(row=4, column=0)
        self.entry_cost = Entry()
        self.entry_cost.grid(row=4, column=1)

        self.button_search = Button(text="ค้นหา", command=self.search, font=FONT, width=8)
        self.button_search.grid(row=5, column=0)

        self.button_insert = Button(text="เพิ่ม", command=self.insert_row, font=FONT, width=8)
        self.button_insert.grid(row=5, column=1)

        self.button_delete = Button(text="ลบ", command=self.delete_row, font=FONT, width=8)
        self.button_delete.grid(row=5, column=2)

        self.button_create_doc = Button(text="พิมพ์", font=FONT, width=8)
        self.button_create_doc.grid(row=5, column=3)

        self.button_home = Button(text="กลับ", command=self.back_home, font=FONT, width=8)
        self.button_home.grid(row=5, column=4)

        self.button_cal = Button(text="คิดเงิน", command=self.cal, font=FONT, width=8)
        self.button_cal.grid(row=6, column=0, pady=10)

        self.window.mainloop()

    def update_tree(self):
        for _ in self.tv.get_children():
            self.tv.delete(_)
        for _ in range(len(self.order.list_order)):
            self.tv.insert("", index=_, iid=_, value=(self.order.list_order[_].item_id, self.order.list_order[_].item_name,
                                             self.order.list_order[_].item_cost, self.order.list_order[_].item_amount))

    def cal(self):
        for index_order in range(len(self.order.list_order)):
            for index_stock in range(len(order.list_stock)):
                print(order.list_stock[index_stock].item_amount)
                print(order.list_stock[index_stock].item_id)
                print(self.order.list_order[index_order].item_id)
                if int(self.order.list_order[index_order].item_id) == int(order.list_stock[index_stock].item_id):
                    order.list_stock[index_stock].item_amount -= self.order.list_order[index_order].item_amount
                    print(order.list_stock[index_stock].item_amount)
        self.update_file_csv()

    def insert_row(self):
        item_id = self.entry_id.get()
        item_name = self.entry_name.get()
        try:
            item_cost = int(self.entry_cost.get())
        except ValueError:
            self.messagebox.showinfo(title="Ooop", message="กรุุณาใส่เฉพาะตัวเลขในช่องราคา")
            return
        else:
            x = Item(item_id, item_name, item_cost, amount=1)
            global COST
            COST += int(item_cost)
            self.label_num_cost.configure(text=COST)
            self.entry_id.delete(0, "end")
            self.entry_name.delete(0, "end")
            self.entry_cost.delete(0, "end")
            self.entry_id.focus()
            self.order.insert_item(x)
            self.update_tree()

    def delete_row(self):
        x = self.tv.selection()[0]
        global COST
        COST -= int(self.order.list_order[int(x)].item_cost)
        self.label_num_cost.configure(text=COST)
        self.order.delete_item(x)
        self.update_tree()

    def search(self):
        id = self.entry_id.get()
        for _ in range(len(order.list_stock)):
            # print(self.order.list_stock[_].item_id)
            if str(order.list_stock[_].item_id) == str(id):
                name = order.list_stock[_].item_name
                cost = order.list_stock[_].item_cost
                self.entry_name.insert(0, name)
                self.entry_cost.insert(0, cost)
                return
        self.messagebox.showinfo(title="Ooops", message="ไม่มีสินค้า")

    def update_file_csv(self):
        print("updated")
        list_dic_stock = []
        for _ in order.list_stock:
            dic_stock = {
                "id": _.item_id,
                "name": _.item_name,
                "cost": _.item_cost,
                "amount": _.item_amount
            }
            list_dic_stock.append(dic_stock)
        df = pd.DataFrame(list_dic_stock)
        df.to_csv("./item.csv", index=False)

    def back_home(self):
        self.window.destroy()
        home_page.HomePage()
