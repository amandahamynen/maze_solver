from pyamaze import maze, agent, COLOR
from tremaux import Tremaux
from left_wall_follower import LeftWallFollower
from dead_end_filler import DeadEndFiller

def main(x):
    m = maze(x,x)
    m.CreateMaze()
    #m.CreateMaze(loadMaze="data/maze-55.csv")

    #t = Tremaux(m, x)
    #tremaux_reitti = t.tremaux()
    #a=agent(m,filled=True,footprints=True)
    #m.tracePath({a:tremaux_reitti}, delay=100)
    #m.run()

    #f = LeftWallFollower(m, x)
    #wall_follower_reitti = f.wall_follower()
    #a=agent(m,filled=True, shape='arrow')
    #m.tracePath({a:wall_follower_reitti}, delay=200)
    #m.run()

    d = DeadEndFiller(m, x)
    dead_end_filler_etsinta, dead_end_filler_reitti = d.dead_end_filling()
    a=agent(m,filled=True,footprints=True, color=COLOR.red)
    b=agent(m,filled=True,footprints=True, color=COLOR.green)
    m.tracePath({a:dead_end_filler_etsinta},showMarked=True, delay=200)
    m.tracePath({b:dead_end_filler_reitti},showMarked=True, delay=200)
    m.run()

if __name__ == '__main__':
    x = 10
    main(x)