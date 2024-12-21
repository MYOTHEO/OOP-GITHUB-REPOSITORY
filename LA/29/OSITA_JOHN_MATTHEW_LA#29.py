import tkinter as tk

root = tk.Tk()
root.title("OOP")
root.geometry("400x300")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="OOP LA29 JOHN_MATTHEW_OSITA BSIT 2A")
label.grid(row=0, column=0, padx=10, pady=10)
root.mainloop()