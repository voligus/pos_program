from tkinter import *
import ui_order
import ui_stock
FONT = ("Angsana New", 16)


class HomePage:

    def __init__(self):
        self.window = Tk()
        self.window.title("Home")
        self.window.geometry("250x270")
        self.window.configure(padx=50, pady=50)

        self.label_home = Label(text="หน้าแรก", font=FONT)
        self.label_home.grid(row=0)

        self.label = Label(text="")
        self.label.grid(row=1, column=0)

        self.button_receipt_page = Button(text="ใบเสร็จ", command=self.change_to_order, font=FONT, width=20)
        self.button_receipt_page.grid(row=2, column=0)

        self.label = Label(text="")
        self.label.grid(row=3, column=0)

        self.button_item_page = Button(text="สต็อก", command=self.change_to_stock, font=FONT, width=20)
        self.button_item_page.grid(row=4, column=0)

        self.window.mainloop()

    def change_to_order(self):
        self.window.destroy()
        ui_order.OderInterface()

    def change_to_stock(self):
        self.window.destroy()
        ui_stock.StockInterface()


