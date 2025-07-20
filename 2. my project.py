# relief ---> gives border styles
# borderwidth---> to fix border's width



import tkinter as tk

from PIL import Image, ImageTk

import mysql.connector

from tkinter import messagebox


conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="12345",
    database="morning11",

)
def savedata():
    name = box1.get()
    email = box2.get()
    phone = box3.get()
    message = box4.get("1.0", tk.END)

    cursor = conn.cursor()
    query = "INSERT INTO contactinfo (fullname, email, phone_no, message) VALUES (%s, %s, %s, %s)"
    values = (name, email, phone, message)
    cursor.execute(query, values)
    conn.commit()

    messagebox.showinfo("Data Saved", "Your Message saveed sucessfuly in Database..")


    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END)
    box4.delete("1.0", tk.END)

    showinfo.config(text = f"Thank you! {name} ! We Will connect shortly")




app= tk.Tk()

app.geometry("1080x630")
app.title("MY CONTACT US FORM")
app. config(background="#c3f7d9")


frame1=tk.Frame(app,relief="ridge" ,borderwidth=20, bg="#5fde94",)
frame1.pack(fill="x")

contact_lbl=tk.Label(frame1, text= "CONTACT US FORM", font=("robort",30 ,"bold"),bg="#5fde94",fg="#1c5735")
contact_lbl.pack()


frame2=tk.Frame(app,relief="groove",borderwidth=20,bg="#5fde94"  )
frame2.pack(fill="x")

open_img= Image.open("contact.jpg")
read_img=ImageTk.PhotoImage(open_img)

img_label=tk.Label(frame2, image=read_img,height=200)
img_label.pack()


# now we make frame 3, which we divide in frame4 & 5 
frame3=tk.Frame(app,relief="sunken",borderwidth=20,bg="#5fde94"  )
frame3.pack(fill="x")

frame4=tk.Frame(frame3)
frame4.grid(row=0, column=0)

frame5=tk.Frame(frame3)
frame5.grid(row=0, column=1)


# now we make labels of contact form i.e.- name, mobile, ...

lbl1=tk.Label(frame4, text="Name",font=("robort",20 ,"bold"))
lbl2=tk.Label(frame4, text="E-Mail",font=("robort",20 ,"bold"))

lbl3=tk.Label(frame5, text="Phone",font=("robort",20 ,"bold"))
lbl4=tk.Label(frame5, text="Message",font=("robort",20 ,"bold"))

lbl5=tk.Label(frame4, text=":",font=("robort",20 ,"bold"))
lbl6=tk.Label(frame4, text=":",font=("robort",20 ,"bold"))
lbl7=tk.Label(frame5, text=":",font=("robort",20 ,"bold"))
lbl8=tk.Label(frame5, text=":",font=("robort",20 ,"bold"))

box1=tk.Entry(frame4,font=("robort",20))
box2=tk.Entry(frame4,font=("robort",20))
box3=tk.Entry(frame5,font=("robort",20))
box4=tk.Text(frame5,font=("robort",20),width=20, height=2)

lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1,pady=18)
lbl5.grid(row=1,column=2)
lbl6.grid(row=2,column=2)
box1.grid(row=1,column=3)
box2.grid(row=2,column=3)


lbl3.grid(row=1,column=1)
lbl4.grid(row=2,column=1,pady=18)
lbl7.grid(row=1,column=2)
lbl8.grid(row=2,column=2)
box3.grid(row=1,column=3)
box4.grid(row=2,column=3)

# spaces-->
space1=tk.Label(frame4, text="")
space1.grid(row=0,column=0, padx=40,pady=5)

space2=tk.Label(frame5, text="")
space2.grid(row=0,column=0, padx=40,pady=5)

frame6 = tk.Frame(app)
frame6.pack(fill = "x")

btn = tk.Button(frame6, text = "Send Message", font = ("robort", 18, "bold"), bg="#5fde94",fg="#1c5735", command=savedata)
btn.pack(pady=10)

showinfo=tk.Label(frame6, text= "",bg="#a4dbbc")
showinfo.pack(fill="x", pady=7)


app.mainloop( )



# new chages--->

# changes through onlinw github