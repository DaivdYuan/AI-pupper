
import time
import math

# Function to simulate a dog running in a playful manner
def play_run(pupper):
    for i in range(3):
        pupper.turn(math.pi / 4, 2) # Turn left at a fast pace
        pupper.forward_for_time(1, 1) # Move forward for 1 second at a fast pace
        pupper.turn(-math.pi / 4, 2) # Turn right at a fast pace
        pupper.forward_for_time(1, 1) # Move forward for 1 second at a fast pace

# Function to simulate a dog walking in a relaxed manner
def relaxed_walk(pupper):
    for i in range(5):
        pupper.forward_for_time(1, 0.5) # Move forward for 1 second at a slower pace
        pupper.slowStand() # Stand still for a moment
        pupper.turn(math.pi / 2, 0.5) # Turn left at a slower pace
        pupper.slowStand() # Stand still for a moment
        pupper.turn(-math.pi / 2, 0.5) # Turn right at a slower pace
        pupper.slowStand() # Stand still for a moment

# Function to simulate a dog playing fetch
def play_fetch(pupper):
    pupper.slowStand() # Stand still and get ready
    pupper.turn(math.pi / 4, 1) # Turn left at a moderate pace
    pupper.forward_for_time(2, 0.75) # Move forward for 2 seconds at a moderate pace towards the ball
    pupper.turn(-math.pi / 2, 1) # Turn right at a fast pace to go back to the owner
    pupper.forward_for_time(2, 1) # Move forward for 2 seconds at a fast pace, bring the ball back to the owner
    pupper.turn(math.pi / 4, 1) # Turn left at a moderate pace
    pupper.forward_for_time(2, 0.75) # Move forward for 2 seconds at a moderate pace for another game of fetch

# Create a Pupper object
pupper = Pupper()

# Playful run
play_run(pupper)

# Relaxed walk
relaxed_walk(pupper)

# Play fetch
play_fetch(pupper)

# Rest and turn off
pupper.rest()
pupper.is_active = False