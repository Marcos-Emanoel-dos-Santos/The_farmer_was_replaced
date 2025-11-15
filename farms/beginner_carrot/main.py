control = 'carrot'
while True:
	if control == 'carrot':
		# Plants carrots until you cannot afford them anymore
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if get_ground_type() == Grounds.Grassland:
					till()
				move(East)
			move(North)
		can_plant = True
		while can_plant:
			for i in range(get_world_size()):
				for j in range(get_world_size()):
					if can_harvest():
						harvest()
					if num_items(Items.Hay) < 100 or num_items(Items.Wood) < 100:
						can_plant = False
					plant(Entities.Carrot)
					move(East)
				move(North)
		control = 'hay_and_bush'
		
	# Plants hay and bush otherwise.
	elif control == 'hay_and_bush':
		while num_items(Items.Hay) < 1000 or num_items(Items.Wood) < 1000:
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
		control = 'carrot'