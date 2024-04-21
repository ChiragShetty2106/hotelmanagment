from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from time import strftime
from datetime import datetime



class roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variable
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


        #title
        lb1_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)
        
        # 2nd image (LOGO)
        img2 = Image.open(r"C:\Users\HP\Desktop\hotel\1633410403702hotel-images 2\hotel images\logohotel.png")
        img2 = img2.resize((100, 40),Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lb2img = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lb2img.place(x=5, y=2, width=100, height=40)

        
        #LABEL FRAME
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ROOMBOOKING DETAILS",padx=2,font=("times new roman", 12, "bold"))
        Labelframeleft.place(x=5,y=50,width=425,height=490)


        #labels and entries

        #cust_CONTACT
        lbl_cust_contact=Label(Labelframeleft,text="CUSTOMER CONTACT",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_conatct=ttk.Entry(Labelframeleft,textvariable=self.var_contact,width=20,font=("arial", 13, "bold"))
        entry_conatct.grid(row=0,column=1,sticky=W)

        #fetch data btn

        btnfetch_data=Button(Labelframeleft,command=self.fetch_contact,text="FETCH",font=("arial",10, "bold"),bg="black",fg="gold",width=8)
        btnfetch_data.place(x=350,y=4)

        #CHECK IN DATE
        CHECK_IN_DATE=Label(Labelframeleft,text="CHECK_IN_DATE",font=("arial", 12, "bold"),padx=2,pady=6)
        CHECK_IN_DATE.grid(row=1,column=0,sticky=W)

        TXT_CHECK_IN=ttk.Entry(Labelframeleft,textvariable=self.var_checkin,width=29,font=("arial", 13, "bold"))
        TXT_CHECK_IN.grid(row=1,column=1)
        

        #CHECK_OUT_DATE
        CHECK_OUT_DATE=Label(Labelframeleft,text="CHECK_OUT_DATE",font=("arial", 12, "bold"),padx=2,pady=6)
        CHECK_OUT_DATE.grid(row=2,column=0,sticky=W)

        enter_check_out=ttk.Entry(Labelframeleft,textvariable=self.var_checkout,width=29,font=("arial", 13, "bold"))
        enter_check_out.grid(row=2,column=1)

        #room_type
        room_type=Label(Labelframeleft,text="ROOM_TYPE",font=("arial", 12, "bold"),padx=2,pady=6)
        room_type.grid(row=3,column=0,sticky=W)

        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomtype from details")
        ide=my_cursor.fetchall()

        combo_room_type=ttk.Combobox(Labelframeleft,textvariable=self.var_roomtype,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_room_type["value"]=ide
        combo_room_type.current(0)
        combo_room_type.grid(row=3,column=1)


        #AVAILABLE room
        lbl_avaliable_room=Label(Labelframeleft,text="AVAILABLE_ROOM",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_avaliable_room.grid(row=4,column=0,sticky=W)


        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        my_cursor.execute("select roomno from details")
        rows=my_cursor.fetchall()

        combo_roomno=ttk.Combobox(Labelframeleft,textvariable=self.var_roomavailable,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_roomno["value"]=rows
        combo_roomno.current(0)
        combo_roomno.grid(row=4,column=1)

        #txt_availableroom=ttk.Entry(Labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial", 13, "bold"))
        #txt_availableroom.grid(row=4,column=1)

        #meal
        lbl_avaliable_meal=Label(Labelframeleft,text="MEAL",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_avaliable_meal.grid(row=5,column=0,sticky=W)

        txt_available_meal=ttk.Entry(Labelframeleft,textvariable=self.var_meal,width=29,font=("arial", 13, "bold"))
        txt_available_meal.grid(row=5,column=1)

        #no_of_days
        lbl_no_of_days=Label(Labelframeleft,text="NO OF DAYS",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_no_of_days.grid(row=6,column=0,sticky=W)

        txt_no_of_days=ttk.Entry(Labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial", 13, "bold"))
        txt_no_of_days.grid(row=6,column=1)

        
        #PAID_TAX
        lbl_PAID_TAX=Label(Labelframeleft,text="PAID TAX",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_PAID_TAX.grid(row=7,column=0,sticky=W)

        txt_PAID_TAX=ttk.Entry(Labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial", 13, "bold"))
        txt_PAID_TAX.grid(row=7,column=1)

        #SUB_TOTAL
        lbl_SUB_TOTAL=Label(Labelframeleft,text="SUB TOTAL",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_SUB_TOTAL.grid(row=8,column=0,sticky=W)

        txt_SUB_TOTAL=ttk.Entry(Labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial", 13, "bold"))
        txt_SUB_TOTAL.grid(row=8,column=1)

        #TOTAL_COST
        lbl_TOTAL_COST=Label(Labelframeleft,text="TOTAL COST",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_TOTAL_COST.grid(row=9,column=0,sticky=W)

        txt_TOTAL_COST=ttk.Entry(Labelframeleft,textvariable=self.var_total,width=29,font=("arial", 13, "bold"))
        txt_TOTAL_COST.grid(row=9,column=1)

        #bill buttonn

        btnadd=Button(Labelframeleft,text="bill",command=self.total,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=10,column=0,padx=1,sticky=W)



        
        #BUTTON
        btn_frame=Frame(Labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="DELETE",command=self.mdelete,font=("arial", 12, "bold"),bg="black",fg="gold",width=8)
        btndelete.grid(row=0,column=2,padx=1)

        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnRESET.grid(row=0,column=3,padx=1)

        #RIGHTSIDE IMAGE

        img3 = Image.open(r"C:\Users\HP\Desktop\hotel\1633410403702hotel-images 2\hotel images\bed.jpg")
        img3 = img3.resize((520,300),Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lb2img = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lb2img.place(x=760, y=55, width=520, height=200)



        #TABLE FRAME search system

        TABLE_FRAME=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW details and search system",padx=2,font=("times new roman", 12, "bold"))
        TABLE_FRAME.place(x=435,y=280,width=860,height=260)

        lblsearchby=Label(TABLE_FRAME,text="search by:",font=("arial", 12, "bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(TABLE_FRAME,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_search["value"]=("CONTACT","ROOM")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()
        txtsearch=ttk.Entry(TABLE_FRAME,textvariable=self.txt_search,width=24,font=("arial", 13, "bold"))
        txtsearch.grid(row=0,column=2,padx=2)

        
        btnsearch=Button(TABLE_FRAME,text="SEARCH",command=self.search,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(TABLE_FRAME,text="SHOWALL",command=self.fetch_data,font=("arial", 12, "bold"),bg="black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=1)


        #SHOW DATA TABLE

        DETAILE_TABLe=Frame(TABLE_FRAME,bd=2,relief=RIDGE)
        DETAILE_TABLe.place(x=0,y=50,width=860,height=180)

        Scroll_x=ttk.Scrollbar(DETAILE_TABLe,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(DETAILE_TABLe,orient=VERTICAL)

        self.room_table=ttk.Treeview(DETAILE_TABLe,column=("contact","checkin","checkout","roomtype","roomavailable","meal",
                                                                   "noofdays"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_x.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact",text="CONTACT")
        self.room_table.heading("checkin",text="CHECKIN")
        self.room_table.heading("checkout",text="CHECKOUT")
        self.room_table.heading("roomtype",text="ROOMTYPE")
        self.room_table.heading("roomavailable",text="ROOMAVAILABLE")
        self.room_table.heading("meal",text="MEAL")
        self.room_table.heading("noofdays",text="NOOFDAYS")
        

        self.room_table["show"]="headings"
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noofdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursorr)
        self.fetch_data()
    
    #add btn
    def add_data(self):
        if self.var_contact.get()==""or self.var_checkin.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showwarning("success","room booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something is wrong:{str(es)}",parent=self.root)
    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
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

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])


    #update
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noofdays=%s where contact=%s",(
                    
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()   
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","room detail has been updated succesfully",parent=self.root)

    #delete
    def mdelete(self):
        mdelete=messagebox.askyesno("hotel managment system","do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            query="delete from room where contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
        
    



    #all data fetch

    def fetch_contact(self):
      if self.var_contact.get()=="":
        messagebox.showerror("Error","please enter contact number",parent=self.root)
      else:
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        query=("select name from customer where mobile=%s")
        value=(self.var_contact.get(),)
        my_cursor.execute(query,value)
        row=my_cursor.fetchone()

        if row==None:
          messagebox.showerror("Error","this number not found",parent=self.root)
        else:
          conn.commit()
          conn.close()
        #name
          showdataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
          showdataframe.place(x=450,y=55,width=300,height=180)

          lbl4name=Label(showdataframe,text="name:",font=("arial",12,"bold"))
          lbl4name.place(x=0,y=0)

          lbl=Label(showdataframe,text=row,font=("arial",12,"bold"))
          lbl.place(x=90,y=0)
         
        #gender
          conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
          my_cursor=conn.cursor()
          query=("select gender from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblgender=Label(showdataframe,text="gender:",font=("arial",12,"bold"))
          lblgender.place(x=0,y=30)

          lbl2=Label(showdataframe,text=row,font=("arial",12,"bold"))
          lbl2.place(x=90,y=30)

        #email
          conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
          my_cursor=conn.cursor()
          query=("select email from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblemail=Label(showdataframe,text="email:",font=("arial",12,"bold"))
          lblemail.place(x=0,y=60)

          lbl3=Label(showdataframe,text=row,font=("arial",12,"bold"))
          lbl3.place(x=90,y=60)

        #nationality
          conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
          my_cursor=conn.cursor()
          query=("select nationality from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lblnationality=Label(showdataframe,text="nationality:",font=("arial",12,"bold"))
          lblnationality.place(x=0,y=90)

          lbl4=Label(showdataframe,text=row,font=("arial",12,"bold"))
          lbl4.place(x=90,y=90)


        #address
          conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
          my_cursor=conn.cursor()
          query=("select address from customer where mobile=%s")
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
          row=my_cursor.fetchone()

          lbladdress=Label(showdataframe,text="address:",font=("arial",12,"bold"))
          lbladdress.place(x=0,y=120)

          lbl5=Label(showdataframe,text=row,font=("arial",12,"bold"))
          lbl5.place(x=90,y=120)

    
    #search system

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def total(self):
      indate=self.var_checkin.get()
      outdate=self.var_checkout.get()
      indate=datetime.strptime(indate,"%d/%m/%Y")
      outdate=datetime.strptime(outdate,"%d/%m/%Y")
      self.var_noofdays.set(abs(outdate-indate).days)

      if (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="LUXURY"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        tax="Rs."+str("%.2f"%((q5)*0.09))
        st="Rs."+str("%.2f"%((q5)))
        tt="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(tax)
        self.var_actualtotal.set(st)
        self.var_total.set(tt)

      elif (self.var_meal.get()=="lunch" and self.var_roomtype.get()=="SINGLE"):
        q1=float(300)
        q2=float(700)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        tax="Rs."+str("%.2f"%((q5)*0.09))
        st="Rs."+str("%.2f"%((q5)))
        tt="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(tax)
        self.var_actualtotal.set(st)
        self.var_total.set(tt)

      elif (self.var_meal.get()=="breakfast" and self.var_roomtype.get()=="DUPLEX"):
        q1=float(500)
        q2=float(1000)
        q3=float(self.var_noofdays.get())
        q4=float(q1+q2)
        q5=float(q3+q4)
        tax="Rs."+str("%.2f"%((q5)*0.09))
        st="Rs."+str("%.2f"%((q5)))
        tt="Rs."+str("%.2f"%(q5+((q5)*0.09)))
        self.var_paidtax.set(tax)
        self.var_actualtotal.set(st)
        self.var_total.set(tt)













       



if __name__ == "__main__":
    root = Tk()
    obj =roombooking(root)
    root.mainloop()

