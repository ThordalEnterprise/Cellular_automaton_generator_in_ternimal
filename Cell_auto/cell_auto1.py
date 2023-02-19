# import libraries
import time, random, warnings
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
warnings.filterwarnings("ignore")

powers_of_two = np.array([[4], [2], [1]])  

x_count = 0
y_count = 9999
while x_count < y_count:
    try:
        current_path = os.getcwd()
        parent_directory = os.path.abspath(os.path.join(current_path, os.pardir))
        if "Collection_1" in current_path:
            os.chdir(parent_directory)

        def step(x, rule_binary):
            # Shift the array to the right and left to create a 3xN array
            x_shift_right = np.roll(x, 1)
            x_shift_left = np.roll(x, -1)
            y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)
            # Compute the sum of each row weighted by powers of 2
            # This gives a decimal number between 0 and 7 for each triplet of values
            z = np.sum(powers_of_two * y, axis=0)
            # Compute the index of the rule to apply based on the decimal numbers
            # Subtract the decimal numbers from 7 to reverse their order
            rule_index = 7 - z
            # Use rule_binary as a lookup table to get the new values
            # This works because rule_binary is a binary number with 8 bits
            # and the bits correspond to the possible values of z
            # The bits in rule_binary are ordered from left to right
            # so they correspond to the values of z in reverse order
            return np.unpackbits(np.array([rule_binary], dtype=np.uint8))[rule_index]


        def cellular_automaton(rule_number: int, size: int, steps: int,
                                init_cond: str = 'random', impulse_pos: str = 'center') -> np.ndarray:
            # Ensure arguments are valid
            assert 0 <= rule_number <= 256
            assert init_cond in ['random', 'impulse']
            assert impulse_pos in ['left', 'center', 'right']
            
            # Convert rule number to binary array
            rule_binary_str = np.binary_repr(rule_number, width=8)
            rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.int8)
            
            # Initialize grid of zeros
            x = np.zeros((steps, size), dtype=np.int8)
            
            # Random initialization of the first step
            if init_cond == 'random':
                x[0, :] = np.array(np.random.randint(2, size=size), dtype=np.int8)

            # Starting with an initial impulse
            if init_cond == 'impulse':
                if impulse_pos == 'left':
                    x[0, 0] = 1
                elif impulse_pos == 'right':
                    x[0, size - 1] = 1
                else:
                    x[0, size // 2] = 1
            
            # Iterate over steps and apply the step function to each row
            for i in range(steps - 1):
                x[i + 1, :] = step(x[i, :], rule_binary)
            
            return x


        # Set up the parameters for the cellular automaton
        random_x = random.randint(1,256)
        empte_array = []
        if random_x in empte_array:
            random_x = random.randint(1,256)
        
        empte_array.append(random_x)

        rule_number = random_x
        size = 100
        steps = 400
        init_cond = random.choice(['random', 'impulse'])
        impulse_pos = random.choice(['left', 'right', 'center'])

        # Generate the cellular automaton using the specified parameters
        x = cellular_automaton(rule_number, size, steps, init_cond, impulse_pos)

        # Set up parameters for the animation of the cellular automaton
        steps_to_show = 100
        iterations_per_frame = 3
        frames = int(steps // iterations_per_frame)
        interval = 50

        # Set up the figure and axes for the animation
        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_axis_off()

        rand_x = random.randint(0,163)
        skinz = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
        color_skinz=skinz[rand_x]

        def animate(i):
            ax.clear()  # clear the axes before drawing the next frame
            ax.set_axis_off()  # turn off the axis
            
            # create an empty array for the current frame
            Y = np.zeros((steps_to_show, size), dtype=np.int8)  
            
            # compute the upper and lower boundaries for the current frame
            upper_boundary = (i + 1) * iterations_per_frame 
            lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show 
            
            # loop over the time steps in the current frame and copy the state of the cells into Y
            for t in range(lower_boundary, upper_boundary):  
                Y[t - lower_boundary, :] = x[t, :]
            
            # create an image of the current frame using the selected color map
            img = ax.imshow(Y, interpolation='none',cmap=color_skinz)
            
            # return the image
            return [img]

            
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        # call the animator
        collection = "Cellular Automata #"

  
        cur_path=os.getcwd()
        if "Cell_auto" not in cur_path:
            os.chdir("Cell_auto/Collection_1/")
        else:
            os.chdir("Collection_1/")

        file = open("REC.txt",'a')
        file.writelines(str(collection)+str(x_count+1)+' - Rule #'+str(rule_number)+' - Skin #'+str(color_skinz)+" - Initcond #"+str(init_cond)+" - Position #"+str(impulse_pos)+" - \n")
        file.close() 
        anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)
        anim.save(str(collection)+str(x_count+1)+' Rule #'+str(rule_number)+' Skin #'+str(color_skinz)+" - Initcond #"+str(init_cond)+" - Position #"+str(impulse_pos)+'.gif', writer='Pillow')
        x_count+=1
        print(str(x_count)+" out of "+str(y_count))
    except Exception as EE:
        print(EE)
        pass


