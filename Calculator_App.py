import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")

        # Entry widget for displaying the result
        self.entry = tk.Entry(root, width=20, font=("Arial", 14), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]

        self.row_val = 1
        self.col_val = 0

        for button_text in self.buttons:
            tk.Button(root, text=button_text, width=5, height=2, command=lambda b=button_text: self.on_click(b)).grid(row=self.row_val, column=self.col_val)
            self.col_val += 1
            if self.col_val > 3:
                self.col_val = 0
                self.row_val += 1

    def on_click(self, button_text):
        current_text = self.entry.get()

        if button_text == "=":
            try:
                result = eval(current_text)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif button_text == "C":
            self.entry.delete(0, tk.END)
        else:
            self.entry.insert(tk.END, button_text)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
