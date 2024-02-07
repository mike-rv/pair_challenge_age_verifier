from lib.age_verifier import *
import pytest

def test_age_verifier_user_is_old_enough():
    actual = age_verifier("1985-02-16")
    expected = "Access granted!"
    assert actual == expected

def test_age_verifier_user_is_not_old_enough():
    actual = age_verifier("2015-12-25")
    expected = "Access denied!"
    assert actual == expected
    
def test_age_verifier_wrong_format():
    with pytest.raises(Exception) as err:
        age_verifier()
    actual = str(err.value)
    expected = "Wrong date format!"
    assert actual == expected
