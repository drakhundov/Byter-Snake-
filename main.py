import pygame
import snake, fruit, config


pygame.init()

score = 0

killed = False


clock = pygame.time.Clock()

display = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
pygame.display.set_caption('Byter')

fruit.generate()

while not killed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			killed = True

		elif event.type == pygame.KEYDOWN:
			if snake.pos['y_change'] == 0:
				if event.key == pygame.K_UP:
					snake.pos['y_change'] = -snake.SPEED
					snake.pos['x_change'] = 0

				if event.key == pygame.K_DOWN:
					snake.pos['y_change'] = snake.SPEED
					snake.pos['x_change'] = 0

			if snake.pos['x_change'] == 0:
				if event.key == pygame.K_LEFT:
					snake.pos['x_change'] = -snake.SPEED
					snake.pos['y_change'] = 0

				if event.key == pygame.K_RIGHT:
					snake.pos['x_change'] = snake.SPEED
					snake.pos['y_change'] = 0

	# clear screen
	display.fill((0, 0, 0))
	
	snake.move()
	snake.draw(display)

	if fruit.eaten():
		score += 1
		fruit.generate()

	fruit.draw(display)
	
	snake.check_tail()

	pygame.display.update()
	clock.tick(config.FPS)


pygame.quit()
exit()