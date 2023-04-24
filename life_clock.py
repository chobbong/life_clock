from tkinter import *
import tkinter
from datetime import datetime, timedelta

# define some colors
cor1 = "#3d3d3d"  # black
cor2 = "#21c25c"  # green

root = Tk()
root.title("Clock")
root.geometry('350x220')
root.resizable(width=False, height=False)
root.configure(background=cor1)


def calculate_time_difference(target_datetime):
    current_datetime = datetime.now()
    difference = target_datetime - current_datetime

    if difference.days < 0:
        return "Time has passed"
    else:
        return str(difference).split(".")[0]  # Remove microseconds


def update_clock():
    try:
        target_datetime = datetime.strptime(e1.get(), "%Y-%m-%d %H:%M:%S")
        time_difference = calculate_time_difference(target_datetime)

        l3.config(text="남은 시간: " + time_difference)
    except ValueError:
        l3.config(text="Invalid date format")

    l3.after(1000, update_clock)


def clock():
    time = datetime.now().strftime("%H:%M:%S")
    weekday = datetime.now().strftime("%A")
    day = datetime.now().strftime("%d")
    month = datetime.now().strftime("%B")
    year = datetime.now().strftime("%Y")
    l1.config(text=time)
    l1.after(200, clock)

    l2.config(text=weekday + " " + str(day) + "/" + str(month) + "/" + str(year))


l1 = Label(root, font=("Arial 80"), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=EW)

l2 = Label(root, font=("Arial 20"), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=EW)

l3 = Label(root, font=("Arial 20"), bg=cor1, fg=cor2)
l3.grid(row=2, column=0, sticky=EW)

e1 = Entry(root, font=("Arial 20"), bg=cor1, fg=cor2, justify=CENTER)
e1.grid(row=3, column=0, sticky=EW)
e1.insert(0, "YYYY-MM-DD HH:MM:SS")

clock()
update_clock()
root.mainloop()
