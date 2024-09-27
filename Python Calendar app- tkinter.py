import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import ttkbootstrap as ttk
#from tkcalendar import Calendar
from datetime import date 

window = ttk.Window(themename = 'darkly')
window.title('Calendar')

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

#window.attributes('-fullscreen', True)
i=0

def si(event):
    global photo
    screen_width = event.width
    screen_height = event.height
    photo = bgimg_array[i].resize((screen_width,screen_height))
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image( 0, 0, image = photo, anchor = "nw")
    #canvas.create_text(75,75, text='Tasks',font=('Helvetica',25))

def change_index():
    global i,photo

    limit = len(bgimg_array)
    if i==limit-1: i=0
    else: i+=1

    photo = bgimg_array[i].resize((canvas.winfo_width(), canvas.winfo_height()))
    photo = ImageTk.PhotoImage(photo)
    canvas.create_image(0, 0, image=photo, anchor="nw")

"""
def add():
    global filepath,i
    new_window = Toplevel()
    new_window.title('Add images')
    new_window.geometry('600x75')
    
    canvas_new=ttk.Canvas( new_window) 
    canvas_new.pack(fill = "both", expand = True)

    label = tk.Label(new_window,text='insert image file path:')
    label_window = canvas_new.create_window(10,10,anchor = 'nw',window = label)

    entry = tk.Entry(new_window,width= 50)
    entry_window = canvas_new.create_window(175,10,anchor = 'nw',window = entry)

    def update():
        global photo, i
        filepath = entry.get()
        for imgs in bgimg_array:
            if filepath not in [str(img) for img in bgimg_array]:
                photo3 = Image.open(filepath)
                bgimg_array.append(photo3)
                i = len(bgimg_array) - 1
                change_index
                photo = bgimg_array[i].resize(canvas.winfo_width(), canvas.winfo_height())
                photo = ImageTk.PhotoImage(photo)
                canvas.create_image( 0, 0, image = photo, anchor = "nw")
      
    addbuttonnew = Button(new_window, text ='Enter', command= update )
    addbuttonnew_window = canvas_new.create_window(600,10,anchor = 'nw',window = addbuttonnew)
"""

photo1=Image.open("C:/Users/manya/Downloads/a.jpg")
photo2=Image.open("C:/Users/manya/Downloads/b.jpg")
photo3=Image.open("C:/Users/manya/Downloads/c.jpg")
photo4=Image.open("C:/Users/manya/Downloads/d.jpg")
photo5=Image.open("C:/Users/manya/Downloads/e.jpg")
photo6=Image.open("C:/Users/manya/Downloads/f.jpg")
photo7=Image.open("C:/Users/manya/Downloads/snoopy.jpeg")

bgimg_array = [photo1,photo2,photo3,photo4,photo5,photo6,photo7]
photo = ImageTk.PhotoImage(bgimg_array[i])
canvas=ttk.Canvas( window) 
canvas.pack(fill = "both", expand = True)
canvas.bind('<Configure>',si)

"""
btn_inactive = Image.open('C:/Users/manya/Downloads/button.png').resize((100,50))
btn_active = Image.open('C:/Users/manya/Downloads/button inactive.png').resize((50,50))

window.btn_inactive=ImageTk.PhotoImage(btn_inactive)
window.btn_active=ImageTk.PhotoImage(btn_active)

def onenter(event):
    Changebutton.config(image =window.btn_active)
def onleave(enter):
    Changebutton.config(image =window.btn_inactive)
"""
Changebutton = Button(window,text ='Change Background', command= change_index )
Changebutton_window = canvas.create_window(10,10,anchor = 'nw',window = Changebutton)

menu_frame = ttk.Frame(canvas, width = 350, height = 850)
label_tasks= Label(menu_frame, text='Menu',font=('Helvetica',12),fg='white')
label_tasks.pack()
menu_frame.pack_propagate(False)
menu_frame.place(x=11, y=45)

today = date.today
month= ['January', ' February','March','April','May','June','July','August','September','October','November','December']
monthcurrent_index = today.month
def changemonth_prev():
    global monthcurrent_index
    if monthcurrent_index==0: monthcurrent_index=11
    else: monthcurrent_index -=1
    updatemonthlabel()
def changemonth_next():
    global monthcurrent_index
    if monthcurrent_index == len(month) - 1:
        monthcurrent_index = 0
    else:
        monthcurrent_index += 1
    updatemonthlabel()
def updatemonthlabel():
    MonthLabel.config(text = month[monthcurrent_index])

monthchange_frame = ttk.Frame(menu_frame )
PrevMonthButton = ttk.Button(monthchange_frame,text = '<', command=changemonth_prev)
MonthLabel = ttk.Label(monthchange_frame,text = month[monthcurrent_index], anchor="center", width = 10, )
NextMonthButton = ttk.Button(monthchange_frame,text = '>',command=changemonth_next)
PrevMonthButton.pack(side=LEFT)
MonthLabel.pack(side=LEFT)
NextMonthButton.pack(side=RIGHT)


calendar_frame = ttk.Frame(menu_frame)
calendar_frame.place(x=5,y=100)


def create_calendar(year, month):
    # Create a calendar object
    cal = calendar.Calendar()
    # Get the dates of the month
    month_dates = cal.monthdayscalendar(year,month)

    # Create labels for the days of the week
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    for d, day in enumerate(days):
        labelweek = ttk.Label(calendar_frame, text=day, width = 5, background='grey')
        labelweek.grid(row=0, column=d)

    # Create labels for the dates
    for week_num, week in enumerate(month_dates, start=1):
        for day_num, day in enumerate(week, start=0):
            if day == 0:
                continue  # Placeholder for days outside the month
            labelday = ttk.Label(calendar_frame, text=day, width = 2)
            labelday.grid(row=week_num, column=day_num)

# Create the calendar for the current month
create_calendar(2024, 3)

'''
monthdisplay_frame = ttk.Frame(month_frame )
button1 = Button(monthdisplay_frame,text ='January', width = 8 ).grid(row = 0, column=1,)
button2 = Button(month_frame,text ='Feburary', width = 8 ).grid(row = 0, column=2 ,)
button3 = Button(month_frame,text ='March', width = 8  ).grid(row = 0, column= 3,)
button4 = Button(month_frame,text ='April', width = 8  ).grid(row = 0, column=4, )
button5 = Button(month_frame,text ='May',width = 8   ).grid(row = 0, column= 5,)
button6 = Button(month_frame,text ='June', width = 8  ).grid(row = 0, column= 6,)
button7 = Button(month_frame,text ='July', width = 8  ).grid(row =0 , column=7, )
'''

monthchange_frame.place(x=175, y= 45)

"""
Changebutton.bind('<Enter>',onenter)
Changebutton.bind('<Leave>',onleave)

addbutton = Button(window,text ='Add image', command= add )
addbutton_window = canvas.create_window(150,10,anchor = 'nw',window = addbutton)
"""

window.mainloop()