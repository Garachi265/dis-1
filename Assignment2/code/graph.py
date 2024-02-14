import matplotlib.pyplot as plt

# Read data from the file
with open('values.dat', 'r') as file:
    data = file.readlines()

# Extract x and y values
x_values = []
y_values = []
for line in data:
    parts = line.split()
    x_values.append(int(parts[0]))
    y_values.append(float(parts[1]))

# Plot the points
plt.plot(x_values, y_values, marker='o', linestyle='-')
plt.xlabel('n')
plt.ylabel('x[n]')
plt.title('x(n) = (-1)^(n) * 5^(n+2)')
plt.grid(True)
plt.show()

