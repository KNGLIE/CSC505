import tkinter
from tkinter import *
from tkinter import ttk
# imports modules needed
application_window = Tk()
# Creates title
application_window.title("Shopping App")
application_window.mainloop()

#initial window
application_window = Tk()
# Title
application_window.title("Shopping App")
# Frame widget for scrollbar
frame_item = Frame(application_window)
frame_item.pack()
#hold items in listbox
listbox_item = Listbox(frame_item, bg = "black", fg = "white", height = 15, width = 50, font = "Times New Roman")
listbox_item.pack(side = tkinter.LEFT)
#Scrollbar
scrollbar_item = Scrollbar(frame_item)
scrollbar_item.pack(side = tkinter.RIGHT, fill = tkinter.Y)
listbox_item.config(command = listbox_item.yview)
#button
entry_button = Button(application_window, text = "Add Item", width = 50, command = enteritem)
entry_button.pack(pady = 3)
delete_button = Button(application_window, text = "Delete Selected Item", width = 50, command = deleteitem)
delete_button.pack(pady = 3)
application_window.mainloop()
def enteritem():
    # a new window to take input
    input_text = ""
    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title = "Warning", message = "Enter the item name")
        else:
            listbox_task.insert(END, input_text)
root1.destroy()
root1 = Tk()
root1.title("Add Item")
entry_task = Text(root1, width = 40, height = 4)
entry_task.pack()
button_temp =Button(root1, text = "Add Item", command = add)
button_temp.pack()
root1.mainloop()
def deleteitem():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])
