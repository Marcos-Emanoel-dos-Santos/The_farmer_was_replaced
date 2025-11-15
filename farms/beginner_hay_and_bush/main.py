while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if (i+j)%2 == 0:
				plant(Entities.Bush)
			else:
				plant(Entities.Grass)
			move(East)
		move(North)
	