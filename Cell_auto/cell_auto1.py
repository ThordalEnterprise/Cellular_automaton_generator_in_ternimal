# import libraries
import time, random, warnings
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, re
import matplotlib.pyplot as plt
import matplotlib.animation as animation
warnings.filterwarnings("ignore")

powers_of_two = np.array([[4], [2], [1]])  # shape (3, 1)

x_count = 0
while x_count < 10000:
    try:
        os.chdir("/Users/Jacob/Desktop/Cell_auto")
        def step(x, rule_binary):
            """Makes one step in the cellular automaton.

            Args:
                x (np.array): current state of the automaton
                rule_binary (np.array): the update rule

            Returns:
                np.array: updated state of the automaton
            """
            x_shift_right = np.roll(x,  1)  # circular shift to right <3 kan edits
            x_shift_left = np.roll(x, -1)  # circular shift to left <3 kan edits
            y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)  # stack row-wise, shape (3, cols)
            z = np.sum(powers_of_two * y, axis=0).astype(np.int8)  # LCR pattern as number

            return rule_binary[7 - z]

        def cellular_automaton(rule_number, size, steps,
                            init_cond='random', impulse_pos='center'):
            """Generate the state of an elementary cellular automaton after a pre-determined
            number of steps starting from some random state.

            Args:
                rule_number (int): the number of the update rule to use
                size (int): number of cells in the row
                steps (int): number of steps to evolve the automaton
                init_cond (str): either `random` or `impulse`. If `random` every cell
                in the row is activated with prob. 0.5. If `impulse` only one cell
                is activated.
                impulse_pos (str): if `init_cond` is `impulse`, activate the
                left-most, central or right-most cell.

            Returns:
                np.array: final state of the automaton
            """
            assert 0 <= rule_number <= 1000000
            assert init_cond in ['random', 'impulse']
            assert impulse_pos in ['left', 'center', 'right']
            
            rule_binary_str = np.binary_repr(rule_number, width=8)
            rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.in16)
            x = np.zeros((steps, size), dtype=np.int8)
            
            if init_cond == 'random':  # random init of the first step
                x[0, :] = np.array(np.random.rand(size) < 0.5, dtype=np.int8)

            if init_cond == 'impulse':  # starting with an initial impulse
                if impulse_pos == 'left':
                    x[0, 0] = 1
                elif impulse_pos == 'right':
                    x[0, size - 1] = 1
                else:
                    x[0, size // 2] = 1
            
            for i in range(steps - 1):
                x[i + 1, :] = step(x[i, :], rule_binary)
            
            return x

        random_x = random.randint(1,256)
        empte_array = []
        if random_x in empte_array:
            while random_x in empte_array:
                random_x = random.randint(1,256)

        empte_array.append(random_x)

        rule_number = random_x # select the update rule <3
        size = 100  # number of cells in one row -- <3 Brede
        steps = 400 # number of time steps --  <3 Length 
        init_cond_array = ['random', 'impulse']
        init_cond_rand = random.randint(0,1)
        init_cond=init_cond_array[init_cond_rand]  # start with only one cell  <3  ['random', 'impulse']
        
        impulse_pos_array = ['left', 'right', 'center']
        impulse_pos_rand = random.randint(0,2)

        impulse_pos=impulse_pos_array[impulse_pos_rand]  # start with the central cell <3 -- left - right - center

        x = cellular_automaton(rule_number, size, steps, init_cond, impulse_pos)

        steps_to_show = 100  # number of steps to show in the animation window <3 Skala
        iterations_per_frame = 3  # how many steps to show per frame - <3 Speed
        frames = int(steps // iterations_per_frame)  # number of frames in the animation
        interval=50  # interval in ms between consecutive frames -- <3 Speed

        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_axis_off()

        rand_x = random.randint(0,163)
        skinz = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
        color_skinz=skinz[rand_x]

        def animate(i):
            ax.clear()  # clear the plot
            ax.set_axis_off()
            
            Y = np.zeros((steps_to_show, size), dtype=np.int8)  # initialize with all zeros
            upper_boundary = (i + 1) * iterations_per_frame  # window upper boundary
            lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show  # window lower bound.
            print("Working #"+str(x_count+1))
            for t in range(lower_boundary, upper_boundary):  # assign the values
                Y[t - lower_boundary, :] = x[t, :]
            
            #img = ax.imshow(Y, interpolation='none',cmap='RdPu')
            img = ax.imshow(Y, interpolation='none',cmap=color_skinz)
            #plt.gcf().text(0.5, 0.1, 'by Jacob Thordal', fontsize=12, fontfamily='Verdana')
            return [img]
            
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        # call the animator
        collection = "Cellular Automata #"
        file = open("REC.txt",'a')
        file.writelines(str(collection)+str(x_count+1)+' - Rule #'+str(rule_number)+' - Skin #'+str(color_skinz)+" - Initcond #"+str(init_cond)+" - Position #"+str(impulse_pos)+" - \n")
        file.close()  
        os.chdir("/Users/Jacob/Desktop/Cell_auto/Collection_1")
        anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)
        anim.save(str(collection)+str(x_count+1)+' Rule #'+str(rule_number)+' Skin #'+str(color_skinz)+" - Initcond #"+str(init_cond)+" - Position #"+str(impulse_pos)+'.gif', writer='Pillow')
        x_count+=1
    except Exception as EE:
        pass


