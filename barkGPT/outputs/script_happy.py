
import time
import math

# Function to simulate a dog excitedly wagging its tail
def wag_tail(pupper):
    pupper.turnI(math.pi / 10, 2) # Turn slightly left
    pupper.turnI(-math.pi / 5, 4) # Turn right with a larger angle and faster speed
    pupper.turnI(math.pi / 10, 2) # Turn back slightly left
    pupper.turnI(-math.pi / 5, 4) # Turn right with a larger angle and faster speed
    pupper.turnI(math.pi / 10, 2) # Turn back slightly left

# Function to simulate a dog jumping up and down with excitement
def jump(pupper):
    pupper.slowRest() # Get ready to jump
    pupper.slowStand() # Stand up slowly
    pupper.forward_for_time(0.5, 1) # Jump up for half a second
    pupper.slowStand() # Stay standing up
    pupper.slowRest() # Sit down slowly

# Function to simulate a dog circling around with excitement
def circle(pupper):
    for i in range(3):
        pupper.turn(math.pi / 2, 0.75) # Turn left at a moderate pace
        pupper.forward_for_time(1, 0.5) # Move forward for 1 second at a slower pace
        pupper.turn(-math.pi / 2, 0.75) # Turn right at a moderate pace
        pupper.forward_for_time(1, 0.5) # Move forward for 1 second at a slower pace

# Create a Pupper object
pupper = Pupper()

# Excitedly wag tail
for i in range(3):
    wag_tail(pupper)
    time.sleep(0.5)

# Jump up and down with excitement
jump(pupper)

# Circle around with excitement
circle(pupper)

# Rest and turn off
pupper.rest()
pupper.is_active = False