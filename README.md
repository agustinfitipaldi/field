# field

Interactive 2D and 3D vector field plotter using Plotly.

## Installation

```bash
pip install -e .
```

## Usage

```bash
field
```

Enter expressions for the vector components using `x`, `y`, and optionally `z`:

```
u: -y
v: x
w (enter for 2D):
```

Supports standard math functions: `sin`, `cos`, `tan`, `sqrt`, `exp`, `log`, `arctan`, etc.

### Examples

**2D rotation field:**
```
u: -y
v: x
```

**3D helix:**
```
u: -y
v: x
w: 1
```

**Radial field:**
```
u: x
v: y
```
