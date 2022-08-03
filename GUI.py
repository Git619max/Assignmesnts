from tkinter import*
from plyer import notification
from PIL import ImageTk, Image
from tkinter.font import*
from tkinter import messagebox
from click import command
import time

root=Tk()#creating the application main window
root.title("Task Reminder")
root.geometry("600x400")
HIGHT=1000
WIDTH=1000

def get_details():
    # get_title = title.get()
    get_msg = taskentry.get()
    get_hour=hourenrty.get()
    get_min = minenrty.get()
    # print(get_title,get_msg, tt)

    if  get_msg == "" or get_hour=="" or get_min == "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(float(get_hour))
        hour_to_sec = int_time * 60 * 60
        int_time = int(float(get_min))
        min_to_sec = int_time * 60
         
        messagebox.showinfo("notifier set", "set notification ?")
        root.destroy()
        time.sleep(hour_to_sec + min_to_sec)

        notification.notify(message=get_msg,
                            app_name="Notifier",
                            # app_icon="ico.ico",
                            toast=True,
                            timeout=10)
                            

canvas=Canvas(root,bg='#b30000',height=HIGHT,width=WIDTH)
canvas.create_text(300,35,text='Remind Me',fill='White',font=("Courier", 45, "italic"))
canvas.pack()

frame=Frame(root,bg= '#e6e6e6')
frame.place(relx=0.2,rely=0.15,relheight=0.85,relwidth=0.8)

save_reminder=PhotoImage(file='E:\project\save reminder\\save reminder.png')
Button(frame,text='Save Reminder',image=save_reminder,command=get_details).pack(side=BOTTOM)

label_str=Label(frame,text='Specific Time Reminder',fg="red",bg='#e6e6e6',font=('courier',16,BOLD))
label_str.place(relx=0.11)
pt=Label(frame,text='Pick a time',bg="#e6e6e6",font=('Cambria'))
pt.place(x=90,y=25)

hourenrty=Entry(frame,bg='#ffffff')
hourenrty.place(x=80,y=50,relwidth=0.1)
minenrty=Entry(frame,bg='#ffffff')
minenrty.place(x=130,y=50,relwidth=0.1)
# ampmentry=Entry(frame,bg='#ffffff')
# ampmentry.place(x=180,y=50,relwidth=0.1)

frame1=Frame(root,bg= '#ffffff')
frame1.place(rely=0.15,relheight=0.85,relwidth=0.28)

label_tr=Label(frame1,text='What to remember?',fg="red",bg='white',font=('courier',12,BOLD,ITALIC))
label_tr.pack()

f_task=Label(frame1,text=('Tasks'),bg="#ffffff")
f_task.place(x=25,y=25)
taskentry=Entry(frame1,bg='#e6e6e6')
taskentry.pack()

root.mainloop()#Entering the event main loop
