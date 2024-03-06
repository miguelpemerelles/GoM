import  numpy as np
#import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gol import game_of_life


def main():
    N = int(input("Enter the size of the lattice (N): "))
    dynamics = input("Enter the dynamics (\'g\' for Glider, \'be\' for Beehive, \'bl\' for Blinker or \'r\' for random: ")
    model_anim = game_of_life(N)
    if dynamics == 'g':
        model_anim.glider()
    elif dynamics == 'be':
        model_anim.beehive()
    elif dynamics == 'bl':
        model_anim.blinker()

    fig, ax = plt.subplots()
    img = ax.imshow(model_anim.lattice)

    def update(frame):
        #prev_count = model_anim.count()
        model_anim.update_lattice()
        img.set_array(model_anim.lattice)
        #print(model_anim.count()-prev_count)
        return img,

    ani = FuncAnimation(fig, update, frames=100, interval=100, blit=True) #Change interval to go faster.
        
    plt.show()
    

main()