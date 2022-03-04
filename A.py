import turtle as t
print("0-شمسي")
print("1-نجمة")
print("2-قلب")
print("3-مثلث")
print("4-مربع")
print("5-خماسي")
print("6-سداسي")
print("7-سباعي")
Flag = True
while (Flag):

    W =input( "ضع رقم الرسمة الهندسية هنا: (مثلا 1)")


    if W == '0':

        t.bgcolor('black')
        t =t.Turtle()
        t.color('white')
        t.speed(2000)
        for i in range(185):
            t.forward(100)
            t.right(30)
            t.forward(20)
            t.left(60)
            t.forward(50)
            t.right(30)

            t.penup()
            t.setposition(0, 0)
            t.pendown()

            t.right(2)

    elif W == '1':
        t.bgcolor('black')
        t = t.Turtle()
        t.color('white')
        t.pensize(5)
        for i in range(10):
            t.fd(200)
            t.rt(144)

        t.done()


    elif W == "2":

        pen1 = t.Turtle()
        pen2 = t.Turtle()
        pen1.color('red')
        pen1.width(3)
        pen2.color('red')
        pen2.width(3)
        pen2_name = "love"

        if pen2_name == "2":
            pen2.left(40)
            pen1.left(144)

            pen2.forward(100)
            pen1.forward(100)

            for side in range(193):
                pen2.forward(1)
                pen1.forward(1)
                pen2.left(1)
                pen1.right(1)

            pen2.hideturtle()
            pen1.hideturtle()

        t.done()

    elif W == '3' :
        a = 0
        while a < 3:
            t.bgcolor('black')
            t.color('white')

            t.pensize(5)
            t.forward(100)
            t.left(120)
            a = a + 1
        t.done()

    elif W == "4":
        a = 0
        while a < 4:
            t.bgcolor('black')
            t.color('white')

            t.pensize(5)
            t.forward(200)
            t.left(90)
            a = a + 1
        t.done()

    elif W == '5':
        a = 0
        while a < 5:
            t.bgcolor('black')
            t.color('white')

            t.pensize(5)
            t.forward(100)
            t.left(72)
            a = a + 1
        t.done()

    elif W == '6' :
        a = 0
        while a < 6:
            t.bgcolor('black')
            t.color('white')

            t.pensize(5)
            t.forward(100)
            t.left(60)
            a = a + 1
        t.done()

    elif W == '7' :
        a = 0
        while a < 7:
            t.bgcolor('black')
            t.color('white')

            t.pensize(5)
            t.forward(100)
            t.left(51)
            a = a + 1
        t.done()