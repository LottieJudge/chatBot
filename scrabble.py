letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letters_to_points = list(zip(letters, points))
print(letters_to_points)
letters_to_points.append([" ", 0])

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letters_to_points:
      point_total += letters_to_points
    
