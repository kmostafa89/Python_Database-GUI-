"""
Created on Thursday Jun 1 10:41:57 2017

@author: Mostafa



in this app the user can:
    View
    Search
    Add
    update
    delete
    and close the app

the book infor will include :
    Tite
    Authoe
    Year
    ISBN
"""

from tkinter import *
import back_end

# the function used in the 'bind' function below , to connect the listbox with the enry boxes 
#this function is reponsible for filling in the entry box with the select item from the listbox

def get_selected_row(event):
    global selected_tuple
    index = List.curselection()[0]
    selected_tuple = List.get(index)
    e1.delete(0, END)
    e1.insert(END , selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END , selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END , selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END , selected_tuple[4])


# below I have used additional function to combine the back_end functions with the buttons 

# in the view function we first delete all the items in the list box and loop through the results of the back_end view function
def view_command():
    List.delete(0,END)
    for row in back_end.view():
        List.insert(END , row)

# similarly for search command we delete the items in the listbox first before executing the search query and pulling the data through
def search_command():
    List.delete(0,END)
    for row in back_end.search(title = title_text.get() , author = author_text.get() , year = year_text.get() , isbn = isbn_text.get()):
        List.insert(END , row)


# for the add command , we have 4 arguments which are used based on the data in the entry box from the user
#I used StringVar() to store the values of entry boxes and used those variables as arguments for my back_end function below:
#e.g title_text is a StringVar() which is assigned to the enry box below upon creating the enry box

def add_command():
    back_end.insert(title = title_text.get() , author = author_text.get() , year = year_text.get() , isbn = isbn_text.get())
    List.delete(0,END)
    List.insert(END , (title_text.get() , author_text.get() , year_text.get() , isbn_text.get()))


#for the delete command we use the id argument which is the primary key in our database
#i got the id from the get_selectd_tuple function I declared above
# selected_tuple return a tuple of values in the listbox and the first value is the id

def delete_command():
    back_end.delete(selected_tuple[0])
    List.delete(0,END)
    view_command()




def update_command():
    back_end.update(selected_tuple[0],title_text.get() , author_text.get() , year_text.get() , isbn_text.get())
    List.delete(0 , END)
    view_command()





def close_command():
    window.destroy()

window = Tk()
window.wm_title("Book Store")


l1 = Label(window , text ="Title")
l1.grid(row = 0 , column = 0  )


title_text = StringVar()
e1 = Entry(window , width = 20 , textvariable = title_text)
e1.grid(row = 0 , column = 1  )

l2 = Label(window , text ="Author")
l2.grid(row = 0 , column = 2 )

author_text = StringVar()
e2 = Entry(window , width = 20 , textvariable = author_text)
e2.grid(row = 0 , column  = 3 )

l3  = Label(window , text = "Year")
l3.grid(row = 1 , column =0 )


year_text = StringVar()
e3 = Entry(window , width = 20 , textvariable = year_text)
e3.grid(row = 1 , column = 1  )



l4 = Label(window , text = "ISBN")
l4.grid(row = 1 , column = 2)


isbn_text = StringVar()
e4 = Entry(window , width = 20 , textvariable = isbn_text )
e4.grid(row = 1, column = 3 )


List = Listbox(window, width = 35 , height = 6)
List.grid(row = 2 , column = 0 , rowspan = 6 , columnspan = 2 )
"""
we need to connect the scroll bar to the required object , in this case the list we created above
"""
sc = Scrollbar(window)
sc.grid(row = 2 , column = 2 , rowspan =6)

List.configure(yscrollcommand = sc.set)
sc.configure(command = List.yview)

List.bind('<<ListboxSelect>>',get_selected_row)


""" crrating the buttons of our fron end GUI" Graphic user interface"""

b1 = Button(window , text = "View all " , width = 12 , command = view_command)
b1.grid(row = 2 , column = 3)

b2 = Button(window , text = "Search" , width = 12 , command = search_command)
b2.grid(row = 3 , column = 3)

b2 = Button(window , text = "Add" , width = 12 , command = add_command)
b2.grid(row = 4 , column = 3)

b3 = Button(window , text = "Update" , width = 12, command = update_command)
b3.grid(row = 5 , column = 3)

b4 = Button(window , text = "Delete" , width = 12 , command = delete_command)
b4.grid(row = 6 , column = 3)

b5 = Button(window , text = "Close" , width = 12 , command = close_command)
b5.grid(row = 7 , column = 3)




window.mainloop()
