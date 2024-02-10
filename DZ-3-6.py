word = input("Введите слово из маленьких латинских букв: ")

glasnye = 0
soglasnye = 0

for letter in word:
    if letter in ['a', 'e', 'i', 'o', 'u']:
        glasnye += 1
    elif letter.isalpha():
        soglasnye += 1
    else:
        print(False)
        break

if soglasnye + glasnye == len(word):
    print("Количество гласных букв:", glasnye)
    print("Количество согласных букв:", soglasnye)