import pygame
import random

atoms=[] # list of all atoms
window_size = 300
pygame.init()
window = pygame.display.set_mode((window_size, window_size))


def draw(surface, x, y, color, size):
    for i in range(0, size):
        pygame.draw.line(surface, color, (x, y-1), (x, y+2), abs(size))

def force(atoms1, atoms2, g):
    for i in range(len(atoms1)):
        f_x = 0 # horizontal force function
        f_y = 0 # vertical force function
        for j in range(len(atoms2)):
            a = atoms1[i]
            b = atoms2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]
            r = (dx*dx + dy*dy)**0.5
            if( r > 0 and r < 100):
                F = (g*a["m"]*b["m"])/(r**2)
                f_x += F*dx
                f_y += F*dy
        a["v_x"] += (f_x)/(a["m"]) # a = F/m
        a["v_y"] += (f_y)/(a["m"])
        a["v_x"] *= 0.5 #to make the particles a bit slower
        a["v_y"] *= 0.5
        a["x"] += a["v_x"]
        a["y"] += a["v_y"]
        if(a["x"] <= 0 or a["x"] >= window_size):
            a["v_x"] *=-1
        if(a["y"] <= 0 or a["y"] >= window_size):
            a["v_y"] *=-1       

def randomxy():
    return round(random.random()*window_size + 1)
               
def atom(x, y, c, m):
    return {"x": x, "y": y, "v_x": 0, "v_y": 0, "color": c, "m": m}

def create(number, color, mass):
    group = []
    for i in range(number):
        group.append(atom(randomxy(), randomxy(), color, mass))
        atoms.append((group[i]))
    return group

green = create(500, "green", 4)
red = create(50, "red", 100)
blue = create(50, "blue", 1)

run = True
while run:
    window.fill(0)
    force(blue, red, -0.5)
    force(red, blue, -0.5)
    force(blue, green, -0.8)
    force(green, blue, 0.001)
    force(blue, blue, 0)
    force(red, red, -0.5)
    force(red, green, 0.25)
    force(green, red, 0.25)
    force(green, green, 0)
    for i in range(len(atoms)):
        draw(window, atoms[i]["x"], atoms[i]["y"], atoms[i]["color"], 3)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
exit()