# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to reverse a string
def reverse_string(string):
    return string[::-1]

# Function to count the occurrence of each character in a string
def count_characters(string):
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

# Function to convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to generate Fibonacci sequence up to a given limit
def generate_fibonacci(limit):
    fibonacci_seq = [0, 1]
    while fibonacci_seq[-1] + fibonacci_seq[-2] <= limit:
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return fibonacci_seq

# Function to find the maximum element in a list
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Function to check if a string is a palindrome
def is_palindrome(string):
    return string == string[::-1]

# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return 3.14159 * radius**2

# Function to check if a year is a leap year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Function to convert a decimal number to binary
def decimal_to_binary(decimal):
    return bin(decimal)[2:]

# Function to calculate the square of a number
def square(n):
    return n**2

# Function to check if a string is a pangram
def is_pangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    string = string.lower()
    string = ''.join(e for e in string if e.isalpha())
    string_set = set(string)
    return string_set == alphabet

# Function to check if a number is even
def is_even(n):
    return n % 2 == 0

#Function to calculate the cube of a number
def cube(n):
    return n**3

# Function to check if a string is an anagram
def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)

# Function to check if a number is a perfect square
def is_perfect_square(n):
    return int(n**0.5)**2 == n

# Function to calculate the power of a number
def power(base, exponent):
    return base ** exponent

# Function to check if a string is a valid email address
def is_valid_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

# Function to check if a number is a palindrome
def is_palindrome_number(number):
    return str(number) == str(number)[::-1]


# Menu function
def menu():
    print("Welcome to the Python Program!")
    print("Please select an option:")
    print("1. Calculate the factorial of a number")
    print("2. Check if a number is prime")
    print("3. Reverse a string")
    print("4. Count the occurrence of each character in a string")
    print("5. Convert temperature from Celsius to Fahrenheit")
    print("6. Generate Fibonacci sequence up to a given limit")
    print("7. Find the maximum element in a list")
    print("8. Check if a string is a palindrome")
    print("9. Calculate the area of a circle")
    print("10. Check if a year is a leap year")
    print("11. Convert a decimal number to binary")
    print("12. Calculate the square of a number")
    print("13. Check if a string is a pangram")
    print("14. Check if a number is even")
    print("15. Calculate the cube of a number")
    print("16. Check if two strings are anagrams")
    print("17. Check if a number is a perfect square")
    print("18. Calculate the power of a number")
    print("19. Check if a string is a valid email address")
    print("20. Check if a number is a palindrome")
    print("0. Exit")

# Main program
while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting the program...")
        break

    elif choice == "1":
        number = int(input("Enter a number: "))
        print("Factorial:", factorial(number))

    elif choice == "2":
        number = int(input("Enter a number: "))
        print("Is prime:", is_prime(number))

    elif choice == "3":
        string = input("Enter a string: ")
        print("Reversed string:", reverse_string(string))

    elif choice == "4":
        string = input("Enter a string: ")
        print("Character count:", count_characters(string))

    elif choice == "5":
        celsius = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

    elif choice == "6":
        limit = int(input("Enter the limit: "))
        print("Fibonacci sequence:", generate_fibonacci(limit))

    elif choice == "7":
        numbers_list = input("Enter a list of numbers, separated by spaces: ").split()
        numbers_list = [int(num) for num in numbers_list]
        print("Maximum number:", find_max(numbers_list))

    elif choice == "8":
        string = input("Enter a string: ")
        print("Is palindrome:", is_palindrome(string))

    elif choice == "9":
        radius = float(input("Enter the radius of the circle: "))
        print("Area of the circle:", calculate_circle_area(radius))

    elif choice == "10":
        year = int(input("Enter a year: "))
        print("Is leap year:", is_leap_year(year))

    elif choice == "11":
        decimal = int(input("Enter a decimal number: "))
        print("Binary representation:", decimal_to_binary(decimal))
   
    elif choice == "12":
        number = int(input("Enter a number: "))
        print("Square:", square(number))

    elif choice == "13":
        string = input("Enter a string: ")
        print("Is pangram:", is_pangram(string))
    
    elif choice == "14":
        number = int(input("Enter a number: "))
        print("Is even:", is_even(number))
  
    elif choice == "15":
        number = int(input("Enter a number: "))
        print("Cube:", cube(number))

    elif choice == "16":
        string1 = input("Enter the first string: ")
        string2 = input("Enter the second string: ")
        print("Are anagrams:", is_anagram(string1, string2))

    elif choice == "17":
        number = int(input("Enter a number: "))
        print("Is perfect square:", is_perfect_square(number))

    elif choice == "18":
        base = int(input("Enter the base number: "))
        exponent = int(input("Enter the exponent: "))
        print("Power:", power(base, exponent))

    elif choice == "19":
        email = input("Enter an email address: ")
        print("Is valid email address:", is_valid_email(email))

    elif choice == "20":
        number = int(input("Enter a number: "))
        print("Is palindrome number:", is_palindrome_number(number))
    
    else:
        print("Invalid choice. Please try again.")
