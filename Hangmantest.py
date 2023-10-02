import pygame
import math
import random
pygame.init()

WEIDTH,HEIGHT=800,500
screen=pygame.display.set_mode((WEIDTH,HEIGHT))
pygame.display.set_caption("Hang Man")
FPS=40
clock=pygame.time.Clock()
run=True

hangman_status=0
word=["UNIVERSE","BALLS","HAPPINESS","NATURE","TEAMWORK","DIMONDS","PRACTICE"]
words=random.choice(word)
guessed=[]




#IMAGES
images=[]
for i in range(7):
    a=("hangman"+str(i)+".png")
    image=pygame.image.load(a)
    images.append(image)
#BUTTONS
RADIUS=20
GAP=15
LETTERS=[]
startx=round((WEIDTH-(GAP+RADIUS*2)*13)/2)
starty=400
A=65
for i in range(26):
    x= startx + GAP*2+((RADIUS*2+GAP)*(i%13))
    y= starty+((i//13)*(RADIUS*2+GAP))
    LETTERS.append([x,y,chr(A+i),True])

#FONTS ON BUTTONS
LETTER_FONT=pygame.font.SysFont("new roman",40)
Word_font=pygame.font.SysFont("new roman",60)
TITLE_FONT=pygame.font.SysFont("new roman",70)

#FUNCTION TO DRAW
def draw():
     screen.fill((255,255,255))

     text=TITLE_FONT.render("WELCOME TO HANGMAN ",1,(0,0,0))
     screen.blit(text,(WEIDTH/2-text.get_width()/2,20))


     display_word=""
     for i in words:
         if i in guessed:
             display_word += i+""
         else:
             display_word+=" _"    
         text=Word_font.render(display_word,1,(0,0,0))  
         screen.blit(text,(400,200))       




     for letter in LETTERS:
         x,y,ltr,visible=letter
         if visible:
             pygame.draw.circle(screen,(0,0,0),(x,y),RADIUS,3)
             text=LETTER_FONT.render(ltr,1,(0,0,0))
             screen.blit(text,(x-text.get_width()/2,y-text.get_height()/2))
          

     screen.blit(images[hangman_status],(150,100))
     pygame.display.update()




#FUNCTION WSED AT STARTING
def display_message(message):
     pygame.time.delay(1000)
     screen.fill((0,0,0))
     text=Word_font.render(message,1,(255,255,255))
     screen.blit(text,(WEIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
     pygame.display.update()
     pygame.time.delay(5000)  


#FUCTION TO DRAW RECTANGLE
button1=pygame.Rect(335,140,140,55)
surf=TITLE_FONT.render("PLAY",True,(0,0,0))
button2=pygame.Rect(335,290,140,55)
buff=TITLE_FONT.render("QUIT",True,(0,0,0))


    
     
#FUNCTION WSED TO RUN GAME
def main():
   global hangman_status  
   run=True
   while run:
     clock.tick(FPS)


     for i in pygame.event.get():
        if i.type==pygame.QUIT:
            run=False
        if i.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y=pygame.mouse.get_pos()
            for letter in LETTERS:
                x,y,ltr,visible=letter
                if visible: 
                     distance=math.sqrt((x-m_x)**2+(y-m_y)**2)
                    
                     if distance<=RADIUS:
                      letter[3]=False
                      guessed.append(ltr)
                      if ltr not in words:
                          hangman_status+=1
    
     draw()
    
     won=True
     for letter in words:
        if letter not in guessed:
            won=False
            break

     if won:
        display_message("YOU WON!")
        break
     if hangman_status==6:
        display_message("YOU LOST!")
        
        break

#ACTUAL LOOP TO RUN GAME
    
while run:
    screen.fill((225,225,225))
    
    for i in pygame.event.get():
            



        
        
        
        
        
        
        if i.type==pygame.QUIT:    
          run=False
          pygame.quit()  
    
    a,b=pygame.mouse.get_pos()
    if button1.x<=a <=button1.x+100 and button1.y<=b<=button1.y+100:
        pygame.draw.rect(screen,(100,100,100),button1)
        if i.type==pygame.MOUSEBUTTONDOWN:
            main()
            run=False
    if button2.x<=a <=button2.x+100 and button2.y<=b<=button2.y+100:
        pygame.draw.rect(screen,(100,100,100),button2)
        if i.type==pygame.MOUSEBUTTONDOWN:
            pygame.quit()
    screen.blit(surf,(button1.x+10,button1.y+5))
    screen.blit(buff,(button2.x+10,button2.y+5))
    
    
    pygame.display.update()
    


