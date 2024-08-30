import tkinter as tk
import random
import time

class TMTA:
    def __init__(self, root):
        self.root = root
        self.root.title("TMT-A Test")
        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        self.start_time = None
        self.current_num = 1
        self.buttons = []
        self.generate_buttons()

    def generate_buttons(self):
        positions = [(x, y) for x in range(100, 500, 100) for y in range(100, 500, 100)]
        random.shuffle(positions)

        for i in range(1, 26):
            btn = tk.Button(self.root, text=str(i), command=lambda i=i: self.on_button_click(i))
            x, y = positions.pop()
            self.canvas.create_window(x, y, window=btn)
            self.buttons.append(btn)

    def on_button_click(self, number):
        if number == self.current_num:
            if number == 1:
                self.start_time = time.time()
            if number == 25:
                end_time = time.time()
                total_time = end_time - self.start_time
                tk.messagebox.showinfo("TMT-A Test", f"Test completed in {total_time:.2f} seconds")
                self.root.quit()
            self.current_num += 1

if __name__ == "__main__":
    root = tk.Tk()
    app = TMTA(root)
    root.mainloop()
