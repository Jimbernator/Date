#testdate.py
from libdate import day_of_week

def test_day_of_week():
    test_cases = [
        (2023, 12, 26, "Tuesday"),
        (2022, 1, 1, "Saturday"),
        (2000, 2, 29, "Tuesday"),
        (1999, 12, 31, "Friday"),
        (1980, 7, 28, "Monday"),
        (1963, 2, 19, "Tuesday"),
        # Add more test cases as needed
    ]

    for year, month, day, expected_day in test_cases:
        result = day_of_week(year, month, day)
        assert result == expected_day, f"Failed for {year}-{month:02d}-{day:02d}. Expected {expected_day}, got {result}"

    print("All test cases passed!")

# Run the test
test_day_of_week()
