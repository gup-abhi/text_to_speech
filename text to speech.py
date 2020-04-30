# importing tkinter module
import tkinter as tk
# importing gtts from gTTS
from gtts import gTTS
# importing playsound from playsound module
from playsound import playsound

# creating window
win = tk.Tk()
# giving title to our window
win.title("Text To Speech")
# specifying the size of our window
win.geometry("200x70")

# creating function to convert text to speech
def text_to_speech():
    # getting text that user entered into the entry field
    text = entry.get()
    # converting text to the speech
    speech = gTTS(text = text, lang = "en")
    # saving the speech
    speech.save("speech.mp3")
    # playing the speech
    playsound("speech.mp3")

# creating the label to print
label = tk.Label(win, text = "Enter here : ")
label.grid(row = 0, column = 0)

# creating a enrty field to get user text to be converted to speech
entry = tk.Entry(win)
entry.grid(row = 1, column = 0)

# creating button to convert text to speech by calling our function
button = tk.Button(win, text = "Go", command = text_to_speech)
button.grid(row = 1, column = 1)

# creating window loop
win.mainloop()
