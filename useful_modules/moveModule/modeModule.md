# moveModule

Handles basic movement of the drone.


## myDir(direction)

### MOVES THE DRONE TO ANY DIRECTION

Parameters:
- direction (North, East, South, West) as parameter.

Returns whether the drone could move (True) or not (False)

### Example:
``` python
mvDir(North)
```
moves the drone 1 block to the north and returns true



## go_to(x, y)
### MOVES THE DRONE TO A SPECIFIC COORDINATE

Receives as parameters:
- the target position's x (column) and y (row).
- note that both start at 0, so to move to the 4th column, you must type in 3.

Returns whether the movement was successful or not.
- WARNING: the drone goes straight to that position, so if there's an obstacle ahead, the function won't handle that.

### Example:
``` python
while True:
    go_to(3, 4)
```
moves the drone to the farm coordinate (3, 4)



## serpeLikeMv(x1, y1, x2, y2)
### MAKES A SERPENT-LIKE MOVEMENT ACROSS A GRID
Receives as parameters:
- starting column x1
- starting row y1
- ending column x2
- ending row y2
Note that the farm columns and rows start at 0 and not 1.

# Returns whether the movement was successfull or not

### Example:
``` python
while serpeLikeMv(0, 0, get_world_size()-1, get_world_size()-1):
    if can_harvest():
        harvest()
```
Moves across the field harvesting all ready to harvest crops.