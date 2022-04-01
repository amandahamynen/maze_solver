from importlib.resources import path
from pyamaze import maze, agent
from tremaux import Tremaux
from left_wall_follower import LeftWallFollower

def main(x):
    m = maze(x,x)
    m.CreateMaze()
    #t = Tremaux(m, x)
    #tremaux_reitti = t.tremaux()
    #a=agent(m,filled=True,footprints=True)
    #m.tracePath({a:tremaux_reitti}, delay=100)
    #m.run()
    f = LeftWallFollower(m, x)
    wall_follower_reitti = f.wall_follower()
    a=agent(m,filled=True, shape='arrow')
    m.tracePath({a:wall_follower_reitti}, delay=200)
    m.run()

if __name__ == '__main__':
    x = 10
    main(x)