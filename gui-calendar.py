from tkinter import *
import calendar

def show_cal():
    fetch_cal=int(year_field.get())
    cal_window=Tk()
    cal_window.config(background='white')
    cal_window.title(f"Calender of the year {fetch_cal}")
    cal_window.geometry("550x600")
    cal_data=calendar.calendar(fetch_cal)
    cal_year=Label(cal_window,text=cal_data,font="Consolas 10 bold")
    cal_year.grid(row=6,column=1,padx=10)

    cal_window.mainloop()


if __name__ == '__main__':
    main_window=Tk()

    main_window.config(background='white')

    main_window.title("CALENDAR")

    main_window.geometry("250x140")

    year = Label(main_window, text="Enter Year", bg="light green")

    year_field = Entry(main_window)

    show_btn = Button(main_window, text="Show Calendar", fg="Black",bg="Light Blue",command=show_cal)
    exit_btn = Button(main_window,text='EXIT',fg='Black',bg='Red',command=exit)

    year.grid(row=1,column=2)
    year_field.grid(row=2,column=2)
    show_btn.grid(row=3,column=2)
    exit_btn.grid(row=4,column=2)

    main_window.mainloop()