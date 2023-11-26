# (c) Avishkar Patil
# IBM Skillbuild Cybersecurity 2023
# Steganography Tool - Hide a Secret Text Message in an Image

import cv2
import os
import tkinter as tk
from tkinter import ttk, filedialog
import sv_ttk

def encode():
    global img, msg, password, d, c

    img = cv2.imread(file_path)
    msg = entry_msg.get()
    password = entry_password.get()

    d = {}
    c = {}

    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    m = 0
    n = 0
    z = 0

    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    cv2.imwrite("encDataImg.jpg", img)
    os.system("start encDataImg.jpg")

    console_output.set("Image encoded successfully. encDataImg.jpg created.")
    print("Image encoded successfully. encDataImg.jpg created.")


def decode():
    global img, msg, password, d, c

    message = ""
    n = 0
    m = 0
    z = 0

    pas = entry_passcode.get()

    if password == pas:
        for i in range(len(msg)):
            message = message + c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        console_output.set(f"Decryption message: {message}")
        print(f"Decryption message: {message}")
    else:
        console_output.set("Key is not valid")
        print("Key is not valid")


def select_image():
    global img, file_path
    file_path = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title='Select Image File',
        filetypes=(("Image files", (".png", ".jpg", ".jpeg")), ("All files", ".*"))
    )

    if file_path:
        img = cv2.imread(file_path)

        if img is not None:
            console_output.set("Image selected successfully.")
            print("Image selected successfully.")
        else:
            console_output.set("Error: Unable to read the selected image.")
            print("Error : Unable to read the selected image.")
    else:
        console_output.set("Error: No image selected.")
        print("Error: No image selected.")


root = tk.Tk()
# root = ThemedTk(theme="arc")
root.title("Steganography Tool")
sv_ttk.set_theme("dark")

# Create and place widgets
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_title = ttk.Label(frame, text="Steganography Tool", font=("Arial", 16, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10, padx=5)

label_msg = ttk.Label(frame, text="Enter Message to Hind : ")
label_msg.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)

entry_msg = ttk.Entry(frame)
entry_msg.grid(row=2, column=1, pady=5, padx=5, sticky=tk.W)

label_password = ttk.Label(frame, text="Enter Passcode : ")
label_password.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)

entry_password = ttk.Entry(frame, show="*")
entry_password.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

btn_encode = ttk.Button(frame, text="Encode", command=encode)
btn_encode.grid(row=4, columnspan=2, pady=15, padx=5)

btn_select_image = ttk.Button(frame, text="Select Image", command=select_image)
btn_select_image.grid(row=1, columnspan=2, pady=15, padx=5)

label_passcode = ttk.Label(frame, text="Enter Passcode for Decryption : ")
label_passcode.grid(row=5, column=0, pady=5, padx=5, sticky=tk.W)

entry_passcode = ttk.Entry(frame, show="*")
entry_passcode.grid(row=5, column=1, pady=5, padx=5, sticky=tk.W)

btn_decode = ttk.Button(frame, text="Decode", command=decode)
btn_decode.grid(row=6, columnspan=2, pady=15, padx=5)

console_output = tk.StringVar()
label_console = ttk.Label(frame, textvariable=console_output, wraplength=300)
label_console.grid(row=7, column=0, columnspan=2, pady=10, padx=5, sticky=tk.W)

label_cc = ttk.Label(frame, text="- By Avishkar Patil", font=("Arial", 8))
label_cc.grid(row=7, column=1, columnspan=1, pady=10, padx=5)

root.mainloop()

































