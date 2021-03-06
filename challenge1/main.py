from robot import robot
from robotAI import robotAI
from simulator import *
from harry_plotter import harry_plotter

def main():
    sim = simulator("127.0.0.1", 25000)
    sim.connect()

    p3dx = robot(sim, "Pioneer_p3dx")
    p3dxAI = robotAI(p3dx)

    h = harry_plotter(p3dx, p3dxAI)

    while True:
        p3dx.update()
        h.update()
        p3dxAI.tick()
        p3dxAI.print_ai_state()

    sim.disconnect()

if __name__ == "__main__":
    main()
