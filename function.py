#59 Functions in python
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

# Function to check if a string is a valid URL
def is_valid_url(url):
    import re
    pattern = r'^(https?://)?(www\.)?[a-zA-Z0-9]+\.[a-zA-Z]{2,}(\/\S*)?$'
    return re.match(pattern, url) is not None

# Function to calculate the sum of all elements in a list
def calculate_sum(numbers):
    return sum(numbers)

# Function to check if a string is a valid palindrome sentence
def is_palindrome_sentence(sentence):
    import re
    sentence = re.sub(r'[^a-zA-Z]', '', sentence.lower())
    return sentence == sentence[::-1]

# Function to find the median of a list of numbers
def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
    else:
        return sorted_numbers[n//2]

# Function to check if a number is a perfect number
def is_perfect_number(number):
    factors = [1]
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            factors.extend([i, number // i])
    return sum(factors) == number

# Function to calculate the factorial of a number using recursion
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Function to check if a year is a leap year using the calendar module
def is_leap_year_calendar(year):
    import calendar
    return calendar.isleap(year)

# Function to convert a binary number to decimal
def binary_to_decimal(binary):
    return int(binary, 2)

# Function to calculate the perimeter of a rectangle
def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

# Function to check if a string is a valid palindrome ignoring non-alphanumeric characters
def is_valid_palindrome(string):
    import re
    string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    return string == string[::-1]

# Function to check if a number is a perfect cube
def is_perfect_cube(number):
    cube_root = round(number ** (1/3))
    return cube_root ** 3 == number

# Function to check if a year is a leap year without using the calendar module
def is_leap_year_simple(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Function to check if a string is a valid password (at least 8 characters, containing letters, numbers, and symbols)
def is_valid_password(password):
    import re
    pattern = r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(pattern, password) is not None

# Function to calculate the hypotenuse of a right triangle
def calculate_hypotenuse(side1, side2):
    return (side1**2 + side2**2) ** 0.5

# Function to check if a string is a valid IPv4 address
def is_valid_ipv4(ipv4):
    import re
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(pattern, ipv4):
        octets = ipv4.split('.')
        if all(0 <= int(octet) <= 255 for octet in octets):
            return True
    return False

# Function to calculate the sum of digits in a number
def calculate_digit_sum(number):
    return sum(int(digit) for digit in str(number))

# Function to check if a string is a valid ISBN-10 number
def is_valid_isbn10(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 10 or not isbn[:-1].isdigit():
        return False
    checksum = sum(int(isbn[i]) * (10 - i) for i in range(9)) % 11
    last_digit = int(isbn[-1]) if isbn[-1] != 'X' else 10
    return checksum == last_digit

# Function to calculate the volume of a sphere
def calculate_sphere_volume(radius):
    return (4/3) * 3.14159 * radius**3

# Function to check if a string is a valid ISBN-13 number
def is_valid_isbn13(isbn):
    isbn = isbn.replace('-', '')
    if len(isbn) != 13 or not isbn.isdigit():
        return False
    checksum = sum(int(isbn[i]) * (1 if i % 2 == 0 else 3) for i in range(12))
    last_digit = int(isbn[-1])
    return (10 - checksum % 10) % 10 == last_digit

# Function to check if a string is a palindrome ignoring spaces
def is_palindrome_ignore_spaces(string):
    string = string.replace(' ', '')
    return string == string[::-1]

# Function to check if a number is a power of two
def is_power_of_two(number):
    return number > 0 and (number & (number - 1)) == 0

# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height

# Function to check if a string is a valid social security number (SSN)
def is_valid_ssn(ssn):
    import re
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return re.match(pattern, ssn) is not None

# Function to convert a decimal number to hexadecimal
def decimal_to_hexadecimal(decimal):
    return hex(decimal).lstrip('0x').rstrip('L')

# Function to check if a string is a valid palindrome permutation
def is_palindrome_permutation(string):
    import collections
    string = string.lower().replace(' ', '')
    counter = collections.Counter(string)
    odd_count = sum(count % 2 == 1 for count in counter.values())
    return odd_count <= 1

# Function to calculate the sum of all even Fibonacci numbers up to a limit
def sum_even_fibonacci(limit):
    fibonacci_seq = [0, 1]
    even_sum = 0
    while fibonacci_seq[-1] <= limit:
        if fibonacci_seq[-1] % 2 == 0:
            even_sum += fibonacci_seq[-1]
        fibonacci_seq.append(fibonacci_seq[-1] + fibonacci_seq[-2])
    return even_sum

# Function to check if a string is a valid credit card number
def is_valid_credit_card(number):
    number = number.replace(' ', '')
    if not number.isdigit():
        return False
    reversed_digits = [int(digit) for digit in reversed(number)]
    doubled_digits = [2 * digit if i % 2 == 1 else digit for i, digit in enumerate(reversed_digits)]
    summed_digits = [digit if digit < 10 else digit - 9 for digit in doubled_digits]
    return sum(summed_digits) % 10 == 0

# Function to calculate the perimeter of a triangle
def calculate_triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3

# Function to check if a string is a valid palindrome ignoring case
def is_palindrome_ignore_case(string):
    string = string.lower()
    return string == string[::-1]

# Function to calculate the sum of squares of numbers up to a given limit
def sum_of_squares(limit):
    return sum(i**2 for i in range(limit + 1))

# Function to check if a string is a valid time in the format HH:MM
def is_valid_time(time):
    import re
    pattern = r'^([01]\d|2[0-3]):([0-5]\d)$'
    return re.match(pattern, time) is not None

# Function to convert a binary number to octal
def binary_to_octal(binary):
    octal = oct(int(binary, 2))
    return octal.lstrip('0o')

# Function to check if a string is a valid palindrome ignoring punctuation
def is_palindrome_ignore_punctuation(string):
    import re
    string = re.sub(r'[^\w\s]', '', string.lower())
    return string == string[::-1]

# Function to calculate the sum of a geometric series
def calculate_geometric_series_sum(a, r, n):
    return a * (1 - r**n) / (1 - r)

# Function to check if a string is a valid IPv6 address
def is_valid_ipv6(ipv6):
    import re
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return re.match(pattern, ipv6) is not None

# Function to calculate the GCD (Greatest Common Divisor) of two numbers
def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to check if a string is a valid palindrome with a given skip character count
def is_valid_palindrome_with_skip(string, skip_count):
    string = string.replace(' ', '')
    return string == string[::-1] and len(string) >= skip_count

# Function to calculate the sum of a arithmetic series
def calculate_arithmetic_series_sum(a, d, n):
    return (n / 2) * (2*a + (n - 1) * d)

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
    print("21. Check if a string is a valid URL")
    print("22. Calculate the sum of all elements in a list")
    print("23. Check if a string is a valid palindrome sentence")
    print("24. Find the median of a list of numbers")
    print("25. Check if a number is a perfect number")
    print("26. Calculate the factorial of a number using recursion")
    print("27. Check if a year is a leap year using the calendar module")
    print("28. Convert a binary number to decimal")
    print("29. Calculate the perimeter of a rectangle")
    print("30. Check if a string is a valid palindrome ignoring non-alphanumeric characters")
    print("31. Check if a number is a perfect cube")
    print("32. Check if a year is a leap year without using the calendar module")
    print("33. Calculate the average of a list of numbers")
    print("34. Check if a string is a valid password")
    print("35. Calculate the hypotenuse of a right triangle")
    print("36. Check if a string is a valid IPv4 address")
    print("37. Calculate the sum of digits in a number")
    print("38. Check if a string is a valid ISBN-10 number")
    print("39. Calculate the volume of a sphere")
    print("40. Check if a string is a valid ISBN-13 number")
    print("41. Check if a string is a palindrome ignoring spaces")
    print("42. Check if a number is a power of two")
    print("43. Calculate the area of a triangle")
    print("44. Check if a string is a valid social security number (SSN)")
    print("45. Convert a decimal number to hexadecimal")
    print("46. Check if a string is a valid palindrome permutation")
    print("47. Calculate the sum of all even Fibonacci numbers up to a limit")
    print("48. Check if a string is a valid credit card number")
    print("49. Calculate the perimeter of a triangle")
    print("50. Check if a string is a valid palindrome ignoring case")
    print("51. Calculate the sum of squares of numbers up to a given limit")
    print("52. Check if a string is a valid time in the format HH:MM")
    print("53. Convert a binary number to octal")
    print("54. Check if a string is a valid palindrome ignoring punctuation")
    print("55. Calculate the sum of a geometric series")
    print("56. Check if a string is a valid IPv6 address")
    print("57. Calculate the GCD (Greatest Common Divisor) of two numbers")
    print("58. Check if a string is a valid palindrome with a given skip character count")
    print("59. Calculate the sum of an arithmetic series")
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

    elif choice == "21":
        url = input("Enter a URL: ")
        print("Is valid URL:", is_valid_url(url))

    elif choice == "22":
        numbers_list = input("Enter a list of numbers, separated by spaces: ").split()
        numbers_list = [int(num) for num in numbers_list]
        print("Sum of numbers:", calculate_sum(numbers_list))

    elif choice == "23":
        sentence = input("Enter a sentence: ")
        print("Is palindrome sentence:", is_palindrome_sentence(sentence))

    elif choice == "24":
        numbers_list = input("Enter a list of numbers, separated by spaces: ").split()
        numbers_list = [int(num) for num in numbers_list]
        print("Median:", find_median(numbers_list))

    elif choice == "25":
        number = int(input("Enter a number: "))
        print("Is perfect number:", is_perfect_number(number))

    elif choice == "26":
        number = int(input("Enter a number: "))
        print("Factorial:", factorial_recursive(number))

    elif choice == "27":
        year = int(input("Enter a year: "))
        print("Is leap year:", is_leap_year_calendar(year))

    elif choice == "28":
        binary = input("Enter a binary number: ")
        print("Decimal representation:", binary_to_decimal(binary))

    elif choice == "29":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print("Perimeter of the rectangle:", calculate_rectangle_perimeter(length, width))

    elif choice == "30":
        string = input("Enter a string: ")
        print("Is valid palindrome:", is_valid_palindrome(string))

    elif choice == "31":
        number = int(input("Enter a number: "))
        print("Is perfect cube:", is_perfect_cube(number))

    elif choice == "32":
        year = int(input("Enter a year: "))
        print("Is leap year:", is_leap_year_simple(year))

    elif choice == "33":
        numbers_list = input("Enter a list of numbers, separated by spaces: ").split()
        numbers_list = [int(num) for num in numbers_list]
        print("Average:", calculate_average(numbers_list))

    elif choice == "34":
        password = input("Enter a password: ")
        print("Is valid password:", is_valid_password(password))

    elif choice == "35":
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        print("Hypotenuse:", calculate_hypotenuse(side1, side2))

    elif choice == "36":
        ipv4 = input("Enter an IPv4 address: ")
        print("Is valid IPv4 address:", is_valid_ipv4(ipv4))

    elif choice == "37":
        number = int(input("Enter a number: "))
        print("Sum of digits:", calculate_digit_sum(number))

    elif choice == "38":
        isbn = input("Enter an ISBN-10 number: ")
        print("Is valid ISBN-10 number:", is_valid_isbn10(isbn))

    elif choice == "39":
        radius = float(input("Enter the radius of the sphere: "))
        print("Volume of the sphere:", calculate_sphere_volume(radius))

    elif choice == "40":
        isbn = input("Enter an ISBN-13 number: ")
        print("Is valid ISBN-13 number:", is_valid_isbn13(isbn))

    elif choice == "41":
        string = input("Enter a string: ")
        print("Is palindrome ignoring spaces:", is_palindrome_ignore_spaces(string))

    elif choice == "42":
        number = int(input("Enter a number: "))
        print("Is power of two:", is_power_of_two(number))

    elif choice == "43":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print("Area of the triangle:", calculate_triangle_area(base, height))

    elif choice == "44":
        ssn = input("Enter a social security number (SSN): ")
        print("Is valid SSN:", is_valid_ssn(ssn))

    elif choice == "45":
        decimal = int(input("Enter a decimal number: "))
        print("Hexadecimal representation:", decimal_to_hexadecimal(decimal))

    elif choice == "46":
        string = input("Enter a string: ")
        print("Is palindrome permutation:", is_palindrome_permutation(string))

    elif choice == "47":
        limit = int(input("Enter the limit: "))
        print("Sum of even Fibonacci numbers:", sum_even_fibonacci(limit))

    elif choice == "48":
        credit_card = input("Enter a credit card number: ")
        print("Is valid credit card number:", is_valid_credit_card(credit_card))

    elif choice == "49":
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))
        print("Perimeter of the triangle:", calculate_triangle_perimeter(side1, side2, side3))

    elif choice == "50":
        string = input("Enter a string: ")
        print("Is palindrome ignoring case:", is_palindrome_ignore_case(string))

    elif choice == "51":
        limit = int(input("Enter the limit: "))
        print("Sum of squares:", sum_of_squares(limit))

    elif choice == "52":
        time = input("Enter a time in the format HH:MM: ")
        print("Is valid time:", is_valid_time(time))

    elif choice == "53":
        binary = input("Enter a binary number: ")
        print("Octal representation:", binary_to_octal(binary))

    elif choice == "54":
        string = input("Enter a string: ")
        print("Is palindrome ignoring punctuation:", is_palindrome_ignore_punctuation(string))

    elif choice == "55":
        a = float(input("Enter the first term (a): "))
        r = float(input("Enter the common ratio (r): "))
        n = int(input("Enter the number of terms (n): "))
        print("Sum of geometric series:", calculate_geometric_series_sum(a, r, n))

    elif choice == "56":
        ipv6 = input("Enter an IPv6 address: ")
        print("Is valid IPv6 address:", is_valid_ipv6(ipv6))

    elif choice == "57":
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))
        print("GCD (Greatest Common Divisor):", calculate_gcd(a, b))

    elif choice == "58":
        string = input("Enter a string: ")
        skip_count = int(input("Enter the skip character count: "))
        print("Is valid palindrome with skip count:", is_valid_palindrome_with_skip(string, skip_count))

    elif choice == "59":
        a = int(input("Enter the first term (a): "))
        d = int(input("Enter the common difference (d): "))
        n = int(input("Enter the number of terms (n): "))
        print("Sum of arithmetic series:", calculate_arithmetic_series_sum(a, d, n))

    else:
        print("Invalid choice. Please try again.")
