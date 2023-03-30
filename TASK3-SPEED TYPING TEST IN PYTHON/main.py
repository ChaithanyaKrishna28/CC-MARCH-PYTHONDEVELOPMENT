from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading

#####functionality#######
time = 0
totaltime = 60
wrongwords =0
elapsedtimeinminutes = 0
def start_timer():
    start_button.config(state=DISABLED)
    global time
    text_area.config(state=NORMAL)
    text_area.focus()
    for time in range(1,61):
        elapsed_timer_label.config(text=time)
        remainingtime = totaltime - time
        remaining_timer_label.config(text=remainingtime)
        sleep(1)   #for delay of one seconds
        root.update()
    text_area.config(state=DISABLED)
    reset_button.config(state=NORMAL)

#wpm wrong words
def count():
    global wrongwords
    while time!=totaltime:
        entered_paragraph = text_area.get(1.0,END).split()  #enteres paragraph
        totalwords = len(entered_paragraph)
    totalwords_count_label.config(text=totalwords)
    
    para_words_list = label_paragraph['text'].split()

    #comparing the given pargraph an entered paragraph for wrong words count and right words count
    for pair in list(zip(para_words_list,entered_paragraph)):
        if pair[0] != pair[1]:
             wrongwords += 1
    wrong_count_label.config(text=wrongwords)
    elapsedtimeinminutes = time/60
    wpm = (totalwords-wrongwords)/elapsedtimeinminutes
    wpm = round(wpm)
    WPM_count_label.config(text=wpm)
    gross_wpm = totalwords/elapsedtimeinminutes
    #accuracy
    accuracy = (wpm/gross_wpm)*100
    accuracy = round(accuracy)
    Accuracy_percent_label.config(text=str((accuracy))+"%")


def start():
    t1 = threading.Thread(target=start_timer)
    t1.start()

    t2 = threading.Thread(target=count)
    t2.start()

def reset():
    global time,elapsetimeinminutes
    time = 0
    elapsedtimeinminutes = 0
    start_button.config(state=NORMAL)
    reset_button.config(state=DISABLED)
    text_area.config(state=NORMAL)
    text_area.delete(1.0,END)
    text_area.config(state=DISABLED) 

    elapsed_timer_label.config(text='0')
    remaining_timer_label.config(text='0')
    WPM_count_label.config(text='0')
    Accuracy_percent_label.config(text='0')
    totalwords_count_label.config(text='0')
    wrong_count_label.config(text='0')



#######GUI##########
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.title("SPEED TYPING CALCULATOR")
root.resizable(0,0)
root.overrideredirect(TRUE)  #removing the title bar
Frame(root)
root.geometry('940x735+200+10')
mainframe = Frame(root,bd=4)
mainframe.grid()
titleframe = Frame(mainframe,bg='orange',padx=5,pady=5)
titleframe.grid()
titlelabel = Label(titleframe,text='SPEED TYPING TEST',font=("algerian", 28, "bold"),bg='goldenrod3',fg='white',width=38,bd=10)
titlelabel.grid()

paragraphframe = Frame(mainframe)
paragraphframe.grid(row=1,column=0)

paragraph_list = [
    " Finance is the soul and blood of any business and no firm can survive without finance  It concerns itself with the management of the monetary affairs of the firm and how money can be raised on the best terms available",
    "Today Startups are being widely recognized as important engines for growth and job generation Through innovation and scalable technology and  startups can generate impactful solutions and thereby act as vehicles for socioeconomic development and transformation",
    "The Taj Mahal is the materialized vision of love and marks a perfect indelible remark on its Mughal Architecture and This historical monument is the mausoleum of Emperor Shan Jahans beloved wife Empress Arjuman Banu Begum most commonly known as Mumtaz Mahal",
    "Truth and nonviolence constituting the essence of Gandhiji creed are philosophical concepts Gandhijis contribution to philosophical thought was not only to translate these concepts into his own daily life but by his acceptance of these concepts as governing his own life as an individual and as a social being and to induce large numbers to follow the same path individually and as social beings",
    "The computer is the databased electronic machine initially invented by Charles Babbage back in 1837 He is called the Father of computer and With the computer discovery the man has entered a new period of improvement In this modern era and lives would be impossible without owning a computer and A computer provides us with a wide range of possibilities and there is an infinite number of things that can be done with the help of a computer",
    "The unusual and fast increase in Earth average temperature is called Global Warming and This increase has considerably been higher in the last century due to human intervention with nature and The release of greenhouse gases in the atmosphere has been one of the primary reasons behind the increase in temperature The increased consumption of fossils fuels has increased the concentration of greenhouse gases and The impact of Global Warming is much higher than just a jump in temperature",
    "Perhaps the most relevant form of mass communication newspapers can be described as a periodical publication containing news articles worldwide The oldest newspapers in the world were handwritten pamphlets informing people about world affairs and essential commodities prices and However these NEWSPAPERS were circulated only with permission granted by the ruling government Much has changed since then",
    "Among Web professionals Web development usually refers to the main non-design aspects of building Web sites writing markup and coding 2 Web development may use content management systems CMS to make content changes easier and available with basic technical skills",
    "Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python1 and Python 2.0 was released in 2000 and Python3 released in 2008 was a major revision not completely backwardcompatible with earlier versions and Python2, released in 2020 was the last release of Python 2",
    "As I sit in my room late at night and staring at the computer screen and I decide it would be a good idea to create this text and There isn't much meaning to it and other than to get some simple practice and A lot of the texts that have been created are rather short and and do not give a good representation of actual typing speed and accuracy and They lack the length to gauge where your strengths and weaknesses are when typing",
    "Bringing Business Stability and Maintaining Full Employment Conditions are Another main objective of taxation is to bring about business stability and maintain full employment conditions and A low rate of taxation during a business depression shall accelerate more income to the people and help in raising demand",
    "In this fastpaced world and time is money and everything needs to be done in the shortest time possible and You see that several job postings include a minimum typing speed in terms of words per minute in their list of requirements"
]
random.shuffle(paragraph_list)

label_paragraph = Label(paragraphframe,text=paragraph_list[0],wraplength=912,justify='left',font=('arial',14,'bold'))
label_paragraph.grid(row=0,column=0)
#text area

text_area_frame = Frame(mainframe)
text_area_frame.grid(row=3,column=0)

text_area=Text(text_area_frame,font=('arial',12,'bold'),width=100,height=10,bd=4,relief=GROOVE,wrap=WORD,state=DISABLED)
text_area.grid()

# labels

frame_output = Frame(mainframe)
frame_output.grid(row=4,column=0)

#elapsed time

elapsed_time_label = Label(frame_output,text='Elapsed Time',font=('Tahomn',12,'bold'),fg='red')
elapsed_time_label.grid(row=0,column=0,padx=5)

#elapse timer label

elapsed_timer_label = Label(frame_output,text='0',font=('Tahomn',12,'bold'))
elapsed_timer_label.grid(row=0,column=1,padx=5)

#remaining time label
remaining_time_label = Label(frame_output,text='Remaining Time',font=('Tahomn',12,'bold'),fg='red')
remaining_time_label.grid(row=0,column=2,padx=5)
# remaining timer label
remaining_timer_label = Label(frame_output,text='60',font=('Tahomn',12,'bold'))
remaining_timer_label.grid(row=0,column=3,padx=5)
#words per minute label
WPM_label = Label(frame_output,text='WPM',font=('Tahomn',12,'bold'),fg='red')
WPM_label.grid(row=0,column=4,padx=5)
#wpm count
WPM_count_label = Label(frame_output,text='0',font=('Tahomn',12,'bold'))
WPM_count_label.grid(row=0,column=5,padx=5)
#Accuracy label
Accuracy_label = Label(frame_output,text='Accuracy',font=('Tahomn',12,'bold'),fg='red')
Accuracy_label.grid(row=0,column=6,padx=5)
#Accuracy count
Accuracy_percent_label = Label(frame_output,text='0',font=('Tahomn',12,'bold'))
Accuracy_percent_label.grid(row=0,column=7,padx=5)

#total words label
totalwords_label = Label(frame_output,text='Total Words',font=('Tahomn',12,'bold'),fg='red')
totalwords_label.grid(row=0,column=8,padx=5)
#total words count label
totalwords_count_label = Label(frame_output,text='0',font=('Tahomn',12,'bold'))
totalwords_count_label.grid(row=0,column=9,padx=5)
#wrong words
wrongwords_label = Label(frame_output,text='WrongsWords',font=('Tahomn',12,'bold'),fg='red')
wrongwords_label.grid(row=0,column=10,padx=5)
#wrong words count label
wrong_count_label = Label(frame_output,text='0',font=('Tahomn',12,'bold'))
wrong_count_label.grid(row=0,column=11,padx=5)


#buttons frame
buttons_frame = Frame(mainframe)
buttons_frame.grid(row=5,column=0)

start_button = ttk.Button(buttons_frame,text='Start',command=start)
start_button.grid(row=0,column=0,padx=10)
#reset button
reset_button = ttk.Button(buttons_frame,text='Reset',state=DISABLED,command=reset)
reset_button.grid(row=0,column=1,padx=10)
#exit button
exit_button = ttk.Button(buttons_frame,text='Exit',command=root.destroy)
exit_button.grid(row=0,column=2,padx=10)
#using ttk themes

#creating key board
key_board_frame = Frame(mainframe)
key_board_frame.grid(row=6,column=0)

frame1to0 = Frame(key_board_frame)
frame1to0.grid(row=0,column=0)
label1 = Label(frame1to0,text='1',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label2 = Label(frame1to0,text='2',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label3 = Label(frame1to0,text='3',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label4 = Label(frame1to0,text='4',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label5 = Label(frame1to0,text='5',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label6 = Label(frame1to0,text='6',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label7 = Label(frame1to0,text='7',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label8 = Label(frame1to0,text='8',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label9 = Label(frame1to0,text='9',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
label0 = Label(frame1to0,text='0',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
#griding
label1.grid(row=0,column=0,padx=5)
label2.grid(row=0,column=1,padx=5)
label3.grid(row=0,column=2,padx=5)
label4.grid(row=0,column=3,padx=5)
label5.grid(row=0,column=4,padx=5)
label6.grid(row=0,column=5,padx=5)
label7.grid(row=0,column=6,padx=5)
label8.grid(row=0,column=7,padx=5)
label9.grid(row=0,column=8,padx=5)
label0.grid(row=0,column=9,padx=5)

#alphabets
frameqtop = Frame(key_board_frame)
frameqtop.grid(row=1,column=0,pady=5)
labelQ = Label(frameqtop,text='Q',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelW = Label(frameqtop,text='W',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelE = Label(frameqtop,text='E',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelR = Label(frameqtop,text='R',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelT = Label(frameqtop,text='T',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelY = Label(frameqtop,text='Y',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelU = Label(frameqtop,text='U',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelI = Label(frameqtop,text='I',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelO = Label(frameqtop,text='O',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelP = Label(frameqtop,text='P',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)

#griding
labelQ.grid(row=0,column=0,padx=5)
labelW.grid(row=0,column=1,padx=5)
labelE.grid(row=0,column=2,padx=5)
labelR.grid(row=0,column=3,padx=5)
labelT.grid(row=0,column=4,padx=5)
labelY.grid(row=0,column=5,padx=5)
labelU.grid(row=0,column=6,padx=5)
labelI.grid(row=0,column=7,padx=5)
labelO.grid(row=0,column=8,padx=5)
labelP.grid(row=0,column=9,padx=5)

frameAtoL = Frame(key_board_frame)
frameAtoL.grid(row=2,column=0,pady=3)
labelA = Label(frameAtoL,text='A',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelS = Label(frameAtoL,text='S',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelD = Label(frameAtoL,text='D',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelF = Label(frameAtoL,text='F',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelG = Label(frameAtoL,text='G',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelH = Label(frameAtoL,text='H',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelJ = Label(frameAtoL,text='J',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelK = Label(frameAtoL,text='K',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)
labelL = Label(frameAtoL,text='L',bg='black',fg='white',font=('arial',10,'bold'),height=2,width=5,bd=10,relief=GROOVE)

labelA.grid(row=0,column=0,padx=5)
labelS.grid(row=0,column=1,padx=5)
labelD.grid(row=0,column=2,padx=5)
labelF.grid(row=0,column=3,padx=5)
labelG.grid(row=0,column=4,padx=5)
labelH.grid(row=0,column=5,padx=5)
labelJ.grid(row=0,column=6,padx=5)
labelK.grid(row=0,column=7,padx=5)
labelL.grid(row=0,column=8,padx=5)

frameZtoM = Frame(key_board_frame)
frameZtoM.grid(row=3,column=0,pady=3)
labelZ = Label(frameZtoM,text='Z',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelX = Label(frameZtoM,text='X',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelC = Label(frameZtoM,text='C',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelV = Label(frameZtoM,text='V',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelB = Label(frameZtoM,text='B',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelN = Label(frameZtoM,text='N',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)
labelM = Label(frameZtoM,text='M',bg='black',fg='white',font=('arial',10,'bold'),width=5,height=2,bd=10,relief=GROOVE)

labelZ.grid(row=0,column=0,padx=5)
labelX.grid(row=0,column=1,padx=5)
labelC.grid(row=0,column=2,padx=5)
labelV.grid(row=0,column=3,padx=5)
labelB.grid(row=0,column=4,padx=5)
labelN.grid(row=0,column=5,padx=5)
labelM.grid(row=0,column=6,padx=5)

#spacebar
space_frame = Frame(key_board_frame)
space_frame.grid(row=4,column=0)
label_space = Label(space_frame,bg='black',fg='white',font=('arial',10,'bold'),width=40,height=2,relief=GROOVE,bd=10)
label_space.grid(row=0,column=0)
# binding the keys to laptop keyboard

label_numbers = [label1,label2,label3,label4,label5,label6,label7,label8,label9,label0]
label_alphabets = [labelA,labelB,labelC,labelD,labelE,labelF,labelG,labelH,labelI,labelJ,labelK,labelL,labelM,
                   labelN,labelO,labelP,labelQ,labelR,labelS,labelT,labelU,labelV,labelW,labelX,labelY,labelZ
                    ]
space_label = [label_space]
binding_numbers = ['1','2','3','4','5','6','7','8','9','0']
binding_small_alphabets= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
binding_capital_alphabets= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#binding numbers 
def changeBG(widget):
    widget.config(bg='blue')
    widget.after(500,lambda:widget.config(bg='black'))
for number in range(len(binding_numbers)):
    root.bind(binding_numbers[number],lambda event,label= label_numbers[number]:changeBG(label))
#binding the capital alphabets
for alphabet in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[alphabet],lambda event,label= label_alphabets[alphabet]:changeBG(label))
#binding the small alphabets
for alphabet in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[alphabet],lambda event,label= label_alphabets[alphabet]:changeBG(label))
#binding the space bar
root.bind('<space>',lambda event:changeBG(space_label[0]))


root.mainloop()