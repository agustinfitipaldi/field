import plotly.graph_objects as go
import numpy as np

x = np.linspace(-2, 2, 8)
y = np.linspace(-2, 2, 8)
z = np.linspace(-2, 2, 8)
X, Y, Z = np.meshgrid(x, y, z)

U = -Y
V = X  
W = Z*0.5

fig = go.Figure(data=go.Cone(
    x=X.flatten(),
    y=Y.flatten(),
    z=Z.flatten(),
    u=U.flatten(),
    v=V.flatten(),
    w=W.flatten(),
    sizemode="absolute",
    sizeref=3
))

fig.show()
