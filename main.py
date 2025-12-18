import customtkinter as ctk
from customtkinter import CTkLabel

app = ctk.CTk()
app.title("Calculator")
app.geometry("310x520")
app.resizable(False, False)

entry = ctk.CTkEntry(
    app,
    width=290,
    height=70,
    font=("Roboto Medium", 28),
    justify="right",
    fg_color="#1e1e1e",
    text_color="#ecf0f1",
    corner_radius=10,
    border_width=1,
    border_color="#34495e"
)
entry.insert(0, "0")
entry.pack(pady=20)

def button_click(value):
    if entry.get() in ["Error", "0"] and value not in ["=", "C", "⌫"]:
        entry.delete(0, "end")

    if value == "C":
        entry.delete(0, "end")
    elif value == "⌫":
        if not entry.get():
            return
        entry.delete(len(entry.get())-1, "end")
    elif value == "=":
        if not entry.get():
            return
        try:
            result = str(eval(entry.get()))
            entry.delete(0, "end")
            if result.endswith(".0"):
                entry.insert("end", result[:-2])
            else:
                entry.insert("end", result)
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    else:
        if value not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", value)
        else:
            if not entry.get():
                return
            endy = entry.get()[-1]
            if endy not in ["+", "-", "*", "/", "%", "."]:
                entry.insert("end", value)

def key_event(event):
    key = event.keysym

    if key in "0123456789":
        entry.insert("end", key)
    elif key in ["plus", "KP_Add"]:
        if not entry.get():
            return
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "+")
    elif key in ["minus", "KP_Subtract"]:
        if not entry.get():
            return
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "-")
    elif key in ["asterisk", "KP_Multiply"]:
        if not entry.get():
            return
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "*")
    elif key in ["slash", "KP_Divide"]:
        if not entry.get():
            return
        endy = entry.get()[-1]
        if endy not in ["+", "-", "*", "/", "%", "."]:
            entry.insert("end", "/")
    elif key == "Return":
        button_click("=")
    elif key == "BackSpace":
        button_click("⌫")
    elif key == "Escape":
        button_click("C")
    elif key == "period" or key == "KP_Decimal":
        entry.insert("end", ".")

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
            color = ("#f1c40f", "#f39c12")
            text_color = "black"
        elif text in ["C", "⌫"]:
            color = ("#e74c3c", "#c0392b")
            text_color = "white"
        else:
            color = ("#2c3e50", "#34495e")
            text_color = "white"

        btn = ctk.CTkButton(
            frame,
            text=text,
            width=65,
            height=65,
            font=("Arial Bold", 20),
            fg_color=color,
            text_color=text_color,
            hover_color="#95a5a6",
            corner_radius=12,
            command=lambda t=text: button_click(t)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)

app.bind("<Key>", key_event)

text = "Created by CLX | Simple ideas, Real products."
footer = CTkLabel(app, text=text, font=("Arial", 10), text_color="#bdc3c7")
footer.pack(pady=10)

app.mainloop()