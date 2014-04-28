import pygame, sys, os, random
from pygame.locals import *
pygame.init() #inicia pygame
#inicia la ventana y su nombre
dimx=1280;dimy=720 #dimensiones de la ventana
spritesheet = pygame.image.load(os.path.join("Arq44x76.png"))
warning=pygame.image.load(os.path.join("warn.png"))
ven=pygame.display.set_mode((dimx,dimy),pygame.FULLSCREEN)
spritesheet.convert();warning.convert()
pygame.display.set_caption("Nombre del juego")
background = pygame.image.load(os.path.join("media","background.png"))
backgroundrect = background.get_rect()
#background.fill((255,255,255)) # relleno de fondo a cambiar por imagen
background = background.convert()  
ven.blit(background,(0,0))
arq=[]
for alf in range(1,11,1): # recorrer 10 elementos para arq
   arq.append(spritesheet.subsurface((48*(alf-1),0,48,76)))
for nbr in range(len(arq)):
    arq[nbr].set_colorkey((255,255,255)) # blanco = alpha
    arq[nbr] = arq[nbr].convert_alpha()
    print "alpha en =", nbr
#bliteo de todos los cuadros
#for nbr in range(len(arq)):
#    ven.blit(arq[nbr], (nbr*48, 0))  #blit de el arq[]
#    print "blit de =", nbr

clock = pygame.time.Clock()        #clock para milisec.
mainloop = True
FPS = 65                   #FPS dejemos la caga con los fps :D okno C:
playtime = 0
cycletime = 0
interval = .10 # cuanto tiempo esta cada imagen app .-.
picnr = 0
posx=300;posy=300 #posiciones de img
der= False;aba=False;izq=False;arr= False # variables de movimiento en falso
standf=True;standb=False #detenido hacia adelante o atras
while mainloop:
    milliseconds = clock.tick(FPS)  # milisec despues del ultimo frame
    seconds = milliseconds / 1000.0 # seconds q pasaron del utimo frame
    playtime += seconds
    cycletime += seconds
    mypicture = arq[picnr]
    mouspos=pygame.mouse.get_pos()
    #condicionales de stand y direccion
    if (der and izq and arr and aba) == False:
        standf=True
    if (der or izq or arr or aba) == True:
        standf=False
    if cycletime > interval:
        if standf:
            picnr=0
            ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy)) #limpia imagen anterior
            ven.blit(mypicture, (posx,posy))
        if standb:
            picnr=3
            ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy)) 
            ven.blit(mypicture, (posx,posy))                
        if (der or izq or aba)and (not arr):
            ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy)) 
            ven.blit(mypicture, (posx,posy))
            picnr += 1
            if picnr >= 3:
                picnr = 1
        # if (arr or izq)and (not der or aba):
        #     if picnr!=5:
        #         picnr = 4 
        #     ven.blit(background.subsurface((300,300,48,76)),(posx,posy)) 
        #     ven.blit(mypicture, (posx,posy))
        #     picnr += 1
        #     if picnr >= 6:
        #         picnr = 4
            
        if arr:
            if picnr!=5:
                picnr=4
            ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy)) 
            ven.blit(mypicture, (posx,posy))
            picnr += 1
            if picnr >= 6:
                picnr = 4
        cycletime = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False # X de la ventana
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False; sys.exit() # ESC salir
            #if presionar tecla
            if event.key == pygame.K_d: der=True
            if event.key == pygame.K_a: izq = True
            if event.key == pygame.K_w: arr= True
            if event.key == pygame.K_s: aba= True
        elif event.type == pygame.KEYUP:
            #if soltar tecla
            if event.key == pygame.K_d: der=False
            if event.key == pygame.K_a: izq = False
            if event.key == pygame.K_w: arr= False
            if event.key == pygame.K_s: aba= False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]==True:
               if (590<mouspos[0]<670)and (408<mouspos[1]<440):
                  ven.blit(warning,(random.randint(0,dimx),random.randint(0,dimy)))
    if der and posx<(dimx-48):
        ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy))#limpia y redibuja
        posx +=3;ven.blit(mypicture, (posx,posy))
    if izq and posx > 0:
        ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy))
        posx -=3;ven.blit(mypicture, (posx,posy))
    if arr and posy > 0:
        ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy))
        posy -=3;ven.blit(mypicture, (posx,posy))
    if aba and posy<(dimy-76):
        ven.blit(background.subsurface((posx,posy,48,76)),(posx,posy))
        posy +=3;ven.blit(mypicture, (posx,posy))

    pygame.display.flip()
#dia de visita de flaco y diego