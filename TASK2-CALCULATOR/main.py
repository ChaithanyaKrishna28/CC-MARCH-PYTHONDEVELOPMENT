import tkinter as tk
import math

class Calculator:
    def __init__(self,master):
        self.master = master
        self.master.title("CALCULATOR")
        self.result = tk.StringVar()
        self.expression = ''
        self.frame = tk.Frame(master)
        self.frame.grid()
        #self.master.geometry('600x500')
        #self.master.resizable(0,0)
        self.entry = tk.Entry(master,textvariable=self.result,width=35,justify='right',font=('algerian',20,'bold'),bg='powder blue',fg='black',borderwidth=30)
        self.entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_decimal = tk.Button(master, text=".", padx=40, pady=20, command=lambda: self.button_click("."),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)

        button_add = tk.Button(master, text="+", padx=41, pady=20, command=lambda: self.button_click('+'),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=lambda: self.button_click('-'),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_multiply = tk.Button(master, text="*", padx=41, pady=20, command=lambda:self.button_click('*'),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_divide = tk.Button(master, text="/", padx=41, pady=20, command=lambda:self.button_click('/'),fg='black',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        
        button_clear = tk.Button(master, text="AC", padx=41, pady=20, command=self.button_clear,fg='Red',bg='Dark grey',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_del = tk.Button(master, text="DEL", padx=41, pady=20, command=self.button_delete,fg='black',bg='red',width=10,font=('algerian',20,'bold'),borderwidth=8)
        button_equal = tk.Button(master, text="=", padx=41, pady=20, command=self.button_equal,fg='black',bg='green',width=10,font=('algerian',20,'bold'),borderwidth=8)

      #  self.create_button_frame('=',1,0)
       # self.create_button_frame('+',1,1)
        button_1.grid(row=1, column=0,)
        button_2.grid(row=1, column=1)
        button_3.grid(row=1, column=2)
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_0.grid(row=4, column=0)
        button_decimal.grid(row=4,column=1)
        button_clear.grid(row=4, column=2)
        button_del.grid(row=5, column=1)
        button_equal.grid(row=5,column=2)
        button_add.grid(row=5, column=0)
        button_subtract.grid(row=6, column=0)
        button_multiply.grid(row=6, column=1)
        button_divide.grid(row=6, column=2)

        
        self.bottom_title = tk.Label(self.master,text='CALCULATOR HI',justify='center',font=('algerian',25,'bold'),bg='black',fg='white')
        self.bottom_title.grid(row=7,column=1,pady=20)


    def button_click(self,n):
        self.expression = self.expression + str(n)
        self.result.set(self.expression)
        
        
        pass
    
    def button_equal(self):
        try:
            self.expression
            self.total_result = str(eval(self.expression))
            self.result.set(self.total_result)
            self.expression = ''
        except:
            self.result('Error')
            self.expression = ''

    def button_clear(self):
        self.entry.delete(0,tk.END)
        self.expression = ''
        self.result.set('')
        pass
    def button_delete(self):
        self.text = self.expression[:-1]
        self.expression = self.text
        self.result.set(self.expression)
root = tk.Tk()
root.configure(bg='powder blue')
calc = Calculator(root)
frame1 = tk.Frame(root,cursor="dot")
frame1.grid()
root.mainloop()