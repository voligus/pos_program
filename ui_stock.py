from tkinter import messagebox
from tkinter.ttk import Treeview, Style
from item import Item
from order import Order
import pandas as pd
import home_page
from tkinter import *
FONT = ("Angsana New", 20)

list_stock = []
data = pd.read_csv("./item.csv")
dict_data = data.to_dict(orient="records")
for _ in dict_data:
    item = Item(_["id"], _["name"], _["cost"], _["amount"])
    list_stock.append(item)
# print(list_item)
order = Order(list_stock)


class StockInterface:

    def __init__(self,):
        self.window = Tk()
        self.order = order
        self.window.title("สต้อกสินค้า")
        self.window.configure(padx=50, pady=50)

        self.label_receipt = Label(text="สต้อกสินค้า", font=("Angsana New", 24, "bold"))
        self.label_receipt.grid(row=0, column=0, columnspan=4)

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

        self.tv['columns'] = ('id', 'name', 'cost', 'amount')
        self.tv.column('id', anchor=CENTER, width=150)
        self.tv.column('name', anchor=CENTER, width=150)
        self.tv.column('cost', anchor=CENTER, width=150)
        self.tv.column("amount", anchor=CENTER, width=150)

        self.tv.heading('id', text='ID', anchor=CENTER)
        self.tv.heading('name', text='NAME', anchor=CENTER)
        self.tv.heading('cost', text='COST', anchor=CENTER)
        self.tv.heading('amount', text='amount', anchor=CENTER)
        self.tv.grid(row=1, column=0, columnspan=4)

        self.scrollbar = Scrollbar(orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=5, sticky="ns")

        if len(self.order.list_stock) != 0:
            for _ in range(len(self.order.list_stock)):
                self.tv.insert("", index=_, iid=_,
                               value=(self.order.list_stock[_].item_id, self.order.list_stock[_].item_name,
                                      self.order.list_stock[_].item_cost, self.order.list_stock[_].item_amount))

        self.button_add_item = Button(text="เพิ่ม", command=self.insert_item, font=FONT, width=8)
        self.button_add_item.grid(row=2, column=0)

        self.button_add_amount_item = Button(text="เพิ่มสินค้า",command=self.insert_amount_item, font=FONT, width=8)
        self.button_add_amount_item.grid(row=2, column=1)

        self.button_delete_item = Button(text="ลบ", command=self.delete_item, font=FONT, width=8)
        self.button_delete_item.grid(row=2, column=2)

        self.button_back = Button(text="กลับ", command=self.back_home, font=FONT, width=8)
        self.button_back.grid(row=2, column=3)

        self.window.mainloop()

    def back_home(self):
        self.window.destroy()
        home_page.HomePage()

    def update_tree(self):
        for _ in self.tv.get_children():
            self.tv.delete(_)
        for _ in range(len(self.order.list_stock)):
            self.tv.insert("", index=_, iid=_, value=(self.order.list_stock[_].item_id, self.order.list_stock[_].item_name,
                                             self.order.list_stock[_].item_cost, self.order.list_stock[_].item_amount))

    def update_file_csv(self):
        list_dic_stock = []
        for _ in self.order.list_stock:
            dic_stock = {
                "id": _.item_id,
                "name": _.item_name,
                "cost": _.item_cost,
                "amount": _.item_amount
            }
            list_dic_stock.append(dic_stock)
        df = pd.DataFrame(list_dic_stock)
        df.to_csv("./item.csv", index=False)

    def delete_item(self):
        target_item = self.order.list_stock[int(self.tv.selection()[0])]
        self.order.list_stock.remove(target_item)
        self.update_tree()
        self.update_file_csv()

    def insert_amount_item(self):
        target_item = self.order.list_stock[int(self.tv.selection()[0])]

        def cancel():
            get_item_window.destroy()

        def agree():
            answer = messagebox.askokcancel(title="ต้องการเพิ่มจำนวนสินค้านี้ใช่หรือไม่",
                                            message=f"id :{target_item.item_id}\n"
                                                    f"name :{target_item.item_name}\n"
                                                    f"cost : {target_item.item_cost}\n"
                                                    f"amount:{entry_amount_item.get()}"
                                            )
            if answer:
                target_item.item_amount += int(entry_amount_item.get())
                self.update_tree()
                self.update_file_csv()
                get_item_window.destroy()
            else:
                return

        get_item_window = Tk()
        get_item_window.title("เพิ่มจำนวนสินค้า")
        get_item_window.configure(padx=20, pady=20)

        label_amount_item = Label(get_item_window, text="amount", font=FONT)
        label_amount_item.grid(row=0, column=0)
        entry_amount_item = Entry(get_item_window)
        entry_amount_item.grid(row=0, column=1)

        button_ok = Button(get_item_window, text="ตกลง", font=FONT, command=agree)
        button_ok.grid(row=1, column=0)

        button_cancel = Button(get_item_window, text="ยกเลิก", font=FONT, command=cancel)
        button_cancel.grid(row=1, column=1)

    def insert_item(self):
        def cancel():
            get_item_window.destroy()

        def agree():
            answer = messagebox.askokcancel(title="ต้องการเพิ่มสินค้านี้ใช่หรือไม่",
                                            message=f"id :{entry_id_item.get()}\n"
                                                    f"name :{entry_name_item.get()}\n"
                                                    f"cost : {entry_cost_item.get()}")
            if answer:
                new_item = Item(entry_id_item.get(), entry_name_item.get(), entry_cost_item.get())
                self.order.list_stock.append(new_item)
                self.update_tree()
                self.update_file_csv()
                get_item_window.destroy()
            else:
                return

        get_item_window = Tk()
        get_item_window.title("สินค้าใหม่")
        get_item_window.configure(padx=20, pady=20)

        label_id_item = Label(get_item_window, text="ID", font=FONT)
        label_id_item.grid(row=0, column=0)
        entry_id_item = Entry(get_item_window)
        entry_id_item.grid(row=0, column=1)

        label_name_item = Label(get_item_window, text="name", font=FONT)
        label_name_item.grid(row=1, column=0)
        entry_name_item = Entry(get_item_window)
        entry_name_item.grid(row=1, column=1)

        label_cost_item = Label(get_item_window, text="cost", font=FONT)
        label_cost_item.grid(row=2, column=0)
        entry_cost_item = Entry(get_item_window)
        entry_cost_item.grid(row=2, column=1)

        button_ok = Button(get_item_window, text="ตกลง", font=FONT, command=agree)
        button_ok.grid(row=3, column=0)

        button_cancel = Button(get_item_window, text="ยกเลิก", font=FONT, command=cancel)
        button_cancel.grid(row=3, column=1)

        get_item_window.mainloop()
