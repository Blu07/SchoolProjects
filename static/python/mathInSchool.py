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




delta_x = 0.00001 
x = 4

print(f"f({x}) = {round(f(x), 2)}")
print(f"f'({x}) = {round(derived(f, x, delta_x), 3)}")
print(f"Newtons sym. kvot. for f({x}) = {round(newt_sym_kvot(f, x, delta_x), 2)}")

tegngraf()