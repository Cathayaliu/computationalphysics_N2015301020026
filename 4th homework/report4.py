import ace
import matplotlib.pyplot as plt
import math
if __name__ == "__main__":
    ace.A_FUCK_BALL(15,math.pi/3,-300,4.1*0.0001,0.0039,501)
    ace.A_FUCK_BALL(15,math.pi/4,-300,4.1*0.0001,0.0039,501)
    ace.A_FUCK_BALL(15,math.pi/5,-300,4.1*0.0001,0.0039,501)
    ace.A_FUCK_BALL(15,math.pi/6,-300,4.1*0.0001,0.0039,501)
    plt.title('A test')
    plt.xlabel('y&z/m')
    plt.ylabel('x/m')
    plt.xlim((0,25))
    plt.ylim((0,12))

    plt.show()