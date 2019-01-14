import home
import setup
def start():
	file = open('key.txt','r')
	rod = file.read()
	y = input('Are u NEw ? y/n: ')
	if y == 'y':
		setup.setup()
	elif y == 'n':
		print('...')	
	if not rod:
		key = input('Enter the KEy : ')
		if not key:
			print('You should get a key !!!')
		else:	
			x = input('Enter Your Summoner LVL (EUW): ')
			home.run(x, key)
	else:
		x = input('Enter Your Summoner LVL (EUW): ')
		home.run(x, rod)
	end = input('PRESS ENTER TO LEAVE .........')

start()
