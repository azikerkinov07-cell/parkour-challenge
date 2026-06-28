# levels.py
import pygame

def create_levels():
    return [
        # Level 1
        {"platforms": [pygame.Rect(0,560,800,40), pygame.Rect(150,460,200,20), pygame.Rect(450,380,180,20), pygame.Rect(100,280,150,20)],
         "hazards": [pygame.Rect(280,540,100,20)], "goal": pygame.Rect(720,220,50,60), "start": (80,400)},
        
        # Level 2
        {"platforms": [pygame.Rect(0,560,800,40), pygame.Rect(100,480,130,20), pygame.Rect(320,400,140,20), pygame.Rect(550,320,150,20), pygame.Rect(200,230,160,20)],
         "hazards": [pygame.Rect(220,540,110,20), pygame.Rect(480,300,60,20)], "goal": pygame.Rect(710,150,50,60), "start": (80,400)},
        
        # Level 3
        {"platforms": [pygame.Rect(0,560,250,40), pygame.Rect(320,470,110,20), pygame.Rect(500,390,130,20), pygame.Rect(150,310,120,20), pygame.Rect(650,240,130,20), pygame.Rect(300,170,150,20)],
         "hazards": [pygame.Rect(200,540,140,20), pygame.Rect(420,360,70,20)], "goal": pygame.Rect(720,100,50,60), "start": (80,400)},
        
        # Level 4
        {"platforms": [pygame.Rect(0,560,800,40), pygame.Rect(80,450,140,20), pygame.Rect(280,370,100,20), pygame.Rect(480,290,160,20), pygame.Rect(650,200,120,20)],
         "hazards": [pygame.Rect(180,540,160,20), pygame.Rect(350,350,50,20)], "goal": pygame.Rect(730,130,50,60), "start": (80,400)},
        
        # Level 5
        {"platforms": [pygame.Rect(0,560,200,40), pygame.Rect(250,470,110,20), pygame.Rect(420,380,130,20), pygame.Rect(180,290,100,20), pygame.Rect(520,230,140,20), pygame.Rect(650,150,130,20), pygame.Rect(100,100,120,20)],
         "hazards": [pygame.Rect(220,540,130,20), pygame.Rect(380,360,60,20), pygame.Rect(580,210,70,20)], "goal": pygame.Rect(720,60,50,60), "start": (80,400)}
    ]