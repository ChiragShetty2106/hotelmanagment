from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox



class cust_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variable
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()
        


        #title
        lb1_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 15, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lb1_title.place(x=0, y=0, width=1295, height=50)

        # 2nd image (LOGO)
        img2 = Image.open(r"C:\Users\HP\Desktop\hotel\1633410403702hotel-images 2\hotel images\logohotel.png")
        img2 = img2.resize((100, 40),Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lb2img = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lb2img.place(x=5, y=2, width=100, height=40)

        #LABEL FRAME
        Labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="customer details",padx=2,font=("times new roman", 12, "bold"))
        Labelframeleft.place(x=5,y=50,width=425,height=490)

        #labels and entries

        #cust_ref
        lbl_cust_ref=Label(Labelframeleft,text="CUSTOMER ref",font=("arial", 12, "bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(Labelframeleft,textvariable=self.var_ref,width=29,font=("arial", 13, "bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        
        #cust_name
        cname=Label(Labelframeleft,text="CUSTOMER NAME",font=("arial", 12, "bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(Labelframeleft,textvariable=self.var_cust_name,width=29,font=("arial", 13, "bold"))
        txtcname.grid(row=1,column=1)

        #mother name
        mname=Label(Labelframeleft,text="MOTHER NAME",font=("arial", 12, "bold"),padx=2,pady=6)
        mname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(Labelframeleft,textvariable=self.var_mother,width=29,font=("arial", 13, "bold"))
        txtmname.grid(row=2,column=1)

        #gender combobox
        gender=Label(Labelframeleft,text="GENDER",font=("arial", 12, "bold"),padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(Labelframeleft,textvariable=self.var_gender,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_gender["value"]=("MALE","FEMALE")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #postcode
        pcode=Label(Labelframeleft,text="POSTCODE",font=("arial", 12, "bold"),padx=2,pady=6)
        pcode.grid(row=4,column=0,sticky=W)
        txtpcode=ttk.Entry(Labelframeleft,textvariable=self.var_post,width=29,font=("arial", 13, "bold"))
        txtpcode.grid(row=4,column=1)

        #phone numbr
        number=Label(Labelframeleft,text="PHONE NUMBER",font=("arial", 12, "bold"),padx=2,pady=6)
        number.grid(row=5,column=0,sticky=W)
        txtnumber=ttk.Entry(Labelframeleft,textvariable=self.var_mobile,width=29,font=("arial", 13, "bold"))
        txtnumber.grid(row=5,column=1)

        #email
        name=Label(Labelframeleft,text="EMAIL",font=("arial", 12, "bold"),padx=2,pady=6)
        name.grid(row=6,column=0,sticky=W)
        txtname=ttk.Entry(Labelframeleft,textvariable=self.var_email,width=29,font=("arial", 13, "bold"))
        txtname.grid(row=6,column=1)

        #nationality combo
        nationality=Label(Labelframeleft,text="NATIONALITY",font=("arial", 12, "bold"),padx=2,pady=6)
        nationality.grid(row=7,column=0,sticky=W)

        combo_nation=ttk.Combobox(Labelframeleft,textvariable=self.var_nationality,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_nation["value"]=("INDIAN","AMERICAN","SOUTH-AFRICAN","RUSSIAN")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)


        #ID PROOF combo
        idproof=Label(Labelframeleft,text="idproof",font=("arial", 12, "bold"),padx=2,pady=6)
        idproof.grid(row=8,column=0,sticky=W)

        combo_PROOF=ttk.Combobox(Labelframeleft,textvariable=self.var_id_proof,font=("arial", 12, "bold"),width=27,state="readonly")
        combo_PROOF["value"]=("DRIVING LICENCE","BIRTHCERTIFICATE","VOTERID")
        combo_PROOF.current(0)
        combo_PROOF.grid(row=8,column=1)


        #id number
        idnumber=Label(Labelframeleft,text="ID NUMBER",font=("arial", 12, "bold"),padx=2,pady=6)
        idnumber.grid(row=9,column=0,sticky=W)
        txtidnumber=ttk.Entry(Labelframeleft,textvariable=self.var_id_number,width=29,font=("arial", 13, "bold"))
        txtidnumber.grid(row=9,column=1)

        #ADDRESS
        aname=Label(Labelframeleft,text="ADDRESS",font=("arial", 12, "bold"),padx=2,pady=6)
        aname.grid(row=10,column=0,sticky=W)
        txtaname=ttk.Entry(Labelframeleft,textvariable=self.var_address,width=29,font=("arial", 13, "bold"))
        txtaname.grid(row=10,column=1)


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

        #TABLE FRAME search system
        TABLE_FRAME=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW details and search system",padx=2,font=("times new roman", 12, "bold"))
        TABLE_FRAME.place(x=435,y=50,width=860,height=490)

        lblsearchby=Label(TABLE_FRAME,text="search by:",font=("arial", 12, "bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(TABLE_FRAME,textvariable=self.search_var,font=("arial", 12, "bold"),width=24,state="readonly")
        combo_search["value"]=("mobile","ref")
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
        DETAILE_TABLe.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(DETAILE_TABLe,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(DETAILE_TABLe,orient=VERTICAL)

        self.cust_details_table=ttk.Treeview(DETAILE_TABLe,column=("ref","name","mother","gender","post","mobile",
                                                                   "email","nationality","idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_x.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.cust_details_table.xview)
        Scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref",text="REFER NO")
        self.cust_details_table.heading("name",text="NAME")
        self.cust_details_table.heading("mother",text="MOTHER NAME")
        self.cust_details_table.heading("gender",text="GENDER")
        self.cust_details_table.heading("post",text="POSTCODE")
        self.cust_details_table.heading("mobile",text="MOBILE")
        self.cust_details_table.heading("email",text="EMAIL")
        self.cust_details_table.heading("nationality",text="NATIONALITY")
        self.cust_details_table.heading("idproof",text="ID PROOF")
        self.cust_details_table.heading("idnumber",text="ID NUMBER")
        self.cust_details_table.heading("address",text="ADDRESS")

        self.cust_details_table["show"]="headings"
        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name",width=100)
        self.cust_details_table.column("mother",width=100)
        self.cust_details_table.column("gender",width=100)
        self.cust_details_table.column("post",width=100)
        self.cust_details_table.column("mobile",width=100)
        self.cust_details_table.column("email",width=100)
        self.cust_details_table.column("nationality",width=100)
        self.cust_details_table.column("idproof",width=100)
        self.cust_details_table.column("idnumber",width=100)
        self.cust_details_table.column("address",width=100)

        self.cust_details_table.pack(fill=BOTH,expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cursorr)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()==""or self.var_mother.get()=="":
            messagebox.showerror("Error","all fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showwarning("success","customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("warning",f"something is wrong:{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursorr(self,event=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("error","please enter mobile number",parent=self.root)

        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set name=%s,mother=%s,gender=%s,post=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s where ref=%s",(
                    
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("update","customer detail has been updated succesfully",parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("hotel managment system","do you want delete this customer",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
            my_cursor=conn.cursor()
            query="delete from customer where ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
            self.fetch_data()
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    
    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_id_proof.set(""),
        self.var_id_number.set(""),
        self.var_address.set("")
       
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
    
    #search system
    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="chirag989",database="hh")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj =cust_win(root)
    root.mainloop()

