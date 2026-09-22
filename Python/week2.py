print("===== TASK 2: GRADE CALCULATOR =====")

marks = []
total = 0

for i in range(5):
    mark = float(input("Enter marks for subject " + str(i + 1) + ": "))
    marks.append(mark)
    total = total + mark

average = total / 5

print("\nMarks obtained:")
for i in range(5):
    print("Subject", i + 1, ":", marks[i])

print("Total marks:", total)
print("Average mark:", average)

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if all(mark >= 50 for mark in marks):
    print("Overall Result: PASS")
else:
    print("Overall Result: FAIL")


print("\n===== TASK 3: STRING CAPITALIZATION =====")

text = input("Enter a string with at least 8 characters: ")

if len(text) < 8:
    print("Please enter a string with at least 8 characters.")
else:
    result = ""

    for i in range(len(text)):
        character = text[i]
        ascii_value = ord(character)

        if i % 2 == 0:
            if ascii_value >= 97 and ascii_value <= 122:
                ascii_value = ascii_value - 32

        result = result + chr(ascii_value)

    print("Modified string:", result)

print("\n===== TASK 4: NUMBER ANALYSIS =====")

number = int(input("Enter a positive integer with at least 3 digits: "))

if number <= 0:
    print("Please enter a positive number.")

elif len(str(number)) < 3:
    print("Please enter a number with at least 3 digits.")

else:
    print("Decimal:", number)
    print("Binary:", bin(number))
    print("Octal:", oct(number))
    print("Hexadecimal:", hex(number))

    last_digit = number % 10
    print("Last digit:", last_digit)

    if number % 2 == 0:
        print("Even or Odd: Even")
    else:
        print("Even or Odd: Odd")