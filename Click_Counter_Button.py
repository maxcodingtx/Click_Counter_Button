
#Click_Counter_Button - This program creates a button that tracks the amount of times you have clicked on it

import tkinter as tk

app = tk.Tk()
app.geometry("800x600")
app.title("Click Counter Button")




click_button = tk.Button(app, text="Click Here", font=('arial', 18), bg='white', height=7, width=20, command="")
click_button.place(relx=.5, rely=.33, anchor='center')


click_label_count = tk.Label(app, text="Clicks on button\n ↓", font=("arial", 18), bg='white',)
click_label_count.place(relx=.5, rely=.66, anchor='center')


click_count = tk.Label(app, font=('arial', 12), bg='white')
click_count.place(relx=.5,rely=.75,anchor='center')




app.mainloop()