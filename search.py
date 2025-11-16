import customtkinter as ctk
import tkinter as tk
from tkinter import *

app = ctk.CTk()

app.title("Stock Dashboard")
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
app.geometry("700x550")

# Frame
frame = ctk.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)
frame.columnconfigure(0, weight=1)  # Allow textbox to expand
frame.columnconfigure(1, weight=0)  # Keep button compact

# text-box
textbox=ctk.CTkTextbox(master=frame,width =350,height= 40) 
textbox.grid(row=0,column = 0,padx=(10,5),pady=10,sticky = "ew")

text = """ Enter stock name... """
textbox.insert("0.0",text)  

# button                 -- fetch data from text-box
def button_event ():
    data = textbox.get("0.0","end")  # save data
    my_data.set(str(data))           # set data to my data
button = ctk.CTkButton(master=frame,text="🔍  Search",command= button_event
                       ,width=100,height=40)
button.grid(row=0,column=1,pady=10,padx=(5, 10))

#
my_data=tk.StringVar()
# label
label =ctk.CTkLabel(master=frame,
                    # text="LABEL",
                    textvariable = my_data,       # make a variable
                    width = 500,height=400,fg_color="white",corner_radius=8)
label.grid(padx=10,pady=10,row=1,column=0,columnspan=2,sticky="ew")


app.mainloop()
