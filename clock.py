import pygame 

pygame.init()

screen = pygame.display.set_mode((500,600))

GREEN = (0,153,0)
RED= (153,0,0)
BLACK= (0,0,0)


running = True

font = pygame.font.SysFont("Timenewroman", 24)

text_1 = font.render('+' , True, BLACK) 
text_2 = font.render('-' , True, BLACK) 
text_3 = font.render('+' , True, BLACK) 
text_4 = font.render('-' , True, BLACK) 
text_5 = font.render('Start' , True, BLACK) 
text_6 = font.render('Reset' , True, BLACK) 

while running:
	
	screen.fill(GREEN)

	pygame.draw.rect(screen, RED, (100,50,50,50))
	pygame.draw.rect(screen, RED, (100,200,50,50))
	pygame.draw.rect(screen, RED, (200,50,50,50))
	pygame.draw.rect(screen, RED, (200,200,50,50))
	pygame.draw.rect(screen, RED, (300,50,150,50))
	pygame.draw.rect(screen, RED, (300,50,150,50))
	pygame.draw.rect(screen, RED, (300,150,150,50))

	
	screen.blit(text_1, (100,50))
	screen.blit(text_2, (100,200))
	screen.blit(text_3, (200,50))
	screen.blit(text_4, (200,200))
	screen.blit(text_5, (300,50))
	screen.blit(text_6, (300,150))

	pygame.draw.rect(screen,BLACK,(50,520,400,50))	
    	

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("ERROR")

		pygame.display.flip()

pygame.quit()		
