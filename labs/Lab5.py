vowel_counts = {}
consonant_counts = {}
string = input("Please enter a string: ")
lowercase = string.lower()

for consonant in "qwrtypsdfghjklzxcvbnm":
	consonantCount = lowercase.count(consonant)
	consonant_counts[consonant] = consonantCount
consonantCounts = consonant_counts.values()
total_consonants = sum(consonantCounts)

for vowel in "aeiou":
	vowelCount = lowercase.count(vowel)
	vowel_counts[vowel] = vowelCount
vowelCounts = vowel_counts.values()
total_vowels = sum(vowelCounts)

print("There are: " + str(total_vowels) + " vowels in " + string )
print("There are: " + str(total_consonants) + " consonants in" + string)
print("There are: " + str(len(lowercase)) + " letters in" + string)