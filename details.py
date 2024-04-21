from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime



class detailsroom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

    
        #title
        lb1_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)
        
        # 2nd image (LOGO)
        img2 = Image.open(r"C:\Users\HP\Desktop\hotel\1633410403702hotel-images 2\hotel images\logohotel.png")
        img2 = img2.resize((100, 40),Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lb2img = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lb2img.place(x=5, y=2, width=100, height=40)

        
        #LABEL FRAME
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="NEW ROOM ADD",padx=2,font=("times new roman", 12, "bold"))
        Labelframeleft.place(x=5,y=50,width=540,height=350)


        
        #labels and entries

        #FLOOR
        lbl_FLOOR=Label(Labelframeleft,text="FLOOR",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_FLOOR.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_FLOOR=ttk.Entry(Labelframeleft,textvariable=self.var_floor,width=20,font=("arial", 13, "bold"))
        entry_FLOOR.grid(row=0,column=1,sticky=W)

        #ROOM NO
        lbl_ROOM_NO=Label(Labelframeleft,text="ROOM NO",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_ROOM_NO.grid(row=1,column=0,sticky=W)
        self.var_roomno=StringVar()

        entry_ROOM_NO=ttk.Entry(Labelframeleft,textvariable=self.var_roomno,width=20,font=("arial", 13, "bold"))
        entry_ROOM_NO.grid(row=1,column=1,sticky=W)

        #ROOM TYPE
        lbl_ROOM_TYPE=Label(Labelframeleft,text="ROOM TYPE",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_ROOM_TYPE.grid(row=2,column=0,sticky=W)
        self.var_roomtype=StringVar()

        entry_ROOM_TYPE=ttk.Entry(Labelframeleft,textvariable=self.var_roomtype,width=20,font=("arial", 13, "bold"))
        entry_ROOM_TYPE.grid(row=2,column=1,sticky=W)


        
        #BUTTON
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial", 12, "bold"),bg="black",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)

        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnRESET.grid(row=0,column=3,padx=1)

        #TABLE FRAME 

        TABLE_FRAME=LabelFrame(self.root,bd=2,relief=RIDGE,text="SHOW ROOM DETAILS",padx=2,font=("times new roman", 12, "bold"))
        TABLE_FRAME.place(x=600,y=55,width=600,height=350)

        Scroll_x=ttk.Scrollbar(TABLE_FRAME,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(TABLE_FRAME,orient=VERTICAL)
        self.room_table=ttk.Treeview(TABLE_FRAME,column=("floor","roomno","roomtype"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_x.set)
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)
        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor",text="FLOOR")
        self.room_table.heading("roomno",text="ROOM NO")
        self.room_table.heading("roomtype",text="ROOM TYPE")
        
        
        self.room_table["show"]="headings"
        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomtype",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursorr)
        self.fetch_data()


    #add btn
    def add_data(self):
        if self.var_floor.get()==""or self.var_roomtype.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                    self.var_floor.get(),
                    self.var_roomno.get(),
                    self.var_roomtype.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showwarning("success","room added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something is wrong:{str(es)}",parent=self.root)

    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #get cursor
    def get_cursorr(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomtype.set(row[2])

    #update
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set floor=%s,roomtype=%s where roomno=%s",(
                    
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get(),
                      
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","new room detail has been updated succesfully",parent=self.root)
        
    #delete
    def mdelete(self):
        mdelete=messagebox.askyesno("hotel managment system","do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            query="delete from details where roomno=%s"
            value=(self.var_roomno.get(),)
            my_cursor.execute(query,value)
            
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomtype.set("")





if __name__ == "__main__":
    root = Tk()
    obj =detailsroom(root)
    root.mainloop()