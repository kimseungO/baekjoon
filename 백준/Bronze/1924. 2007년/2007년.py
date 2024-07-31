import datetime as dt

n, k = map(int, input().split())

x = dt.datetime.strptime(f"2007-{n}-{k}", "%Y-%m-%d")
week = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
print(week[x.weekday()])
