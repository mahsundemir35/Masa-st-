import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Ekran için metin değişkeni
        self.screen_value = tk.StringVar()
        self.screen_value.set("0")

        # Ekran
        self.screen = tk.Entry(master, textvariable=self.screen_value, justify="right", font=("Arial", 20))
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Düğmeler
        button_texts = [
            "C", "+/-", "%", "/",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "=",
        ]
        self.buttons = []
        for row in range(5):
            for col in range(4):
                button_text = button_texts[row * 4 + col]
                button = tk.Button(master, text=button_text, width=5, height=2, font=("Arial", 14),
                                   command=lambda text=button_text: self.button_click(text))
                button.grid(row=row+1, column=col, padx=5, pady=5)
                self.buttons.append(button)

        # Geçmiş işlemler
        self.history = []

    # Düğmeye tıklandığında çağrılacak fonksiyon
    def button_click(self, text):
        if text == "C":
            self.screen_value.set("0")
        elif text == "+/-":
            if self.screen_value.get() != "0":
                if self.screen_value.get().startswith("-"):
                    self.screen_value.set(self.screen_value.get()[1:])
                else:
                    self.screen_value.set("-" + self.screen_value.get())
        elif text == "%":
            self.screen_value.set(str(float(self.screen_value.get()) / 100))
        elif text == "=":
            try:
                result = eval(self.screen_value.get())
                self.screen_value.set(str(result))
                self.history.append(self.screen_value.get())
            except:
                self.screen_value.set("ERROR")
        else:
            if self.screen_value.get() == "0" or self.screen_value.get() == "ERROR":
                self.screen_value.set(text)
            else:
                self.screen_value.set(self.screen_value.get() + text)

    # Geçmiş işlemleri gösteren fonksiyon
    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("History")
        history_window.geometry("300x300")
        history_text = tk.Text(history_window, font=("Arial", 12))
        history_text.insert(tk.END, "Calculation History:\n\n")
        for i, expr in enumerate(self.history):
            history_text.insert(tk.END, f"{i+1}. {expr}\n")
        history_text.pack(expand=True, fill="both")
