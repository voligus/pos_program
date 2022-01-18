from tkinter import *
from tkinter.ttk import *
window = Tk()
window.title("table")
window.config(width=600, height=600)


def delete():
    x = tv.selection()[0]
    print(x)
    tv.delete(x)


tv = Treeview(show="headings")
style = Style()
style.configure(
    "Treeview",
    rowheight=40,
    font=(None, 20))
style.configure(
    "Treeview.Heading",
    font=(None, 20)
)

tv['columns'] = ('Rank', 'Name', 'Badge')
tv.column('Rank', anchor=CENTER, width=150)
tv.column('Name', anchor=CENTER, width=150)
tv.column('Badge', anchor=CENTER, width=150)

tv.heading('Rank', text='Id', anchor=CENTER)
tv.heading('Name', text='rank', anchor=CENTER)
tv.heading('Badge', text='Badge', anchor=CENTER)

tv.insert(parent='', index=0, values=('1','Vineet','Alpha'))
tv.insert(parent='', iid=1, text='', values=('2','Aกกก','Bravo'))
tv.insert(parent='', index=2, iid=2, text='', values=('3','Vinod','Charlie'),)
tv.insert(parent='', index=3, iid=3, text='', values=('4','Vimal','Delta'))
tv.insert("", END, values=('5', 'Manjeet', 'Echo'))
tv.insert("", END, values=('5', 'Manjeet', 'Echo'))
tv.insert("", END, values=('5', 'Manjeet', 'Echo'))
tv.insert("", END, values=('5', 'Manjeet', 'Echo'))
tv.grid(row=0, column=0, sticky="nsew")

scrollbar = Scrollbar(orient=VERTICAL, command=tv.yview)
tv.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0, column=1, sticky="ns")

label = Label(text="hello")
label.grid(row=4, column=0)
button = Button(text="ลบ", command=delete)
button.grid(row=4, column=1)

window.mainloop()

