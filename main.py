from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("My Best ToDo List !")
root.geometry("500x500")

#define font
my_font = Font(family="Brush Script MT",
                size=30,
                weight="bold")
#create frame
my_frame = Frame(root)
my_frame.pack(pady=30)

#create listbox
my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646",
                  activestyle="none")
my_list.pack()

#create dummy list
stuff = ["minum air","cari buku","mana mana"]
for item in stuff:
    my_list.insert(END, item)

#create scrollbar
#my_scrollbar = Scrollbar(my_frame)
#my_scrollbar.pack(side=RIGHT,fill=Y)

#Add scrollbar
#my_list.config(yscrollcommand=my_scrollbar.set)
#my_scrollbar.config(command=my_list.yview)

#create entry box to add item to list
my_entry= Entry(root, font= ("Helvetica", 20))
my_entry.pack(pady=20)

#create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

#function
def delete_item():
    my_list.delete(ANCHOR)
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0,END)
def cross_off_item():
    pass
def uncross_item():
    pass

#create some button
delete_button =Button(button_frame, text = "lalala", command= delete_item)
add_button =Button(button_frame, text = "Add", command= add_item)
cross_off_button =Button(button_frame, text = "Cross Off Item", command= cross_off_item)
uncross_button =Button(button_frame, text = "Uncross", command= uncross_item)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20 )
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)

root.mainloop()