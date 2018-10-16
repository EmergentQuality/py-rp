colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

for color in colors:
    print(color)
    colors[color] = len(colors[color])
    colors.append(color)
print(colors)
