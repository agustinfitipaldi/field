#!/usr/bin/env python3
import plotly.graph_objects as go
import numpy as np
from numpy import sin, cos, tan, sqrt, exp, log, log10, arcsin, arccos, arctan, sinh, cosh, tanh, abs, pi, e
import sys

def plot_vector_field_3d(u_expr, v_expr, w_expr, bounds=(-2, 2), points=8):
    x = np.linspace(bounds[0], bounds[1], points)
    y = np.linspace(bounds[0], bounds[1], points)
    z = np.linspace(bounds[0], bounds[1], points)
    X, Y, Z = np.meshgrid(x, y, z)
    
    # Evaluate expressions
    # WARNING: using eval() - don't run untrusted code!
    namespace = {"np": np, "x": X, "y": Y, "z": Z,
                 "sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt,
                 "exp": exp, "log": log, "log10": log10,
                 "arcsin": arcsin, "arccos": arccos, "arctan": arctan,
                 "sinh": sinh, "cosh": cosh, "tanh": tanh,
                 "abs": abs, "pi": pi, "e": e}
    U = eval(u_expr, namespace)
    V = eval(v_expr, namespace)
    W = eval(w_expr, namespace)
    
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
    
    fig.update_layout(scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    ))
    
    fig.show()

def plot_vector_field_2d(u_expr, v_expr, bounds=(-3, 3), points=20):
    x = np.linspace(bounds[0], bounds[1], points)
    y = np.linspace(bounds[0], bounds[1], points)
    X, Y = np.meshgrid(x, y)
    
    namespace = {"np": np, "x": X, "y": Y,
                 "sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt,
                 "exp": exp, "log": log, "log10": log10,
                 "arcsin": arcsin, "arccos": arccos, "arctan": arctan,
                 "sinh": sinh, "cosh": cosh, "tanh": tanh,
                 "abs": abs, "pi": pi, "e": e}
    U = eval(u_expr, namespace)
    V = eval(v_expr, namespace)
    
    # Plotly for 2D - using scatter with arrows
    fig = go.Figure()
    
    # Create arrow annotations
    for i in range(0, len(x), max(1, len(x)//15)):  # subsample for clarity
        for j in range(0, len(y), max(1, len(y)//15)):
            fig.add_annotation(
                x=X[j,i], y=Y[j,i],
                ax=X[j,i] + U[j,i]*0.3, ay=Y[j,i] + V[j,i]*0.3,
                xref='x', yref='y',
                axref='x', ayref='y',
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='blue'
            )
    
    fig.update_layout(
        xaxis_title='x',
        yaxis_title='y',
        width=800,
        height=800,
        xaxis=dict(scaleanchor="y", scaleratio=1)
    )
    
    fig.show()

if __name__ == "__main__":
    print("Vector Field Plotter")
    print("=" * 40)

    u_expr = input("u: ").strip()
    v_expr = input("v: ").strip()
    w_expr = input("w (enter for 2D): ").strip()

    if not u_expr or not v_expr:
        print("Error: u and v components are required")
        sys.exit(1)

    if w_expr:
        # 3D mode
        plot_vector_field_3d(u_expr, v_expr, w_expr)
    else:
        # 2D mode
        plot_vector_field_2d(u_expr, v_expr)
