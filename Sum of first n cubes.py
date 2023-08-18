# Input:
# N=5
# Output:
# 225
# Explanation:
# 13+23+33+43+53=225
############################
def sum_of_cubes_efficient(n):
    total = (n * (n + 1) // 2) ** 2
    return total

n = int(input("Enter a value for n: "))
result = sum_of_cubes_efficient(n)
print(f"The sum of cubes from 1^3 to {n}^3 is {result}")

