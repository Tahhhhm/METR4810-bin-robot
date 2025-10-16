# This code combines all the functions and models and lays out operational procedure of the METR4810
# Miniturized Garbage Bin Prototype
from MOTOR_CODE import MotorController

motor_assembly = MotorController([23, 24, 17, 27]) # This is what we're using on the prototype

# Navigate (near entire) track to find delivery zones and bins

# Use A* search algorithm to compute the shortest path to each bin

# Travel to the closest bin and record the lid colour

# Extract contents from the bin

# Move to the deposit zone

# If bin lid was red, deposit to landfill pile, else deposit to recycling pile

# Repeat until all bins are cleared — collection is complete
