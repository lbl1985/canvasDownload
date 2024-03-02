import tkinter as tk

def main():
    root = tk.Tk()
    
    label = tk.Label(root, text="Hello, Tkinter!")
    label.grid(row=0, column=0)
    entry = tk.Entry(root)
    entry.grid(row=0, column=1)
    entry = tk.Entry(root)
    entry.pack()
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()