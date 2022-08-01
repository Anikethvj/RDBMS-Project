

# CLIENT SIDE

from tkinter import *
import tkinter.messagebox
#import backend

class match:

    
    def __init__(self, root):
        self.root=root
        self.root.title("Online Match Ticket Booking System")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg="#1e3d59")

        
        match_id=StringVar()
        ticket_id=StringVar()
        """ match_no=StringVar() """

        #Fuctions
        def iExit():
            iExit=tkinter.messagebox.askyesno("Online Ticket Management System", "Do you want to exit?")
            if iExit>0:
                root.destroy()
            return

        def disdata():
            matchList.delete(0,END)
            for row in backend.viewMatches():
                matchList.insert(END, row, str(""))
            for row in backend.viewticket():
                matchList.insert(END, row, str(""))

        def searchdb():
            matchList.delete(0,END)
            for row in backend.SearchMatchData(match_id.get(),ticket_id.get()):
                matchList.insert(END, row, str(""))
                
        def matchrec(event):
            global sd
            searchmatch=matchList.curselection()[0]
            sd=matchList.get(searchmatch)
            self.txtmatch_id.delete(0,END)
            self.txtmatch_id.insert(END,sd[1])
            self.txtticket_id.delete(0,END)
            self.txtticket_id.insert(END,sd[2])
            """ self.txtmatch_no.delete(0,END)
            self.txtmatch_no.insert(END,sd[3]) """

    
        #Frames
        MainFrame=Frame(self.root, bg="#1e3d59")
        MainFrame.grid()

        TFrame=Frame(MainFrame, bd=5, padx=54, pady=8, bg="#1e3d59", relief=RIDGE)
        TFrame.pack(side=TOP)

        self.TFrame=Label(TFrame, font=('Arial', 51, 'bold'), text="ONLINE MATCH TICKET BOOKING SYSTEM", bg="#1e3d59", fg="#f5f0e1")
        self.TFrame.grid() 

        BFrame=Frame(MainFrame, bd=2, width=1350, height=70, padx=18, pady=10, bg="#1e3d59", relief=RIDGE)
        BFrame.pack(side=BOTTOM)

        DFrame=Frame(MainFrame, bd=2, width=1300, height=400, padx=20, pady=20, bg="#1e3d59", relief=RIDGE)
        DFrame.pack(side=BOTTOM)

        DFrameL=LabelFrame(DFrame, bd=2, width=1000, height=600, padx=20, bg="#1e3d59", relief=RIDGE, font=('Arial', 20, 'bold'), text="Match Information\n", fg="#f5f0e1")
        DFrameL.pack(side=LEFT)

        DFrameR=LabelFrame(DFrame, bd=2, width=450, height=300, padx=31, pady=3, bg="#1e3d59", relief=RIDGE, font=('Arial', 20, 'bold'), text="Match Details\n", fg="#f5f0e1")
        DFrameR.pack(side=RIGHT)

        #Labels & Entry Box

        self.lblmatch_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="match ID:", padx=2, pady=2, bg="#1e3d59", fg="#f5f0e1")
        self.lblmatch_id.grid(row=0, column=0, sticky=W)
        self.txtmatch_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_id, width=39, bg="#1e3d59", fg="#f5f0e1")
        self.txtmatch_id.grid(row=0, column=1) 

        self.lblticket_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Ticket ID:", padx=2, pady=2, bg="#1e3d59", fg="#f5f0e1")
        self.lblticket_id.grid(row=1, column=0, sticky=W)
        self.txtticket_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=ticket_id, width=39, bg="#1e3d59", fg="#f5f0e1")
        self.txtticket_id.grid(row=1, column=1) 

        """ self.lblmatch_id=Label(DFrameL, font=('Arial', 18, 'bold'), text="Match Number:", padx=2, pady=2, bg="#1e3d59", fg="#f5f0e1")
        self.lblmatch_id.grid(row=2, column=0, sticky=W)
        self.txtmatch_id=Entry(DFrameL, font=('Arial', 18, 'bold'), textvariable=match_no, width=39, bg="#1e3d59", fg="#f5f0e1")
        self.txtmatch_id.grid(row=2, column=1)  """
        
        #ListBox & ScrollBar
        sb=Scrollbar(DFrameR)
        sb.grid(row=0, column=1, sticky='ns')

        matchList=Listbox(DFrameR, width=41, height=16, font=('Arial', 12, 'bold'), bg="#1e3d59", fg="#f5f0e1", yscrollcommand=sb.set)
        matchList.bind('<<ListboxSelect>>', matchrec)
        matchList.grid(row=0, column=0, padx=8)
        sb.config(command=matchList.yview)

        #Buttons


        self.btndis=Button(BFrame, text="Display", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="#f5f0e1", command=disdata)
        self.btndis.grid(row=0, column=1)

        self.btnse=Button(BFrame, text="Search", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="#f5f0e1", command=searchdb)
        self.btnse.grid(row=0, column=3)

        self.btnx=Button(BFrame, text="Exit", font=('Arial', 20, 'bold'), width=10, height=1, bd=4, bg="#f5f0e1", command=iExit)
        self.btnx.grid(row=0, column=6)


if __name__=='__main__':
    root=Tk()
    datbase=match(root)
    root.mainloop()