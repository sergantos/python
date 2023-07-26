from tkinter import *
import calendar
import datetime
root = Tk()
root.title('Calendar')
days = []
now = datetime.datetime.now()
year = now.year
month = now.month

def prew():
    global month, year
    month -= 1
    if month == 0:
        month = 12
        year -= 1
    fill()

def next():
    global month, year
    month += 1
    if month == 13:
        month = 1
        year += 1
    fill()

def fill():
    info_label['text'] = calendar.month_name[month] + ', ' + str(year)
    month_days = calendar.monthrange(year, month)[1]
    if month == 1:
        prew_month_days = calendar.monthrange(year-1, 12)[1]
    else:
        prew_month_days = calendar.monthrange(year, month - 1)[1]
    week_day = calendar.monthrange(year, month)[0]
    for n in range(month_days):
        days[n + week_day]['text'] = n+1
        days[n + week_day]['fg'] = 'black'
        if year == now.year and month == now.month and n == now.day:
            days[n + week_day]['background'] = 'green'
        else:
            days[n + week_day]['background'] = 'lightgray'
    for n in range(week_day):
        days[week_day - n - 1]['text'] = prew_month_days - n
        days[week_day - n - 1]['fg'] = 'gray'
        days[week_day - n - 1]['background'] = '#f3f3f3'
    for n in range(6*7 - month_days - week_day):
        days[week_day + month_days + n]['text'] = n+1
        days[week_day + month_days + n]['fg'] = 'gray'
        days[week_day + month_days + n]['background'] = '#f3f3f3'
    for n in range(7):
        lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, font=('Verdana', 10, 'normal'), fg='darkblue')
        lbl.grid(row=1, column=n, sticky='nsew')
    for row in range(6):
        for col in range(7):
            lbl = Label(root, text='0', width=4, height=2, 
                        font=('Verdana', 16, 'bold'))
            lbl.grid(row=row+2, column=col, sticky='nsew')
            days.append(lbl)

fill()
root.mainloop()