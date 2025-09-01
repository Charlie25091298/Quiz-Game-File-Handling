import pgzrun, random, time


HEIGHT = 500
WIDTH = 600
TITLE = "Quiz Master"
rectquestion = Rect(20,80,420,150)
recttitle = Rect(0,0,600,60)
rectanswer1 = Rect(20,250,200,100)
rectanswer2 = Rect(240,250,200,100)
rectanswer3 = Rect(20,370,200,100)
rectanswer4 = Rect(240,370,200,100)
recttime = Rect(460,80,120,150)
rectskip = Rect(460,250,120,220)
file = open("questions.txt","r")

question = []
currentquestion = 1
questions = file.readlines()
numberofquestions = len(questions)
seconds = 10
def getquestion() :
    global question
    question1 = questions[0]
    question = question1.split(",")
getquestion()   
def draw() :
    screen.fill("black")
    screen.draw.filled_rect(rectquestion,"blue")
    screen.draw.filled_rect(recttitle,"black")
    screen.draw.filled_rect(rectanswer1,"orange")
    screen.draw.filled_rect(rectanswer2,"orange")
    screen.draw.filled_rect(rectanswer3,"orange")
    screen.draw.filled_rect(rectanswer4,"orange")
    screen.draw.filled_rect(recttime,"blue")
    screen.draw.filled_rect(rectskip, "green")
    
    screen.draw.textbox(question[0],rectquestion,color = "white")
    screen.draw.textbox(f"Question {currentquestion} of {numberofquestions}",recttitle, color = "white")
    screen.draw.textbox(question[1],rectanswer1,color = "black")
    screen.draw.textbox(question[2],rectanswer2,color = "black")
    screen.draw.textbox(question[3],rectanswer3,color = "black")
    screen.draw.textbox(question[4],rectanswer4,color = "black")
    screen.draw.textbox(str(seconds),recttime, color = "white")
    screen.draw.textbox("skip",rectskip, color = "white")


def update_time() :
    global seconds
    if seconds > 0 :
        seconds -= 1

clock.schedule_interval(update_time,1)


def update() :
    pass

pgzrun.go()        