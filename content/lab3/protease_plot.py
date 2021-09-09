import matplotlib.pyplot as plot
import numpy as np
#ONCHHH
cords = np.array([( 1.1280,  0.2091,  0.0000), (-1.1878,  0.1791,  0.0000), ( 0.0598, -0.3882,  0.0000), (-1.3085,  1.1864,  0.0001), (-2.0305, -0.3861, -0.0001), (-0.0014, -1.4883, -0.0001)])
fig = plot.figure()
ax = fig.add_subplot(111, projection='3d', elev=90, azim=-90)
ax.scatter(cords[:,0], cords[:,1], cords[:,2], s=(800,650,600,100,100,100), c=('red','purple','grey','cyan','cyan','cyan'), depthshade=False)

db = 0.03
ax.plot(cords[0:3:2,0]+db, cords[0:3:2,1]-db, cords[0:3:2,2], linewidth=3, c='black')
ax.plot(cords[0:3:2,0]-db, cords[0:3:2,1]+db, cords[0:3:2,2], linewidth=3, c='black')

ax.plot(cords[1:3,0], cords[1:3,1], cords[1:3,2], linewidth=5, c='lightgrey')

ax.plot(cords[2:6:3,0], cords[2:6:3,1], cords[2:6:3,2], linewidth=5, c='lightgrey')

ax.plot(cords[1:4:2,0], cords[1:4:2,1], cords[1:4:2,2], linewidth=5, c='lightgrey')
ax.plot(cords[1:5:3,0], cords[1:5:3,1], cords[1:5:3,2], linewidth=5, c='lightgrey')

#ax.plot(cords[0:2,0], cords[0:2,1], cords[0:2,2], linewidth=2)#, marker='o', markersize=10)
ax.set_zlim([-0.01, 0.01])
plot.axis('off')
fig.show()
#fig.clf()
