def hayFarm():
	if can_harvest():
		harvest()
	plant(Entities.Grass)
	if get_pos_x() == get_world_size() - 1:
		move(North)
	move(East)