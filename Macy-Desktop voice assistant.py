
import subprocess
import sys
import pygame

def install(module):
    subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# install("pyttsx3")
# install("speechRecognition")
# install("wikipedia")
# install("pipwin")
# subprocess.check_call([sys.executable, "-m", "pipwin", "install", "pyaudio"])

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import turtle
import time
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!, My name is macy, your voice assistant")

    elif hour>=12 and hour<18:
        speak("Good afternoon sir !, My name is macy, your voice assistant")

    else:
        speak("Good Evening Sir!!! ,My name is macy, your voice assistant")

    speak("Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#Games
#1
def the_pong_game():
    scr = turtle.Screen()
    scr.setup(width=900, height=750)
    scr.title("The PONG Game by Siddhant Kumar")
    scr.bgcolor("black")
    scr.tracer()

    # Border
    bor1 = turtle.Turtle()
    bor1.speed(0)
    bor1.shape('square')
    bor1.color('white')
    bor1.shapesize(stretch_len=37.5, stretch_wid=30.5)
    bor1.penup()
    bor1.goto(0, 0)

    bor2 = turtle.Turtle()
    bor2.speed(0)
    bor2.shape('square')
    bor2.color('black')
    bor2.shapesize(stretch_len=37.2, stretch_wid=30.2)
    bor2.penup()
    bor2.goto(0, 0)

    # Left Paddle
    l_paddle = turtle.Turtle()
    l_paddle.speed(0)
    l_paddle.shape("square")
    l_paddle.color("white")
    l_paddle.shapesize(stretch_wid=5, stretch_len=1)
    l_paddle.penup()
    l_paddle.goto(-350, 0)

    # Right Paddle
    r_paddle = turtle.Turtle()
    r_paddle.speed(0)
    r_paddle.shape("square")
    r_paddle.color("white")
    r_paddle.shapesize(stretch_wid=5, stretch_len=1)
    r_paddle.penup()
    r_paddle.goto(350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("circle")
    ball.color("white")
    ball.shapesize(stretch_wid=1, stretch_len=1)
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 7
    ball.dy = 7

    # Score Board
    s_board = turtle.Turtle()
    s_board.speed(0)
    s_board.shape("square")
    s_board.color("white")
    s_board.penup()
    s_board.hideturtle()
    s_board.goto(0, 320)
    s_board.write("Player A : 0       |       Player B : 0", align="center", font=("Courier", 24, 'normal'))

    # Functions
    def l_paddle_up():
        y = l_paddle.ycor()
        y += 20
        l_paddle.sety(y)

    def r_paddle_up():
        y = r_paddle.ycor()
        y += 20
        r_paddle.sety(y)

    def l_paddle_down():
        y = l_paddle.ycor()
        y -= 20
        l_paddle.sety(y)

    def r_paddle_down():
        y = r_paddle.ycor()
        y -= 20
        r_paddle.sety(y)

    # Linking the keyboard
    scr.listen()
    scr.onkeypress(l_paddle_up, "w")
    scr.onkeypress(l_paddle_down, "s")
    scr.onkeypress(r_paddle_up, "Up")
    scr.onkeypress(r_paddle_down, "Down")

    # Scores
    score_a = 0
    score_b = 0

    # Main game loop
    while True:
        scr.update()

        # Ball Movement
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collisions
        # Top and bottom
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        elif ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1

        # Left and right
        if ball.xcor() > 350:
            score_a += 1
            s_board.clear()
            s_board.write("Player A : {}       |       Player B : {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        elif ball.xcor() < -350:
            score_b += 1
            s_board.clear()
            s_board.write("Player A : {}       |       Player B : {}".format(score_a, score_b), align="center",
                          font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1

        # Paddle and ball collisions
        if ball.xcor() < -340 and ball.ycor() < l_paddle.ycor() + 50 and ball.ycor() > l_paddle.ycor() - 50:
            ball.dx *= -1

        elif ball.xcor() > 340 and ball.ycor() < r_paddle.ycor() + 50 and ball.ycor() > r_paddle.ycor() - 50:
            ball.dx *= -1

#2
def the_snake_game():

    delay = 0.1
    score = 0
    high_score = 0

    # Creating a window screen
    wn = turtle.Screen()
    wn.title("Snake Game")
    wn.bgcolor("blue")
    # the width and height can be put as user's choice
    wn.setup(width=600, height=600)
    wn.tracer(0)

    # head of the snake
    head = turtle.Turtle()
    head.shape("square")
    head.color("white")
    head.penup()
    head.goto(0, 0)
    head.direction = "Stop"

    # food in the game
    food = turtle.Turtle()
    colors = random.choice(['red', 'green', 'black'])
    shapes = random.choice(['square', 'triangle', 'circle'])
    food.speed(0)
    food.shape(shapes)
    food.color(colors)
    food.penup()
    food.goto(0, 100)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0  High Score : 0", align="center",
              font=("candara", 24, "bold"))

    # assigning key directions
    def goup():
        if head.direction != "down":
            head.direction = "up"

    def godown():
        if head.direction != "up":
            head.direction = "down"

    def goleft():
        if head.direction != "right":
            head.direction = "left"

    def goright():
        if head.direction != "left":
            head.direction = "right"

    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)

    wn.listen()
    wn.onkeypress(goup, "w")
    wn.onkeypress(godown, "s")
    wn.onkeypress(goleft, "a")
    wn.onkeypress(goright, "d")

    segments = []

    # Main Gameplay
    while True:
        wn.update()
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")  # tail colour
            new_segment.penup()
            segments.append(new_segment)
            delay -= 0.001
            score += 10
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
        # Checking for head collisions with body segments
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        move()
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                colors = random.choice(['red', 'blue', 'green'])
                shapes = random.choice(['square', 'circle'])
                for segment in segments:
                    segment.goto(1000, 1000)
                segment.clear()

                score = 0
                delay = 0.1
                pen.clear()
                pen.write("Score : {} High Score : {} ".format(
                    score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(delay)

    wn.mainloop()

#3
def flappy_game():
    def draw_floor():
        screen.blit(floor_surface, (floor_x_pos, 900))
        screen.blit(floor_surface, (floor_x_pos + 576, 900))

    def create_pipe():
        random_pipe_pos = random.choice(pipe_height)
        bottom_pipe = pipe_surface.get_rect(midtop=(700, random_pipe_pos))
        top_pipe = pipe_surface.get_rect(midbottom=(700, random_pipe_pos - 300))
        return bottom_pipe, top_pipe

    def move_pipes(pipes):
        for pipe in pipes:
            pipe.centerx -= 5
        return pipes

    def draw_pipes(pipes):
        for pipe in pipes:
            if pipe.bottom >= 1024:
                screen.blit(pipe_surface, pipe)
            else:
                flip_pipe = pygame.transform.flip(pipe_surface, False, True)
                screen.blit(flip_pipe, pipe)

    def remove_pipes(pipes):
        for pipe in pipes:
            if pipe.centerx == -600:
                pipes.remove(pipe)
        return pipes

    def check_collision(pipes):
        for pipe in pipes:
            if bird_rect.colliderect(pipe):
                #death_sound.play()
                return False

        if bird_rect.top <= -100 or bird_rect.bottom >= 900:
            return False

        return True

    def rotate_bird(bird):
        new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
        return new_bird

    def bird_animation():
        new_bird = bird_frames[bird_index]
        new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
        return new_bird, new_bird_rect

    def score_display(game_state):
        if game_state == 'main_game':
            score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)
        if game_state == 'game_over':
            score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
            score_rect = score_surface.get_rect(center=(288, 100))
            screen.blit(score_surface, score_rect)

            high_score_surface = game_font.render(f'High score: {int(high_score)}', True, (255, 255, 255))
            high_score_rect = high_score_surface.get_rect(center=(288, 850))
            screen.blit(high_score_surface, high_score_rect)

    def update_score(score, high_score):
        if score > high_score:
            high_score = score
        return high_score

    #pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=512)
    pygame.init()
    screen = pygame.display.set_mode((576, 1024))
    clock = pygame.time.Clock()
    game_font = pygame.font.SysFont('04B_19.ttf', 40)

    # Game Variables
    gravity = 0.30
    bird_movement = 0
    game_active = True
    score = 0
    high_score = 0

    bg_surface = pygame.image.load("background-day.png").convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

    floor_surface = pygame.image.load("base.png").convert()
    floor_surface = pygame.transform.scale2x(floor_surface)
    floor_x_pos = 0

    bird_downflap = pygame.transform.scale2x(
        pygame.image.load("C:\\Users\\Kartik\\Desktop\\flappy\\bluebird-downflap.png").convert_alpha())
    bird_midflap = pygame.transform.scale2x(
        pygame.image.load("C:\\Users\\Kartik\\Desktop\\flappy\\bluebird-midflap.png").convert_alpha())
    bird_upflap = pygame.transform.scale2x(
        pygame.image.load("C:\\Users\\Kartik\\Desktop\\flappy\\bluebird-upflap.png").convert_alpha())
    bird_frames = [bird_downflap, bird_midflap, bird_upflap]
    bird_index = 0
    bird_surface = bird_frames[bird_index]
    bird_rect = bird_surface.get_rect(center=(100, 552))

    BIRDFLAP = pygame.USEREVENT + 1
    pygame.time.set_timer(BIRDFLAP, 200)

    bird_surface = pygame.image.load('bluebird-midflap.png').convert_alpha()
    bird_surface = pygame.transform.scale2x(bird_surface)
    bird_rect = bird_surface.get_rect(center = (100,512))

    pipe_surface = pygame.image.load("C:\\Users\\Kartik\\Desktop\\flappy\\pipe-green.png")
    pipe_surface = pygame.transform.scale2x(pipe_surface)
    pipe_list = []
    SPAWNPIPE = pygame.USEREVENT
    pygame.time.set_timer(SPAWNPIPE, 1200)
    pipe_height = [400, 600, 800]

    game_over_surface = pygame.transform.scale2x(
        pygame.image.load("C:\\Users\\Kartik\\Desktop\\flappy\\message.png").convert_alpha())
    game_over_rect = game_over_surface.get_rect(center=(288, 512))

    flap_sound = pygame.mixer.Sound("C:\\Users\\Kartik\\Desktop\\flappy\\sound_sfx_wing.wav")
    death_sound = pygame.mixer.Sound("C:\\Users\\Kartik\\Desktop\\flappy\\sound_sfx_hit.wav")
    score_sound = pygame.mixer.Sound("C:\\Users\\Kartik\\Desktop\\flappy\\sound_sfx_point.wav")
    score_sound_countdown = 100

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active:
                    bird_movement = 0
                    bird_movement -= 12
                    flap_sound.play()
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    pipe_list.clear()
                    bird_rect.center = (100, 512)
                    bird_movement = 0
                    score = 0

            if event.type == SPAWNPIPE:
                pipe_list.extend(create_pipe())

            if event.type == BIRDFLAP:
                if bird_index < 2:
                    bird_index += 1
                else:
                    bird_index = 0

                bird_surface, bird_rect = bird_animation()

        screen.blit(bg_surface, (0, 0))

        if game_active:
            # Bird
            bird_movement += gravity
            rotated_bird = rotate_bird(bird_surface)
            bird_rect.centery += bird_movement
            screen.blit(bird_surface, bird_rect)
            game_active = check_collision(pipe_list)

            # Pipes
            pipe_list = move_pipes(pipe_list)
            pipe_list = remove_pipes(pipe_list)
            draw_pipes(pipe_list)

            score += 0.01
            score_display('main_game')
            score_sound_countdown -= 1
            if score_sound_countdown <= 0:
                score_sound.play()
                score_sound_countdown = 100
        else:
            screen.blit(game_over_surface, game_over_rect)
            high_score = update_score(score, high_score)
            score_display('game_over')

        # Floor
        floor_x_pos -= 1
        draw_floor()
        if floor_x_pos <= -576:
            floor_x_pos = 0

        pygame.display.update()
        clock.tick(100)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query


#Casual Conversations
        if 'Hello' in query:
            speak('hi,what can i do for you today')

        elif "how are you" in query:
           speak("I am perfectly fine. How's your day going?")

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is,{strTime}")

        elif  "can you do me a favour" in query:
            speak("What can I do for you?")

        elif 'who created you' in query:
            speak("I was created by a bunch of kids")

        elif "weather" in query:
            webbrowser.open('https://weather.com/en-IN/weather/today/')

        elif 'i want to play a game' in query:
            speak('which game do you want to play. pong game or snake game or flappy bird')

        #Website acessing commands
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'close youtube' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'close instagram' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'close facebook' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'close google' in query:
            os.system("taskkill /im chrome.exe /f")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'close stackoverflow' in query:
            os.system("taskkill /im chrome.exe /f")

        elif "open prime video" in query:
            webbrowser.open("www.primevideo.com")

        elif "close prime video" in query:
            os.system("taskkill/im chrome.exe /f")

        elif "open netflix" in query:
            webbrowser.open("www.netflix.com")

        elif "close netflix" in query:
            os.system("takkill/im chrome.exe /f")

        elif 'open hotstar' in query:
            webbrowser.open("www.hotstar.com")

        elif "close hotstar" in query:
            os.system("taskkill/im chrome.exe /f")

        elif "open Z5" in query:
            webbrowser.open("www.zee5.com")

        elif "close Z5" in query:
            os.system("taskkill/im chrome.exe /f")

        elif 'play music' in query:
            music_dir ='C:\\Users\\Kartik\\Desktop\\CS KK'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'bye bye' in query:
            exit()

        #Play Games

        elif 'pong game' in query:
            speak('use W S keys to move the left paddle and Up and Down keys to move the right paddle')
            the_pong_game()


        elif 'snake game' in query:
            speak('use w,a,s,d keys to move the snake and change its direction')
            the_snake_game()

        elif 'flappy ' in query:
            speak('use spacebar to make the bird fly')
            flappy_game()

        #For the use of this command, please replace 'app_name' with the name of the app you want to open and also replace
        #'app_location' with the location of the app in your machine.

        #########################################

        elif 'something' in query:
            speak('Do not worry, I am your secret keeper')
            DATA = takeCommand()
            file = open('secret.txt', 'a')
            file.write(DATA               )
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')

        elif 'today' in query:
            speak('Tell me, I am excited to know')
            story = takeCommand()
            file = open('today.txt', 'a')
            file.write(story)
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')

        elif 'goals' in query:
            speak('Thats impressive, let me store that to motivate you')
            passion = takeCommand()
            file = open('goal.txt', 'a')
            file.write(passion)
            file.close()
            speak('Do not worry, I am fully secured with passwords and face recognition')


        elif 'remember my secrets' in query:
            speak('Yes I do remember, I am your secret keeper')

            file = open('secret.txt', 'r')
            a= file.read()
            file.close()
            speak(a)



        elif 'my goal' in query:
            speak('yes, I do remember your goals')

            file = open('goal.txt', 'r')
            b=file.read()
            file.close()
            speak(b)


        #########################################


