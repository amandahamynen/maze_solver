from pyamaze import maze, agent

# Tällä hetkellä vain testataan, että pyamaze toimii

m = maze(5,5)
m.CreateMaze(loadMaze="data/maze-55.csv")
a=agent(m,filled=True,footprints=True)
m.tracePath({a:m.path})
m.run()