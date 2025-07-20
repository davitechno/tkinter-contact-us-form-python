import tkinter as tk

# pip install pillow         ---> in cmd window for image rnning

from PIL import Image, ImageTk

app= tk.Tk()

app.geometry("600x500")

img = Image.open("nature.jpg")
new_img= ImageTk.PhotoImage(img)

lbl= tk.Label(app, image= new_img, width=600)
lbl.pack()

app.mainloop()





def savedata():
    name= box1.get()
    email= box2.get()
    phone= box3.get()
    message=box4.get("1.0", tk.END)

    curser.execute(f"insert into contactinfo(fullname,email,phone_no,message) values ('{name}', {email}, '{phone}', '{message}';")

    conn.commit()

    messagebox.showinfo("Data Saved", "Your Message saveed sucessfuly in Database..")


    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END)
    box4.delete("1.0", tk.END)

    showinfo.config(text = f"Thank you! {name} ! We Will connect shortly")
    
