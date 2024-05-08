def Fibonacci_loop(months, offsprings):
    """Calculate the number of rabbit pairs after a given number of months with a given offspring rate.

    Args:
        months (int): The number of months.
        offsprings (int): The number of offspring pairs produced by each pair in each month.

    Returns:
        int: The total number of rabbit pairs after the specified number of months.
    """
    # Initialize parent (adult rabbits) and child (newborn rabbits) to 1 pair each
    parent, child = 1, 1

    # Iterate over the specified number of months (subtract 1 for initial month)
    for itr in range(months - 1):
        # Update child (newborn rabbits) to become parents for the next month
        # Update parent (adult rabbits) by adding the product of child and offspring rate
        child, parent = parent, parent + (child * offsprings)

    # Return the number of rabbit pairs after the specified number of months
    return child

# Example usage:
months = 29
offsprings = 5
total_rabbits = Fibonacci_loop(months, offsprings)
print(f'Total number of rabbits after {months} months with {offsprings} offspring pairs per pair: {total_rabbits}')
