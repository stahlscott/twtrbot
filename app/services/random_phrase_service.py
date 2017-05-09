from random import choice, randint


class RandomPhraseService():
    def __init__(self, component_type_dao, component_dao):
        self._component_type_dao = component_type_dao
        self._component_dao = component_type_dao

    def lucas_name(self):
        first_name = choice(self._component_type_dao.get_component_type_by_name('LucasFirstName').components).word
        last_name = choice(self._component_type_dao.get_component_type_by_name('LucasLastName').components).word
        return [first_name, last_name]

    def screensaver(self):
        ss_descriptor = choice(
            self._component_type_dao.get_component_type_by_name('ScreensaverDescription').components).word
        ss_noun = choice(self._component_type_dao.get_component_type_by_name('ScreensaverNoun').components).word
        return [ss_descriptor, ss_noun]

    def prince_song(self):
        rand_int = randint(1, 10)  # roll to determine whether to add prefix, suffix, or both
        prefix_odds = [1, 2]  # if rolling 1 or 2, include prefix
        suffix_odds = [2, 3, 4, 5]  # if rolling 2-5, include suffix

        prefix = choice(self._component_type_dao.get_component_type_by_name('PrincePrefix').components).word \
            if rand_int in prefix_odds else ''
        suffix = choice(self._component_type_dao.get_component_type_by_name('PrinceSuffix').components).word \
            if rand_int in suffix_odds else ''
        adjective = choice(self._component_type_dao.get_component_type_by_name('PrinceAdjective').components).word
        noun = choice(self._component_type_dao.get_component_type_by_name('PrinceNoun').components).word

        return [prefix, adjective, noun, suffix]

    def quest_log(self):
        max_num = 10  # random number of things to collect/kill, up to max_num * 2
        total_num = randint(2, max_num) * 2  # * 2 to keep it an even number
        in_progress_num = randint(1, total_num)
        quest_progress = str(in_progress_num) + '/' + str(total_num)
        completed = ' (COMPLETED)' if total_num == in_progress_num else ''  # add COMPLETED if quest complete

        rand_int = randint(1, 10)  # randomize if adding a prefix or not
        prefix = choice(self._component_type_dao.get_component_type_by_name('QuestLogPrefix').components).word \
                 + ' ' if 4 <= rand_int <= 8 else ''
        noun = prefix + choice(self._component_type_dao.get_component_type_by_name('QuestLogNoun').components).word

        if rand_int > 5:
            action = choice(self._component_type_dao.get_component_type_by_name('QuestLogPart').components).word \
                     + ' Collected'
        else:
            noun = noun + 's'  # pluralize
            action = choice(self._component_type_dao.get_component_type_by_name('QuestLogAction').components).word

        return [quest_progress, noun, action, completed]

    def congress_vote(self):
        title = choice(self._component_type_dao.get_component_type_by_name('CongressTitle').components).word
        last_name = choice(self._component_type_dao.get_component_type_by_name('CongressLastName').components).word
        party = choice(self._component_type_dao.get_component_type_by_name('CongressParty').components).word
        state = choice(self._component_type_dao.get_component_type_by_name('CongressState').components).word
        vote = choice(self._component_type_dao.get_component_type_by_name('CongressVote').components).word
        bill_number = str(randint(1, 5999))
        verb = choice(self._component_type_dao.get_component_type_by_name('CongressVerb').components).word
        noun = choice(self._component_type_dao.get_component_type_by_name('CongressNoun').components).word

        return [title, last_name, party, state, vote, bill_number, verb, noun]
