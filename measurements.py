import  numpy as np
#import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from gol import game_of_life

def main():
    with open('update_counts.txt', 'w') as file:
        #total_ups = []
        for _ in range(500):
            model = game_of_life(50)
            prev_count = model.count()
            model.update_lattice()
            updates = 1
            consecutive_zeros = 0
            while consecutive_zeros < 5:
                model.update_lattice()
                #print(updates)
                if model.count() - prev_count == 0:
                    consecutive_zeros += 1
                else:
                    if consecutive_zeros == 0:
                        consecutive_zeros = 0
                        prev_count = model.count()
                        updates += 1
                    else:
                        prev_count = model.count()
                        updates += consecutive_zeros
                        consecutive_zeros = 0
                if updates == 10000:
                    break
            if updates != 10000:
                file.write(f"{updates}\n")
                #total_ups.append(updates)
            print(updates)

        #print(total_ups)

    """plt.hist(total_ups, bins=range(min(total_ups), max(total_ups) + 1), align='left', edgecolor='black')
    plt.xlabel('Number of Updates')
    plt.ylabel('Frequency')
    plt.title('Histogram of Update Counts')
    plt.show()"""

    with open('update_counts.txt', 'r') as file:
        total_ups = [int(line.strip()) for line in file]

    # Calculate the maximum value in total_ups
    max_total_ups = max(total_ups)

    # Determine the number of bins needed based on the maximum value
    num_bins = max_total_ups // 100 + 1

    # Generate bin edges from 0 to the next multiple of 100 greater than max_total_ups
    bins = np.linspace(0, num_bins * 100, num=num_bins + 1)

    # Plot the histogram with specified bins
    plt.hist(total_ups, bins=bins, align='left', edgecolor='black')

    # Labeling the axes and title
    plt.xlabel('Number of Updates')
    plt.ylabel('Frequency')
    plt.title('Histogram of Update Counts')

    # Show the plot
    plt.show()

main()
        



