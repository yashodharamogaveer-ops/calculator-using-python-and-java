import subprocess
import tkinter as tk
import re 
win=tk.Tk()
win.title("Calculator")
win.geometry("312x324")
win.resizable(0,0)
def click(item):
    global expression
    if item==".":
        parts=re.split(r'[\+\-\*/]', expression)
        last_number=parts[-1] 
        if '.' in last_number:
            return
    expression = expression + str(item)
    input_text.set(expression)
def clear():
    global expression
    expression = ""
    input_text.set("")
def equal():
    global expression
    if expression:
        try:
            result = result = subprocess.check_output(['python', '-c', f'print({expression})'], universal_newlines=True)
            input_text.set(result.strip())
            expression = result.strip()
        except Exception:
            input_text.set("Error")
            expression = ""
    else:
        input_text.set("Error")
expression = ""
input_text = tk.StringVar()
input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)
btns_frame = tk.Frame(win, width=312, height=272.5, bg="grey")
btns_frame.pack()
clear_btn = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide= tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click("/")).grid(row=0, column=3, padx=1, pady=1)
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click("*")).grid(row=1, column=3, padx=1, pady=1)
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(4)).grid(row=2, column=0, padx=1, pady=1)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(5)).grid(row=2, column=1, padx=1, pady=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(6)).grid(row=2, column=2, padx=1, pady=1)
subtract = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click("-")).grid(row=2, column=3, padx=1, pady=1)
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(1)).grid(row=3, column=0, padx=1, pady=1)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(2)).grid(row=3, column=1, padx=1, pady=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click("+")).grid(row=3, column=3, padx=1, pady=1)
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: equal()).grid(row=4, column=3, padx=1, pady=1)
win.mainloop()