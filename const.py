from collections import namedtuple

actionList = ['ORGANIZE', 'SUPPLY', 'REFIT', 'DOCKING', 'FACTORY', 'SORTLE',
              'PORT']

MainScreen = namedtuple('MainScreen', actionList)
SideBar = namedtuple('SideBar', actionList)
TopBar = namedtuple('TopBar', ['RANK', 'ITEM', 'QUEST'])

OrganizeScreen = namedtuple('OrganizeScreen', ['FLEETS'])
SupplyScreen = namedtuple('SupplyScreen', ['SUPPLYALL', 'FLEETS', 'SELECT',
                                           'START'])
BattleScreen = namedtuple('BattleScreen', ['FORMATION', 'ADVANCE', 'RETREAT'])
ExpeditonScreen = namedtuple('ExpeditonScreen', ['AREA', 'EXPPOS', 'FLEETS',
                                                 'SELECT', 'START'])
SortleScreen = namedtuple('SortleScreen', ['SORTLE', 'EXERCISE', 'EXPEDITION'])
DockingScreen = namedtuple('DockingScreen', ['DOCKS'])

AdvanceScreen = namedtuple('AdvanceScreen', ['AREA', 'MAP', 'EO', 'SELECT',
                                             'START'])

QuestScreen = namedtuple('QuestScreen', ['PAGE', 'OFFSET', 'CLOSE'])
WaitTime = namedtuple('WaitTime', ['SHORT', 'MIDDLE', 'LONG'])

INITPOS = (800, 30)  # 起始點
    
mainButtonPos = MainScreen(
    ORGANIZE = (200, 125),  # 編成
    SUPPLY = (75, 225),  # 補給
    REFIT = (325, 225),  # 改裝
    DOCKING = (125, 350),  # 入渠
    FACTORY = (275, 350),  # 入渠
    SORTLE = (200, 250),  # 出擊
    PORT = (50, 50),
    )

SideBarButtonPos = SideBar(
    ORGANIZE = (25, 150),
    SUPPLY = (25, 205),
    REFIT = (25, 260),
    DOCKING = (25, 315),
    FACTORY = (25, 370),
    SORTLE = (0, 0),
    PORT = (75, 425),
    )

topBarButtonPos = TopBar(
    RANK = (160, 50),
    ITEM = (400, 50),
    QUEST = (560, 50),
    )

organizeButtonPos = OrganizeScreen(
    FLEETS = ( (130, 120), (160, 120), (190, 120), (220, 120),),
    )

supplyButtonPos = SupplyScreen(
    SUPPLYALL = (120, 125),  # 全補給
    SELECT = (
        (120, 175), (120, 225), (120, 275),
        (120, 325), (120, 375), (120, 425),),
    FLEETS = ( (150, 125), (180, 125), (210, 125), (240, 125),),
    START = (700, 450),
    )

battleButtonPos = BattleScreen(
    FORMATION = (
        (450, 175), (575, 175), (700, 175),
        (525, 350), (650, 350)
    ),
    ADVANCE = (300, 250),
    RETREAT = (500, 250)
    )

expeditonButtonPos = ExpeditonScreen(
    AREA = ( (140, 425), (200, 425), (260, 425), (310, 425), (370, 425),),
    EXPPOS = (
        (400, 170), (400, 200), (400, 230), (400, 260),
        (400, 290), (400, 320), (400, 350), (400, 380),
    ),
    FLEETS = ( (360, 120), (390, 120), (420, 120), (450, 120),),
    SELECT = (675, 450),
    START = (625, 450),
    )

sortleButtonPos = SortleScreen(
    SORTLE = (225, 225),
    EXERCISE = (450, 225),
    EXPEDITION = (675, 225),
    )

dockingButtonPos = DockingScreen(
    DOCKS=( (250, 160), (250, 240), (250, 320), (250, 400),),
    )

advanceButtonPos = AdvanceScreen(
    AREA = (
        (160, 440), (230, 440), (310, 440),
        (380, 440), (450, 440), (530, 440),
    ),
    MAP = ( (275, 200), (625, 200), (275, 350),
           (625, 350), (450, 200), (450, 200)),
    EO = (725, 275),
    SELECT = (675, 450),
    START = (625, 450),
    )


questButtonPos = QuestScreen(
    PAGE = ( (350, 465), (405, 465), (460, 465), (515, 465), (570, 465),),
    OFFSET = ( (450, 140), (450, 210), (450, 280), (450, 350), (450, 420),),
    CLOSE = (400, 400),
    )

waitTime = WaitTime(
    SHORT=.4,
    MIDDLE=.6,
    LONG=1.2
    )
