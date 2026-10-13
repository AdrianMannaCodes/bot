import tkinter as tk
root = tk.Tk()
root.geometry("1000x750")
root.config(bg="#00f0f0")
count = 0
def doubleClick():
    global count 
    count -= -2
    label.config(text=f"klakojn: {count}")
label = tk.Label(
  root,
  text="Bonvenon! Alklaku la iĵon, ĝi estas sub la grandskribon.",
  font=("Arial", 24, "bold"),
  bg="#00f0f0",
  fg="#252525"
)
label.pack(pady=20)
button = tk.Button(
    root,
    text="alklaku min",
    font=("Helvetica", 16),
    bg="#10fe00",
    fg="#0a0a0a",
    relief="raised",
    bd=2,
    command=doubleClick 
)
button.pack(pady=20)
root.mainloop()
