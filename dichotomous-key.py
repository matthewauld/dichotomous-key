"""
Tools to play a game like guess who.
By default, plays with the test_population listed at the bottom, but can be
played with any population in the same format
"""
from collections import Counter


def play_game(pop):
	"""
	Play a Guess who like game
	Args:
		pop (dict): A dictionary in the form {'name':[list of traits]}
	"""
	while len(pop) > 1:
		trait = next_question(pop)
		if ask_question("does your object have a "+trait+"?") == 'yes':
			pop = isolate_trait(pop, trait)
		else:
			pop = remove_trait(pop, trait)
	make_a_guess("is your object "+list(pop.keys())[0]+"?")



def next_question(pop):
	"""
	Give the next trait that should be asked about, to ensure fewest
	number of questions needed.

	Args:
		pop (dict): A dictionary in the form {'name':[list of traits]}
	Returns:
		trait (any): The ideal trait to ask
	"""
	traits = []
	half_pop_size = len(pop)/2
	for key, value in pop.items():
		traits += value
	traits = Counter(traits)

	for key, value in traits.items():
		traits[key] = abs(value - half_pop_size)
	trait = min(traits, key=traits.get)
	return trait



def remove_trait(pop, trait):
	"""
	Remove all indaviduals with the specificed traits.

	Args:
		pop (dict): A dictionary in the form {'name':[list of traits]}
		trait (any): A trait to be removed
	Returns:
		results (dict): same as pop
	"""
	results = {}
	for key, value in pop.items():
		if trait in value:
			pass
		else:
			results[key] = value
	return results


def isolate_trait(pop, trait):
	"""
	Isolate all indaviduals with the specificed traits.

	Args:
		pop (dict): A dictionary in the form {'name':[list of traits]}
		trait (any): A trait to be isolated
	Returns:
		results (dict): same as pop
	"""
	results = {}
	for key, value in pop.items():
		if trait in value:
			results[key] = value

	return results


def ask_question(prompt):
	"""
	Ask user a question.
	"""
	user_input = input(prompt)
	while user_input.upper() not in ['YES', 'NO']:
		print("- Please answer using either yes or no.", end = "")
		user_input = input()
	return user_input.lower()

def make_a_guess(object):
	"""
	Makes a guess
	"""
	print(object)
	return input("- Was this the correct answer?")

	exit()
