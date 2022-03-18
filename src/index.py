from pyamaze import maze, agent

# Tällä hetkellä vain testataan, että pyamaze toimii

m = maze()
m.CreateMaze()
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})
m.run()