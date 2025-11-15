def woodFarm():
	if can_harvest():
		harvest()
	x = get_pos_x()
	y = get_pos_y()
	if (x+y)%2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)
	if get_pos_x() == get_world_size() - 1:
		move(North)
	move(East)