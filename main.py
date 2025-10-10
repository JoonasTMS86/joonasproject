import Tkinter as tk

window = tk.Tk()
window.title("Joonas Project")

greeting = tk.Label(text="Welcome, user! Would you like to contribute\nto this free and open source project?\n\n" \
"Please feel free to do so.\n\nRegards,\nJoonas, the creator of this project",
height = 13,
anchor = "w",
justify = "left")
greeting.pack()

window.mainloop()
