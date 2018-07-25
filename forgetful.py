# Import needed sub-programs to act as tools with given function
import pygame
import time
import random

# Initialising pygame sub-program
pygame.init()

# Calling height and width of the frame of the program as Variables
display_height = 900
display_width = 600

# Changing essential colours from RGB colour code to Variables
black = (0,0,0)
white = (255,255,255)
grey = (96, 96, 96)
yellow = (255, 233, 0)
orange = (255, 147, 7)
orange2 = (255, 102, 0)
dark_orange = (175, 105, 0)
green = (0, 255, 12)
dark_green = (3, 130, 8)
dark_red = (114, 9, 0)
brown = (81, 48, 16)
red = (255,0,0)
blue = (0,97,255)

# Sets the height and width of program using variables on lines 7, 8
gamedisplay = pygame.display.set_mode((display_height,display_width))

# Sets title of the Window
pygame.display.set_caption('For-Get-Ful')

# A variable to set up a method of maintaining a certain FPS count
clock = pygame.time.Clock()

# Starts the program background off as white from Variable line 12
gamedisplay.fill(white)

# Update the screen to show off the colour implemented on line 38
pygame.display.flip()

# A tool to display any text on any surface
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# A tool to display the characters on-screen whilst adjusting color and size
def game_subject(text,dw,dh,color,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (dw,dh)
    gamedisplay.blit(TextSurf, TextRect)

def after_timer():
    pygame.draw.rect(gamedisplay, black,(5,10,140,250))
    pygame.draw.rect(gamedisplay, black,(155,10,140,250))
    pygame.draw.rect(gamedisplay, black,(305,10,140,250))
    pygame.draw.rect(gamedisplay, black,(455,10,140,250))
    pygame.draw.rect(gamedisplay, black,(605,10,140,250))
    pygame.draw.rect(gamedisplay, black,(755,10,140,250))
    pygame.display.update()
    clock.tick(60)

# A tool to display buttons
def intro_button(msg,x,y,w,h,ic,ac,action=None):
    mouse1 = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse1[0] > x and y+h > mouse1[1] > y:
        pygame.draw.rect(gamedisplay, ac,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textsurf, textrect = text_objects (msg,smalltext,black)
        textrect.center = ( (x+(w/2)), (y+(h/2)) )
        gamedisplay.blit(textsurf,textrect)
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "set":
                settings()
            elif action == "set_back":
                game_intro()

    else:
        pygame.draw.rect(gamedisplay, ic,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textsurf, textrect = text_objects (msg,smalltext,black)
        textrect.center = ( (x+(w/2)), (y+(h/2)) )
        gamedisplay.blit(textsurf,textrect)

# Program In-game loop
def game_loop():
    font = pygame.font.Font("freesansbold.ttf", 225)
    text = ''

    # In-game random 6-digit number generator
    subject1 = random.randint(1,9)
    subject1 = str(subject1)

    subject2 = random.randint(1,9)
    subject2 = str(subject2)

    subject3 = random.randint(1,9)
    subject3 = str(subject3)

    subject4 = random.randint(1,9)
    subject4 = str(subject4)

    subject5 = random.randint(1,9)
    subject5 = str(subject5)

    subject6 = random.randint(1,9)
    subject6 = str(subject6)

    subjects_tog = (subject1,subject2,subject3,subject4,subject5,subject6)
    subjects_tog = str(subjects_tog)

    # In-game objects
    time_bar = pygame.Rect(0,590,900,80)

    # In-game objects
    time_bar_2 = pygame.Rect(0,270,900,95)

    display_input_1 = pygame.Rect(5,375,140,205)
    display_input_2 = pygame.Rect(155,375,140,205)
    display_input_3 = pygame.Rect(305,375,140,205)
    display_input_4 = pygame.Rect(455,375,140,205)
    display_input_5 = pygame.Rect(605,375,140,205)
    display_input_6 = pygame.Rect(755,375,140,205)

    # Random box color generator
    subject_color = (blue,green,red,yellow)
    ran_color1 = random.choice(subject_color)
    ran_color2 = random.choice(subject_color)
    ran_color3 = random.choice(subject_color)
    ran_color4 = random.choice(subject_color)
    ran_color5 = random.choice(subject_color)

    loop = True

   # To keep the game running longer than 1 frame
    while loop:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          pressed = pygame.key.get_pressed()
          if pressed[pygame.K_ESCAPE]:
             game_intro()

      pygame.display.update()
      gamedisplay.fill(black)

      # Subject display squares
      pygame.draw.rect(gamedisplay, orange,(5,10,140,250))
      pygame.draw.rect(gamedisplay, orange,(155,10,140,250))
      pygame.draw.rect(gamedisplay, orange,(305,10,140,250))
      pygame.draw.rect(gamedisplay, orange,(455,10,140,250))
      pygame.draw.rect(gamedisplay, orange,(605,10,140,250))
      pygame.draw.rect(gamedisplay, orange,(755,10,140,250))

      # Random in-game subject numbers
      game_subject(subject1,73.5,140,black,115)
      game_subject(subject2,225,140,black,115)
      game_subject(subject3,375,140,black,115)
      game_subject(subject4,525,140,black,115)
      game_subject(subject5,675,140,black,115)
      game_subject(subject6,827,140,black,115)

      # fake-input display squares
      pygame.draw.rect(gamedisplay, ran_color1, display_input_1)
      pygame.draw.rect(gamedisplay, ran_color2, display_input_2)
      pygame.draw.rect(gamedisplay, ran_color3, display_input_3)
      pygame.draw.rect(gamedisplay, ran_color4, display_input_4)
      pygame.draw.rect(gamedisplay, ran_color5, display_input_5)
      pygame.draw.rect(gamedisplay, ran_color2, display_input_6)

      # Time bar and its function
      pygame.draw.rect(gamedisplay, ran_color4, time_bar)
      time_bar_numb = time_bar.move_ip(-1,0)

      if time_bar == pygame.Rect(-900,590,900,80):
          game_loop2()

      # Time bar and its function
      pygame.draw.rect(gamedisplay, ran_color1, time_bar_2)
      time_bar_numb_2 = time_bar_2.move_ip(+1,0)

      pygame.display.update()
      clock.tick(60)

      def game_loop2():

          font = pygame.font.Font("freesansbold.ttf", 225)
          text = ''

          # In-game objects
          time_bar = pygame.Rect(0,590,900,80)

          # In-game objects
          time_bar_2 = pygame.Rect(0,270,900,35)

          # In-game objects
          time_bar_3 = pygame.Rect(0,315,900,25)

          # In-game objects
          time_bar_4 = pygame.Rect(0,350,900,15)

          # In-game objects
          new_tb = pygame.Rect(1800,590,900,80)

          # Proffesional help: skrx----------------------------------------------
          input_boxes = [
          pygame.Rect(5,375,140,205),
          pygame.Rect(155,375,140,205),
          pygame.Rect(305,375,140,205),
          pygame.Rect(455,375,140,205),
          pygame.Rect(605,375,140,205),
          pygame.Rect(755,375,140,205),
          ]
          # Proffesional help: skrx----------------------------------------------

          # Random box color generator
          subject_color = (blue,green,red,yellow)
          ran_color1 = random.choice(subject_color)
          ran_color2 = random.choice(subject_color)
          ran_color3 = random.choice(subject_color)
          ran_color4 = random.choice(subject_color)
          ran_color5 = random.choice(subject_color)

          loop = True

         # To keep the game running longer than 1 frame
          while loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_ESCAPE]:
                   game_intro()
                elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if text == subject1+subject2+subject3+subject4+subject5+subject6:
                                print("correct")
                                text = str(text)
                                gamedisplay.fill(black)
                                game_subject("You Win",450,300,green,170)
                                pygame.display.update()
                                time.sleep(2)
                                game_loop()
                            elif text != subject1+subject2+subject3+subject4+subject5+subject6:
                                print("incorrect")
                                text = str(text)
                                gamedisplay.fill(black)
                                game_subject("You Lose",450,300,red,170)
                                pygame.display.update()
                                time.sleep(2)
                                game_intro()
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            pygame.display.update()
            gamedisplay.fill(black)

            # Proffesional help: skrx----------------------------------------------
            # Draw the boxes.
            for box in input_boxes:
                pygame.draw.rect(gamedisplay, ran_color5, box)

            # Blit one number after the other at the corresponding box.
            for number, box in zip(text, input_boxes):
                txt_surface = font.render(number, True, black)
                gamedisplay.blit(txt_surface, (box.x+5, box.y+5))
            # Proffesional help: skrx----------------------------------------------

            # Subject display squares
            pygame.draw.rect(gamedisplay, orange,(5,10,140,250))
            pygame.draw.rect(gamedisplay, orange,(155,10,140,250))
            pygame.draw.rect(gamedisplay, orange,(305,10,140,250))
            pygame.draw.rect(gamedisplay, orange,(455,10,140,250))
            pygame.draw.rect(gamedisplay, orange,(605,10,140,250))
            pygame.draw.rect(gamedisplay, orange,(755,10,140,250))

            # Random in-game subject numbers
            game_subject(subject1,73.5,140,orange,115)
            game_subject(subject2,225,140,orange,115)
            game_subject(subject3,375,140,orange,115)
            game_subject(subject4,525,140,orange,115)
            game_subject(subject5,675,140,orange,115)
            game_subject(subject6,827,140,orange,115)

            # Time bar and its function
            pygame.draw.rect(gamedisplay, red, time_bar)
            time_bar_numb = time_bar.move_ip(-1,0)

            if time_bar == pygame.Rect(-900,590,900,80):
                gamedisplay.fill(black)
                game_subject("You Lose",450,300,red,170)
                pygame.display.update()
                time.sleep(2)
                game_intro()

            # Time bar and its function
            pygame.draw.rect(gamedisplay, red, time_bar_2)
            time_bar_numb_2 = time_bar_2.move_ip(+1,0)

            # Time bar and its function
            pygame.draw.rect(gamedisplay, red, time_bar_3)
            time_bar_numb_3 = time_bar_3.move_ip(-1,0)

            # Time bar and its function
            pygame.draw.rect(gamedisplay, red, time_bar_4)
            time_bar_numb_4 = time_bar_4.move_ip(+1,0)

            # Time bar and its function
            pygame.draw.rect(gamedisplay, green, new_tb)
            new_tb_move = new_tb.move_ip(-1,0)

            pygame.display.update()
            clock.tick(60)

            # Proffesional help: skrx----------------------------------------------
            # Draw the boxes.
            for box in input_boxes:
                pygame.draw.rect(gamedisplay, ran_color5, box)

            # Blit one number after the other at the corresponding box.
            for number, box in zip(text, input_boxes):
                txt_surface = font.render(number, True, black)
                gamedisplay.blit(txt_surface, (box.x+5, box.y+5))
            # Proffesional help: skrx----------------------------------------------

            pygame.display.update()
            clock.tick(60)

# Program intro/main menu
def game_intro():

     intro = True

     # To keep the game running longer than 1 frame
     while intro:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()

       gamedisplay.fill(black)
       pygame.draw.rect(gamedisplay,orange,(190,130,530,130))

       # The big text in the main menu displaying "For-Get-Ful"
       largetext = pygame.font.Font("freesansbold.ttf",90)
       textsurf, textrect = text_objects("For-Get-Ful", largetext, black)
       textrect.center = ((display_height/2),(200))
       gamedisplay.blit(textsurf,textrect)

       # Menu-Buttons; Play, Quit, Settings
       intro_button("Play",-870,275,1800,30,green,dark_green,"play")
       intro_button("How To Play",-830,315,1800,30,orange,dark_orange,"set")
       intro_button("Quit",-870,355,1800,30,red,dark_red,"quit")

       pygame.display.update()
       clock.tick(15)

#Program Settings Page
def settings():
       set_s = True

     # To keep the game running longer than 1 frame
       while set_s:
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 quit()
             pressed = pygame.key.get_pressed()
             if pressed[pygame.K_ESCAPE]:
                game_intro()

         gamedisplay.fill(black)
         pygame.draw.rect(gamedisplay, orange,(10,10,880,125))
         pygame.draw.rect(gamedisplay, orange,(600,145,290,385))
         intro_button("( Take me home, country road )",10,542.5,880,50,red,dark_red,"set_back")
         game_subject("How To Play",310,75,black,100)

         pygame.display.update()
         clock.tick(15)

# Sequential events
game_intro()
game_loop()
settings()
pygame.quit()
quit()
