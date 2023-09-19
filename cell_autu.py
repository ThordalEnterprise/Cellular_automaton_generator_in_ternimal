# import libraries
import time, random, warnings, os, matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
warnings.filterwarnings("ignore")
import shutil

app = __name__


num_iterations = int(input("How many images do you want to generate? "))


y_count = num_iterations

import time
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os
import shutil

def step(x, rule_binary, powers_of_two):
    x_shift_right = np.roll(x, 1)
    x_shift_left = np.roll(x, -1)
    y = np.vstack((x_shift_right, x, x_shift_left)).astype(np.int8)
    z = np.sum(powers_of_two * y, axis=0).astype(np.int8)
    return rule_binary[7 - z]

def cellular_automaton(rule_number, size, steps, init_cond='random', impulse_pos='center'):
    assert 1 <= rule_number <= 256
    assert init_cond in ['random', 'impulse']
    assert impulse_pos in ['left', 'center', 'right']

    powers_of_two = np.array([[4], [2], [1]])
    rule_binary_str = np.binary_repr(rule_number, width=8)
    rule_binary = np.array([int(ch) for ch in rule_binary_str], dtype=np.int8)
    
    x = np.zeros((steps, size), dtype=np.int8)
    
    if init_cond == 'random':
        x[0, :] = np.array(np.random.rand(size) < 0.5, dtype=np.int8)
    elif init_cond == 'impulse':
        if impulse_pos == 'left':
            x[0, 0] = 1
        elif impulse_pos == 'right':
            x[0, size - 1] = 1
        else:
            x[0, size // 2] = 1
    
    for i in range(steps - 1):
        x[i + 1, :] = step(x[i, :], rule_binary, powers_of_two)
    
    return x

def generate_cellular_automaton():
    x_count = 0
    while x_count < y_count:
        print(str(x_count+1)+" out of "+str(y_count))
        x_count +=1
        random_x = random.randint(1, 256)
        empte_array = []
        
        if random_x in empte_array:
            random_x = random.randint(1, 256)
        
        empte_array.append(random_x)
        
        rule_number = random_x
        size = 100
        steps = 400
        init_cond = random.choice(['random', 'impulse'])
        impulse_pos = random.choice(['left', 'right', 'center'])

        x = cellular_automaton(rule_number, size, steps, init_cond, impulse_pos)
        steps_to_show = 100
        iterations_per_frame = 3
        frames = int(steps // iterations_per_frame)
        interval = 50

        collection = "Cellular Automata 1st Edition "
        rand_x = random.randint(0, 163)
        skinz = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']
        color_skinz = skinz[rand_x]

        fig = plt.figure(figsize=(10, 10))
        ax = plt.axes()
        ax.set_axis_off()

        def animate(i):
            ax.clear()
            ax.set_axis_off()
            Y = np.zeros((steps_to_show, size), dtype=np.int8)
            upper_boundary = (i + 1) * iterations_per_frame
            lower_boundary = 0 if upper_boundary <= steps_to_show else upper_boundary - steps_to_show
            for t in range(lower_boundary, upper_boundary):
                Y[t - lower_boundary, :] = x[t, :]
            img = ax.imshow(Y, interpolation='none', cmap=color_skinz)
            return [img]

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)

        file = open("REC.txt", 'a')
        file.writelines(str(collection) + ' - Rule #'+str(rule_number) + ' - Skin #'+str(color_skinz) + " - Interval #"+str(interval) + " - Frames #" + str(frames)+ " - steps_to_show #"+str(steps_to_show)+" - steps #"+str(steps) + " - size #"+str(size)+" - init_cond #"+str(init_cond)+ " - impulse_pos #"+str(impulse_pos)+ " - \n")
        file.close()

        anim = animation.FuncAnimation(fig, animate, frames=frames, interval=interval, blit=True)
        anim.save('output'+str(x_count)+".gif", writer='Pillow')

        original_folder = os.getcwd()
        destination_folder = 'output'
        file_name = 'output'+str(x_count)+".gif"

        if os.path.isfile(original_folder + '/' + file_name):
            shutil.move(original_folder + '/' + file_name, destination_folder + '/' + file_name)
        else:
            print(file_name + ' not found in ' + original_folder)

generate_cellular_automaton()

print("Done")
