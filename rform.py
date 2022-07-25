from tkinter import*
root = Tk()
root.title('Registration Form')
root.geometry("500x300")

def submit_value():
    print("Your Registration form is Submitted")


Label(root,text="Registration Form", font="times 15 bold").grid(row=0,column=3)

name_user=Label(root,text="Student Name")
name_user.grid(row=1,column=2)
branch_user=Label(root, text="Branch").grid(row=2,column=2)
gender_user=Label(root, text="Gender").grid(row=3,column=2)
phone_user=Label(root, text="Contect no.").grid(row=4,column=2)
country_user=Label(root,text="Country").grid(row=5,column=2)

name_value=StringVar
branch_value=StringVar
gender_value=StringVar
phone_value=StringVar
country_value=StringVar
check_value=IntVar

name_box=Entry(root,textvariable=name_value).grid(row=1,column=3)
branch_box=Entry(root,textvariable=branch_value).grid(row=2,column=3)
gender_box=Entry(root,textvariable=gender_value).grid(row=3,column=3)
phone_box=Entry(root,textvariable=phone_value).grid(row=4,column=3)
country_box=Entry(root,textvariable=country_value).grid(row=5,column=3)

check_box=Checkbutton(text="Remember me ?").grid(row=7,column=3)

Button(text="Submit",command=submit_value).grid(row=8,column=3)

root.mainloop()
