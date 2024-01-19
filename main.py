import math as m
import pygame 
import random as r
from pygame.locals import *

pygame.init()

green = (0, 255, 0)
red = (255, 0, 0)

grid_size = int(500)

number_of_points = int(26)

coord_label = [""] * number_of_points
pos_x = [0] * number_of_points
pos_y = [0] * number_of_points

coordinate_delta_x = [0] * number_of_points
coordinate_delta_y = [0] * number_of_points
coordinate_median_deltas = [0.00] * number_of_points

cost = int(0)
total_cost = int(0)

current_pos_x = int(0)
current_pos_y = int(0)
nearest_neighbor = str("")
current_position = str("0")

screen = pygame.display.set_mode((grid_size+50, grid_size+50))
pygame.display.set_caption("Nearest Neighbor Problem")

def random_coordinate(MIN, MAX):
	return [r.randint(MIN, MAX), r.randint(MIN, MAX)]

def index_alphabet(INDEX):
	if INDEX == 0:
		return 'A'
	else:
		return chr(ord('A') + INDEX)

for x, _ in enumerate(coord_label):
	coord_label[x] = str(index_alphabet(x))
	pos_x[x], pos_y[x] = random_coordinate(5, grid_size)[0], random_coordinate(5, grid_size)[1]

print("Randomly generated points: ", coord_label)
print("Associated X positions: ", pos_x)
print("Associated Y positions: ", pos_y)

current_position = coord_label[0]
current_pos_x = pos_x[0]
current_pos_y = pos_y[0]

for x in range(0,number_of_points):
	coordinate_delta_x[x] = abs((current_pos_x - pos_x[x]))
	coordinate_delta_y[x] = abs((current_pos_y - pos_y[x]))
	coordinate_median_deltas[x] = (float(coordinate_delta_x[x]) + float(coordinate_delta_y[x])) / 2

print("Mean difference: ", coordinate_median_deltas)

valid_positions = [pos for pos in coord_label if pos != "A"]
nearest_neighbor = min(valid_positions, key=lambda pos: coordinate_median_deltas[coord_label.index(pos)])

print("Origin point: ", current_position)
print("Nearest neighbor point: ", nearest_neighbor)

cost += coordinate_median_deltas[coord_label.index(nearest_neighbor)]

print("Cost (distance to nearest neighbor point): ", cost)

for x in range(number_of_points):
	pygame.draw.circle(screen, (255, 255, 255), (pos_x[x], pos_y[x]), 3)
	font = pygame.font.Font(None, 12)
	text = font.render(coord_label[x], True, (255, 255, 255))
	screen.blit(text, (pos_x[x] + 10, pos_y[x] + 10))

pygame.draw.line(screen, green, (current_pos_x, current_pos_y), (pos_x[coord_label.index(nearest_neighbor)], pos_y[coord_label.index(nearest_neighbor)]), 2)
pygame.draw.circle(screen, green, (current_pos_x, current_pos_y), 5)
pygame.draw.circle(screen, red, (pos_x[coord_label.index(nearest_neighbor)], pos_y[coord_label.index(nearest_neighbor)]), 5)

pygame.display.flip()

running = True
while running:
	for event in pygame.event.get():
		if event.type == QUIT:
			running = False

pygame.quit()

input("")
	
	
	


