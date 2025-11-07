import pytest
import tempfile
import os

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def is_even(self, number):
        return number % 2 == 0

    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial not defined for negative numbers")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


# =========================
# Basic Tests
# =========================
def test_addition():
    assert 1 + 1 == 2


def test_subtraction():
    assert 5 - 3 == 2


def test_uppercase():
    assert "hello".upper() == "HELLO"


# =========================
# Test Class Structure
# =========================
class TestMathOperations:
    def test_multiplication(self):
        assert 3 * 4 == 12

    def test_division(self):
        assert 10 / 2 == 5  # 5.0 == 5 is True as well

    def test_floor_division(self):
        assert 10 // 3 == 3


# =========================
# Assert Statements
# =========================
def test_basic_assertions():
    # Equality / inequality
    assert 5 == 5
    assert "hello" != "world"

    # Comparison
    assert 10 > 5
    assert 3 <= 3
    assert 2 < 4

    # Membership
    assert 3 in [1, 2, 3]
    assert 4 not in [1, 2, 3]

    # Identity
    x = [1, 2, 3]
    y = x
    assert x is y
    assert [1, 2, 3] is not [1, 2, 3]  # Different objects

    # Type checking
    assert isinstance("hello", str)
    assert type(42) is int

    # Truthiness
    assert True
    assert not False
    assert 1  # Truthy
    assert not 0  # Falsy
    assert "hello"  # Truthy
    assert not ""  # Falsy


# =========================
# Testing Exceptions
# =========================
def test_zero_division_builtin():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_value_error_builtin():
    with pytest.raises(ValueError):
        int("not_a_number")


def test_specific_exception_message_builtin():
    with pytest.raises(ValueError, match="invalid literal"):
        int("abc")


def test_calculator_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)


def test_factorial_negative_number():
    calc = Calculator()
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calc.factorial(-5)


# =========================
# Complex Assertions
# =========================
def test_list_operations():
    numbers = [1, 2, 3, 4, 5]

    # List comprehensions in assertions
    assert all(x > 0 for x in numbers)
    assert any(x % 2 == 0 for x in numbers)

    # List equality / length
    assert numbers == [1, 2, 3, 4, 5]
    assert numbers != [1, 2, 3]
    assert len(numbers) == 5


def test_string_operations():
    text = "Hello World"
    assert text.startswith("Hello")
    assert text.endswith("World")
    assert "lo Wo" in text
    assert text.upper() == "HELLO WORLD"
    assert text.lower() == "hello world"


def test_dictionary_operations():
    person = {"name": "John", "age": 30, "city": "New York"}
    assert person["name"] == "John"
    assert "age" in person
    assert "country" not in person
    # Compare as sets for keys
    assert set(person.keys()) == {"name", "age", "city"}
    assert person.values()  # truthy (non-empty)


# =========================
# Fixtures (Basic)
# =========================
@pytest.fixture
def sample_data():
    """Fixture that returns sample data for tests"""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def calculator():
    """Fixture that provides a Calculator instance"""
    return Calculator()


def test_sum_with_fixture(sample_data):
    assert sum(sample_data) == 15


def test_calculator_add(calculator):
    result = calculator.add(5, 3)
    assert result == 8


def test_calculator_multiply(calculator):
    result = calculator.multiply(4, 7)
    assert result == 28


# =========================
# Fixtures (Setup & Teardown)
# =========================
@pytest.fixture
def temporary_file():
    """Fixture with setup and teardown"""
    # Setup - create temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8')
    temp_file.write("Hello, World!\nTest Line 1\nTest Line 2")
    temp_file.close()

    # Provide the file path to tests
    yield temp_file.name

    # Teardown - clean up the file
    if os.path.exists(temp_file.name):
        os.unlink(temp_file.name)


@pytest.fixture
def database_connection():
    """Simulate database connection lifecycle"""
    # (using prints to demonstrate setup/teardown order)
    print("\nSetting up database connection...")
    connection = {"connected": True, "data": []}
    yield connection
    print("Closing database connection...")
    connection["connected"] = False


def test_file_operations(temporary_file):
    """Test reading from temporary file"""
    with open(temporary_file, 'r', encoding='utf-8') as f:
        content = f.read()

    assert "Hello, World!" in content
    assert "Test Line 1" in content
    assert "Test Line 2" in content


def test_database_operations(database_connection):
    """Test database operations"""
    assert database_connection["connected"] is True
    # Simulate adding data
    database_connection["data"].append("test_item")
    assert len(database_connection["data"]) == 1


# =========================
# Fixture Scopes
# =========================
@pytest.fixture(scope="function")
def function_scope_fixture():
    """Runs for each test function (default)"""
    print("\nFunction fixture setup")
    yield "function_data"
    print("Function fixture teardown")


@pytest.fixture(scope="class")
def class_scope_fixture():
    """Runs once per test class"""
    print("\nClass fixture setup")
    yield "class_data"
    print("Class fixture teardown")


@pytest.fixture(scope="module")
def module_scope_fixture():
    """Runs once per test module"""
    print("\nModule fixture setup")
    yield "module_data"
    print("Module fixture teardown")


@pytest.fixture(scope="session")
def session_scope_fixture():
    """Runs once per test session"""
    print("\nSession fixture setup")
    yield "session_data"
    print("Session fixture teardown")


class TestFixtureScopes:
    def test_one(self, function_scope_fixture, class_scope_fixture, module_scope_fixture, session_scope_fixture):
        assert function_scope_fixture == "function_data"

    def test_two(self, function_scope_fixture, class_scope_fixture, module_scope_fixture, session_scope_fixture):
        assert class_scope_fixture == "class_data"


# =========================
# Fixture Dependency
# =========================
@pytest.fixture
def user_data():
    return {"username": "testuser", "email": "test@example.com"}


@pytest.fixture
def user_profile(user_data):
    """Fixture that depends on another fixture"""
    profile = user_data.copy()
    profile["premium"] = True
    profile["joined_date"] = "2024-01-01"
    return profile


@pytest.fixture
def complete_user(user_profile):
    """Fixture with multiple dependencies"""
    user_profile["settings"] = {"theme": "dark", "notifications": True}
    return user_profile


def test_user_profile(user_profile):
    assert user_profile["username"] == "testuser"
    assert user_profile["premium"] is True
    assert "joined_date" in user_profile


def test_complete_user(complete_user):
    assert complete_user["username"] == "testuser"
    assert complete_user["settings"]["theme"] == "dark"
    assert complete_user["settings"]["notifications"] is True


# =========================
# Parameterized Testing (Basic)
# =========================
@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (2.5, 3.5, 6.0),
])
def test_addition_parameterized(a, b, expected):
    calc = Calculator()
    result = calc.add(a, b)
    assert result == expected


@pytest.mark.parametrize("input_val,expected", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (4, True),
    (-2, True),  # Negative even numbers
])
def test_is_even_parameterized(input_val, expected):
    calc = Calculator()
    result = calc.is_even(input_val)
    assert result == expected


# =========================
# Parameterized Testing (Advanced)
# =========================
@pytest.mark.parametrize("operation,a,b,expected", [
    ("add", 5, 3, 8),
    ("subtract", 10, 4, 6),
    ("multiply", 6, 7, 42),
    ("divide", 15, 3, 5.0),
])
def test_all_operations(operation, a, b, expected):
    calc = Calculator()

    if operation == "add":
        result = calc.add(a, b)
    elif operation == "subtract":
        result = calc.subtract(a, b)
    elif operation == "multiply":
        result = calc.multiply(a, b)
    elif operation == "divide":
        result = calc.divide(a, b)
    else:
        raise ValueError("Unknown operation")

    assert result == expected


@pytest.mark.parametrize("input_number,expected_factorial", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
])
def test_factorial_parameterized(input_number, expected_factorial):
    calc = Calculator()
    result = calc.factorial(input_number)
    assert result == expected_factorial


# =========================
# Parameterized Exception Testing
# =========================
@pytest.mark.parametrize("a,b,expected_exception", [
    (10, 0, ValueError),
    (5, 0, ValueError),
    (-10, 0, ValueError),
])
def test_division_by_zero_parameterized(a, b, expected_exception):
    calc = Calculator()
    with pytest.raises(expected_exception):
        calc.divide(a, b)


@pytest.mark.parametrize("negative_number", [-1, -5, -10, -100])
def test_factorial_negative_parameterized(negative_number):
    calc = Calculator()
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        calc.factorial(negative_number)
