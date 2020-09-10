def find_capital(argv):

	import sys
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}


	if len(sys.argv) != 2:
		sys.exit(1)

	state = sys.argv[1]
	reponse = capital_cities[states[state]] if state in states else "Unknow state"
	print(reponse)

if __name__ == '__main__':
	import sys
	find_capital(sys.argv)