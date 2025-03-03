import numpy as np

#this script creates an ulam spiral in the terminal

def get_valid_integer(prompt="Enter the number of rings of the spiral (integer larger than 1) >>:"):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input > 1:
                return user_input
            else:
                print("input must be greated than 1, please try again")
        except ValueError:
            print("Invalid input. Please enter an integer.")


def generate_ulam_spiral(n):
    #generates an ulam spiral of size n, n being odd
    #The value that will be passed will always be odd (2*rings+1) so no need to check

    #initialize a numpy matrix filled with zeroes
    grid=np.zeros((n, n), dtype=int)

    #start at the center of the grid
    x, y = n // 2, n // 2

    #initialize the first number
    current_number = 1
    grid[x, y] = current_number

    #define possible directions
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction_index = 3 #the spiral starts moving to the right

    step_size = 1
    while current_number < n**2:
        for _ in range(2):
            dx, dy = directions[direction_index]
            for _ in range(step_size):
                if current_number >= n**2:
                    break
                x += dx
                y += dy
                current_number +=1
                grid[x, y] = current_number
            direction_index = (direction_index - 1) % 4 #this changes direction, minus makes it counter-clockwise
        step_size += 1 #increase the step size after two directions
    return grid

def prime_sieve(limit):
    is_prime = np.ones(limit+1, dtype=bool)
    is_prime[:2] = False #0 and 1 are not prime
    for i in range(2, int(limit**0.5) + 1):

        if is_prime[i]:
            is_prime[i * i : limit + 1 : i] = False
    return is_prime

def draw_spiral_characters(matrix, prime_list):
    #this function draws the matrix with pretty characters
    #The starting 1 will be displayed as 1
    #The rest of numbers will be displayed with * for primes and blank for non primes
    # #according to the boolean list passed on to prime_list
    print("Printing square:\n\n\n")
    for x in range(len(matrix)):
        for y in range(len(matrix)):
            spiral_char = "0"
            if matrix[x][y] == 1:
                spiral_char = "1"
            else:
                if prime_list[matrix[x][y]]:
                    spiral_char = "*"
                else:
                    spiral_char =" "

            print(f"{spiral_char:^3} ", end="")
        print("\n", end="")
    print("\n", end="")


rings_number=get_valid_integer()

spiral_side=2*rings_number+1
max_number=spiral_side*spiral_side

list_of_primes=prime_sieve(max_number)

test_spiral=generate_ulam_spiral(spiral_side)

draw_spiral_characters(test_spiral, list_of_primes)

print("Spiral coded  by Fer :)")


