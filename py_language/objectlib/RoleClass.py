#!/usr/bin/env python3
# Author Zuxing Gu

class Role(object):
    def __init__(self, name, weapon, life_value=100, money=15000):
        self.name = name
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self):
        print("useing %s shooting..." % (self.weapon))

    def got_shot(self):
        print("ah...,I got shot...")

    def buy_gun(self, gun_name):
        print("just bought %s" % gun_name)
