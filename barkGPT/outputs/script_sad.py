import time
import math

# Function to simulate a dog with droopy ears and tail
def droop(pupper):
    for i in range(3):
        pupper.turn(-math.pi / 8, 0.5) # Turn right slightly
        pupper.slowStand() # Stand still and look down
        pupper.turn(math.pi / 4, 0.5) # Turn left more
        pupper.slowStand() # Stand still and look down
        pupper.turn(-math.pi / 8, 0.5) # Turn back right slightly

# Function to simulate a dog lying down and refusing to move
def lie_down(pupper):
    pupper.slowRest() # Lie down gradually
    pupper.rest() # Stay lying down

# Create a Pupper object
pupper = Pupper()

# Droop tail and ears
droop(pupper)

# Lie down and refuse to move
lie_down(pupper)

# Rest and turn off
pupper.rest()
pupper.is_active = False