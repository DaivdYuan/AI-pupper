
import time
import math

# Function to simulate a dog shaking water off its body
def shake(pupper):
    pupper.slowStand() # Stand up slowly
    pupper.turnI(-math.pi / 4, 4) # Turn right and shake head
    pupper.turnI(math.pi / 2, 4) # Turn left and shake body
    pupper.turnI(-math.pi / 2, 4) # Turn right and shake body
    pupper.turnI(math.pi / 2, 4) # Turn left and shake body
    pupper.turnI(-math.pi / 4, 4) # Turn right and shake head
    pupper.slowRest() # Return to resting position

# Create a Pupper object
pupper = Pupper()

# Shake
shake(pupper)

# Rest and turn off
pupper.rest()
pupper.is_active = False