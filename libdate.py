def day_of_week(year, month, day):
    # January and February are counted as months 13 and 14 of the previous year
    if month < 3:
        month += 12
        year -= 1
    
    # Zeller's Congruence formula
    q = day
    m = month
    K = year % 100
    J = year // 100

    h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) - (2 * J)) % 7
    
    # Mapping the result to the corresponding day of the week
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    day_of_week = days[h]

    return day_of_week

