import unittest
from BMI import bmi_gauge
def test_bmi_gauge_under():
    strs = bmi_gauge(18.4, 122, 69)
    assert strs == "The BMI for a person who is 69.0 inches with a weight of 122.0 lbs is 18.4 which is underweight"
def test_bmi_gauge_normal_lowend():
    strs = bmi_gauge(18.5, 126, 70)
    assert strs == "The BMI for a person who is 70.0 inches with a weight of 126.0 lbs is 18.5 which is normal"
def test_bmi_gauge_normal_int():
    strs = bmi_gauge(22.5,125,63)
    assert strs == "The BMI for a person who is 63 inches with a weight of 125 lbs is 21.5 which is normal"
def test_bmi_gauge_normal_highend():
    strs = bmi_gauge(24.8, 164, 69)
    assert strs == "The BMI for a person who is 69.0 inches with a weight of 164.0 lbs is 24.8 which is normal"
def test_bmi_gauge_over_lowend():
    strs = bmi_gauge(25.0, 165, 69)
    assert strs == "The BMI for a person who is 69.0 inches with a weight of 165.0 lbs is 25.0 which is overweight"
def test_bmi_gauge_over_interior():
    strs = bmi_gauge(25.7, 170, 69)
    assert strs == "The BMI for a person who is 69.0 inches with a weight of 170.0 lbs is 25.7 which is overweight"
def test_bmi_gauge_over_highend():
    strs = bmi_gauge(29.9, 198, 69)
    assert strs == "The BMI for a person who is 69.0 inches with a weight of 198.0 lbs is 29.9 which is overweight"
def test_bmi_gauge_obese_true():
    strs = bmi_gauge(61.0, 336, 63)
    assert strs == "The BMI for a person who is 63.0 inches with a weight of 336.0 lbs is 61.0 which is obese"
if __name__ == '__main__':
    unittest.main()
