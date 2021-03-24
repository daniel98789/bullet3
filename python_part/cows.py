import PyBulletEnv
import Obj


if __name__ == "__main__":
    env = PyBulletEnv.PyBulletEnv()
    env.setup()
    cow = Obj.Obj("data/cow/cow.obj", 0.005)
    cow.createObjectURDF([0, 1, 2.7], 1.0)
    cow.createObjectURDF([3, 1, 2.7], 0.5)
    cow.createObjectURDF([6, 1, 2.7], 0.25)
    cow.createObjectURDF([9, 1, 2.7], 0.1)

    #cow.createObjectObj([0, 1, 3], 0.1)

    

    """
    cow2 = Obj.Obj("data/cow/cow.obj", 0.01)
    #cowID = cow.createObject([0, 0, 1])
    cow2ID = cow2.createObject([6, 0, 1])

    deer = Obj.Obj("data/deer/deer.obj", 0.1)
    deerID = deer.createObject([10, 0, 0])
    """
   
    env.run()
