import turtle
from ball import Ball
import math
import random
import time

turtle.colormode(1)
turtle.tracer(0, 0)
turtle.hideturtle()
running=True
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2


my_ball=Ball(5,5,4,6,70,"red")
number_of_balls = 7
minimum_ball_radius = 3
maximum_ball_radius = 100
minimum_ball_dx = -7
maximum_ball_dx = 7
minimum_ball_dy = -5
maximum_ball_dy = 5

turtle.register_shape('giphy.gif')
picture1 = turtle.clone()
picture1.shape('giphy.gif')

turtle.register_shape('wow.gif')
picture2 = turtle.clone()
picture2.shape('wow.gif')

turtle.register_shape('tenor.gif')
picture3 = turtle.clone()
picture3.shape('tenor.gif')

turtle.register_shape('tenor (1).gif')
picture4 = turtle.clone()
picture4.shape('tenor (1).gif')

turtle.register_shape('just_do_it.gif')
picture5 = turtle.clone()
picture5.shape('just_do_it.gif')

turtle.register_shape('thats_awesome.gif')
picture6 = turtle.clone()
picture6.shape('thats_awesome.gif')

turtle.register_shape('Bradley-Cooper-Wow.gif')
picture7 = turtle.clone()
picture7.shape('Bradley-Cooper-Wow.gif')

turtle.register_shape('picture8.gif')
picture8 = turtle.clone()
picture8.shape('picture8.gif')

turtle.register_shape('picture9.gif')
picture9 = turtle.clone()
picture9.shape('picture9.gif')

turtle.register_shape('picture10.gif')
picture10 = turtle.clone()
picture10.shape('picture10.gif')


BALLS = []
for i in range (number_of_balls):
    x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
    y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
    dx=random.randint(minimum_ball_dx,maximum_ball_dx)
    dy=random.randint(minimum_ball_dy,maximum_ball_dy)
    r=random.randint(minimum_ball_radius,maximum_ball_radius)
    color=(random.random(),random.random(),random.random())
    ball_1=Ball(x,y,dy,dx,r,color)
    BALLS.append(ball_1)
 
def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width,screen_height)

def collide (ball_a,ball_b):
    if ball_a==ball_b:
        return False
    d=math.sqrt(math.pow(ball_a.pos()[0]-ball_b.pos()[0],2 )+ math.pow(ball_a.pos()[1]-ball_b.pos()[1],2))
    if ((ball_a.r)+(ball_b.r))<=d:
        return False
    return True


def check_all_balls_collision ():
    all_balls=[]
    all_balls.append(my_ball)
    for ball in BALLS:
        all_balls.append(ball)

    for ball_a in all_balls:
        if my_ball.r>351:
            return False
        for ball_b in all_balls:
            if collide(ball_b,ball_a):
                r_a = ball_a.r
                r_b=ball_b.r
                x=random.randint(-screen_width+maximum_ball_radius,screen_width-maximum_ball_radius)
                y=random.randint(-screen_height+maximum_ball_radius,screen_height-maximum_ball_radius)
                dx=random.randint(minimum_ball_dx,maximum_ball_dx)
                dy=random.randint(minimum_ball_dy,maximum_ball_dy)
                r=random.randint(minimum_ball_radius,maximum_ball_radius)
                color=(random.random(),random.random(),random.random())
                
                if r_a > r_b:
                    print("collide!")
                    if my_ball==ball_b:
                        running = False    
                    if my_ball == ball_a:
                        picture1.penup()
                        picture1.goto(200,200)
                        picture1.showturtle()
                    ball_b.new_ball(x,y,dx,dy,r,color)
                    ball_a.r+=2
                    ball_a.shapesize(ball_a.r/10)
                if my_ball.r>120:
                   picture2.penup()
                   picture2.goto(-200,-200)
                   picture2.showturtle()
                if my_ball.r>160:
                   picture3.penup()
                   picture3.goto(200,-200)
                   picture3.showturtle()
                   
                if my_ball.r>220:
                   picture4.penup()
                   picture4.goto(-200,200)
                   picture4.showturtle()
                   
                if my_ball.r>260:
                   picture5.penup()
                   picture5.goto(-300,-250)
                   picture5.showturtle()
                   
                if my_ball.r>280:
                   picture6.penup()
                   picture6.goto(-200,-50)
                   picture6.showturtle()

                if my_ball.r>300:
                   picture7.penup()
                   picture7.goto(300,0)
                   picture7.showturtle()

                if my_ball.r>320:
                   picture8.penup()
                   picture8.goto(200,300)
                   picture8.showturtle()

                if my_ball.r>340:
                   picture9.penup()
                   picture9.goto(-200,270)
                   picture9.showturtle()
                
                if my_ball.r>350:
                   picture10.penup()
                   picture10.goto(0,0)
                   picture10.showturtle()
                
                
                
                  
                        
                if r_a < r_b:
                    print("collide!")
                    if my_ball==ball_a:
                        running = False
                    ball_a.new_ball(x,y,dx,dy,r,color)
                    ball_b.r+=5
                    ball_b.shapesize(ball_b.r/10)
                

def movearound():
   my_ball.x = turtle.getcanvas().winfo_pointerx()-screen_width*2

   my_ball.y =screen_height*2- turtle.getcanvas().winfo_pointery()
   my_ball.goto(my_ball.x,my_ball.y)


while running==True:
    screen_width=turtle.getcanvas().winfo_width()/2
    screen_height=turtle.getcanvas().winfo_height()/2
    movearound() 
    move_all_balls()
    check_all_balls_collision()
    turtle.update()
    time.sleep(.1)



turtle.mainloop()
  


    
                

