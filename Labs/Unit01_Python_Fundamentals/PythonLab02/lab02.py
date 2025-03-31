def alpha_slices():
    alph = "abcdefghij"
    print(alph[0:3])
    print(alph[2:5])
    print(alph + alph[3:6])

def this_to_that(sentence):
    return sentence.replace("this", "that")


def clean_string(sentence):
    return sentence.strip()

def count_email_domains(emails):
    domains = {}
    for address in emails:
        index = address.find("@")
        key = address[index + 1: ]
        if key in domains:
            domains[key] += 1
        else:
            domains[key] = 1

    return domains


def pet_names():
    animals = {"buddy" : "cat", "tank": "dog", "dave" : "fish"}
    for animal in animals:
        print(animal + " is a " + animals[animal])


def are_anagrams(word1, word2):
    letters = {}
    for letter in word1:
        letters[letter] = True
    for letter in word2:
        if letter not in letters:
            return False
        
    return True

alpha_slices()
print(this_to_that("this cat went to this market this apple"))
print(clean_string("     this cat went to this market this apple      "))
emails = ["user1@example.com", "user2@example.com",
"user3@gmail.com", "user4@example.com"]
print(count_email_domains(emails))
pet_names()
print(are_anagrams("listen", "silent"))



