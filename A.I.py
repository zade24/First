import time

print("")
print("")

intro = "hello user,im chat bot".title()
print(intro)
time.sleep(1.5)

x = "no"
y  = "yes"

print("")

def say_hi(name):
    print("hello ",name)

print("what is your name")
print("")
name = input()
time.sleep(1.5)
print("")

say_hi(name)

def check():
    if response == answer:
        print("you sre very much correct!!")
    else:
        print("you are wrong")

            
        
      

def anti_check():
    if response != answer:
        print('you are wrong')

print("")
time.sleep(1.5)
print("Would you like to do a quiz " + name + "??")
print("")
intro_2 = input()
print("")

if intro_2 == "yes":
    time.sleep(1.5)

    print(""" 
          A)   Maths
          B)   Life sciences
          C)   business studies
          D)   Computer application technology
          E)   life oreintation
    """)

    print("which subject would you like to do")
    print("")
    intro_3 = input()
    print("")
    time.sleep(1.5)

    if intro_3 == "a":
        time.sleep(1.5)
        print("what is 50 + 50")
        response = input()
        answer = "100"
        time.sleep(1.5)
        check()



    elif intro_3 == "b":
            print("what is the powerhouse of the cell? ")
            response = input()
            answer = 'mitochondria'
            check()


            

    
        

    elif intro_3 == "c":
        print("What is the ACT that allow for compensation to employees whom are injured during performing their duties?")
        response  = input()
        answer = "COIDA"
        check()
        


    elif intro_3 == "d" or 'D':
        print("what is the software that allow for the  communication between the computer and the hardware devices? ")
        response = input()
        answer = "diver"
        check()


    elif intro_3 == "e" or "E":
        print("what the key to a healthy self esteem?")
        print("""
        A)Having having confidences in your self
        B)Listening to others? """)
        response = input()
        answer = "a"
        check()
        


else:
    exit()

from tkinter import *

win = Tk()
win.title("Calculator")
win.geometry('600x400')#size
win.resizable(0, 0)#locks size of window

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

#function to clear input field
def bt_clear():
    global expression
    expression = ""
    input_text.set("") 

#function of eqaul button
def bt_eqaul():
    global expression
    result  = str(eval(expression))
    input_text.set(result)   

expression = " "
input_text = StringVar()

#input field frame
input_frame = Frame(win, width="300", height="50")
input_frame.pack(side=TOP)

input_field = Entry(input_frame, font=("arial", 18, "bold"), width=45, justify=RIGHT, textvariable=input_text)
input_field.grid(row=0, column=0)

#increases height of input field
input_field.pack(ipady=10)

#button frame
btns_frame = Frame(win, width=310, height=270)
btns_frame.pack()

#columnspan = amount of column butonm will occupym,padx-pady gives spacong outside border of button

#first row of calcuator
clear = Button(btns_frame, text="C", width=38, height=3, command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = Button (btns_frame, text="/", width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

#second row of calculator
seven = Button(btns_frame, text="7", width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = Button(btns_frame, text=8, width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = Button(btns_frame, text="9", width=10 ,height=3, command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)
multipy = Button(btns_frame, text="*", width=10, height=3, command=lambda: btn_click('*')).grid(row=1, column=3, padx=1, pady=1)

#third row of calculator
six = Button(btns_frame, text="6", width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=0, padx=1, pady=1)
five = Button(btns_frame, text="5", width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)
four = Button(btns_frame, text="4", width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=2, padx=1, pady=1)
add = Button(btns_frame, text="+", width=10, height=3, command=lambda: btn_click('+')).grid(row=2, column=3, padx=1,pady=1)

#fourth row of calculator
three = Button(btns_frame, text="3", width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=0, padx=1, pady=1)
two = Button(btns_frame, text="2", width=10, height=3, command=lambda: btn_click(2)).grid(row=3 , column=1, padx=1, pady=1)
one = Button(btns_frame, text="1", width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=2, padx=1, pady=1)
subtract = Button(btns_frame, text="-", width=10, height=3, command=lambda: btn_click('-')).grid(row=3, column=3, padx=1, pady=1)


zero = Button(btns_frame, text="0", width=10, height=3, command=lambda: btn_click(0)).grid(row=4, column=0, padx=1, pady=1)
decimal = Button(btns_frame, text=".", width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=1, padx=1, pady=1)
eqaul = Button(btns_frame, text="=", width=10, height=3, command=lambda: bt_eqaul()).grid(row=4, column=2, padx=1, pady=1)



a = "iam a compureb p[rogrammer"
print(a)
\


win.mainloop()
#keeps application visible
00