import tkinter as tk

root = tk.Tk()
root.title('My First Applictaion')
tk.Label(root,text='Hello',fg='red',bg='black').pack()
tk.Entry(root).pack()
root.mainloop()


