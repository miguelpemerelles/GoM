import  numpy as np
#import random
import matplotlib.pyplot as plt
from gol import game_of_life

"""def main():
    N = 50
    total_N = 2500
    model = game_of_life(N)
    model.glider()

    #I am going to set the origin at point [0,0] in the arra.y
    updates = 10
    com_values = []

    com_sum = 0
    for i in range(N):
        for j in range(N):
            point = np.sqrt(i**2 + j**2)* model.lattice[i, j]
            com_sum += point
    com_initial = com_sum/total_N
    com_values.append(com_initial)
    for t in range(updates):
        model.update_lattice()

        com_sum = 0
        for i in range(N):
            for j in range(N):
                point = np.sqrt(i**2 + j**2)* model.lattice[i, j]
                com_sum += point
        com_final = com_sum/total_N
        com_values.append(com_final)   

    #v = (com_final-com_initial)/updates
    #print(v)
        
    #THIS SEEMS TO WORK BUT I HAVE IGNORED BOUNDARY CONDITIONS AND IT IS NOT FITTED. NEXT TIME FINISH IT!
    plt.plot(range(updates + 1), com_values, marker='o')
    plt.xlabel('Updates')
    plt.ylabel('Center of Mass')
    plt.title('Center of Mass vs. Updates')
    plt.grid(True)
    plt.show()"""


"""def main():
    N = 50
    total_N = 2500
    model = game_of_life(N)
    model.glider()

    updates = 30
    com_values = []

    # Calculate initial center of mass
    com_initial = np.sum(np.indices(model.lattice.shape) * model.lattice) / total_N
    com_values.append(com_initial)

    for t in range(updates):
        model.update_lattice()

        # Calculate the change in center of mass caused by the update
        com_diff = (np.sum(np.indices(model.lattice.shape) * model.lattice) / total_N) - com_initial
        com_initial += com_diff
        com_values.append(com_initial)

    plt.plot(range(updates + 1), com_values, marker='o')
    plt.xlabel('Updates')
    plt.ylabel('Center of Mass')
    plt.title('Center of Mass vs. Updates')
    plt.grid(True)
    plt.show()"""



def main():
    N = 50
    total_N = 2500
    model = game_of_life(N)
    model.glider()
    for _ in range(80):
        model.update_lattice()

    updates = 20
    com_x_values = []
    com_y_values = []
    com_values = []
    update_values = []

    active_points = np.sum(model.lattice)
    com_initial = np.sum(np.indices(model.lattice.shape) * model.lattice) /(2*active_points) #THE 2 HERE IS SKETCHY
    com_values.append(com_initial)

    com_x_initial = 0
    com_y_initial = 0
    com_initial_r = 0
    initial_updates = 0
    period = 4 ##WOULD HAVE TO ACTUALLY CALCULATE THE PERIOD MYSELF

    """
    My code right now is very ugly, I believe that it works (specially at point with no boundary), however, at boundaries
    I am not sure what is expected? There is a mention of discarding data when glider is crossing a border, which I have done
    by ignoring data when nn is at a boundary, this might be too much actually, maybe we just care if i and j are at the boundary...
    In any case, I am not sure if the com is expected to go back to the beggining or if it is expected to keep going on its path?
    Periodic? Or continuous line? 

    I also still have to fit the data. AND keep the data in a data file. Should do that for measurements.py too!
    """

    for t in range(updates + 1):
        while any(model.is_at_boundary(i, j) for i, j in zip(*model.lattice.nonzero())):
            com_x_initial= com_y
            com_y_initial = com_y
            com_initial_r = com_initial
            print("boundary")
            for _ in range(period):
                model.update_lattice()
                initial_updates += 1
        active_points = np.sum(model.lattice)
        com_x_sum = 0
        com_y_sum = 0
        for i in range(N):
            for j in range(N):
                """while model.is_at_boundary(i, j) and model.lattice[i, j] == 1:
                    print("boundary")
                    model.update_lattice()"""
                com_x_sum += i * model.lattice[i, j]
                com_y_sum += j * model.lattice[i, j]
        com_x = com_x_initial + com_x_sum / active_points #total_N
        com_y = com_y_initial + com_y_sum / active_points #total_N
        com_x_values.append(com_x)
        com_y_values.append(com_y)
        model.update_lattice()
        initial_updates += 1
        update_values.append(initial_updates)

        # Calculate the change in center of mass caused by the update
        com_diff = (np.sum(np.indices(model.lattice.shape) * model.lattice) / (2*active_points)) - com_initial
        com_initial += com_initial_r + com_diff
        com_values.append(com_initial)

    #plt.plot(range(updates + 1), com_x_values, marker='o', label='X Coordinate')
    #plt.plot(range(updates + 1), com_y_values, marker='s', label='Y Coordinate')
    plt.plot(update_values, com_x_values, marker='o', label='X Coordinate')
    plt.plot(update_values, com_y_values, marker='s', label='Y Coordinate')
    #plt.plot(range(updates + 2), com_values, marker='x', label='R Coordinate')
    plt.xlabel('Updates')
    plt.ylabel('Center of Mass')
    plt.title('Center of Mass vs. Updates')
    plt.legend()
    plt.grid(True)
    plt.show()

main()

"""
I am not really satisfied in how I calculate com in term of i and j, still feels like it should be i**2 and j**2 and sqrt()??
How to take into account periodic boundary conditions:
When the active cells hit a boundary, the values stop updating while the model keeps updating until they arent in a boundary anymore.
To stay consistent, when values are updated again, we add the last com to all the following com's.
"""








