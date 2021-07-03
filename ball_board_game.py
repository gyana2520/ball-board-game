import turtle
import random
import time
def welcome_screen():
	wel = turtle.Turtle()
	for x in range(20):
		wel.color(1-(x/20), 1-(x/20), 1-(x/20))
		screen.clear()
		k = pow(x, 1, 3)
		wel.write('starting'+'.'*(k+1), align = 'center', font = ('arial', 40))
		screen.delay(200)

def create_board():
	board = turtle.Turtle()
	board.ht()
	board.pu()
	board.goto(-200, -225)
	board.pd()
	board.begin_fill()
	board.fd(400)
	board.left(90)
	board.fd(450)
	board.left(90)
	board.fd(400)
	board.left(90)
	board.fd(450)
	board.end_fill()
	board.goto(-200, -185)
	board.color('white')
	board.fd(20)
	board.left(90)
	board.fd(400)
	board.left(90)
	board.fd(20)
	board.left(90)
	board.fd(400)
	board.ht()

def initials():
	new_ball = turtle.Turtle()
	new_ball.shape('circle')
	new_ball.shapesize(0.5, 0.5)
	new_ball.pu()
	x = random.randrange(-195, 195)
	new_ball.color('white')
	new_ball.goto(x, 220)
	return new_ball, x

def get_position(time):
	s = 5* (time**2)
	return s

def add_score(score):
	turt_score.clear()
	score += 1
	turt_score.write(score, align = 'center', font = ('algerian', 50))
	if (score > high_score):
		high_score_printer()
	return score

def add_left(left):
	turt_left.clear()
	left += 1
	turt_left.write(left, align = 'center', font = ('algerian', 50))
	return left

def drop_ball(dt = 1, score = 0, left = 0):
	new_ball, x = initials()
	time = 0
	while (time<=9):
		h = get_position(time)
		new_ball.goto(x, 220 - h)
		time += dt
	if (abs(x - turtle.xcor()) < 20):
		new_ball.color('green')
		score = add_score(score)
		new_ball.goto(x, -250)
	else:
		new_ball.color('red')
		left = add_left(left)
		new_ball.goto(x, -240)
	return score, left

def board_right():
	turtle.fd(5)

def board_left():
	turtle.back(5)

def high_score_printer():
	global high_score
	turt_high.clear()
	high_score += 1
	turt_high.write('high score: {}'.format(high_score), align = 'center', font = ('algerian', 50))

def get_response():
	screen.clear()
	turtle.color(0, 1, 1)
	turtle.write('Do you want to play again?', align = 'center', font = ('arial', 40))
	turtle.ht()
	turtle.pu()
	turtle.goto(0, -75)
	turtle.pd()
	turtle.write('press y or n: ', align = 'center', font = ('arial', 40))
	turtle.onkey(start_match, 'y')
	turtle.onkey(end_match, 'n')
	try:
		k = input()
	except:
		k = ''

def end_match():
	screen.clear()
	turtle.ht()
	turtle.color(1, 0.5, 0.5)
	turtle.pu()
	turtle.goto(0, 60)
	turtle.write('High score: {}'.format(high_score), align = 'center', font = ('arial', 50))
	turtle.goto(0, 0)
	turtle.write('Thanks for playing'.format(high_score), align = 'center', font = ('arial', 50))
	turtle.goto(0, -60)
	turtle.write(':)'.format(high_score), align = 'center', font = ('arial', 50))
	time.sleep(2)
	screen.bye()

def start_match():
	global score, left, turtle, screen, turt_score, turt_left, turt_high
	screen = turtle.Screen()
	welcome_screen()
	screen.clear()
	create_board()
	turt_high = turtle.Turtle()
	turt_high.color('yellow')
	turt_high.ht()
	turt_high.pu()
	turt_high.goto(0, 250)
	turt_high.write('high score: {}'.format(high_score), align = 'center', font = ('algerian', 50))
	score, left = 0, 0
	turtle.shape('square')
	turtle.shapesize(0.5, 2)
	turtle.color('white')
	turtle.pu()
	turtle.goto(0, -195)
	turtle.onkeypress(board_right, 'Right')
	turtle.onkeypress(board_left, 'Left')
	screen.listen()
	turt_score = turtle.Turtle()
	turt_score.ht()
	turt_score.pu()
	turt_score.color('green')
	turt_score.goto(-300, 0)
	turt_score.write('0', align = 'center', font = ('algerian', 50))
	turt_left = turtle.Turtle()
	turt_left.ht()
	turt_left.pu()
	turt_left.color('red')
	turt_left.goto(300, 0)
	turt_left.write('0', align = 'center', font = ('algerian', 50))
	while (left<10):
		score, left = drop_ball(0.1, score, left)

	final = turtle.Turtle()
	final.color('yellow')
	final.ht()
	final.write('your score is {}.'.format(score), align = 'center', font = ('algerian', 32))
	print ('your score is {}.'.format(score))
	time.sleep(2)
	get_response()

high_score = 0
start_match()