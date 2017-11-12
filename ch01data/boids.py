from matplotlib import animation
from matplotlib import pyplot as plt
import numpy as np

boid_count = 10

limits = np.array([2000,4000])

def new_flock(count, lower_limits, upper_limits):
    width = upper_limits - lower_limits
    # Sets the the limits then randomise the values of both x and y values.
    return (lower_limits[:,np.newaxis] + np.random.rand(2, count) * width[:,np.newaxis])

def update_boids(positions, velocities):
    # boids tends to move towards middle, based on the set strength.
    move_to_middle_strength = 0.1
    middle = np.mean(positions, 1)
    direction_to_middle = middle[:, np.newaxis] - positions
    velocities += direction_to_middle * move_to_middle_strength

    # individuals avoid collision by repelling when too close.
    # find the separation between each individuals and others for each axis.
    separations = positions[:,np.newaxis,:] - positions[:,:,np.newaxis]
    squared_displacements = separations * separations # element wise
    square_distances = np.sum(squared_displacements, 0)
    alert_distance = 100
    far_away = square_distances > alert_distance
    separations_if_close = np.copy(separations)
    separations_if_close[0,:,:][far_away] = 0
    separations_if_close[1,:,:][far_away] = 0
    velocities += np.sum(separations_if_close, 1) # plus here because want to add distance when too close to each other

    # trying to match speed of nearby birds.
    velocity_differences = velocities[:,np.newaxis,:] - velocities[:,:,np.newaxis]
    formation_flying_distance = 10000
    formation_flying_strength = 0.125
    very_far = square_distances > formation_flying_distance
    velocity_differences_if_close = np.copy(velocity_differences)
    velocity_differences_if_close[0,:,:][very_far] = 0
    velocity_differences_if_close[1,:,:][very_far] = 0
    velocities -= np.mean(velocity_differences_if_close, 1) * formation_flying_strength # minus here because want to reduce the vel differences between nearby inds.

    #update position based on velocities
    positions += velocities

def animate(frame):
    update_boids(positions, velocities)
    scatter.set_offsets(positions.transpose()) # because position stores by separating x and y, need to transpose to merge each 100 paris together to plot

positions=new_flock(100, np.array([100,900]), np.array([200,1100]))
# randomised constant background velocity
velocities=new_flock(100, np.array([0,-20]), np.array([10,20]))

figure = plt.figure()
axes = plt.axes(xlim=(0, limits[0]), ylim=(0, limits[0]))
scatter=axes.scatter(positions[0,:],positions[1,:])

anim=animation.FuncAnimation(figure, animate,
                        frames=50, interval=50)
plt.show()

