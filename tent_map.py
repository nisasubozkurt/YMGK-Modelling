import numpy as np
import matplotlib.pyplot as plt

def generate_and_plot_tent_map(x0, r, iterations):
    """
    Generates the tent map sequence for the given parameters and plots the results.

    Args:
        x0: The initial value.
        r: The control parameter.
        iterations: The number of iterations to generate.
    """

    sequence = [x0]
    for _ in range(iterations - 1):  # Adjust iterations to avoid redundant calculation
        x0 = tent_map(x0, r)
        sequence.append(x0)

    plt.plot(sequence, 'b-', linewidth=0.5)
    plt.title('Tent Map: r = {}'.format(r))
    plt.xlabel('İterasyon')
    plt.ylabel('Değer')
    plt.show()

def tent_map(x, r):
    """
    Applies the tent map function to a given value.

    Args:
        x: The input value.
        r: The control parameter.

    Returns:
        The result of applying the tent map function.
    """

    if x < 0.5:
        return r * x
    else:
        return r * (1 - x)

# Example usage:
generate_and_plot_tent_map(x0=1, r=1.65, iterations=100)