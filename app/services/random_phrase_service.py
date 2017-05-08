from random import choice, randint

from app.daos.phrase_dao import PhraseDAO
from app.daos.component_type_dao import ComponentTypeDAO
from app.daos.component_dao import ComponentDAO


class RandomPhraseService():
    def __init__(self, db):
        self._phrase_dao = PhraseDAO(db=db)
        self._component_type_dao = ComponentTypeDAO(db=db)
        self._component_dao = ComponentDAO(db=db)

    def hello_random(self):
        return ['Hello', 'World']
        # return [choice(GREETINGS), choice(NOUNS)]

    def lucas_name(self):
        first_name_type_id = self._component_type_dao.get_component_type_by_name('LucasFirstNames').id
        last_name_type_id = self._component_type_dao.get_component_type_by_name('LucasLastNames').id
        first_name = choice(self._component_dao.get_all_components_by_type_id(first_name_type_id)).word
        last_name = choice(self._component_dao.get_all_components_by_type_id(last_name_type_id)).word
        return [first_name, last_name]

    def screensaver(self):
        ss_descriptor_type_id = self._component_type_dao.get_component_type_by_name('ScreensaverDescriptions').id
        ss_noun_type_id = self._component_type_dao.get_component_type_by_name('ScreensaverNouns').id
        ss_descriptor = choice(self._component_dao.get_all_components_by_type_id(ss_descriptor_type_id)).word
        ss_noun = choice(self._component_dao.get_all_components_by_type_id(ss_noun_type_id)).word
        return [ss_descriptor, ss_noun]

    def prince_song(self):
        rand_int = randint(1, 10)
        prefix_odds = [1, 2]
        suffix_odds = [2, 3, 4, 5]

        prince_prefix_type_id = self._component_type_dao.get_component_type_by_name('PrincePrefixes').id
        prince_suffix_type_id = self._component_type_dao.get_component_type_by_name('PrinceSuffixes').id
        prince_adjective_type_id = self._component_type_dao.get_component_type_by_name('PrinceAdjectives').id
        prince_noun_type_id = self._component_type_dao.get_component_type_by_name('PrinceNouns').id

        prefix = choice(self._component_dao.get_all_components_by_type_id(prince_prefix_type_id)).word \
            if rand_int in prefix_odds else ''
        suffix = choice(self._component_dao.get_all_components_by_type_id(prince_suffix_type_id)).word \
            if rand_int in suffix_odds else ''
        adjective = choice(self._component_dao.get_all_components_by_type_id(prince_adjective_type_id)).word
        noun = choice(self._component_dao.get_all_components_by_type_id(prince_noun_type_id)).word

        return [prefix, adjective, noun, suffix]

    def quest_log(self):
        max_num = 10
        total_num = randint(2, max_num) * 2
        in_progress_num = randint(1, total_num)
        quest_progress = str(in_progress_num) + '/' + str(total_num)
        completed = ' (COMPLETED)' if total_num == in_progress_num else ''

        prefix_type_id = self._component_type_dao.get_component_type_by_name('QuestLogPrefix').id
        noun_type_id = self._component_type_dao.get_component_type_by_name('QuestLogNoun').id

        rand_int = randint(1, 10)
        prefix = choice(self._component_dao.get_all_components_by_type_id(prefix_type_id)).word \
                 + ' ' if 4 <= rand_int <= 8 else ''
        noun = prefix + choice(self._component_dao.get_all_components_by_type_id(noun_type_id)).word

        if rand_int > 5:
            parts_type_id = self._component_type_dao.get_component_type_by_name('QuestLogParts').id
            action = choice(self._component_dao.get_all_components_by_type_id(parts_type_id)).word + ' Collected'
        else:
            noun = noun + 's'  # pluralize
            actions_type_id = self._component_type_dao.get_component_type_by_name('QuestLogActions').id
            action = choice(self._component_dao.get_all_components_by_type_id(actions_type_id)).word

        return [quest_progress, noun, action, completed]

    def congress_vote(self):
        title_type_id = self._component_type_dao.get_component_type_by_name('CongressTitle').id
        last_name_type_id = self._component_type_dao.get_component_type_by_name('CongressLastName').id
        party_type_id = self._component_type_dao.get_component_type_by_name('CongressParty').id
        state_type_id = self._component_type_dao.get_component_type_by_name('CongressState').id
        vote_type_id = self._component_type_dao.get_component_type_by_name('CongressVote').id
        verb_type_id = self._component_type_dao.get_component_type_by_name('CongressVerb').id
        noun_type_id = self._component_type_dao.get_component_type_by_name('CongressNoun').id

        title = choice(self._component_dao.get_all_components_by_type_id(title_type_id)).word
        last_name = choice(self._component_dao.get_all_components_by_type_id(last_name_type_id)).word
        party = choice(self._component_dao.get_all_components_by_type_id(party_type_id)).word
        state = choice(self._component_dao.get_all_components_by_type_id(state_type_id)).word
        vote = choice(self._component_dao.get_all_components_by_type_id(vote_type_id)).word
        verb = choice(self._component_dao.get_all_components_by_type_id(verb_type_id)).word
        noun = choice(self._component_dao.get_all_components_by_type_id(noun_type_id)).word

        return [title, last_name, party, state, vote, str(randint(1, 5999)), verb, noun]
