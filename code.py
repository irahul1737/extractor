from tkinter import * #importing tk inter module for creating a interface




#a function for opening the file, processing and returning it as a list
def opening(file_name):
    data=[]
    f=file_name
    fh=open(f)
    for i in fh:
        i=i.rstrip()
        i=i.upper()
        if i.startswith('1CR'):
            data.append(i)
        data.sort()
    return data




# a function to find the difference between original students and students present on the given day
def difference(arr1,arr2):
    a=set(arr1)
    b=set(arr2)
    #print(len(a-b))
    return len(a-b)




#a function to remove the duplicate entries and return the final output
def array(arr1,arr2):
    a=set(arr1)
    b=set(arr2)
    c=list(a-b)
    c.sort()
    l=[]
    for i in c:
        l.append(i[7:])
    if len(c)==0:
        return "No Absentees"
    return l




# a funtion to get the data fromt the interface and it will check valid files of not 
def extract():
    a=e1.get()
    b=e2.get()
    try:
        res=difference(opening(a),opening(b))
        res1=array(opening(a),opening(b))
        myText.set(res)
        myText1.set(res1)
    except:
        res="0"
        res1="Inavalid File Name"
        myText.set(res)
        myText1.set(res1)
        
        
        
        
#from here the code is for the interface
master = Tk()
myText=StringVar()
myText1=StringVar()
Label(master,text="File Name (Original)").grid(row=0, sticky=W)
Label(master,text="File Name (Daily)").grid(row=1, sticky=W)
Label(master,text="No of Absentees").grid(row=3, sticky=W)
Label(master,text="Absentees List").grid(row=5, sticky=W)
result=Label(master,text="",textvariable=myText).grid(row=3,column=1, sticky=W)
result=Label(master,text="",textvariable=myText1).grid(row=5,column=1, sticky=W)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
b = Button(master, text="Calculate", command=extract)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5) 
mainloop()
