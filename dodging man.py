import turtle
import random

turtle.delay(0)
turtle.goto(0,800)
turtle.penup()
#turtle.hideturtle()

turtle.setup(760,1000)
setup_size=(760,1000)
x_setup_size = setup_size[0]
y_setup_size = setup_size[1]

RIGHT_EDGE=400
LEFT_EDGE=-400

y_pos_trash =380
x_trash_pos=380
i=0

level=1
generating_time=5
old_points=0
level_up=10


direction="right"

points = 0
all_trash = ['apple.gif','compost.gif','Paper-Ball.gif','iphone.gif','trash-bag.gif','plastic-bottles.gif','banana.gif']
good_trash = ['compost.gif','apple.gif','banana.gif']
bad_trash = ['plastic-bottles.gif','Paper-Ball.gif','trash-bag.gif','iphone.gif']
man = ["man.gif"]
trash_pos=[]
trash_stamps=[]

right_arrow = "Right"
left_arrow = "Left"
TIME_STEP = 500

borders=turtle.clone()
trash=turtle.clone()
man=turtle.clone()
man.showturtle()
turtle.register_shape("man.gif")
man.shape("man.gif")


MAN_SIZE=20
trash_size=20
man .goto(0,-399)
random_trash=8


Screen=turtle.Screen()
Screen.register_shape("park.gif")
Screen.bgpic("park.gif")
LEFT = 2
RIGHT = 3

title=turtle.clone()
levels_title =turtle.clone()


trashes=[]

count=0
diffculity= input("choose diffculity: 1=easy 2=medium 3=hard 4=insane")
if diffculity == "1":
    generating_time = 5
    TIME_STEP = 1000
    print("that's it?")
elif diffculity == "2":
    generating_time = 4
    TIME_STEP = 700
    print("you're better than this!")
elif diffculity == "3":
    generating_time = 3
    TIME_STEP = 500
    print("you're the best!")
elif diffculity == "4":
    generating_time = 2
    TIME_STEP = 300
    print("you're out")
else:
    print("input not detected!") 

def play():
    global i,count,points,generating_time
    if count % generating_time==0:
        make_trash()
    count+=1
    move_trash()    
    turtle.onkeypress(Right, right_arrow)
    turtle.onkeypress(Left, left_arrow)
    levels()
    
    for piece in trashes:
        if piece.pos()[0] == man.pos()[0]:
            if piece.pos()[1] <-400:
                check_trash(piece)
                
                trash_ind=trashes.index(piece)
                trashes.pop(trash_ind)
                i-=1
                piece.ht()
        elif piece.pos()[1]<=-500:
            if piece.shape() in good_trash:
                points+=1
                trash_ind=trashes.index(piece)
                trashes.pop(trash_ind)
                i-=1
                print (points)
            else:
                quit()
                
    title.goto(330,450)
    title.clear()
    title.color('black')
    title.write("score:" + str(points),True,"center",font=("Times New Roman",20,"normal"))
                
    turtle.ontimer(play,TIME_STEP)
    
def Right():
    global direction
    direction = RIGHT
    move_man()
    print("You pressed the RIGHT key!")

def Left():
    global direction
    direction = LEFT
    move_man()
    print("You pressed the LEFT key!")
##    
turtle.onkeypress(RIGHT, right_arrow)
turtle.onkeypress(LEFT, left_arrow)

turtle.listen()
def move_man():
    man_pos=man.pos()
    x_pos=man_pos[0]
    y_pos=man_pos[1]

    if direction==RIGHT:
        man.goto(x_pos+MAN_SIZE,y_pos)
    elif direction==LEFT:
        man.goto(x_pos-MAN_SIZE,y_pos)
    new_pos=man.pos()
    new_x_pos=new_pos[0]
    
    if new_x_pos >= RIGHT_EDGE:
        man.ht()
        man.goto(new_x_pos-760,y_pos)
        man.showturtle()

    elif new_x_pos <= LEFT_EDGE:
        man.hideturtle()
        man.goto(new_x_pos+760,y_pos)
        man.showturtle()
'''
def randomize_trash():
    global i,trashes
    #trash=[]
    
     
    #random_trash_ind= random.randint(0,6)
    #turtle.register_shape(all_trash[random_trash_ind])
    #trash.shape(all_trash[random_trash_ind])
'''

def move_trash():
    print("moving")
    global y_pos_trash,trash_pos
    trash_pos=[]
    for piece in trashes:
        x,y = piece.pos()
        piece.goto(x,y-40)
        trash_pos.append(piece.pos())
    #y_pos_trash-=40
    #turtle.ontimer(move_trash,TIME_STEP)
    
'''while 1==1:
    trash1= turtle.clone()
    trash1+'1'=turtle.clone()
    Trash = []
    trash = turtle.clone()
    Trash.append(turtle.clone())'''

def make_trash():
    #move_trash()
    global i, trashes,y_pos_trash, x_trash_pos

    trashes.append(turtle.clone())
    random_shape=random.randint(0,6)
    #print(random_shape)
    #print(all_trash)
    turtle.register_shape(all_trash[random_shape])
    #print(i)
    #print(trashes)
    trashes[i].shape(all_trash[random_shape])
    
    
    
    min_x=-int(x_setup_size/2/trash_size)+1
    max_x=int(x_setup_size/2/trash_size)+1
    y_pos_trash=380
    x_trash_pos= random.randint(min_x,max_x)*trash_size
    trashes[i].goto(x_trash_pos,y_pos_trash)
    trash_pos.append((x_trash_pos, y_pos_trash))
    #random_trash_stamp = trash.stamp()
    #trash_stamps.append(random_trash_stamp)
    #turtle.ontimer(make_trash,GENERATING_TIME_STEP)
    i+=1
    
def check_trash(piece):
    global points,random_trash
    if piece.shape() in bad_trash:
        points+=1
        print(points)
    else:
        quit()
 
def make_borders():
    borders.penup()
    borders.goto(-400,-500)
    borders.pendown()
    borders.goto(-400,500)
    borders.goto(400,500)
    borders.goto(400,-500)    
    borders.goto(-400,-500)


def levels():
    global old_points , level_up , points , level , TIME_STEP , generating_time 
    if old_points+level_up== points:
        level+=1
        TIME_STEP = TIME_STEP-50
        levels_title.penup()
        levels_title.goto(0,450)
        levels_title.clear()
        levels_title.write("level: "+str(level),True,"center", font=("Times New Roman",20,"normal"))
        if points % 3 == 0:
            level_up = level_up + 5
        old_points = points
        if generating_time > 1:
            generating_time -= 1
            
        
#move_man()
make_borders()    
play()
#    else:
#        quit()















