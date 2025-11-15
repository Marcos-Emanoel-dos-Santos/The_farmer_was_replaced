# Use this until you have enough carrots
# to afford Variables.
for i in range(get_world_size()):
	for j in range(get_world_size()):
		till()
		move(East)
	move(North)
while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			plant(Entities.Carrot)
			move(East)
		move(North)