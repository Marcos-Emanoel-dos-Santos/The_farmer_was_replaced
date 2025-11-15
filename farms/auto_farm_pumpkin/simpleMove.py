def mv():
	if get_pos_x() == get_world_size() - 1:
		move(North)
	move(East)

def go_to(x, y):
	while x != get_pos_x():
		if x < get_pos_x():
			move(West)
		elif x > get_pos_x():
			move(East)
			
	while y != get_pos_y():
		if y < get_pos_y():
			move(South)
		elif y > get_pos_y():
			move(North)