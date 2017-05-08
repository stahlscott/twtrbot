import app
from app.models.models import *
from app.daos.phrase_dao import PhraseDAO
from app.daos.component_type_dao import ComponentTypeDAO
from app.daos.component_dao import ComponentDAO

# george lucas-ass name generator
LUCAS_FIRST_NAMES = ('Darth', 'Lord', 'Sith Lord', 'Master', 'Jedi Master', 'Jar Jar', 'Fingo', 'Bango', 'Blinko',
                     'Count', 'General', 'Jorston', 'Blorple', 'Jaff', 'B.J.', 'Jaft', 'Jorft', 'Indiana', 'Bindle',
                     'Dongle', 'Oodoo', 'Nerf', 'Flam', 'Fangle', 'Yonto', 'Woppo', 'Lawn', 'Leon', 'Chongo', 'Nadoo',
                     'Fordol', 'Cool', 'Rando', 'Troy', 'Fip', 'Princess', 'Emperor', 'Zip', 'Jimp', 'Bofa', 'Yang',
                     'Abraham', 'Boff')
LUCAS_LAST_NAMES = ('Blayzar', 'Goldstein', 'Maggmarr', 'Ethnicstereotype', 'Starr\'killarr', 'Speedster', 'Blor\'blor',
                    'Villainish', 'Sudoku', 'Bleepblorp', 'Jardiance', 'Xeljanz', 'Flingle', 'Dookarr', 'Icky',
                    'Insanius', 'Darrtt', 'Borgus', 'Gorpgorp', 'Beppoflork', 'Larper', 'Hoopoo', 'Yoodoo', 'Boppo',
                    'Jiffft', 'Jinkle', 'Dorfer', 'Jangus', 'Badguy', 'Doooork', 'Anothername', 'Fop', 'Chingchong',
                    'Zorpo', 'Fisto', 'Bllaasstteerr', 'Zordo', 'Storpo')

# screensaver generator
# SCREENSAVER_ADVERBS = ('Rapidly', 'Slowly', 'Adjustable')
SCREENSAVER_DESCRIPTORS = ('Flying', 'Psychedelic', 'Maze of', 'The Matrix, but with', 'Fading', '3D', 'Spinning',
                           'Floating', 'Speeding', 'Vaporwave', 'Lisa Frank-style', 'Bouncing', 'Scrolling',
                           'Swirling', 'Serene', 'Meditative', 'Randomly Generated', '8-Bit', 'Wavy', 'Crawling',
                           'Dizzying', 'Trippy', 'Repeating', 'Speedy', 'Rainbow', 'Slowly Loading')
SCREENSAVER_NOUNS = ('Toasters', 'Bubbles', 'Cows', 'Squares', 'Geometric Things', 'Marquee Comic Sans Text',
                     'Warp Fields', 'Dolphins', 'Brick Walls', 'Emoji', 'Windows Logos', 'Tux the Penguin', 'Lines',
                     'Squigglies', 'Triangles', 'Star Trek Quotes', 'Family Pictures', 'Nude Pix', 'Flames', 'Skulls',
                     'Computer Dogs Taking Over Your Screen', 'Memez')

# prince song generator
PRINCE_PREFIXES = ('U Want My', 'U Want', 'Time 4', 'U R My', '1 And Only', 'I Want Ur', 'Gimme That', 'Get',
                   'U Got The', 'I M Ur', 'Gonna B Ur', 'Gett On My', 'My', 'U Can Have My')
PRINCE_ADJECTIVES = ('Electric', 'Neon', 'Purple', 'Bat', 'Wet', 'Soft', 'Blue', 'Black', 'Cyber', 'Funky', 'Party',
                     'Downtown', 'Slow', 'Paisley', 'Mellow', 'Loose', 'Cherry', 'Erotic', 'Broken', 'Dirty', 'Hot',
                     'Diamond', 'Nite')
PRINCE_NOUNS = ('Fuck', 'City', 'God', 'Bitch', 'Bodylogic', 'Levels', 'Sweat', 'Cum', 'Temple', 'Sexxx', 'Jack Off',
                'Pussy', 'Computer', 'Motorcycle', 'Lover', 'Grind', 'M.F.', 'Slave', 'Romance', 'Machine', 'Mama',
                'Night', 'Baby', 'Cream', 'Dance', 'Bang', 'Street', 'Chains', 'City', 'Kiss', 'Mistress', 'Xperience',
                'Generation', 'Dick', 'Pearls', 'Orgy', 'Jesus')
PRINCE_SUFFIXES = ('4 U', '2 U', 'Un2 U', 'In2 U', 'On2 U', '4 Every1', '2nite', '4ever', 'In2 The New Millennium',
                   '2000', '-ology', 'With U', 'Pt. 2', '4 Minneapolis', 'All Night', 'Baby', '4 Us', '4 U All',
                   '4 2nite', '4 1 Nite Only')

# quest log generator
QUEST_LOG_NOUN_PREFIX = ('Corrupt', 'Fel', 'Zombie', 'Dark', 'Robotic', 'Leprous', 'Traitorous', 'Demonic', 'Wild',
                         'Undead', 'Fire', 'Ice', 'Storm', 'Diseased', 'Clockwork', 'Flesh', 'Blood', 'Noble',
                         'Stone', 'Tribal', 'Poison')
QUEST_LOG_NOUN = ('Bear', 'Hydra', 'Raptor', 'Basilisk', 'Gryphon', 'Dwarf', 'Gnome', 'Elf', 'Orc', 'Druid', 'Snake',
                  'Squirrel', 'Robot', 'Cow', 'Kobold', 'Angel', 'Ghost', 'Tiger', 'Lizard', 'Commoner', 'Mage',
                  'Knight', 'Shaman', 'Summoner', 'Paladin', 'Death Knight', 'Ghoul', 'Goblin', 'Ranger', 'Hunter',
                  'Assassin', 'Automaton', 'Golem', 'Lich', 'Monk')
QUEST_LOG_COLLECTED_PARTS = ('Asses', 'Tongues', 'Eyes', 'Scales', 'Livers', 'Paws', 'Claws', 'Tails', 'Heads',
                             'Jewels', 'Fingers', 'Ears', 'Toes', 'Toenails', 'Blood Samples', 'Droppings',
                             'Belongings', 'Backpacks', 'Bones', 'Frontal Lobes', 'Traps')
QUEST_LOG_ACTIONS = ('Killed', 'Petted', 'Stared Down', 'Hugged', 'Disemboweled', 'Slain', 'Destroyed', 'Culled',
                     'Saved', 'Scratched', 'Hypnotized', 'Clobbered', 'Assembled', 'Trapped', 'Confronted', 'Tamed',
                     'Imprisoned', 'Dismembered', 'Decapitated', 'Threatened', 'Discovered', 'Photographed',
                     'Colonized', 'Invaded', 'Corrupted', 'Redeemed', 'Hatched', 'Bagged', 'Tagged', 'Judged',
                     'Stopped', '"Removed"', 'Shaken', 'Inspected', 'Tickled', 'Summoned', 'Released', 'Jostled',
                     'Fed')

# congressional vote generator
CONGRESS_TITLE = ('Congressman', 'Congresswoman', 'Rep.')
CONGRESS_LAST_NAME = ('Ridge', 'Jackson', 'Jefferson', 'Kennedy', 'Slaughter', 'Labrador', 'Blumenauer', 'Lieberman',
                      'Ryan', 'McCarthy', 'Lopez', 'Green', 'Collins', 'Murphy', 'Goering', 'Rogers', 'Byrne', 'Brooks',
                      'Knight', 'Lee', 'Chu', 'Ruiz', 'Sanchez', 'Hunter', 'Lewis')
CONGRESS_PARTY = ('D', 'R')
CONGRESS_STATE = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
                  'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
                  'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')
CONGRESS_VOTE = ('YEA', 'NAY')
CONGRESS_VERB = ('Remove', 'Destroy', 'Enhance', 'P.A.T.R.I.O.T.', 'Build Up', 'Honor', 'Believe In', 'Protect',
                 'Deregulate', 'Break Up', 'Educate', 'Rebuild', 'Bring Back', 'Imprison', 'Increase Access To',
                 'Return Control To', 'Drone Strikes For', 'Increase Opportunity For', 'Sanction', 'Rebuild', 'Defund',
                 'Incentivize', 'Rename', 'Increase Competition In', 'End', 'Help Begin', 'Help Grow', 'Defend',
                 'End Sanctions On', 'Mandate', 'Renew', 'Lift Up', 'Support')
CONGRESS_NOUN = ('Your Uterus', 'The World', 'The Children', 'Our Children', 'The South', 'The North',
                 'The Confederacy', 'The Middle East', 'Israel', 'Capitalism', 'Capitalists', 'Small Business Owners',
                 'Russia', 'WikiLeaks', 'E.M.A.I.L.S.', 'Erectile Dysfunction', 'Trump Properties', 'Abortionists',
                 'The States', 'America\'s Cities', 'America\'s Scientists', 'American Health Care', 'Our Doctors',
                 'Our Nurses', 'Our Police', 'Inner Cities', 'Hunger', 'Transparency', 'Fascism', 'The United Nations',
                 'Space Exploration', 'Prayer', 'Jesus Christ', 'Quality Television', 'Homeownership', 'Our Veterans',
                 'The Promise', 'Everything Good', 'The Boys In Blue', 'The Alt Right', 'Socialism', 'H.E.A.L.T.H.',
                 'Job Creators', 'Real Taxpayers', 'The Vote', 'Birth Control Access', 'Any Remaining Muslims',
                 'Subprime Mortgages', 'Confederate Memorials', 'The Troops')


def initdb():
    get_or_create_phrase = PhraseDAO(db).get_or_create_phrase
    get_or_create_component_type = ComponentTypeDAO(db).get_or_create_component_type
    get_or_create_component = ComponentDAO(db).get_or_create_component
    app.db.create_all()

    lucas_name = get_or_create_phrase('GeorgeLucasAssNames')
    prince_song = get_or_create_phrase('PrinceVault')
    screensaver = get_or_create_phrase('NewScreensavers')
    quest_progress = get_or_create_phrase('QuestProgress')
    congressional_vote = get_or_create_phrase('CongressVotes')

    lucas_first_names = get_or_create_component_type(name='LucasFirstNames', phrase_id=lucas_name.id)
    lucas_last_names = get_or_create_component_type(name='LucasLastNames', phrase_id=lucas_name.id)
    prince_prefixes = get_or_create_component_type(name='PrincePrefixes', phrase_id=prince_song.id)
    prince_adjectives = get_or_create_component_type(name='PrinceAdjectives', phrase_id=prince_song.id)
    prince_nouns = get_or_create_component_type(name='PrinceNouns', phrase_id=prince_song.id)
    prince_suffixes = get_or_create_component_type(name='PrinceSuffixes', phrase_id=prince_song.id)
    screensaver_descriptions = get_or_create_component_type(name='ScreensaverDescriptions', phrase_id=screensaver.id)
    screensaver_nouns = get_or_create_component_type(name='ScreensaverNouns', phrase_id=screensaver.id)
    quest_log_prefix = get_or_create_component_type(name='QuestLogPrefix', phrase_id=quest_progress.id)
    quest_log_noun = get_or_create_component_type(name='QuestLogNoun', phrase_id=quest_progress.id)
    quest_log_parts = get_or_create_component_type(name='QuestLogParts', phrase_id=quest_progress.id)
    quest_log_actions = get_or_create_component_type(name='QuestLogActions', phrase_id=quest_progress.id)
    congress_title = get_or_create_component_type(name='CongressTitle', phrase_id=congressional_vote.id)
    congress_last_name = get_or_create_component_type(name='CongressLastName', phrase_id=congressional_vote.id)
    congress_party = get_or_create_component_type(name='CongressParty', phrase_id=congressional_vote.id)
    congress_state = get_or_create_component_type(name='CongressState', phrase_id=congressional_vote.id)
    congress_vote = get_or_create_component_type(name='CongressVote', phrase_id=congressional_vote.id)
    congress_verb = get_or_create_component_type(name='CongressVerb', phrase_id=congressional_vote.id)
    congress_noun = get_or_create_component_type(name='CongressNoun', phrase_id=congressional_vote.id)

    for component in LUCAS_FIRST_NAMES:
        component_obj = get_or_create_component(word=component, component_type_id=lucas_first_names.id)
    for component in LUCAS_LAST_NAMES:
        component_obj = get_or_create_component(word=component, component_type_id=lucas_last_names.id)

    for component in PRINCE_PREFIXES:
        component_obj = get_or_create_component(word=component, component_type_id=prince_prefixes.id)
    for component in PRINCE_ADJECTIVES:
        component_obj = get_or_create_component(word=component, component_type_id=prince_adjectives.id)
    for component in PRINCE_NOUNS:
        component_obj = get_or_create_component(word=component, component_type_id=prince_nouns.id)
    for component in PRINCE_SUFFIXES:
        component_obj = get_or_create_component(word=component, component_type_id=prince_suffixes.id)

    for component in SCREENSAVER_DESCRIPTORS:
        component_obj = get_or_create_component(word=component, component_type_id=screensaver_descriptions.id)
    for component in SCREENSAVER_NOUNS:
        component_obj = get_or_create_component(word=component, component_type_id=screensaver_nouns.id)

    for component in QUEST_LOG_NOUN_PREFIX:
        component_obj = get_or_create_component(word=component, component_type_id=quest_log_prefix.id)
    for component in QUEST_LOG_NOUN:
        component_obj = get_or_create_component(word=component, component_type_id=quest_log_noun.id)
    for component in QUEST_LOG_COLLECTED_PARTS:
        component_obj = get_or_create_component(word=component, component_type_id=quest_log_parts.id)
    for component in QUEST_LOG_ACTIONS:
        component_obj = get_or_create_component(word=component, component_type_id=quest_log_actions.id)

    for component in CONGRESS_TITLE:
        component_obj = get_or_create_component(word=component, component_type_id=congress_title.id)
    for component in CONGRESS_LAST_NAME:
        component_obj = get_or_create_component(word=component, component_type_id=congress_last_name.id)
    for component in CONGRESS_PARTY:
        component_obj = get_or_create_component(word=component, component_type_id=congress_party.id)
    for component in CONGRESS_STATE:
        component_obj = get_or_create_component(word=component, component_type_id=congress_state.id)
    for component in CONGRESS_VOTE:
        component_obj = get_or_create_component(word=component, component_type_id=congress_vote.id)
    for component in CONGRESS_VERB:
        component_obj = get_or_create_component(word=component, component_type_id=congress_verb.id)
    for component in CONGRESS_NOUN:
        component_obj = get_or_create_component(word=component, component_type_id=congress_noun.id)
