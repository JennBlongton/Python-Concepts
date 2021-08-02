# Enumerate --> It allows us to loop over something and have an automatic counter.
lst = ['One Piece', 'Naruto', 'Death Note', 'Attack on Titan', 'Hunter X Hunetr']
for counter, value in enumerate(lst):
    print(counter, value)
# 0 One Piece
# 1 Naruto
# 2 Death Note
# 3 Attack on Titan
# 4 Hunter X Hunetr

#  enumerate also accepts an optional argument that allows us to specify the starting index of the counter.
lst = ['One Piece', 'Naruto', 'Death Note', 'Attack on Titan', 'Hunter X Hunetr']
for counter, value in enumerate(lst, 1):
    print(counter, value)
# 1 One Piece
# 2 Naruto
# 3 Death Note
# 4 Attack on Titan
# 5 Hunter X Hunetr