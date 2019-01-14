import home
import setup
def start():
	y = input('Are u NEw ? y/n: ')
	if y == 'y':
		setup.setup()
	elif y == 'n':
		print('...')	
	x = input('Enter Your Summoner LVL (EUW): ')
	home.run(x)
	end = input('PRESS ENTER TO LEAVE .........')
start()
