from tkinter import *

root = Tk()

root.geometry('370x350')
root.title('Calculator')
root.configure(bg="#192655")

# function to insert values from buttons to text box
def add_to_calc(val):
   inp.insert('end',val)

# function to calculate the expression inside the text box
def calculate():
   try:
      sum = inp.get()
      sum = eval(sum)                               # this eval(sum) is used to evaluate the expression
      inp.delete(0,'end')                 # delete the value inside the text box
      inp.insert(0,sum)
   except:
      inp.delete(0, 'end')                # the try except is used to give error when there is an error in calc
      inp.insert(0,'ERROR')

# this function is used to clear the text screen
def clear():
   inp.delete(0, 'end')

# text box
inp = Entry(root,width=12,font=("Arial", 40),bg='#2D4356',fg='white')
# inp = Text(root,width=43,height=4,bg='#2D4356',fg='white')
inp.place(x=10,y=10)

# buttons
btn9 = Button(root,text='9',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(9))
btn9.place(x=10,y=100)
btn8 = Button(root,text='8',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(8))
btn8.place(x=100,y=100)
btn7 = Button(root,text='7',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(7))
btn7.place(x=190,y=100)

btn6 = Button(root,text='6',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(6))
btn6.place(x=10,y=160)
btn5 = Button(root,text='5',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(5))
btn5.place(x=100,y=160)
btn4 = Button(root,text='4',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(4))
btn4.place(x=190,y=160)

btn3 = Button(root,text='3',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(3))
btn3.place(x=10,y=220)
btn2 = Button(root,text='2',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(2))
btn2.place(x=100,y=220)
btn1 = Button(root,text='1',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(1))
btn1.place(x=190,y=220)

btn_clr = Button(root,text='Clear',width=10,height=2,bg='#2D4356',fg='white',command=clear)
btn_clr.place(x=10,y=280)
btn0 = Button(root,text='0',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc(0))
btn0.place(x=100,y=280)
btn_equals = Button(root,text='=',width=10,height=2,bg='#F15A59',fg='white',command= calculate)
btn_equals.place(x=190,y=280)

btn_div = Button(root,text='/',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc('/'))
btn_div.place(x=280,y=100)
btn_mul = Button(root,text='x',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc('*'))
btn_mul.place(x=280,y=160)
btn_sub = Button(root,text='-',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc('-'))
btn_sub.place(x=280,y=220)
btn_add = Button(root,text='+',width=10,height=2,bg='#2D4356',fg='white',command= lambda: add_to_calc('+'))
btn_add.place(x=280,y=280)




root.mainloop()