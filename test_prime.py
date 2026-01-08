from prime import is_prime

def test_prime_number():
    assert is_prime(7) == True

def test_non_prime_number():
    assert is_prime(10) == False

def test_negative_number():
    assert is_prime(-5) == False

def test_one():
    assert is_prime(1) == False
