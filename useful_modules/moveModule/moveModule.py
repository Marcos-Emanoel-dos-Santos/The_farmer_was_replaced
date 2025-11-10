def mvDir(direction):
	if can_move(direction):
		move(direction)
		return True
	return False



def go_to(x, y):
	direction = None
	
	while x != get_pos_x():
		if x > get_pos_x():
			direction = East
		else:
			direction = West
			
		if not mvDir(direction):
			return False
			
	while y != get_pos_y():
		if y > get_pos_y():
			direction = North
		else:
			direction = South
			
		if not mvDir(direction):
			return False
	
	return True



scan_dir = 1
def serpeLikeMv(x1, y1, x2, y2):
	global scan_dir
	
	curX = get_pos_x()
	curY = get_pos_y()
	
	x_overflow = curX < x1 or curX > x2
	y_overflow = curY < y1 or curY > y2
	if x_overflow or y_overflow:
		scan_dir = 1
		return go_to(x1, y1)
		
	is_on_last_line = (curY == y2)
	# Just so the code window doesn't gets too large.
	is_at_EOL1 = (scan_dir == 1 and curX == x2)
	is_at_EOL2 = (scan_dir == -1 and curX == x1)
	is_at_end_of_line = is_at_EOL1 or is_at_EOL2
	
	move_succeeded = False
	
	if is_on_last_line and is_at_end_of_line:
		scan_dir = 1
		return go_to(x1, y1)

	
	if scan_dir == 1:
		if curX < x2:
			move_succeeded = mvDir(East)
		else:
			scan_dir = -1
			move_succeeded = mvDir(North)
	else:
		if curX > x1:
			move_succeeded = mvDir(West)
		else:
			scan_dir = 1
			move_succeeded = mvDir(North)
		
	if not move_succeeded:
		return False
		
	return True
