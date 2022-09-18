import turtle as t

t.screensize(600,400)# 設定視窗大小
t.showturtle()#t.hideturtle()
t.shape("turtle")
t.speed('slow')
t.bgcolor('Dodger blue')
def draw(x,y,xpos,ypos,pensize=5,pencolorStr="black",penangle=90):
    t.penup()
    t.pensize(pensize)
    t.setheading(penangle)
    t.color(pencolorStr)
    t.pendown()
    t.goto(x, y)
    t.goto(xpos, ypos)
    t.penup()
def movePen(x,y):
    t.penup()
    t.goto(x, y)
x = 200
y = 350
for i in range(-450,450,100):
    
    movePen(0+i,y)
    draw(0+i,50+y,0+i,0+y)
    
    movePen(0+i,0+y)
    draw(0+i,0+y,100+i,0+y)
movePen(0+i+x,0+y)
draw(0+i,50+y,100+i,0+y)
for i in range(-450,450,100):
    
    movePen(50+i,50+y)
    draw(0+i,50+y,0+i,50+y)
    
    movePen(0+i,50+y)
    draw(0+i,50+y,100+i,50+y)
t.exitonclick() #點擊滑鼠關閉視窗
t.mainloop()