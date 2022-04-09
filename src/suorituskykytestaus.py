from pyamaze import maze
from tremaux import Tremaux
from left_wall_follower import LeftWallFollower
from dead_end_filler import DeadEndFiller
import time

def main(koko):
    print(f"Generoidaan {koko}x{koko} labyrinttia...")
    aloitus = time.time()
    m = maze(koko, koko)
    lopetus = time.time()
    print(f"Labyrintti generoitu. Generoiminen kesti {lopetus - aloitus} s")

    aloitus = time.time()
    t = Tremaux(m, koko)
    lopetus = time.time()
    print(f"Tremaux: {lopetus - aloitus} s")

    aloitus = time.time()
    l = LeftWallFollower(m, koko)
    lopetus = time.time()
    print(f"Left wall follower: {lopetus - aloitus} s")

    aloitus = time.time()
    d = DeadEndFiller(m, koko)
    lopetus = time.time()
    print(f"Dead end filler: {lopetus - aloitus} s")


if __name__ == '__main__':
    koko = int(input("Labyrintin koko: "))
    main(koko)
