from age_verifier import AgeVerifier
import pytest

def test_is_adult_true():
    assert AgeVerifier.is_adult(18) == True
    assert AgeVerifier.is_adult(20) == True

def test_is_adult_false():
    assert AgeVerifier.is_adult(15) == False
    assert AgeVerifier.is_adult(10) == False

@pytest.mark.skip(reason="Age cannot be neagtive")
def test_is_adult_negative():
    assert AgeVerifier.is_adult(-5) == False

@pytest.mark.skipif(121 > 120, reason="Неправильне значення віку")
def test_is_adult_imbossible():
     assert AgeVerifier.is_adult(121) == False
