from textwrap import fill
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, filedialog, Toplevel
import os
import sqlite3
from turtle import fillcolor
from tkinter import PhotoImage
from PIL import Image, ImageTk
from pathlib import Path
from water_app_module import WaterApp
import sys
import water



################################################################################################################################################

def create_main_menu():
    menu_frame = ttk.Frame(window)
    menu_frame.grid(row=0, column=0, sticky='nsew')
    menu_bar = tk.Menu(menu_frame)
    main_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_command(label="Электричество")
    menu_bar.add_command(label="Тепло")
    menu_bar.add_command(label="Вода")
    menu_bar.add_command(label="О Программе", command=create_about_frame)
    menu_bar.add_command(label="Выход")
   
    window.config(menu=menu_bar)

#################################################################################################################################################

def create_about_frame():
    # Destroy any existing frames
    for widget in window.winfo_children():
        widget.destroy()
    # Create main menu
    create_main_menu()
    s = ttk.Style()
    s.configure("Frame1.TFrame", background='white')
    main_frame_about = ttk.Frame(window, borderwidth=2, relief="groove", style="Frame1.TFrame")
    main_frame_about.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
    main_frame_about.columnconfigure(0, weight=1)
    about_frame_style = ttk.Style()
    about_frame_style.configure("AboutFrame.TFrame", background='#FAEBD7')  # Set the background color
    about_label_style = ttk.Style()
    about_label_style.configure("AboutFrame.TLabel", background='#FAEBD7')  # Set the background color
    about_frame = ttk.Frame(main_frame_about, borderwidth=2, relief="groove", style="AboutFrame.TFrame")
    about_frame.pack(expand=True)
    original_image = Image.open('data\\logo.png')
    # Resize the image to 200x200
    resized_image = original_image.resize((90, 90))
    # Convert the PIL Image to Tkinter PhotoImage
    logo_image = ImageTk.PhotoImage(resized_image)
    # Create and display the logo
    logo_label = ttk.Label(about_frame, image=logo_image, style="AboutFrame.TLabel")
    logo_label.image = logo_image  # to prevent garbage collection
    logo_label.pack(pady=10)
    about_text = "<APK_soft>\nCopyright © 2024 NPS\nBusiness Edition\n1.0"
    text_label = ttk.Label(about_frame, text=about_text, wraplength=300, justify='center', compound='top', style="AboutFrame.TLabel")
    text_label.pack(pady=10)
    
# ######################################################################################################################################################    

# def manage_water():
#     # Destroy any existing frames
#     for widget in window.winfo_children():
#         widget.destroy()

#     # Create main menu
#     create_main_menu()

#     water_frame = ttk.Frame(window, borderwidth=2, relief="groove", style="Frame1.TFrame")
#     water_frame.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)
#     water_frame.columnconfigure(0, weight=1)

#     # Create an instance of WaterApp and pass the parent frame
#     water_app_instance = WaterApp(water_frame)
#     water_app_instance.on_submit(submit_button)
#     #----------Firebase
#     water_app_instance = WaterApp(water_frame)
#     submit_button = ttk.Button(water_frame, text="Отправить", command=lambda: water_app_instance.on_submit(submit_button))

    
# ####################################################################################################################################################

# ##############################################################################################################################################


window = tk.Tk()
window.title('Window of widgets')
window.geometry('800x500+300+100')
window.attributes('-alpha', 0.97)

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

create_main_menu()

window.mainloop()
