months = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def to_days(date):
    d, m, y = date[0], date[1], date[2]
    leap_years = (y - 1900) // 4 - (y - 1900) // 100 + (y - 1900) // 400
    res = (y - 1900) * 365 + leap_years + d
    for i in range(1, m):
        res += months[i]
    return res


def nullicate(n):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)


def to_date(days):
    res_date = [1, 1, 1900]
    while days > months[res_date[1]]:
        days -= months[res_date[1]]
        res_date[1] += 1
        if res_date[1] == 13:
            res_date[1] = 1
            res_date[2] += 1
            if res_date[2] % 400 == 0 or (res_date[2] % 4 == 0 and res_date[2] % 100):
                months[2] = 29
            else:
                months[2] = 28
    res_date[0] = days
    return res_date

print(to_date(to_days([1,2,1900])))