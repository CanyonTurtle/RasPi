from mcpi import minecraft
mc = minecraft.Minecraft.create("192.168.1.71", 4711)
import random
mc.postToChat("My name is Cannon")

while True:
    mc.setBlock(random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), 0)
