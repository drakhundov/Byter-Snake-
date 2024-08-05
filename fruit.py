import pygame, random
import snake, config

pos = {
	'x': 0,
	'y': 0
}


def generate():
	snake.tails.append([pos['x'], pos['y']])

	pos['x'] = round(random.randrange(0, config.WIDTH - config.BLOCK) / config.BLOCK) * config.BLOCK
	pos['y'] = round(random.randrange(0, config.HEIGHT - config.BLOCK) / config.BLOCK) * config.BLOCK


def draw(display):
	pygame.draw.rect(display, config.COLORS['apple'], (
						pos['x'], pos['y'],
						config.BLOCK, config.BLOCK))


def eaten():
	if (snake.pos['x'] == pos['x'] and 
	    snake.pos['y'] == pos['y']):
		return True

	else:
		return False