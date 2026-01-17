# Count vowels and consonants

word = input().strip().lower()
vowels = ['a', 'e', 'i', 'o', 'u']

vcount = 0
ccount = 0

for c in word:
    if c.isalpha():          # ignore spaces & symbols
        if c in vowels:
            vcount += 1
        else:
            ccount += 1

print("Consonants:", ccount)
print("Vowels:", vcount)
