from tkinter import *

MENU = Tk()
MENU.title("MENU")
MENU.geometry("500x900")

Header1 = ("Bell MT",80)
Header2 = ("Bell MT",40)
Header3 = ("Bell MT",20)
Header4 = ("Stencil",20)
Header5 = ("Times New Roman", 12, "italic")


Text = Label(MENU, text="FRIED", font=Header1)
Text.pack()

Text1 = Label(MENU, text="❖❖❖MENU❖❖❖", font=Header2)
Text1.pack()

Text2 = Label(MENU, text="\n" + "🍔 BURGER 🍔", font=Header3)
Text2.pack()

Text4 = Label(MENU, text="Two Buns and a patty. How hard can it be?", font=Header5)
Text4.pack()

Text3 = Label(MENU, text="MASTERY: NaN%", font=Header4)
Text3.pack()
