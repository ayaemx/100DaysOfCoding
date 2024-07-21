import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def celebrate():
    messagebox.showinfo("Congratulations!", "Welcome to the #100DaysOfCode Challenge!")
    label.config(text="Day 1: Start of an Amazing Journey!")

# Create the main window
root = tk.Tk()
root.title("100 Days of Code Challenge")
root.geometry("600x400")

# Load background image
background_image = Image.open("background.jpg")
background_image = background_image.resize((600, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Create a label with custom styles
label = tk.Label(root, text="100 Days of Code", font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333")
label_window = canvas.create_window(300, 100, anchor="center", window=label)

# Create a celebrate button with custom styles
celebrate_button = tk.Button(root, text="Start Challenge!", command=celebrate, font=("Helvetica", 16), bg="#4CAF50", fg="#ffffff", activebackground="#45a049", relief="flat")
button_window = canvas.create_window(300, 250, anchor="center", window=celebrate_button)

# Run the application
root.mainloop()
