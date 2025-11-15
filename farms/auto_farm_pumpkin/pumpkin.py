from simpleMove import mv, go_to

def pumpkinFarm():
	pumpkinPrice = (num_unlocked(Unlocks.Pumpkins)-1)**2
	unseen_tiles = []
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if can_harvest():
				harvest()
			if get_ground_type() == Grounds.Grassland:
				till()
			mv()
	
	while num_items(Items.Carrot) > pumpkinPrice:
		id1, id2 = 0, 1
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				plant(Entities.Pumpkin)
				unseen_tiles.append( (get_pos_x(), get_pos_y()) )
				mv()

		while len(unseen_tiles) > 0:
			for i in range(len(unseen_tiles) -1, -1, -1):
				x, y = unseen_tiles[i]
				go_to(x, y)
				if get_entity_type() == Entities.Pumpkin and can_harvest():
					unseen_tiles.pop(i)
				elif get_entity_type() != Entities.Pumpkin:
					plant(Entities.Pumpkin)

		
		harvest()
		
	if num_items(Items.Carrot) < pumpkinPrice:
		return 'carrot'
	
pumpkinFarm()