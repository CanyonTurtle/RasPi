from mcpi import minecraft
mc = minecraft.Minecraft.create()

class House:
    def __init__(self, roof_block):
        self.roof_block = roof_block

    def build(self, x, y, z):
        mc.setBlocks(x, y, z, x + 10, y + 5, z + 10, 35, 4)
        mc.setBlocks(x, y + 6, z, x + 10, y + 6, z + 10, roof_block, 0)

my_house = House(42)
my_house.build(10,20,10)
