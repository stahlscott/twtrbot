import random

NOUNS = ['World', 'Butts', 'Hockey Fans']
GREETINGS = ['Hello', 'Greetings', 'Salutations']

LUCAS_FIRST_NAMES = ['Darth', 'Lord', 'Sith Lord', 'Master', 'Jedi Master', 'Jar Jar']
LUCAS_LAST_NAMES = ['Blayzar', 'Goldstein', 'Maggmarr', 'Ethnicstereotype', 'Starr\'killarr']


class RandomGenerator():
    def noun(self):
        return random.choice(NOUNS)

    def lucas_name(self):
        return [random.choice(LUCAS_FIRST_NAMES), random.choice(LUCAS_LAST_NAMES)]
