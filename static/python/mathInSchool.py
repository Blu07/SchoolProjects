import numpy as np
import matplotlib.pyplot as plt


def tegngraf():
    x_lim_low = 1
    x_lim_high = 10
    points = 1000
    
    x = np.linspace(x_lim_low, x_lim_high, points)
    dx = 0.0001

    plt.plot(x, f(x))
    plt.plot(x, newt_sym_kvot(f, x, dx))

    plt.plot_surface()

    plt.grid()
    plt.xlim(x_lim_low, x_lim_high)
    plt.ylim(-2.5, 2.5)
    plt.show()
    return


def derived(func, x, dx):

    der = (func(x+dx)-func(x))/dx
    return der


def newt_sym_kvot(func, c, dx):

    inc = (func(c + dx) - f(c - dx)) / (2 * dx)

    return inc


def f(x: int = 1) -> float:
    """
    Args:
        x: The value to calculate in f(x). Default is 1
    
    Returns:
        Float of calculated f(x)
    """

    try:
     value = np.sin(x)**2 - np.cos(x)**2
     return value
    
    except Exception as err:
        return(err)


import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 3*x + 1

def df(x):
    return 2*x + 3

def dfc(a, b):
    return (f(b) - f(a))/(b - a)

def compare(a, b):
    if b - a == 0:
        return df(a)
    return dfc(a, b)
for a in range(-10, 10):
    for b in range(-10,10):
        print(compare(a, b))
print((dfc(1, 3) - 3) / 2)

# Set up the figure and axes
fig = plt.figure(figsize=(12, 6))

# 3D subplot
ax1 = fig.add_subplot(121, projection='3d')

# Create data points
_x = np.arange(-10, 11, 1)
_y = np.arange(-10, 11, 1)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

# Calculate top values for each pair of points
top = np.array([compare(a, b) for a, b in zip(x, y)])

# Create the 3D bar graph
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(x, y, bottom, width, depth, top, shade=True)
ax1.set_title('Resulting C')

# 2D subplot for the function and its derivative
ax2 = fig.add_subplot(122)

# Create x values for the 2D plot
x_values = np.linspace(-10, 10, 100)

# Plot the function and its derivative
ax2.plot(x_values, f(x_values), label='Function: f(x)')
ax2.plot(x_values, df(x_values), label="Derivative: f'(x)")
ax2.legend()
ax2.set_title('Function and Derivative')

plt.show()

# delta_x = 0.00001 
# x = 4

# print(f"f({x}) = {round(f(x), 2)}")
# print(f"f'({x}) = {round(derived(f, x, delta_x), 3)}")
# print(f"Newtons sym. kvot. for f({x}) = {round(newt_sym_kvot(f, x, delta_x), 2)}")

# tegngraf()