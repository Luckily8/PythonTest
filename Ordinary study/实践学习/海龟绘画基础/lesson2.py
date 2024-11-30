import turtle as t
t.speed(0)
# 画笔尺寸
t.pensize(8)
# 画五环,写字
t.color("blue")
t.circle(50)
t.penup()
t.goto(100,0)
t.pendown()
t.color("black")
t.circle(50)
t.penup()
t.goto(200,0)
t.pendown()
t.color("red")
t.circle(50)

t.penup()
t.goto(-100,180)
t.pendown()
t.write("五环",font=("kaiti",36))

# 隐藏过程
t.hideturtle()
#t.done()
# 保留窗口
t.mainloop()

