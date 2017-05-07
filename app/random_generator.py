from random import choice

NOUNS = ['World', 'Butts', 'Hockey Fans']
GREETINGS = ['Hello', 'Greetings', 'Salutations']

LUCAS_FIRST_NAMES = ['Darth', 'Lord', 'Sith Lord', 'Master', 'Jedi Master', 'Jar Jar']
LUCAS_LAST_NAMES = ['Blayzar', 'Goldstein', 'Maggmarr', 'Ethnicstereotype', 'Starr\'killarr', 'Speedster', 'Blor\'blor',
                    'Villainish']


class RandomGenerator():
    def noun(self):
        return choice(NOUNS)

    def lucas_name(self):
        return [choice(LUCAS_FIRST_NAMES), choice(LUCAS_LAST_NAMES)]

    def screensaver(self):
        return 'Flying Toasters'

    def prince_song(self):
        return 'Electric Fuck'

    def quest_log(self):
        return '4/10 Bear Asses Collected'

    def vote_reporter(self):
        return 'Congressman Ridge (R-PA) Votes YEA on HR 679 to Remove Your Uterus'
