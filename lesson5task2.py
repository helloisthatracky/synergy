word = input()
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 0
consonant_count = 0
for letter in word:
    if letter in vowels:
        vowels_count += 1
    else:
        consonant_count += 1
if vowels_count == 0:
    vowels_count = False
if consonant_count == 0:
    consonant_count = False
print(vowels_count)
print(consonant_count)