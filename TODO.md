# TODO: Transform Particle Simulator into Cool Game

## Step 1: Modify Particle Structure
- Update particle data to include type (player, collectible, enemy)
- Player: type 0, collectible: type 1, enemy: type 2

## Step 2: Add Player Particle
- Create a player particle that follows mouse position
- Player doesn't bounce, stays within bounds

## Step 3: Change Mouse Interactions
- Right-click: Add random collectible or enemy particles
- Left-click: Toggle blink (keep for fun effect)
- Mouse movement: Update player position

## Step 4: Implement Collision Detection
- Check if player collides with collectibles (gain points, remove particle)
- Check if player collides with enemies (lose life, remove particle)

## Step 5: Add Game State Variables
- Score: Increases on collecting green particles
- Lives: Starts at 3, decreases on enemy collision
- Level: Increases every 10 points, increases difficulty

## Step 6: Update Simulation Logic
- Modify perform_simulation_update to handle game mechanics
- Add level progression (more enemies, faster speeds)

## Step 7: Add UI Rendering
- Display score, lives, level using OpenGL text
- Game over screen when lives = 0

## Step 8: Game Over and Restart
- When lives = 0, stop simulation, show game over
- Allow restart with spacebar

## Step 9: Test and Polish
- Run the game, check for bugs
- Adjust colors, speeds, balance gameplay
