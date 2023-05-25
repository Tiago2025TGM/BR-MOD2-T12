import pygame
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def _init_(self):
        super()._init_(HAMMER, HAMMER_TYPE) 
    pygame.init()