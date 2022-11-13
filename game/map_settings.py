# game setup
WIDTH    = 1280	
HEIGTH   = 720
FPS      = 60
TILESIZE = 32

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

#magic
magic_data = {
    'atk':{'strength': 5,'cost':20,'graphic:':'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/skill/atk'},
    'Aura': {'strength': 10,'cost': 10,'graphic':'C:/Users/Admin/Desktop/งานทุกวิชา/เขียนโค้ด/Pro_fun/game/graphic/skill/Aura'}
}

monster_data ={
    'ghost':{'health': 100,'exp': 100,'damage':20,'attack_type':'slash','speed':3,'resistance': 3,'attack_radius':80,'notice_radius':1000},
    'demon':{'health': 200,'exp': 150,'damage':40,'attack_type':'flame','speed':3,'resistance': 3,'attack_radius':120,'notice_radius':1000}
}
