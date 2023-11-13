with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:] # Skip header row

total = 0
for line in lines:
    name, population = line.split(",")
    print(f"Adding {name}")
    total += int(population)

print(f"Average population: {total / len(lines):,}")
