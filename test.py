import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

np.random.seed(7)  # Set the random seed

omap3D = np.zeros((201, 201, 201))  # Create a 3D occupancy map
mapWidth = 200
mapLength = 200
numberOfObstacles = 10
obstacleNumber = 0

while obstacleNumber < numberOfObstacles:
    width = np.random.randint(1, 51)  # The largest integer in the sample intervals for obtaining width, length, and height
    length = np.random.randint(1, 51)
    height = np.random.randint(1, 151)
    xPosition = np.random.randint(0, mapWidth - width + 1)
    yPosition = np.random.randint(0, mapLength - length + 1)

    xObstacle, yObstacle, zObstacle = np.meshgrid(np.arange(xPosition, xPosition + width),
                                                  np.arange(yPosition, yPosition + length),
                                                  np.arange(0, height + 1))
    xyzObstacles = np.column_stack((xObstacle.ravel(), yObstacle.ravel(), zObstacle.ravel()))

    checkIntersection = False
    for i in range(xyzObstacles.shape[0]):
        if np.any(omap3D[xyzObstacles[i, 0], xyzObstacles[i, 1], xyzObstacles[i, 2]] == 1):
            checkIntersection = True
            break

    if checkIntersection:
        continue

    omap3D[xyzObstacles[:, 0], xyzObstacles[:, 1], xyzObstacles[:, 2]] = 1

    obstacleNumber += 1

xGround, yGround, zGround = np.meshgrid(np.arange(mapWidth + 1), np.arange(mapLength + 1), np.arange(1))
xyzGround = np.column_stack((xGround.ravel(), yGround.ravel(), zGround.ravel()))
omap3D[xyzGround[:, 0], xyzGround[:, 1], xyzGround[:, 2]] = 1

fig = plt.figure("3D Occupancy Map")
ax = fig.add_subplot(111, projection='3d')
ax.voxels(omap3D, edgecolor='k')
plt.show()
