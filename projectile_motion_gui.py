import pygame
import math
import os
import pygame_gui
from pygame_gui.core import ObjectID
import pygame_widgets
from pygame_widgets.button import Button
import decimal
pygame.init()

i_icon = os.getcwd() + './sem.png'
icon = pygame.image.load(i_icon)
pygame.display.set_icon(icon)
pygame.display.set_caption('projectile motion')

window = pygame.display.set_mode((1400, 700))
font = pygame.font.SysFont('Segoe UI', 20)

red = '#8B0000'
gray = '#dcdcdc'
black = '#101010'
blue = '#00008B'

clock = pygame.time.Clock() 

theme = '.\entry_line.json'
btheme = 'button.json'
manager = pygame_gui.UIManager((500, 500), theme)
manager.get_theme().load_theme(theme)

text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 100), (300, 35)),
     placeholder_text = 'enter velocity',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry1'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 200), (300, 35)),
     placeholder_text = 'enter theta',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry2'))
text_input = pygame_gui.elements.UITextEntryLine(
     relative_rect = pygame.Rect((100, 300), (300, 35)),
     placeholder_text = 'acceleration due to gravity',
     manager = manager, object_id = ObjectID(class_id = 'text_entry_line',
                                             object_id = '#main_text_entry3'))
manager.get_theme().load_theme(btheme)
button = pygame_gui.elements.ui_button.UIButton(
    relative_rect = pygame.Rect((100, 400), (300, 25)),
    text = 'OK', manager = manager, object_id = ObjectID(class_id = 'button',
                                             object_id = 'text_button'))
def momentum(velocity, theta, g):
    runningmomentum = True
    time_of_flight=2*velocity*math.sin(theta)/g
    horizontal_range = ((velocity*2)*math.sin(2*theta))/g
    num = float(horizontal_range)
    horizontal_range=abs(num)
    time_of_flight=(2*velocity*math.sin(theta))/g
    num = float(time_of_flight)
    time_of_flight=abs(num)
    #y=i*math.tan(theta) / g*(i**2)/(2*(velocity)**2)*math.cos(theta)**2
    h_max=(velocity*math.sin(theta))**2/2*g
    print(h_max)
    print(horizontal_range)

    while runningmomentum:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningmomentum = False
        window.fill(gray)
        x=[]
        for i in range(0,int(horizontal_range/2)):
            x.append(i)
        #print("a:"+str(x)) 
        for i in range(0,int(h_max)):
            x.append(i)
        #print("b:"+str(x))   
        '''for j in range(0,int(h_max)) :
                print("b:"+str(j))
                pygame.draw.circle(window, red, (i, j), 5)

                #pygame.draw.line(window, black, (i,j), (650-i,650-j),4'''
        '''for i in range(int(horizontal_range) , 0,+1):
            for j in range(10, 0, -1):
                pygame.draw.circle(window, red, (x, y), 5)'''


        pygame.draw.line(window, black, (50, 650), (1350, 650), 4)
        pygame.draw.line(window, black, (50, 650), (50, 50), 4)
        drawh_range = font.render(str('horizontalrange is ') +str(horizontal_range)+' mts', True, red)
        drawh_flight = font.render(str('height is ') +str(h_max)+' mts', True, red)
        drawh_time = font.render(str('time of flight is ') +str(time_of_flight)+' seconds', True, red)

        window.blit(drawh_range, (1000, 20))
        window.blit(drawh_flight, (1000, 40))
        window.blit(drawh_time, (1000, 60))

        pygame.display.update()
class parameters():
    runningparameters=True    
    while runningparameters:
        window.fill(gray)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningparameters = False
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry1'):
                velocity = float(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry2'):
                theta = float(event.text)
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry3'):
                g = float(event.text)
    
            manager.process_events(event)    
            if (event.type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_object_id == 'text_button'):
                pygame_widgets.update(event)
                momentum(velocity, theta, g)

        manager.update(clock.tick(60)/1000)    
        manager.draw_ui(window)
        pygame.display.update()
parameters()
pygame.quit()
