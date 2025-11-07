import pytest
from datetime import datetime, timedelta
import re
from typing import List, Dict, Any


# ============================================================================
# 1. CALCULATOR OPERATIONS TESTING
# ============================================================================

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def power(base, exponent):
        return base ** exponent


class TestCalculator:
    def test_addition_positive_numbers(self):
        assert Calculator.add(5, 3) == 8
        assert Calculator.add(100, 200) == 300

    def test_addition_negative_numbers(self):
        assert Calculator.add(-5, -3) == -8
        assert Calculator.add(-10, 5) == -5
        assert Calculator.add(10, -5) == 5

    def test_division_normal(self):
        assert Calculator.divide(10, 2) == 5
        assert Calculator.divide(9, 3) == 3

    def test_division_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            Calculator.divide(10, 0)

    def test_multiplication_decimals(self):
        assert Calculator.multiply(2.5, 4) == 10.0
        assert Calculator.multiply(0.1, 0.2) == pytest.approx(0.02)
        assert Calculator.multiply(3.14, 2) == pytest.approx(6.28)

    def test_power_operations(self):
        assert Calculator.power(2, 3) == 8
        assert Calculator.power(5, 2) == 25
        assert Calculator.power(10, 0) == 1
        assert Calculator.power(2, -1) == 0.5


# ============================================================================
# 3. LIST & DATA STRUCTURE ASSERTIONS
# ============================================================================

def sort_list(data: List) -> List:
    return sorted(data)


def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    return {**dict1, **dict2}


def set_union(set1: set, set2: set) -> set:
    return set1.union(set2)


def set_intersection(set1: set, set2: set) -> set:
    return set1.intersection(set2)


class TestDataStructures:
    def test_list_sorting_integers(self):
        data = [5, 2, 8, 1, 9]
        assert sort_list(data) == [1, 2, 5, 8, 9]

    def test_list_sorting_strings(self):
        data = ["zebra", "apple", "mango", "banana"]
        assert sort_list(data) == ["apple", "banana", "mango", "zebra"]

    def test_dictionary_operations(self):
        dict1 = {"name": "John", "age": 30}
        dict2 = {"city": "Chennai", "country": "India"}
        result = merge_dicts(dict1, dict2)

        assert result["name"] == "John"
        assert result["city"] == "Chennai"
        assert len(result) == 4

    def test_set_union(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        result = set_union(set1, set2)

        assert result == {1, 2, 3, 4, 5}
        assert len(result) == 5

    def test_set_intersection(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        result = set_intersection(set1, set2)

        assert result == {3, 4}
        assert len(result) == 2

    def test_list_comprehensions(self):
        numbers = [1, 2, 3, 4, 5]
        squares = [x ** 2 for x in numbers]

        assert squares == [1, 4, 9, 16, 25]
        assert all(isinstance(x, int) for x in squares)


# ============================================================================
# 4. EXCEPTION HANDLING TESTS
# ============================================================================

class CustomError(Exception):
    """Custom exception for testing"""
    pass


def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File {filename} not found")


def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError(f"Cannot convert {value} to integer")


def raise_custom_error():
    raise CustomError("This is a custom error message")


class TestExceptionHandling:
    def test_division_by_zero_exception(self):
        with pytest.raises(ZeroDivisionError) as exc_info:
            divide_numbers(10, 0)
        assert "not allowed" in str(exc_info.value)

    def test_file_not_found_exception(self):
        with pytest.raises(FileNotFoundError) as exc_info:
            read_file("nonexistent_file.txt")
        assert "not found" in str(exc_info.value)

    def test_invalid_type_conversion(self):
        with pytest.raises(ValueError):
            convert_to_int("abc")

        with pytest.raises(ValueError):
            convert_to_int("12.5.6")

    def test_custom_exception(self):
        with pytest.raises(CustomError) as exc_info:
            raise_custom_error()
        assert "custom error message" in str(exc_info.value)


# ============================================================================
# 5. BOOLEAN LOGIC ASSERTIONS
# ============================================================================

def check_age_and_license(age: int, has_license: bool) -> bool:
    return age >= 18 and has_license


def is_valid_username(username: str) -> bool:
    return username and len(username) >= 3 and username.isalnum()


def check_empty_collection(collection) -> bool:
    return not collection


class TestBooleanLogic:
    def test_multiple_and_conditions(self):
        assert check_age_and_license(20, True) is True
        assert check_age_and_license(20, False) is False
        assert check_age_and_license(16, True) is False
        assert check_age_and_license(16, False) is False

    def test_truthy_falsy_values(self):
        assert bool([1, 2, 3]) is True
        assert bool([]) is False
        assert bool("text") is True
        assert bool("") is False
        assert bool(0) is False
        assert bool(1) is True

    def test_none_type_checking(self):
        value = None
        assert value is None
        assert value == None
        assert not value

        value = "something"
        assert value is not None

    def test_empty_collection_validations(self):
        assert check_empty_collection([]) is True
        assert check_empty_collection([1]) is False
        assert check_empty_collection({}) is True
        assert check_empty_collection(set()) is True
        assert check_empty_collection("") is True


# ============================================================================
# 6. TYPE CHECKING ASSERTIONS
# ============================================================================

def get_user_age() -> int:
    return 25


def convert_string_to_list(text: str) -> List[str]:
    return list(text)


def create_user_dict(name: str, age: int) -> Dict[str, Any]:
    return {"name": name, "age": age}


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class TestTypeChecking:
    def test_function_return_types(self):
        result = get_user_age()
        assert isinstance(result, int)
        assert type(result) == int

    def test_type_conversion_functions(self):
        result = convert_string_to_list("hello")
        assert isinstance(result, list)
        assert all(isinstance(char, str) for char in result)
        assert len(result) == 5

    def test_dictionary_types(self):
        user = create_user_dict("Alice", 30)
        assert isinstance(user, dict)
        assert isinstance(user["name"], str)
        assert isinstance(user["age"], int)

    def test_custom_class_instances(self):
        person = Person("Bob", 25)
        assert isinstance(person, Person)
        assert hasattr(person, "name")
        assert hasattr(person, "age")
        assert type(person.name) == str
        assert type(person.age) == int


# ============================================================================
# 7. MATHEMATICAL FUNCTION TESTING
# ============================================================================

def fibonacci(n: int) -> List[int]:
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def calculate_mean(numbers: List[float]) -> float:
    return sum(numbers) / len(numbers)


def calculate_median(numbers: List[float]) -> float:
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    if n % 2 == 0:
        return (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    return sorted_numbers[n // 2]


def circle_area(radius: float) -> float:
    return 3.14159 * radius ** 2


class TestMathematicalFunctions:
    def test_fibonacci_generation(self):
        assert fibonacci(1) == [0]
        assert fibonacci(2) == [0, 1]
        assert fibonacci(5) == [0, 1, 1, 2, 3]
        assert fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]

    def test_prime_number_identification(self):
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(4) is False
        assert is_prime(17) is True
        assert is_prime(20) is False
        assert is_prime(1) is False

    def test_mean_calculation(self):
        assert calculate_mean([1, 2, 3, 4, 5]) == 3.0
        assert calculate_mean([10, 20, 30]) == 20.0
        assert calculate_mean([5]) == 5.0

    def test_median_calculation(self):
        assert calculate_median([1, 2, 3, 4, 5]) == 3
        assert calculate_median([1, 2, 3, 4]) == 2.5
        assert calculate_median([5]) == 5

    def test_geometric_formulas(self):
        assert circle_area(1) == pytest.approx(3.14159, rel=0.01)
        assert circle_area(2) == pytest.approx(12.56636, rel=0.01)
        assert circle_area(5) == pytest.approx(78.53975, rel=0.01)


# ============================================================================
# 9. DATE & TIME ASSERTIONS
# ============================================================================

def days_between(date1: datetime, date2: datetime) -> int:
    return abs((date2 - date1).days)


def calculate_age(birth_date: datetime) -> int:
    today = datetime.now()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))


def format_date(date: datetime, format_string: str) -> str:
    return date.strftime(format_string)


class TestDateTimeFunctions:
    def test_date_comparisons(self):
        date1 = datetime(2024, 1, 1)
        date2 = datetime(2024, 1, 10)

        assert date2 > date1
        assert date1 < date2
        assert date1 != date2

    def test_date_differences(self):
        date1 = datetime(2024, 1, 1)
        date2 = datetime(2024, 1, 11)

        assert days_between(date1, date2) == 10
        assert days_between(date2, date1) == 10

    def test_date_formatting(self):
        test_date = datetime(2024, 3, 15)

        assert format_date(test_date, "%Y-%m-%d") == "2024-03-15"
        assert format_date(test_date, "%d/%m/%Y") == "15/03/2024"
        assert format_date(test_date, "%B %d, %Y") == "March 15, 2024"

    def test_age_calculation(self):
        birth_date = datetime(2000, 1, 1)
        age = calculate_age(birth_date)

        assert isinstance(age, int)
        assert age >= 24  # As of 2024


# ============================================================================
# 10. REGULAR EXPRESSION ASSERTIONS
# ============================================================================

def validate_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))


def validate_password(password: str) -> bool:
    # At least 8 chars, 1 uppercase, 1 lowercase, 1 digit
    if len(password) < 8:
        return False
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    return has_upper and has_lower and has_digit


def validate_url(url: str) -> bool:
    pattern = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(pattern, url))


class TestRegularExpressions:
    def test_email_validation(self):
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@domain.co.in") is True
        assert validate_email("invalid.email@") is False
        assert validate_email("@example.com") is False
        assert validate_email("notemail.com") is False

    def test_phone_validation(self):
        assert validate_phone("1234567890") is True
        assert validate_phone("+911234567890") is True
        assert validate_phone("12345") is False
        assert validate_phone("abcd1234567") is False

    def test_password_strength(self):
        assert validate_password("Password123") is True
        assert validate_password("Weak1") is False  # Too short
        assert validate_password("nouppercas1") is False
        assert validate_password("NOLOWERCASE1") is False
        assert validate_password("NoDigits") is False

    def test_url_validation(self):
        assert validate_url("http://example.com") is True
        assert validate_url("https://www.google.com") is True
        assert validate_url("https://site.com/path/to/page") is True
        assert validate_url("not-a-url") is False
        assert validate_url("ftp://example.com") is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])