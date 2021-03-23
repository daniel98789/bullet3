import PyBulletEnv
import Obj


if __name__ == "__main__":
    env = PyBulletEnv.PyBulletEnv()
    env.setup()
    cow = Obj.Obj("data/cow/cow.obj", 0.005)
    cow.toURDF()
    cow2 = Obj.Obj("data/cow/cow.obj", 0.01)
    #cowID = cow.createObject([0, 0, 1])
    cow2ID = cow2.createObject([6, 0, 1])

    deer = Obj.Obj("data/deer/deer.obj", 0.1)
    deerID = deer.createObject([10, 0, 0])
    env.run()
