with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:]

total = 0
for line in lines:
    name, population = line.split(",")
    total += int(population)

print(f"Total population: {total:,}")
print(f"Average population: {total / len(lines):,}")
