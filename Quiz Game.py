import pgzrun


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
    
    screen.draw.textbox("question",rectquestion,color = "white")
    screen.draw.textbox("title",recttitle, color = "white")
    screen.draw.textbox("answer",rectanswer1,color = "black")
    screen.draw.textbox("answer",rectanswer2,color = "black")
    screen.draw.textbox("answer",rectanswer3,color = "black")
    screen.draw.textbox("answer",rectanswer4,color = "black")
    screen.draw.textbox("time",recttime, color = "black")
    screen.draw.textbox("skip",rectskip, color = "white")


def update() :
    pass

pgzrun.go()        