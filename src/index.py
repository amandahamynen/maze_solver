from pyamaze import maze, agent
from tremaux import Tremaux

def main(x):
    m = maze(x,x)
    #m.CreateMaze(loadMaze="data/maze-55.csv")
    m.CreateMaze()
    t = Tremaux(m, x)
    tremaux_reitti = t.tremaux()
    a=agent(m,filled=True,footprints=True)
    m.tracePath({a:tremaux_reitti}, delay=100)
    m.run()

if __name__ == '__main__':
    x = 10
    main(x)