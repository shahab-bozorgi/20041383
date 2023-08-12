from tkinter import *



top = Tk()
top.title("mashin Hesab")
top.configure(bg="dimgray")
top.resizable(width=False, height=False)

operator = ''
text_input = StringVar()


#======================================================#
def btnClick(number): 
    global  operator
    operator = operator + str(number)
    text_input.set(operator)

def btnClearText():
    global  operator
    operator = ''
    text_input.set("")


def btnEquation():
    global  operator
    sum = str(eval(operator))
    text_input.set(sum)
    operator = ""
#======================================================#

textDisplay = Entry(top, font=('arial', 20, 'bold'),textvariable=text_input, bd=7, 
                    insertwidth=4 ,bg="lightseagreen", justify="left").grid(columnspan=4)

shomare7 = Button (top, text="7",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick (7)).grid(row=1, column=0) 
shomare8 = Button (top, text="8",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(8)).grid(row=1, column=1) 
shomare9 = Button (top, text="9",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(9)).grid(row=1, column=2) 
shomare4 = Button (top, text="4",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(4)).grid(row=2, column=0) 
shomare5 = Button (top, text="5",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(5)).grid(row=2, column=1) 
shomare6 = Button (top, text="6",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(6)).grid(row=2, column=2) 
shomare1 = Button (top, text="1",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(1)).grid(row=3, column=0) 
shomare2 = Button (top, text="2",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(2)).grid(row=3, column=1) 
shomare3 = Button (top, text="3",padx=15, pady=10, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(3)).grid(row=3, column=2) 
shomare0 = Button (top, text="0",padx=15, pady=20, bd=5, fg="white", bg="teal",  font=('arial', 20, 'bold'), command=lambda:btnClick(0)).grid(row=4, column=1) 

shomare = Button (top, text="+",padx=15, pady=10, bd=5, fg="white", bg="teal", 
                   font=('arial', 20, 'bold'), command=lambda:btnClick("+")).grid(row=1, column=3) 

shomare = Button (top, text="-",padx=15, pady=10, bd=5, fg="white", bg="teal", 
                   font=('arial', 20, 'bold'), command=lambda:btnClick("-")).grid(row=2, column=3) 

shomare = Button (top, text="*",padx=15, pady=10, bd=5, fg="white", bg="teal", 
                   font=('arial', 20, 'bold'), command=lambda:btnClick("*")).grid(row=3, column=3) 

shomare = Button (top, text="/",padx=15, pady=20, bd=5, fg="white", bg="teal",
  font=('arial', 20, 'bold'), command=lambda:btnClick("/")).grid(row=4, column=3) 


shomare = Button (top, text="C",padx=15, pady=20, bd=5, fg="white", bg="darkred",
                   font=('arial', 20, 'bold' ), command=lambda:btnClearText()).grid(row=4, column=0) 

shomare = Button (top, text="=",padx=15, pady=20, bd=5, fg="white", bg="darkgreen",
                    font=('arial', 20, 'bold'), command=lambda:btnEquation()).grid(row=4, column=2) 

top.mainloop()

