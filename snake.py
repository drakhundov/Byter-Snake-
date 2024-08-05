import pygame
import config

tails = []

SPEED = 10

pos = {
	'x': config.WIDTH/2 - config.BLOCK,
	'y': config.HEIGHT/2 - config.BLOCK,
	'x_change': -SPEED,
	'y_change': 0
}


def move():
	# move snake tails
	ltx = pos['x']
	lty = pos['y']

	for i, tail in enumerate(tails):
		_ltx = tail[0]
		_lty = tail[1]

		tails[i][0] = ltx
		tails[i][1] = lty

		ltx = _ltx
		lty = _lty

	# move snake head
	pos['x'] += pos['x_change']
	pos['y'] += pos['y_change']

	# teleport snake, if needed
	if pos['x'] < -config.BLOCK:
		pos['x'] = config.WIDTH

	elif pos['x'] > config.WIDTH:
		pos['x'] = 0

	if pos['y'] < -config.BLOCK:
		pos['y'] = config.HEIGHT

	elif pos['y'] > config.HEIGHT:
		pos['y'] = 0


def draw(display):
	# draw snake tails
	for tail in tails:
		pygame.draw.rect(display, config.COLORS['tail'], (
							tail[0], tail[1],
							config.BLOCK,
							config.BLOCK))

	# draw snake head
	pygame.draw.rect(display, config.COLORS['head'], (
						pos['x'], 
						pos['y'],
						config.BLOCK,
						config.BLOCK))


def check_tail():
	global tails

	for i, tail in enumerate(tails):
		if (pos['x']+pos['x_change'] == tail[0] and 
		    pos['y']+pos['y_change'] == tail[1]):
			tails = tails[:i]
			break
