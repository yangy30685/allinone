import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

tips = sns.load_dataset("tips")
g = sns.jointplot("total_bill", "tip",
                data=tips, kind="hex",
                xlim=(0, 60), ylim=(0, 12))

k = sns.jointplot("total_bill", "tip",
                data=tips, kind="hex",
                xlim=(0, 60), ylim=(0, 12),
                color="k", height=7)

# 2D
def fm(x, y):
    return 20*np.sin(10*np.pi*x) + 0.05 * y**2

x = np.linspace(0, 100, 50)
y = np.linspace(0, 100, 50)

X, Y = np.meshgrid(x,y)
print(X.shape)
#print(Y)

Z = fm(X, Y)
print(Z.shape)

fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, Z,
                    rstride=2, cstride=2,
                    cmap=mpl.cm.coolwarm,
                    linewidth=0.5,
                    antialiased=True)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')

fig.colorbar(surf, shrink=1, aspect=20)
plt.show()