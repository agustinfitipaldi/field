import numpy as np
import matplotlib.pyplot as plt

# Set up a grid
x = np.linspace(-3, 3, 20)  # 20 points from -3 to 3
y = np.linspace(-3, 3, 20)
X, Y = np.meshgrid(x, y)

# Define your vector field components
U = -Y           # x-component (like your -y from the problem)
V = 3*X          # y-component (like your 3x)

# Plot it
plt.figure(figsize=(8,8))
plt.quiver(X, Y, U, V)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Vector Field')
plt.grid()
plt.axis('equal')
plt.show()
