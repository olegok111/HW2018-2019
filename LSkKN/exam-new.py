MONTHS = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def prev_day(date):
    d, m, y = date[2], date[1], date[0]
    leap_year = (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0))
    d -= 1
    if d == 0:
        m -= 1
        if m == 0:
            m = 12
            y -= 1
        elif m == 2 and leap_year:
            d = 29
        else:
            d = MONTHS[m]
    return y, m, d


def move_back():
    pass

dates = {}
periods = [None]
n = int(input())
for i in range(n):
    name = input()
    exam_date = list(map(int, input().split('.')))
    exam_date = (exam_date[2], exam_date[1], exam_date[0])
    days_beforehand = int(input())
    beg_date = exam_date[:]
    predexamday = None
    for j in range(days_beforehand):
        beg_date = prev_day(beg_date)
        if predexamday is None:
            predexamday = beg_date[:]
    periods.append((beg_date, predexamday, len(periods)))
    dates[exam_date] = -1


def nstr(n):
    if n < 10:
        return '0' + str(n)
    else:
        return str(n)


periods.pop(0)
periods_prohod = sorted(periods, key=lambda x: x[1], reverse=True)
for per in periods_prohod:
    cur_date = per[1]
    while True:
        try:
            tmp = dates[cur_date]
            cur_date = prev_day(cur_date)
            if cur_date == per[0]:
                move_back()
        except:
            dates[cur_date] = per[2]
            break
    #print(dates)
ans = sorted(dates.keys())[0]
print(nstr(ans[2]) + '.' + nstr(ans[1]) + '.' + str(ans[0]))
