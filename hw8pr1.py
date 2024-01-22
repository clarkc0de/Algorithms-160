# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:40:55 2022

@author: Owner
"""

from matplotlib import animation
import matplotlib.pyplot as plt
import random 
import seaborn as sns
def tortoise_move(tortoise_pos):
    T=tortoise_pos[-1]
    Tchance=random.randrange(1,11)
    if Tchance<=3: #slow plod
        T+=1
    if Tchance in(4,5):#slip
        T-=6
    if Tchance in(6, 7, 8, 9, 10):#fast plod
        T+=3
    if T<1:
        T=1
    tortoise_pos+=[T]
        
    return tortoise_pos
def hare_move(hare_pos):
    H=hare_pos[-1]
    Hchance=random.randrange(1,11)
    if Hchance in(1, 2):#small slip
        H-=2
    if Hchance in(3, 4, 5):#small hop
        H+=1
    if Hchance in(6,):#big slip
        H-=12
    if Hchance in(7, 8):
        H+=9
    if Hchance in (9, 10):# sleep
        H+=0
    if H<1:
        H=1
    hare_pos+=[H]
        
    return hare_pos
def play_a_game(specified_seed):
    print("BANG!!!!")
    print("AND THEY'RE OFF!!!!")
    random.seed(specified_seed)
    tortoise_pos=tortoise_move([1])
    hare_pos=hare_move([1])
    while tortoise_pos[-1]<70 and hare_pos[-1]<70:
        tortoise_pos=tortoise_move(tortoise_pos)
        hare_pos=hare_move(hare_pos)
    return tortoise_pos, hare_pos
    
    
    
   

def display(frame_number, tortoise_pos, hare_pos):
    """ create an animation using the give data as the vertical values at each frame"""    
    plt.cla()  # clear old contents of current Figure
    data_samples =[tortoise_pos[frame_number], hare_pos[frame_number]]
    axes = sns.barplot(x = ["tortoise", "hare"], y = data_samples, palette='bright')  # new bars
    axes.set_title(f' Race Move {frame_number + 1:,}')
    axes.set(xlabel='Racer', ylabel='Position')
    axes.set_ylim(top= max(max(tortoise_pos), max(hare_pos)) * 1.10)  # scale y-axis by 10%

    # display data value above each patch (bar)
    for bar, position in zip(axes.patches, data_samples):
        text_x = bar.get_x() + bar.get_width() / 2.0  
        text_y = bar.get_height() 
        text = f'{position}'
        axes.text(text_x, text_y, text, ha='center', va='bottom')
        
        

def animate_moves(tortoise_pos, hare_pos):
    """setup and run the animation of the given data"""
    sns.set_style('whitegrid')  # white background with gray grid lines
    figure = plt.figure('Animating the given data')  # Figure for animation

    number_of_frames = len(tortoise_pos)
    data_animation = animation.FuncAnimation(
        figure, display, repeat = False, frames = number_of_frames, # interval = 33,
        fargs=(tortoise_pos, hare_pos))

    #keep one of the statements below active, the other as a comment
    # to either display the animation, or save the animation to a file    
    plt.show()
    #data_animation.save('data.mp4', fps=1)
        
def analyze_data(tortoise_pos,hare_pos):
    x=tortoise_pos
    y=hare_pos
    print("number of moves:", len(x))
    if x[-1]>= 70:
        print("Tortoise wins!!")
    if y[-1]>=70:
        print("Hare wins!!")
def simulate(specified_seed):
    tortoise_pos, hare_pos = play_a_game(specified_seed)
    animate_moves(tortoise_pos, hare_pos)
    analyze_data(tortoise_pos, hare_pos)
    print("tortoise: ", tortoise_pos)
    print("hare: ", hare_pos)
simulate(12001)