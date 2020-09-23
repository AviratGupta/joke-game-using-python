import tkinter as tk
import pyjokes
root=tk.Tk()
root.geometry("300x200")
root.configure(bg = "black")
root.title("joke game")

def joke():
  global joke
  joke = pyjokes.get_joke()
  T.insert(tk.END,joke)
def clear():
  T.delete("1.0","end")
T = tk.Text(root)
T.place(x=5,height=80,width=290)
b = tk.Button(root,text="crack a joke",fg="red",bg="cyan",command=joke)
b.place(x=35,y=100,height=50,width=100)
b2 = tk.Button(root,text="clear",fg="red",bg="cyan",command=clear)
b2.place(x=180,y=100,height=50,width=100)

root.mainloop()
