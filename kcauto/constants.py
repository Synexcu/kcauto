import random

class constants_timer():
    @staticmethod
    def SLEEP_MODIFIER():
        # return random.choice([0,0,0,1,2,3,4,5]) #Modded_Default
        return random.choice([0]) #Instant timer [0,1] (for maps with SELECT NODE TYPE, [0] ONLY is advised. Further sampling later)
    
    def LOOP_BREAK_SECONDS():
        # return random.choice([10,11,12,13,14,15,16,17,18,19,20,21,22,23,25,180,180,180,240,270,300]) #Modded_Default
        return random.choice([0,1]) #Instant timer

# ABOVE THIS ARE ADDITIONAL

# SLEEP_MODIFIER = 0 #SOURCE
# LOOP_BREAK_SECONDS = 15 #SOURCE (15s advised)

MIN_JST_OFFSET = -20
MAX_JST_OFFSET = 20
MIN_PORT = 0
MAX_PORT = 65535
MAX_FLEET_PRESETS = 15

# game window dimensions
GAME_W = 1200
GAME_H = 720

# chrome hook url targets
DEFAULT_CHROME_DEV_PORT = 9222
VISUAL_URL = 'http://www.dmm.com/netgame/social/-/gadgets/=/app_id=854854/'
API_URL = 'kcs2/index.php'

# similarity presets
EXACT = 0.994
FLEET_NUMBER_ICON = 0.99
NEAR_EXACT = 0.95
VISUAL_DAMAGE = 0.95
DEFAULT = 0.8

# click padding presets
PAGE_NAV = (-8, -10, -8, -10)

# external urls
WCTF_DB_URL = (
    'https://raw.githubusercontent.com/TeamFleet/WhoCallsTheFleet/master'
    '/app-db/ships.nedb')
WCTF_SUFFIX_URL = (
    'https://raw.githubusercontent.com/TeamFleet/WhoCallsTheFleet/master'
    '/app-db/ship_namesuffix.nedb')
