# Seed colors and their corresponding magical properties
seed_colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Magical properties
magical_properties = {
    'red': 'fire-breathing',
    'blue': 'water-walking',
    'green': 'invisible',
    'yellow': 'sunshine',
    'purple': 'teleportation'
}

# Whiskers uses dictionary comprehension to label each seed
magic_garden = {color: magical_properties[color] for color in seed_colors if color in magical_properties}

# Display the magic garden dictionary
print("Whiskers' Magic Garden:", magic_garden)

# Reverse the magic properties to see which color corresponds to each property
color_by_magic = {property: color for color, property in magical_properties.items()}

# Display the reversed dictionary
print("Magic by Color:", color_by_magic)
