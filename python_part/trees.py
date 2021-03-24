import PyBulletEnv
import Obj
from numpy import random

if __name__ == "__main__":
    env = PyBulletEnv.PyBulletEnv()
    env.setup()
    tree = Obj.Obj("data/tree/Tree.obj")
    

    forest = []
    for _ in range(2):
        x = random.uniform(0, 20)
        y = random.uniform(0, 20)
        forest.append(tree.createObjectObj([x, y , 3.7], 1.0))

    env.analyze(tree, forest)
    
    env.run()


