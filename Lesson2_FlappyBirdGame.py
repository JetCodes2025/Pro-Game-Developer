import pgzrun
from random import randint

TITLE = 'Flappy Ball'
WIDTH = 800
HEIGHT = 600

R = randint(0,255)
G = randint(0,255)
B = randint(0,255)
CLR = R,G,B
game_over = False
#BLUE = 0, 128, 255
GRAVITY = 2000.0  # pixels per second per second


class Ball:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)


ball = Ball(50, 100)


def draw():
    screen.clear()
    if game_over:
        screen.draw.text("Game Over",center=(WIDTH //2, HEIGHT //2), fontsize = 60,color="red" )
    else:
        ball.draw()
# function update to keep refreshing the screen and helping ball to do move smoothly.
def update(dt):
    global game_over
    if game_over:
        return #stop the loop
    uy = ball.vy
    ball.vy += GRAVITY * dt
    ball.y += (uy + ball.vy) * 0.5 * dt

    #end the game when ball touches the bottom (no bounce)
    if ball.y > HEIGHT - ball.radius:
        game_over = True
        return 

    # detect and handle the bounce of the ball
    if ball.y > HEIGHT - ball.radius:
        ball.y = HEIGHT - ball.radius
        ball.vy = -ball.vy * 0.9 #collision
    
    # As X component does not have acceleration we need to write basic code for it 
    ball.x = ball.x + ball.vx * dt
    if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
        ball.vx = -ball.vx
    
def on_key_down(key):    
    if key == keys.SPACE:
        ball.vy = -500
pgzrun.go()
