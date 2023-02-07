from tkinter import *
import pandas as pd
import random

current_selection = {}

# ---------------------------- DATA ------------------------------- #
filename = "data/italian_words.csv"
try:
    data = pd.read_csv("data/word_to_learn.csv")
except FileNotFoundError:
    master_data = pd.read_csv(filename)
    to_learn = master_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

# -------------------------- WINDOW ----------------------------- #
window = Tk()
window.title("Flash Cards - Italian to English")
window.config(padx=50, pady=50)

# create a canvas to act as card
canvas = Canvas(width=500, height=526)
canvas.grid(row=0, column=0, columnspan=3)
# card data display
card_title = canvas.create_text(250, 50, text="", font=("Ariel", 60, "italic"))
card_title2 = canvas.create_text(250, 450, text="", font=("Ariel", 60, "italic"))
card_word = canvas.create_text(250, 200, text="", font=("Ariel", 40, "italic"))
card_word_reveal = canvas.create_text(250, 300, text="", font=("Ariel", 40, "italic"))


# ------------------------ FUNCTIONS --------------------------- #
def next_word():
    """choose a random word from word list - to learn"""
    global current_selection
    current_selection = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Italian Word", fill="grey")
    canvas.itemconfig(card_word, text=current_selection["Italian"], fill="white")
    # reset english related stuff
    canvas.itemconfig(card_title2, text="")
    canvas.itemconfig(card_word_reveal, text="")


def reveal_word():
    """reveals the english translation of word"""
    canvas.itemconfig(card_title2, text="English Word", fill="grey")
    canvas.itemconfig(card_word_reveal, text=current_selection["English"], fill="white")


def is_known():
    """removes the current selection from list of words"""
    to_learn.remove(current_selection)
    next_word()
    df = pd.DataFrame(to_learn)
    df.to_csv("data/word_to_learn.csv", index=False)


# ------------------------  --------------------------- #
# get a count of word list minus the headings
word_count = len(to_learn) - 1
next_word()

# Buttons
unknown_button = Button(text="Wrong", highlightthickness=0, command=next_word)
unknown_button.grid(row=1, column=0)

reveal_button = Button(text="Reveal", highlightthickness=0, command=reveal_word)
reveal_button.grid(row=1, column=1)

known_button = Button(text="Correct", highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)


window.mainloop()
