from hay import hayFarm
from wood import woodFarm
from carrot import carrotFarm
from pumpkin import pumpkinFarm

def main():
	control = 'pumpkin'
	while True:
		if control == 'hay':
			hayFarm()
			if num_items(Items.Hay) > 3000:
				control = 'wood'
		if control == 'wood':
			woodFarm()
			if num_items(Items.Wood) > 3000:
				control = 'carrot'
		if control == 'carrot':
			control = carrotFarm()
			if num_items(Items.Carrot) > 3000:
				control = 'pumpkin'
		if control == 'pumpkin':
			control = pumpkinFarm()

			
			
if __name__=="__main__":
	main()