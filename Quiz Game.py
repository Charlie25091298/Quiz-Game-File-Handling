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
rectanswers = [rectanswer1,rectanswer2,rectanswer3,rectanswer4]
recttime = Rect(460,80,120,150)
rectskip = Rect(460,250,120,220)
file = open("questions.txt","r")
question = []
currentquestion = 0
questions = file.readlines()
numberofquestions = len(questions)
Gamewon = False
Gameover = False
points = 0
seconds = 10
def getquestion() :
    global question
    question1 = questions[currentquestion]
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
    screen.draw.textbox(f"Question {currentquestion + 1} of {numberofquestions}",recttitle, color = "white")
    screen.draw.textbox(question[1],rectanswer1,color = "black")
    screen.draw.textbox(question[2],rectanswer2,color = "black")
    screen.draw.textbox(question[3],rectanswer3,color = "black")
    screen.draw.textbox(question[4],rectanswer4,color = "black")
    screen.draw.textbox(str(seconds),recttime, color = "white")
    screen.draw.textbox("skip",rectskip, color = "white")


def gameover() :
    global question
    global Gameover
    global seconds
    Gameover = True
    
    
    seconds = 0


    

def on_mouse_down(pos) :
    global rectanswers
    global currentquestion
    global points
    global seconds
    global question
    answervalue = 1
    for rectanswer in rectanswers :
        if rectanswer.collidepoint(pos) :
            if answervalue == int(question[5]) :
                currentquestion +=1
                if currentquestion >= numberofquestions :
                    question = ["Game Won! Well Done! " + str(points),"-","-","-","-",5]
                    gameover()
                else:
                    points += 1
                    seconds = 10
                    getquestion()   
            else :
                question = ["Game Over! Score : " + str(points),"-","-","-","-",5]
                gameover()
        answervalue +=1       
       





def update_time() :
    global seconds
    global question
    if seconds > 0 :
        seconds -= 1
    else :
        question = ["Game Over! Score : " + str(points),"-","-","-","-",5]
        gameover()

clock.schedule_interval(update_time,1)


def update() :
    pass

pgzrun.go()        