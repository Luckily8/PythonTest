# 随机彩球
import random
import turtle as t
t.speed(0)
t.hideturtle()

t.colormode(255)
for i in range(255):
    t.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.circle(i*2)
    # t.forward(i)
    t.left(36)

t.mainloop()
