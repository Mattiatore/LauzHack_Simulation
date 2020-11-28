# LauzHack_Simulation
Simulation, clustering, NN

clustering.py simulates people randomly moving around. Once there are too many people close together, an "illegal gathering" is called, and the simulation stops. The goal is to predict how long it will take for the simulation to stop, given the number of smaller gatherings of each size. People are considered to be in a gathering if they are close to a common point measured in the manhattan distance.
