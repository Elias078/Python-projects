import tkinter
from calendar import Calendar
from tkinter import *
import qrcode as qr
import os
from tkinter import filedialog
import pyautogui
from tkcalendar import *
from time import strftime
import time
import random


root = tkinter.Tk()

root.geometry("810x350")
root.resizable(False, False)
root.title("ALL IN ONE BRAVO")
root.config(bg='gray')


# Function Calls

# QR Code Function

def qr_code():
    def click_qrcode_btn():
        img = qr.make(entry.get())
        file_pathh = filedialog.asksaveasfilename(defaultextension='.png')
        img.save(file_pathh)

    qr_page = tkinter.Tk()
    qr_page.geometry("700x300")
    qr_page.config(bg="grey")
    qr_page.title("QR CODE GENERATOR")
    Button(qr_page, text="QR CODE GEN", width=20, height=2, command=click_qrcode_btn).place(x=20, y=40)
    entry = Entry(qr_page, width=40, font="arial 13")
    entry.place(x=200, y=40, height=50)



# PC CONTROL FUNCTION


def pc_control():
    pc_control_page = tkinter.Tk()
    pc_control_page.geometry("500x200")
    pc_control_page.resizable(False, False)
    pc_control_page.title("PC CONTROL")

    # Inner Functions
    def restart():
        os.system("shutdown /r /t 1")

    def restartT():
        os.system("shutdown /r /t 30")

    def shutdown():
        os.system("shutdown /s /t 1")

    # BTNS
    Button(pc_control_page, text="restart", font="arial 15", cursor="hand2", width=10, command=restart).place(x=10,
                                                                                                              y=70)
    Button(pc_control_page, text="restart + T", font="arial 15", cursor="hand2", width=10, command=restartT).place(
        x=160, y=70)
    Button(pc_control_page, text="shutdown", font="arial 15", cursor="hand2", width=10, command=shutdown).place(x=320,
                                                                                                                y=70)


# Screen Shot Function

def screen_shot():
    screen_shot_page = tkinter.Tk()
    screen_shot_page.geometry("300x300")
    screen_shot_page.resizable(False, False)

    def screenShot():
        myscreenshot = pyautogui.screenshot()
        file_path = filedialog.asksaveasfilename(defaultextension='.png')
        myscreenshot.save(file_path)

    btn = Button(screen_shot_page, text="TAKE SH", bg="black", fg="white", font='arial 15', command=screenShot)
    btn.pack(pady=100)


# calender function

def calender():
    calender_page = tkinter.Tk()
    mycal = Calendar(calender_page, setmode="day", date_pattern='d/m/yy')
    mycal.pack(padx=15, pady=15)
    calender_page.geometry("300x300")
    calender_page.config(bg="lightblue")
    calender_page.title("Calendar")


# Clock Function
def clock():
    clock_page = tkinter.Tk()
    clock_page.title("DIGITAL CLOCK")
    clock_page.resizable(False, False)

    def dig_clock():
        text = strftime('%H:%M:%S')
        label.config(text=text)
        label.after(1000, clock)

    label = Label(clock_page, font=('digital-7', 100, 'bold'), background='black', foreground='red')
    label.pack()
    dig_clock()

# grade Calc Function

def grad_calc():
    grad_calc_page = tkinter.Tk()
    grad_calc_page.title("GRADE CALC")
    grad_calc_page.geometry("400x350")
    grad_calc_page.resizable(False, False)

    # inner function
    def calc():
        english = int(english_entry.get())
        skills = int(skill_entery.get())
        knowledge = int(Knowledge_entry.get())

        total = (english + skills + knowledge)
        Label(grad_calc_page, text=f"{total}", font='arial 15').place(x=250, y=170)

        average = int(total / 3)
        Label(grad_calc_page, text=f"{average}", font='arial 15').place(x=250, y=210)

        if (average > 50):
            grade = "pass"
        else:
            grade = "Fail"
        Label(grad_calc_page, text=f"{grade}", font='arial 15', fg="blue").place(x=250, y=250)

    sub1 = Label(grad_calc_page, text="English", font="arial 10")
    sub2 = Label(grad_calc_page, text="Skills", font="arial 10")
    sub3 = Label(grad_calc_page, text="General Knowledge", font="arial 10")
    total = Label(grad_calc_page, text="Total", font="arial 10")
    ave = Label(grad_calc_page, text="Average", font="arial 10")
    grade = Label(grad_calc_page, text="Grade", font="arial 10")

    sub1.place(x=50, y=20)
    sub2.place(x=50, y=70)
    sub3.place(x=50, y=120)
    total.place(x=50, y=170)
    ave.place(x=50, y=210)
    grade.place(x=50, y=250)

    englishvalue = StringVar()
    skillvalue = StringVar()
    knowledgevalue = StringVar()

    english_entry = Entry(grad_calc_page, textvariable=englishvalue, font="arial 15", width=15)
    skill_entery = Entry(grad_calc_page, textvariable=skillvalue, font="arial 15", width=15)
    Knowledge_entry = Entry(grad_calc_page, textvariable=knowledgevalue, font="arial 15", width=15)

    english_entry.place(x=200, y=20)
    skill_entery.place(x=200, y=70)
    Knowledge_entry.place(x=200, y=120)

    # inner btns
    Button(grad_calc_page, text="Calculate", font="arial 10", bg='white', bd=5, command=calc).place(x=50, y=300)
    Button(grad_calc_page, text="Exit", font="arial 10", bg='white', bd=5, width=8, command=lambda: exit()).place(x=300, y=300)


# Note Pad Function

def not_pad():
    note_pad_page = tkinter.Tk()
    note_pad_page.title("MyNote")
    note_pad_page.geometry("900x800")
    note_pad_page.configure(bg="lightblue")
    note_pad_page.resizable(False, False)

    # inner Function
    def Save_File():
        open_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if open_file is None:
            return
        text = str(entry.ge)
        open_file.write(text)
        open_file.close()

    def Open_File():
        file = filedialog.askopenfile(mode='r', filetype=['text files'])
        if file is not None:
            content = file.read()
        entry.insert(INSERT, content)
    # Inner BTNS

    Button(note_pad_page, text="Save File", command=Save_File).place(x=200, y=10)
    Button(note_pad_page, text="Open File", command=Open_File).place(x=650, y=10)
    entry = Text(note_pad_page, width=100, height=42, wrap=WORD, font=90).place(y=60)

# Roll dice function

def roll_dice():
    roll_dice_page = tkinter.Tk()
    roll_dice_page.title("Roll Dice")
    roll_dice_page.geometry("700x450")
    roll_dice_page.resizable(False, False)
    lable = Label(roll_dice_page, text="", font=('times', 250))

    # Inner Function
    def roll():
        dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        lable.configure(text=f'{random.choice(dice)}{random.choice(dice)}')
        lable.pack()
    # Inner Buttons

    btn = Button(roll_dice_page, text="Click The Button", font=30, bg="black",
                 fg="white", width=40, height=5, command=roll)
    btn.pack(pady=10, padx=10)

# Labels

Label(root, text="Home Page of All In One Bravo", bg='gray', font="arial 25").place(x=100, y=10)

# Root Buttons
Button(root, text="QR CODE GEN", width=20, height=2, command=qr_code).place(x=20, y=80)
Button(root, text="PC Control", width=20, height=2, command=pc_control).place(x=220, y=80)
Button(root, text="SCREEN SHOT", width=20, height=2, command=screen_shot).place(x=420, y=80)
Button(root, text="Calender", width=20, height=2, command=calender).place(x=620, y=80)
Button(root, text="CLOCK", width=20, height=2, command=clock).place(x=20, y=150)
Button(root, text="GRADE CALC", width=20, height=2, command=grad_calc).place(x=220, y=150)
Button(root, text="NOTE PAD", width=20, height=2, command=not_pad).place(x=420, y=150)
Button(root, text="ROLL DICE", width=20, height=2, command=roll_dice).place(x=620, y=150)
Button(root, text="Exit", font="bold 10", bg='pink',width=20, height=2, bd=5, command=lambda: exit()).place(x=310,y=250)


root.mainloop()
