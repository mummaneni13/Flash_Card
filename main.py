import random
from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

to_learn={}
current_card={}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


#-------------------------------------------------------------------------------------------------------------------------------------------

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(to_learn)
    canvas.itemconfig(title, text="French",fill="black")
    canvas.itemconfig(word,text = current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(4000, func=flip_card)

def flip_card():
    canvas.itemconfig(title, text="English",fill="white")
    canvas.itemconfig(word, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data=pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


#-------------------------------------------------------------------------------------------------------------------------------------------
window = Tk()
window.title("Flashcard")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(4000,func=flip_card)

canvas = Canvas(width=800,height=526,)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_img)
title=canvas.create_text(400,150,text="",font=("arial",40,"italic"))
word = canvas.create_text(400,263,text="",font=("arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)


wrong_img =PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)


right_img =PhotoImage(file="images/right.png")
right_button=Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

next_card()


window.mainloop()

