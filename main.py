import customtkinter as ctk

app = ctk.CTk()
app.title("Calculator")
app.geometry("300x450")
app.resizable(False,False)

#Natija oynachasi
entry = ctk.CTkEntry(app, width=280, height=60, font=("Arial", 25), justify="right")
entry.pack(pady=20)

#Tugmalar bosilganda ishlaydigan funksiya
def button_click(value):
    if value == "C":
        entry.delete(0, "end")
    elif value == "⌫":
        entry.delete(len(entry.get())-1, "end")
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, "end")
            entry.insert("end", str(result))
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    else:
        if value not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", value)
        else:
            endy = entry.get()[-1]
            if endy not in ["+", "-", "*", "/", "%", "."]:
                entry.insert("end", value)

#Klaviyatura bilan ishlash
def key_event(event):
    key = event.keysym

    if key in "0123456789":
        entry.insert("end", key)
    elif key in ["plus", "KP_Add"]:
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "+")
    elif key in ["minus", "KP_Subtract"]:
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "-")
    elif key in ["asterisk", "KP_Multiply"]:
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "*")
    elif key in ["slash", "KP_Divide"]:
        entry.insert("end", "/")
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "/")
    elif key == "Return":  # Enter
        button_click("=")
    elif key == "BackSpace":
        button_click("⌫")
    elif key == "Escape":
        button_click("C")
    elif key == "period" or key == "KP_Decimal":
        entry.insert("end", ".")

#Tugmalar ro'ytxati
buttons = [
    ["C", "⌫", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["00", "0", ".", "="]
]

frame = ctk.CTkFrame(app)
frame.pack()

for i, row in enumerate(buttons):
    for j, text in enumerate(row):
        if text in ["+", "-", "*", "/", "=", "%"]:
            color = ("#f1c40f", "#f39c12") # sariqga yaqin rang
            text_color = "black"
        elif text in ["C", "⌫"]:
            color = ("#e74c3c", "#c0392b") # qizilroq
            text_color = "white"
        else:
            color = ("#2c3e50", "#34495e") # navy
            text_color = "white"

        btn = ctk.CTkButton(frame, text = text, width=60, height=60,
                            font=("Arial", 18),
                            fg_color=color,
                            text_color=text_color,
                            hover_color="#95a5a6",
                            command=lambda t=text: button_click(t))
        btn.grid(row=i, column=j, padx=5, pady=5)

#Klaviyatura eventini ulash
app.bind("<Key>", key_event)
app.mainloop()
