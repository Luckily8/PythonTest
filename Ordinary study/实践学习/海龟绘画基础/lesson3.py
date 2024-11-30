# turtle画圆环，填充
import turtle as t
t.speed(0)
t.pensize(8)
t.color("blue")
t.begin_fill()
t.circle(50)
t.end_fill()
t.penup()

t.pendown()
t.color('white')
t.begin_fill()
t.circle(25)
t.end_fill()
# 保持窗口
t.mainloop()
