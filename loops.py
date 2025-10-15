single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []

for digit in single_digits: 
  squares.append(digit ** 2)
  print(digit)

print(squares)

cubes = [digit ** 3 for digit in single_digits]
print(cubes)

# printing every element of a 2d list
grouped_topics = [ ["Algorithms", "Data Structures", "AI"], ["Linear Regression", "SQL"]]
for sublist in grouped_topics:
  for sublist_el in sublist:
    print(sublist_el)
