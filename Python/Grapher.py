from mcpi import minecraft, vec3, block
mc = minecraft.Minecraft.create()

class Graph:
    """This class can be used to graph a function in minecraft."""

    step = 0.01
    graph_block_list = [
        block.Block(35, 1),
        block.Block(35, 2),
        block.Block(35, 3),
        block.Block(35, 4),
        block.Block(35, 5)
    ]
    background_block = block.GLASS

    def setup_graph(self):
        """Draws the background for the graph."""
        ox, oy, oz = self.origin_pos
        #mc.setBlocks(ox + self.xMin, oy + self.yMin, oz + 1, ox + self.xMax, oy + self.yMax, oz + 1, 35, 1)
        mc.setBlocks(ox + self.xMin, oy + self.yMin, oz, ox + self.xMax, oy + self.yMax, oz, self.background_block.id, self.background_block.data)
        mc.setBlocks(ox + self.xMin, oy, oz, ox + self.xMax, oy, oz, 35, 15)
        mc.setBlocks(ox, oy + self.yMin, oz, ox, oy + self.yMax, oz, 35, 15)

    def __init__(self, origin_pos, xMin, xMax, yMin, yMax, mc):
        self.origin_pos = origin_pos
        self.xMin = xMin
        self.xMax = xMax
        self.yMin = yMin
        self.yMax = yMax
        self.mc = mc
        self.setup_graph()

    def plot_on_graph(self, x, y, color):
        """This function plots a point at x,y in the graph, with specified color. MC instance needed."""
        ox, oy, oz = self.origin_pos
        b = self.graph_block_list[color]
        if(y >= self.yMin and y <= self.yMax):
            self.mc.setBlock(ox + x , oy + y, oz, b.id, b.data)

    def prompt_graph_mc(self, function):
        self.mc.postToChat("Right click the ground with your sword to spawn a graph with the origin at that point.")
        mc.postToChat("Graph will be " + str(self.xMax - self.xMin) + " units long and " + str(self.yMax - self.yMin) + " units tall.")

        run = True
        while(run== True):
            evs = self.mc.events.pollBlockHits()
            for e in evs:
                self.origin_pos = vec3.Vec3(e.pos.x, e.pos.y + ( (self.yMax - self.yMin) / 2 ), e.pos.z)
                self.setup_graph()
                self.draw_function(function)
                run = False

    def prompt_graph_mc_shell(self):
        function = raw_input("y = ")
        print("Waiting for user input in minecraft...")
        self.prompt_graph_mc(function)

    def prompt_graph_shell(self):
        function = raw_input("y = ")
        x = input("x position: ")
        y = input("y position: ")
        z = input("z position: ")
        self.origin_pos = vec3.Vec3(x, y, z)
        self.xMin = input("xMin: ")
        self.xMax = input("xMax: ")
        self.yMin = input("yMin: ")
        self.yMax = input("yMax: ")
        
        self.setup_graph()
        self.draw_function(function)
        
    def draw_function(self, function):
        """draws a function on the graph."""
        x= self.xMin * 1.0
        while(x < self.xMax):
            y = eval(function)
            self.plot_on_graph(x, y, 3)
            x += self.step

my_graph = Graph(vec3.Vec3(0,0,0), -50,50,-50,50, mc)
my_graph.prompt_graph_mc_shell()
