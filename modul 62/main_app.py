import pygame

#init
pygame.init()

#variable running game
isRun = True
#display game

window_panjang = 500
window_lebar = 500
window = pygame.display.set_mode((window_panjang, window_lebar))
#object game
#koordinat
x = 250
y = 250

#ukuran
panjang = 20
lebar = 20

#kecepatan gerak
speed = 10


while isRun:
    pygame.time.delay(10)
    #user input, database input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun=False

    #ambil semua keyboard press
    keys = pygame.key.get_pressed()
    #ambil ke kiri
    if keys[pygame.K_LEFT] and x>0:
        x -= speed
    if keys[pygame.K_RIGHT] and x < window_lebar-lebar:
        x += speed
    if keys[pygame.K_DOWN] and y < window_panjang-panjang:
        y += speed
    if keys[pygame.K_UP] and y > 0:
        y -= speed

    #update asset
    window.fill((255,255,255))
    pygame.draw.rect(window, (255,0,125),(x,y,panjang, lebar))
    pygame.display.update()

#render ke display
pygame.quit()



