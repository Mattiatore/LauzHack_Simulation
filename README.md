# LauzHack_Simulation
Simulation, clustering, NN

clustering.py simulates people randomly moving around. Once there are too many people close together, an "illegal gathering" is called, and the simulation stops. The goal is to predict how long it will take for the simulation to stop, given the number of smaller gatherings of each size. People are considered to be in a gathering if they are close to a common point measured in the manhattan distance.

At each step of the simulation, every person moves one unit in a random direction, unless that position is taken or out of the grid. After every person moved, the number of gatherings of 0 people (=empty zones), 1 person, 2 people, up to 5 people are counted. If there is a gathering of at least 6 people, then the simulation is stopped. Otherwise, these 6 numbers are given the number of remaining steps until the end of the simulation as label, and given to the ML algorithm. The goal of the ML algorithm is to see only these 6 values, and guess the label.
