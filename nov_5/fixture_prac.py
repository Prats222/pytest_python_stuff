
import time
import pytest

# ---------- Fixtures ----------

@pytest.fixture(scope="module")
def module_res():
    print("\n[module setup] create module resource")
    yield {"started_at": time.time()}
    print("[module teardown] clean module resource")

@pytest.fixture(scope="class")
def class_res(request):
    print(f"\n  [class setup] for {request.node.name}")
    yield {"class_name": request.node.name}
    print(f"  [class teardown] for {request.node.name}")

@pytest.fixture(scope="function")
def func_res():
    print("    [function setup] make fresh data")
    yield {"stamp": time.time()}
    print("    [function teardown] dispose fresh data")


# ---------- Test Class 1

class TestMath:
    def test_add(self, module_res, class_res, func_res):
        print("      running TestMath::test_add")
        assert 2 + 3 == 5
        assert "class_name" in class_res
        assert "started_at" in module_res
        assert "stamp" in func_res

    def test_mul(self, module_res, class_res, func_res):
        print("      running TestMath::test_mul")
        assert 4 * 5 == 20


# ---------- Test Class 2

class TestStrings:
    def test_upper(self, module_res, class_res, func_res):
        print("      running TestStrings::test_upper")
        assert "hello".upper() == "HELLO"

    def test_contains(self, module_res, class_res, func_res):
        print("      running TestStrings::test_contains")
        text = "pytest fixtures"
        assert "fixtures" in text


# ---------- Standalone tests

def test_solo_one(module_res, func_res):
    print("      running test_solo_one")
    assert isinstance(module_res["started_at"], float)

def test_solo_two(func_res):
    print("      running test_solo_two")
    assert True
