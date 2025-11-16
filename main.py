import customtkinter as ctk
import tkinter as tk
from tkinter import *
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt
import traceback
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # convert graph to image

app = ctk.CTk()

app.title("Stock Dashboard  📈")
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")
app.geometry("700x500")
app.resizable(False, False)

# Frame
frame = ctk.CTkFrame(master=app)
frame.pack(padx=20, pady=20, fill="both", expand=True)
frame.columnconfigure(0, weight=1)  # Allow textbox to expand
frame.columnconfigure(1, weight=0)  # Keep button compact

# text-box / search-box
textbox=ctk.CTkTextbox(master=frame,width =350,height= 40) 
textbox.grid(row=0,column = 0,padx=(10,5),pady=10,sticky = "ew")

text = """ Enter  """
textbox.insert("0.0",text)   # enter stock name

# Canvas for Matplotlib graph (graph to image)
canvas_frame = ctk.CTkFrame(master=frame, fg_color="white", width=500, height=400)
canvas_frame.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

# Function to fetch data and plot graph as image 
# Take input from search-bar , press button , allow button_function to "get" input data 
# Take get input to fetch the stock data from y finace , if exit print image(graph-image) else "not valid stock name"
def button_function1 ():
    stock_name = textbox.get("0.0","end").strip().upper()
    
    if stock_name == "Enter " or stock_name == "":
        print( "⚠ please enter a valid stock name ")
    
    # time
    end = dt.datetime.now()
    start = dt.datetime(2010,1,1)
    
    try :  #code that can handle errors gracefully without crashing the entire program
        df = yf.download(stock_name, start=start, end=end)

        if df.empty:  # stock_name not exist
            print(" ⚠ Invalid Stock Name !")
            return 
        # else
        for widget in canvas_frame.winfo_children():
            widget.destroy()                   # iterates through all child widgets inside canvas_frame and destroys them to prevent overlapping graphs so remove the previous one
        
        #fig = figure and ax=axis for image
        fig, ax = plt.subplots(figsize=(6, 4), dpi=100)  # depth per inch
        ax.plot(df.index, df['Close'], label=stock_name, color='blue')
        ax.set_xlabel("Year")
        ax.set_ylabel("Stock Price")
        ax.set_title(f"{stock_name} Stock Price Over Time")
        ax.legend()
        ax.grid()

        # embed matplotlib graph to Tkinter - laabel as image
        canvas= FigureCanvasTkAgg(fig,master=canvas_frame)
        canvas.get_tk_widget().pack(fill=BOTH, expand=True)
        canvas.draw()

    except Exception as e :
        print(f"Error:{e}")  # handel error


# button
button = ctk.CTkButton(
    master=frame,
    text="🔍  Search",
    command= button_function1,
    width=100,
    height=40,
)
button.grid(row=0, column=1, pady=10, padx=(5, 10))

app.mainloop()


