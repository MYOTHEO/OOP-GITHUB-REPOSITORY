import tkinter as tk


root = tk.Tk()
root.title("OOP")
root.geometry("400x300")
root.configure(bg="CYAN")

pangalan = tk.Entry(root)
pangalan.grid(row=0, column=0, padx=20)

counter = 1 
def iprint():
    global counter
    print(f"{counter}. {pangalan.get()}")
    counter +=1

button_print = tk.Button(root, text="Print", command=iprint)
button_print.grid(row=0, column=1, padx=20, pady=20)
    
root.mainloop()