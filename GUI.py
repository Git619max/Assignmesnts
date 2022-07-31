from tkinter import*
from PIL import ImageTk, Image
from tkinter.font import*

root=Tk()#creating the application main window
root.title("Task Reminder")
root.geometry("600x400")
HIGHT=1000
WIDTH=1000

canvas=Canvas(root,bg='#b30000',height=HIGHT,width=WIDTH)

canvas.create_text(300,35,text='Remind Me',fill='White',font=("Courier", 45, "italic"))
canvas.pack()


frame=Frame(root,bg= '#e6e6e6')
frame.place(relx=0.2,rely=0.15,relheight=0.85,relwidth=0.8)

save_reminder=PhotoImage(file='E:\project\save reminder\\save reminder.png')
Button(frame,text='Save Reminder',image=save_reminder).pack(side=BOTTOM,)

label_str=Label(frame,text='Specific Time Reminder',fg="red",bg='#e6e6e6',font=('courier',16,BOLD))
label_str.place(relx=0.11)

pt=Label(frame,text='Pick a time',bg="#e6e6e6",font=('Cambria'))
pt.place(x=90,y=25)
#drop menu for hour
menu=IntVar()
menu.set(" ")
drop=OptionMenu(frame,menu,"1",'2','3','4','5','6','7','8','9','10','11','12')
drop.place(x=60,y=50)
# #drop menu for mints
# menu=IntVar()
# menu.set(" ")
# drop=OptionMenu(frame,menu,"1",'2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22')
# drop.place(x=140,y=50)
enrty=Entry(frame,bg='#ffffff')
enrty.place(x=130,y=50,relwidth=0.1)

menu=StringVar()
menu.set(" ")
drop=OptionMenu(frame,menu,'am','pm')
drop.place(x=180,y=50)

frame1=Frame(root,bg= '#ffffff')
frame1.place(rely=0.15,relheight=0.85,relwidth=0.28)

label_tr=Label(frame1,text='What to remember?',fg="red",bg='white',font=('courier',12,BOLD,ITALIC))
label_tr.pack()

f_task=Label(frame1,text=('Tasks'),bg="#ffffff")
f_task.place(x=25,y=25)
entry=Entry(frame1,bg='#e6e6e6')
entry.pack()
entry=Entry(frame1,bg='#e6e6e6')
entry.pack()
entry=Entry(frame1,bg='#e6e6e6')
entry.pack()
root.mainloop()#Entering the event main loop
