import random as rnd
import time

cd = []  # coordinates
speed = []
temp = []
colors = []
last_blink_time = time.time()

pause = 0
visible = 1
blinking = 0

def add_ball(x, y):
    global cd, speed, temp, colors
    cd.append(x)
    cd.append(y)
    if len(speed) != 0:
        vx = abs(speed[0]) * rnd.choice([-1, 1])
        vy = abs(speed[0]) * rnd.choice([-1, 1])
        speed.append(vx)
        speed.append(vy)
        temp.append(vx)
        temp.append(vy)
    else:
        vx = 0.1 * rnd.choice([-1, 1])
        vy = 0.1 * rnd.choice([-1, 1])
        speed.append(vx)
        speed.append(vy)
        temp.append(vx)
        temp.append(vy)
    colors.append((rnd.random(), rnd.random(), rnd.random()))
    print(f"Added ball at ({x}, {y})")

def toggle_blinking():
    global blinking, visible
    blinking = not blinking
    if blinking == 0:
        visible = 1
    print("Blinking toggled")

def animate_step():
    global cd, speed, visible, last_blink_time, pause
    if pause == 1:
        return
    if blinking == 1:
        current_time = time.time()
        if current_time - last_blink_time >= 1.0:
            visible = not visible
            last_blink_time = current_time
    i = 0
    j = 1
    while j < len(cd):
        # Bounce X
        if cd[i] >= 500 or cd[i] <= 0:
            speed[i] *= -1
        # Bounce Y
        if cd[j] >= 500 or cd[j] <= 0:
            speed[j] *= -1
        # Move
        cd[i] += speed[i]
        cd[j] += speed[j]
        i += 1
        j += 1

def print_positions():
    if visible == 1:
        print("Current ball positions:")
        for idx in range(0, len(cd), 2):
            x, y = cd[idx], cd[idx + 1]
            r, g, b = colors[idx // 2]
            print(f"Ball {idx//2}: ({x:.2f}, {y:.2f}) Color: ({r:.2f}, {g:.2f}, {b:.2f})")
    else:
        print("Balls are currently invisible (blinking).")

# Simulate adding some balls and animating
add_ball(100, 100)
add_ball(200, 200)
add_ball(300, 300)

print("Initial positions:")
print_positions()

# Simulate animation for 10 steps
for step in range(10):
    animate_step()
    print(f"\nAfter step {step + 1}:")
    print_positions()
    time.sleep(0.1)  # Simulate time delay

toggle_blinking()
print("\nAfter toggling blinking:")
for step in range(5):
    animate_step()
    print(f"Step {step + 1} (blinking):")
    print_positions()
    time.sleep(0.1)
