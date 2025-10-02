#!/usr/bin/env python3
import plotly.graph_objects as go
import plotly.figure_factory as ff
import numpy as np
from numpy import sin, cos, tan, sqrt, exp, log, log10, arcsin, arccos, arctan, sinh, cosh, tanh, abs, pi, e
import sys

def plot_vector_field_3d(u_expr, v_expr, w_expr, bounds=(-2, 2), points=8, sizeref=3):
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
    U = eval(u_expr, namespace) * np.ones_like(X)
    V = eval(v_expr, namespace) * np.ones_like(Y)
    W = eval(w_expr, namespace) * np.ones_like(Z)

    fig = go.Figure(data=go.Cone(
        x=X.flatten(),
        y=Y.flatten(),
        z=Z.flatten(),
        u=U.flatten(),
        v=V.flatten(),
        w=W.flatten(),
        sizemode="absolute",
        sizeref=sizeref
    ))
    
    fig.update_layout(scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    ))
    
    fig.show()

def plot_vector_field_2d(u_expr, v_expr, bounds=(-3, 3), points=20, scale=0.1, arrow_scale=0.3):
    x = np.linspace(bounds[0], bounds[1], points)
    y = np.linspace(bounds[0], bounds[1], points)
    X, Y = np.meshgrid(x, y)

    namespace = {"np": np, "x": X, "y": Y,
                 "sin": sin, "cos": cos, "tan": tan, "sqrt": sqrt,
                 "exp": exp, "log": log, "log10": log10,
                 "arcsin": arcsin, "arccos": arccos, "arctan": arctan,
                 "sinh": sinh, "cosh": cosh, "tanh": tanh,
                 "abs": abs, "pi": pi, "e": e}
    U = eval(u_expr, namespace) * np.ones_like(X)
    V = eval(v_expr, namespace) * np.ones_like(Y)

    # Use quiver plot for proper vector field visualization
    fig = ff.create_quiver(
        X.flatten(), Y.flatten(),
        U.flatten(), V.flatten(),
        scale=scale,
        arrow_scale=arrow_scale,
        name='vectors',
        line_width=2
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

    # Check if user wants to customize settings
    customize = input("Customize? (y/n): ").strip().lower()

    if customize == 'y':
        if w_expr:
            # 3D customization
            bounds_input = input("Bounds (default -2 to 2): ").strip()
            bounds = tuple(map(float, bounds_input.split())) if bounds_input else (-2, 2)

            points_input = input("Grid points (default 8): ").strip()
            points = int(points_input) if points_input else 8

            sizeref_input = input("Arrow size (default 3): ").strip()
            sizeref = float(sizeref_input) if sizeref_input else 3

            plot_vector_field_3d(u_expr, v_expr, w_expr, bounds=bounds, points=points, sizeref=sizeref)
        else:
            # 2D customization
            bounds_input = input("Bounds (default -3 to 3): ").strip()
            bounds = tuple(map(float, bounds_input.split())) if bounds_input else (-3, 3)

            points_input = input("Grid points (default 20): ").strip()
            points = int(points_input) if points_input else 20

            scale_input = input("Vector scale (default 0.1): ").strip()
            scale = float(scale_input) if scale_input else 0.1

            arrow_scale_input = input("Arrow size (default 0.3): ").strip()
            arrow_scale = float(arrow_scale_input) if arrow_scale_input else 0.3

            plot_vector_field_2d(u_expr, v_expr, bounds=bounds, points=points, scale=scale, arrow_scale=arrow_scale)
    else:
        # Use defaults
        if w_expr:
            plot_vector_field_3d(u_expr, v_expr, w_expr)
        else:
            plot_vector_field_2d(u_expr, v_expr)
