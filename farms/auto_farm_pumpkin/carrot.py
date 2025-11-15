def carrotFarm():
	carrotPrice = (num_unlocked(Unlocks.Carrots)-1)**2
	if num_items(Items.Hay) > carrotPrice and num_items(Items.Wood) > carrotPrice:
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				if can_harvest():
					harvest()
				if get_ground_type() == Grounds.Grassland:
					till()
				else:
					plant(Entities.Carrot)
				move(East)
			move(North)
					
	while num_items(Items.Hay) > carrotPrice and num_items(Items.Wood) > carrotPrice:
		x = get_pos_x()
		if can_harvest():
			harvest()
		plant(Entities.Carrot)
		if get_pos_x() == get_world_size() - 1:
			move(North)
		move(East)
	if num_items(Items.Hay) < carrotPrice:
		return 'hay'
	else:
		return 'wood'