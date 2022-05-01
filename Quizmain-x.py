import tkinter
from tkinter import*
import random
import os
print(os.getcwd())


questions = [
"Which snake does not hiss?",
"Who made python?",
"Fullform of GUI?",
"What is the position of python language in the World?",
"What is python?",
"Can tkinter code be  converted into html?",
]







answers_choice = [
   ["Silensnake","Python","Silenkill","None of these",],
   ["Pytho Nergish","Guido van Rossum","Pythen Cargo","None of these",],
   ["Graphical user interface","Gaming utility interface","Gigabyte incount interface","None of these",],
   ["3","1","2","5",],
   ["Snake","Langauge","Both","None of these",],
   ["No","Yes","Maybe",],
]

answers= [1,1,0,1,2,1]


user_answer=[]




def showresult(score):
	lblQuestion.destroy()
	r1.destroy()
	r2.destroy()
	r3.destroy()
	r4.destroy()
	labelimage = Label(
		root,
		background = "#ffffff",
		border=0,
		)
	labelimage.pack(pady=(50,30))
	labelresulttext=Label(
		root,
		font=("consolas",20),
		background="#ffffff"
		)
	labelresulttext.pack()
	if score>= 20:
		img = PhotoImage(file="Gr8.png")
		labelimage.configure(image=img)
		labelimage.image = img 
		labelresulttext.configure(text="You are Fab!!")
	elif(score>=10):
		img = PhotoImage(file="okay.png")
		labelimage.configure(image=img)
		labelimage.image = img 
		labelresulttext.configure(text="You can be better!!!")
	elif(score<10):
		print(score)
		img = PhotoImage(file="Sad.png")
		labelimage.configure(image=img)
		labelimage.image = img 
		labelresulttext.configure(text="You should work hard!!!")




def calc():
	global user_answer,answers
	x = 0
	score=0
	for i in range(0,5):
		print(user_answer[x],answers[x])
		if user_answer[x]==answers[x]:
			score = score + 5
		x+= 1 
	print("total score is:",score)
	showresult(score)










ques=1
score=0
def selected():
	global radiovar,user_answer,score
	global lblQuestion,r1,r2,r3,r4
	global ques
	x = radiovar.get()
	user_answer.append(x)
	radiovar.set(-1)
	print(x)
	if ques < 5:
		 #print(questions[indexes[ques]])
		 lblQuestion.config(text= questions[ques])
		 r1['text']= answers_choice[ques][0]
		 r2['text']= answers_choice[ques][1]
		 r3['text']= answers_choice[ques][2]
		 r4['text']= answers_choice[ques][3]
		 ques +=1
		 
		 
	else:
		calc()
		


def startquiz():
	global lblQuestion,r1,r2,r3,r4
	lblQuestion = Label(
		root,
		text=questions[0],
		font="Consolas",
		width=500,
		justify = "center",
		wraplength = 400,
		background="#ffffff"
		)
	lblQuestion.pack()

	global radiovar
	radiovar = IntVar()
	radiovar.set(-1)

	r1= Radiobutton(
		root,
		text = answers_choice[0][0],
		font = ("Times",12),
		value =0,
		variable=radiovar,
		command = selected,
		background="#ffffff",)

	r1.pack(pady=5)

	r2= Radiobutton(
		root,
		text = answers_choice[0][1],
		font = ("Times",12),
		value =1,
		variable=radiovar,
		command = selected,
		background="#ffffff",
		)

	r2.pack(pady=5)

	r3= Radiobutton(
		root,
		text = answers_choice[0][2],
		font = ("Times",12),
		value =2,
		variable=radiovar,
		command = selected,
		background="#ffffff",)

	r3.pack(pady=5)

	r4= Radiobutton(
		root,
		text = answers_choice[0][3],
		font = ("Times",12),
		value =3,
		variable=radiovar,
		command = selected,
		background="#ffffff",)

	r4.pack(pady=5)



def startIspressed():
	labelimage.destroy()
	lblRules.destroy()
	btnStart.destroy()
	
	startquiz()





root= tkinter.Tk()
root.title('Quizstar')
root.geometry('500x500')
root.config(background='#ffffff')
root.resizable(0,0)
quiz=PhotoImage(file='Quiz1.png')
labelimage = Label(
	root,
	image = quiz,
	background ="#ffffff"
	)

Text = Label(root, text='By Nakshatra')
Text.pack()

labelimage.pack()



img2 = PhotoImage(file="Play.png")
btnStart = Button(
	root,
	image = img2, 
	relief = FLAT,
	border = 0,
	command= startIspressed,
	)
btnStart.place(x=150 , y=300)
labelimage.pack()



lblRules = Label(
	root,
	text="This quiz contains 5questions\n You will get 20sec to solve a question\nOnclick of radio button,that will be final choice\nHence think before you select",
	width=70,
	font=("Square Peg", 9),
	background="#000000",
	foreground=('#FACA2F')
	)

lblRules.place(x=0,y=400)
root.mainloop()