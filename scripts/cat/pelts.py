from random import choice


class SingleColour():
    name = "SingleColour"
    sprites = {1: 'single'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length


class TwoColour():
    name = "TwoColour"
    sprites = {1: 'single', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"


class Tabby():
    name = "Tabby"
    sprites = {1: 'tabby', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} tabby"
        else:
            return self.colour + self.length + " tabby"


class Marbled():
    name = "Marbled"
    sprites = {1: 'marbled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} marbled"
        else:
            return self.colour + self.length + " marbled"


class Rosette():
    name = "Rosette"
    sprites = {1: 'rosette', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} rosette"
        else:
            return self.colour + self.length + " rosette"


class Smoke():
    name = "Smoke"
    sprites = {1: 'smoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} smoke"
        else:
            return self.colour + self.length + " smoke"


class Ticked():
    name = "Ticked"
    sprites = {1: 'ticked', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour}{self.length} ticked"
        else:
            return self.colour + self.length + " ticked"


class Speckled():
    name = "Speckled"
    sprites = {1: 'speckled', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} speckled{self.length}"
        else:
            return f"{self.colour} speckled{self.length}"


class Bengal():
    name = "Bengal"
    sprites = {1: 'bengal', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} bengal{self.length}"
        else:
            return f"{self.colour} bengal{self.length}"


class Mackerel():
    name = "Mackerel"
    sprites = {1: 'mackerel', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} mackerel tabby{self.length}"
        else:
            return f"{self.colour} mackerel tabby{self.length}"


class Classic():
    name = "Classic"
    sprites = {1: 'classic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} classic tabby{self.length}"
        else:
            return f"{self.colour} classic tabby{self.length}"


class Sokoke():
    name = "Sokoke"
    sprites = {1: 'sokoke', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} sokoke tabby{self.length}"
        else:
            return f"{self.colour} sokoke tabby{self.length}"


class Agouti():
    name = "Agouti"
    sprites = {1: 'agouti', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} agouti{self.length}"
        else:
            return f"{self.colour} agouti{self.length}"


class Singlestripe():
    name = "Singlestripe"
    sprites = {1: 'singlestripe', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} singlestripe{self.length}"
        else:
            return f"{self.colour} singlestripe{self.length}"


class Tortie():
    name = "Tortie"
    sprites = {1: 'tortie', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and tortoiseshell{self.length}"
        else:
            return f"tortoiseshell{self.length}"


class Calico():
    name = "Calico"
    sprites = {1: 'calico', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"calico{self.length}"

# WINGED
class SingleColour_wng():
    name = "SingleColour_wng"
    sprites = {1: 'single_wng'}
    white_patches = None

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = self.colour == "white"

    def __repr__(self):
        return self.colour + self.length


class TwoColour_wng():
    name = "TwoColour_wng"
    sprites = {1: 'single_wng', 2: 'white'}

    def __init__(self, colour, length):
        self.colour = colour
        self.length = length
        self.white = True

    def __repr__(self):
        return f"white and {self.colour}{self.length}"

class Pigeonbar():
    name = "Pigeonbar"
    sprites = {1: 'pigeonbar', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pigeon{self.length}"
        else:
            return f"{self.colour} pigeon{self.length}"

class Pigeoncheck():
    name = "Pigeoncheck"
    sprites = {1: 'pigeoncheck', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pigeon{self.length}"
        else:
            return f"{self.colour} pigeon{self.length}"

class Pigeonspread():
    name = "Pigeonspread"
    sprites = {1: 'pigeonspread', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pigeon{self.length}"
        else:
            return f"{self.colour} pigeon{self.length}"

class Pigeonfancy():
    name = "Pigeonfancy"
    sprites = {1: 'pigeonfancy', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} pigeon{self.length}"
        else:
            return f"{self.colour} pigeon{self.length}"

# WURM

class Garter():
    name = "Garter"
    sprites = {1: 'garter', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} garter{self.length}"
        else:
            return f"{self.colour} garter{self.length}"

class Gartercheck():
    name = "Gartercheck"
    sprites = {1: 'gartercheck', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} garter{self.length}"
        else:
            return f"{self.colour} garter{self.length}"

class Garterexotic():
    name = "Garterexotic"
    sprites = {1: 'garterexotic', 2: 'white'}

    def __init__(self, colour, white, length):
        self.white = white  # boolean; does cat have white on it or no
        self.colour = colour
        self.length = length

    def __repr__(self):
        if self.white:
            return f"white and {self.colour} garter{self.length}"
        else:
            return f"{self.colour} garter{self.length}"

# WINGED ATTRIBUTES
pigeon_colours = [
    'SILVER', 'OPAL', 'GREY', 'DARKGREY', 'LIGHTBLUE', 'BLUE', 'DARKBLUE',
    'CREAM', 'FAWN', 'CINNAMON', 'LIGHTRED', 'RED', 'BROWN', 'DARKBROWN'
]
pigeonspread_colours = [
    'SILVER', "FAWN", "CINNAMON", "BROWN", "BLUE", "DARKBLUE", "BLACK"
]
pigeonfancy_colours = [
    'ICE', 'LARK', 'REDPEN', 'BLUEPEN', 'MOTTLEDLIGHT', 'MOTTLED', 'MOTTLEDDARK'
]

blue_colours_wng = ['SILVER', 'OPAL', 'GREY', 'DARKGREY', 'LIGHTBLUE', 'BLUE', 'DARKBLUE', 'ICE', 'BLUEPEN']
brown_colours_wng = ['CINNAMON', 'BROWN', 'DARKBROWN', 'LARK', 'MOTTLEDLIGHT', 'MOTTLED', 'MOTTLEDDARK']
red_colours_wng = ['CREAM', 'FAWN', 'LIGHTRED', 'RED', 'REDPEN']
other_colours_wng = ['']
colour_categories_wng = [blue_colours_wng, brown_colours_wng, red_colours_wng]

plain_wng = ["SingleColour_wng"]
bird = ["Pigeonbar", "Pigeoncheck", "Pigeonspread", "Pigeonfancy"]

pelt_categories_wng = [plain_wng, bird]

# WURM ATTRIBUTES
garter_colours = [
    'BLUE', 'COFFEE', 'DAKRBROWN', 'SNICKERS', 'BROWN', 'PASTEL'
]
garterexotic_colours = [
    'NEONBLUE', 'FLAME', 'SPECKFLAME', 'RED', 'DALMATIAN'
]

blue_colours_wurm = ['BLUE', 'NEONBLUE']
brown_colours_wurm = ['COFFEE', 'DAKRBROWN', 'SNICKERS', 'BROWN']
red_colours_wurm = ['RED', 'FLAME']
white_colours_wurm = ['PASTEL', 'SPECKFLAME', 'DALMATIAN']
colour_categories_wurm = [blue_colours_wurm, brown_colours_wurm, red_colours_wurm, white_colours_wurm]

garter = ["Garter", "Gartercheck", "Garterexotic"]

pelt_categories_wurm = [garter, garter]

# ATTRIBUTES, including non-pelt related
pelt_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN',
    'BLACK'
]
pelt_c_no_white = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER', 'GOLDEN',
    'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
]
pelt_c_no_bw = [
    'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'PALEGINGER', 'GOLDEN', 'GINGER',
    'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN'
]

tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR',
                  'OREO', 'SWOOP', 'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'ORIOLE',
                  'ROBIN', 'BRINDLE', 'PAIGE']
tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
               'classic', 'sokoke', 'agouti', 'singlestripe']

pelt_length = ["short", "medium", "long"]
eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 
    'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT', 'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER',
    'SUNSETICE', 'PURPLE', 'CHOCOLATE', 'RED', 'PINK', 'WARMGRAY', 'PANSY']
red_eyes = ['AMBER', 'COPPER', 'CHOCOLATE', 'RED', 'PINK', 'SUNSETICE']
yellow_eyes = ['YELLOW', 'AMBER', 'PALEYELLOW', 'GOLD', 'GREENYELLOW', 'BRONZE', 'SILVER', 'WARMGRAY']
blue_eyes = ['BLUE', 'DARKBLUE', 'CYAN', 'PALEBLUE', 'HEATHERBLUE', 'COBALT', 'SUNLITICE', 'GREY', 'PURPLE', 'PANSY']
green_eyes = ['PALEGREEN', 'GREEN', 'EMERALD', 'SAGE', 'HAZEL']
# scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
# bite scars by @wood pank on discord
scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
          "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
          "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH"]
scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
          "FROSTSOCK", ]

# make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                     "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                     "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                     ]
wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                    ]
tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
collars = [
    "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
    "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
    "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
    "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
    "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
    "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
    "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
    "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
    "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
]

tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
spotted = ["Speckled", "Rosette"]
plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe"]
exotic = ["Bengal", "Marbled"]
torties = ["Tortie", "Calico"]
pelt_categories_reg = [tabbies, spotted, plain, exotic, torties]

pelt_categories = [tabbies, spotted, plain, exotic, torties, bird, garter]

# SPRITE NAMES
single_colours = [
    'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'PALEGINGER',
    'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM', 'LIGHTBROWN', 'BROWN', 'DARKBROWN', 'BLACK'
]
ginger_colours = ['PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'CREAM']
black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK']
white_colours = ['WHITE', 'PALEGREY', 'SILVER']
brown_colours = ['LIGHTBROWN', 'BROWN', 'DARKBROWN']
colour_categories = [ginger_colours, black_colours, white_colours, brown_colours]
eye_sprites = [
    'YELLOW', 'AMBER', 'HAZEL', 'PALEGREEN', 'GREEN', 'BLUE', 'DARKBLUE', 'BLUEYELLOW', 'BLUEGREEN',
    'GREY', 'CYAN', 'EMERALD', 'PALEBLUE', 'PALEYELLOW', 'GOLD', 'HEATHERBLUE', 'COPPER', 'SAGE', 'COBALT',
    'SUNLITICE', 'GREENYELLOW', 'BRONZE', 'SILVER'
]
little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY', 'LUNA',
                'EXTRA']
mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
             'WINGS']
high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
              'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
              'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED']
mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO']
point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER']
white_sprites = [
    little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

skin_sprites = ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']

# CHOOSING PELT
def choose_pelt(colour=None, white=None, pelt=None, length=None, category=None, determined=False):
    colour = colour
    white = white
    pelt = pelt
    length = length
    category = category
    if pelt is None:
        if category != None:
            pelt = choice(category)
    else:
        pelt = pelt
    if length is None:
        length = choice(pelt_length)
    if pelt == 'SingleColour':
        if colour is None and not white:
            return SingleColour(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour("WHITE", length)
        else:
            return SingleColour(colour, length)
    elif pelt == 'TwoColour':
        if colour is None:
            return TwoColour(choice(pelt_c_no_white), length)
        else:
            return TwoColour(colour, length)
    elif pelt == 'Tabby':
        if colour is None and white is None:
            return Tabby(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Tabby(choice(pelt_colours), white, length)
        else:
            return Tabby(colour, white, length)
    elif pelt == 'Marbled':
        if colour is None and white is None:
            return Marbled(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Marbled(choice(pelt_colours), white, length)
        else:
            return Marbled(colour, white, length)
    elif pelt == 'Rosette':
        if colour is None and white is None:
            return Rosette(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Rosette(choice(pelt_colours), white, length)
        else:
            return Rosette(colour, white, length)
    elif pelt == 'Smoke':
        if colour is None and white is None:
            return Smoke(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Smoke(choice(pelt_colours), white, length)
        else:
            return Smoke(colour, white, length)
    elif pelt == 'Ticked':
        if colour is None and white is None:
            return Ticked(choice(pelt_colours), choice([False, True]), length)
        elif colour is None:
            return Ticked(choice(pelt_colours), white, length)
        else:
            return Ticked(colour, white, length)
    elif pelt == 'Speckled':
        if colour is None and white is None:
            return Speckled(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Speckled(choice(pelt_colours), white, length)
        else:
            return Speckled(colour, white, length)
    elif pelt == 'Bengal':
        if colour is None and white is None:
            return Bengal(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Bengal(choice(pelt_colours), white, length)
        else:
            return Bengal(colour, white, length)
    elif pelt == 'Mackerel':
        if colour is None and white is None:
            return Mackerel(choice(pelt_colours), choice([False, True]),
                            length)
        elif colour is None:
            return Mackerel(choice(pelt_colours), white, length)
        else:
            return Mackerel(colour, white, length)
    elif pelt == 'Classic':
        if colour is None and white is None:
            return Classic(choice(pelt_colours), choice([False, True]),
                           length)
        elif colour is None:
            return Classic(choice(pelt_colours), white, length)
        else:
            return Classic(colour, white, length)
    elif pelt == 'Sokoke':
        if colour is None and white is None:
            return Sokoke(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Sokoke(choice(pelt_colours), white, length)
        else:
            return Sokoke(colour, white, length)
    elif pelt == 'Agouti':
        if colour is None and white is None:
            return Agouti(choice(pelt_colours), choice([False, True]),
                          length)
        elif colour is None:
            return Agouti(choice(pelt_colours), white, length)
        else:
            return Agouti(colour, white, length)
    elif pelt == 'Singlestripe':
        if colour is None and white is None:
            return Singlestripe(choice(pelt_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Singlestripe(choice(pelt_colours), white, length)
        else:
            return Singlestripe(colour, white, length)
    elif pelt == 'SingleColour_wng':
        if colour is None and not white:
            return SingleColour_wng(choice(pelt_colours), length)
        elif colour is None:
            return SingleColour_wng("WHITE", length)
        else:
            return SingleColour_wng(colour, length)
    elif pelt == 'TwoColour_wng':
        if colour is None:
            return TwoColour_wng(choice(pelt_c_no_white), length)
        else:
            return TwoColour_wng(colour, length)
    elif pelt == 'Pigeonbar':
        if colour is None and white is None:
            return Pigeonbar(choice(pigeon_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pigeonbar(choice(pigeon_colours), white, length)
        else:
            if colour in pigeon_colours:
                return Pigeonbar(colour, white, length)
            else:
                return Pigeonbar(choice(pigeon_colours), white, length)
    elif pelt == 'Pigeoncheck':
        if colour is None and white is None:
            return Pigeoncheck(choice(pigeon_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pigeoncheck(choice(pigeon_colours), white, length)
        else:
            if colour in pigeon_colours:
                return Pigeoncheck(colour, white, length)
            else:
                return Pigeoncheck(choice(pigeon_colours), white, length)
    elif pelt == 'Pigeonspread':
        if colour is None and white is None:
            return Pigeonspread(choice(pigeonspread_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pigeonspread(choice(pigeonspread_colours), white, length)
        else:
            if colour in pigeonspread_colours:
                return Pigeonspread(colour, white, length)
            elif colour in pigeonfancy_colours:
                return Pigeonspread(choice(pigeonspread_colours), white, length)
            else:
                if colour == "OPAL":
                    colour = "SILVER"
                elif colour == "GREY" or "DARKGREY" or "LIGHTBLUE":
                    colour = "BLUE"
                elif colour == "CREAM":
                    colour = "FAWN"
                elif colour == "LIGHTRED":
                    colour = "CINNAMON"
                elif colour == "RED":
                    colour = "BROWN"
                elif colour == "DARKBROWN":
                    colour = "BLACK"
                return Pigeonspread(colour, white, length)
    elif pelt == 'Pigeonfancy':
        if colour is None and white is None:
            return Pigeonfancy(choice(pigeonfancy_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Pigeonfancy(choice(pigeonfancy_colours), white, length)
        else:
            if colour in pigeonfancy_colours:
                return Pigeonfancy(colour, white, length)
            else:
                return Pigeonfancy(choice(pigeonfancy_colours), white, length)
    elif pelt == 'Garter':
        if colour is None and white is None:
            return Garter(choice(garter_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Garter(choice(garter_colours), white, length)
        else:
            if colour in garter_colours:
                return Garter(colour, white, length)
            else:
                return Garter(choice(garter_colours), white, length)
    elif pelt == 'Gartercheck':
        if colour is None and white is None:
            return Gartercheck(choice(garter_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Gartercheck(choice(garter_colours), white, length)
        else:
            if colour in garter_colours:
                return Gartercheck(colour, white, length)
            else:
                return Gartercheck(choice(garter_colours), white, length)
    elif pelt == 'Garterexotic':
        if colour is None and white is None:
            return Garterexotic(choice(garterexotic_colours), choice([False, True]),
                                length)
        elif colour is None:
            return Garterexotic(choice(garterexotic_colours), white, length)
        else:
            if colour in garterexotic_colours:
                return Garterexotic(colour, white, length)
            else:
                return Garterexotic(choice(garterexotic_colours), white, length)
    elif pelt == 'Tortie':
        if white is None:
            return Tortie(colour, choice([False, True]), length)
        else:
            return Tortie(colour, white, length)
    else:
        return Calico(colour, length)
    
def describe_appearance(cat, short=False):
    
    # Define look-up dictionaries
    if short:
        renamed_colors = {
            "grey": "gray",
            "palegrey": "gray",
            "darkgrey": "gray",
            "paleginger": "ginger",
            "darkginger": "ginger",
            "lightbrown": "brown",
            "darkbrown": "brown",
            "ghost": "black",
            "lightblue": "blue",
            "darkblue": "blue",
            "lightred": "red"
        }
    else:
        renamed_colors = {
            "grey": "gray",
            "palegrey": "pale gray",
            "darkgrey": "dark gray",
            "paleginger": "pale ginger",
            "darkginger": "dark ginger",
            "lightbrown": "light brown",
            "darkbrown": "dark brown",
            "ghost": "black",
            "lightblue": "light blue",
            "darkblue": "dark blue",
            "lightred": "light red"
        }

    pattern_des = {
        "Tabby": "c_n tabby",
        "Speckled": "speckled c_n",
        "Bengal": "unusually dappled c_n",
        "Marbled": "c_n tabby",
        "Ticked": "c_n ticked",
        "Smoke": "c_n smoke",
        "Mackerel": "c_n tabby",
        "Classic": "c_n tabby",
        "Agouti": "c_n tabby",
        "Singlestripe": "dorsal-striped c_n",
        "Rosette": "unusually spotted c_n",
        "Sokoke": "c_n tabby",
        "Pigeonbar": "c_n pigeon",
        "Pigeoncheck": "c_n pigeon",
        "Pigeonfancy": "c_n pigeon"
    }

    # Start with determining the base color name. 
    color_name = str(cat.pelt.colour).lower()
    if color_name in renamed_colors:
        color_name = renamed_colors[color_name]
    
    # Replace "white" with "pale" if the cat is 
    if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
        color_name = "pale"

    # Time to descibe the pattern and any additional colors. 
    if cat.pelt.name in pattern_des:
        color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
    elif cat.pelt.name in torties:
        # Calicos and Torties need their own desciptions. 
        if short:
            # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
            if cat.pelt.colour in black_colours + brown_colours + white_colours and \
                cat.tortiecolour in black_colours + brown_colours + white_colours:
                color_name = "mottled"
            else:
                color_name = cat.pelt.name.lower()
        else:
            base = cat.tortiebase.lower()
            if base in tabbies + ['bengal', 'rosette', 'speckled']:
                base = 'tabby'
            else:
                base = ''

            patches_color = cat.tortiecolour.lower()
            if patches_color in renamed_colors:
                patches_color = renamed_colors[patches_color]
            color_name = f"{color_name}/{patches_color}"
            
            if cat.pelt.colour in black_colours + brown_colours + white_colours and \
                cat.tortiecolour in black_colours + brown_colours + white_colours:
                    color_name = f"{color_name} mottled"
            else:
                color_name = f"{color_name} {cat.pelt.name.lower()}"

    if cat.white_patches:
        if cat.white_patches == "FULLWHITE":
            # If the cat is fullwhite, discard all other information. They are just white. 
            color_name = "white"
        if cat.white_patches in mostly_white and cat.pelt.name != "Calico":
            color_name = f"white and {color_name}"
        elif cat.pelt.name != "Calico":
            color_name = f"{color_name} and white"
    
    if cat.points:
        color_name = f"{color_name} point"
        if "ginger point" in color_name:
            color_name.replace("ginger point", "flame point")

    if "white and white" in color_name:
        color_name = color_name.replace("white and white", "white")

    # Now it's time for gender
    if cat.genderalign in ["female", "trans female"]:
        color_name = f"{color_name} she-cat"
    elif cat.genderalign in ["male", "trans male"]:
        color_name = f"{color_name} tom"
    else:
        color_name = f"{color_name} cat"

    # Here is the place where we can add some additional details about the cat, for the full non-short one. 
    # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
    if not short:
        
        scar_details = {
            "NOTAIL": "no tail", 
            "HALFTAIL": "half a tail", 
            "NOPAW": "three legs", 
            "NOLEFTEAR": "a missing ear", 
            "NORIGHTEAR": "a missing ear",
            "NOEAR": "no ears"
        }

        additional_details = []
        if cat.vitiligo:
            additional_details.append("vitiligo")
        for scar in cat.scars:
            if scar in scar_details and scar_details[scar] not in additional_details:
                additional_details.append(scar_details[scar])
        
        if len(additional_details) > 1:
            color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
        elif additional_details:
            color_name = f"{color_name} with {additional_details[0]}"
    
    
        if len(cat.scars) >= 3:
            color_name = f"scarred {color_name}"
        if cat.pelt.length == "long":
            color_name = f"long-furred {color_name}"

    return color_name
    