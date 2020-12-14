# Bouncing Balls
# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/train/python

def bouncing_ball(h, bounce, window):
    # your code
    count = -1
    if h>0 and 0<bounce<1 and 0<window<h :
        while h > window:
            h = h*bounce
            count += 2
    print(count)
bouncing_ball(2, 0.5, 1) # 1 
bouncing_ball(3, 0.66, 1.5) # 3
bouncing_ball(30, 0.66, 1.5) #15