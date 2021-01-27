from datetime import datetime

def t_diff(t1,t2):
    t_delta = '%a %d %b %Y %H:%M:%S %z'
    t1 = datetime.strptime(t1, t_delta)
    t2 = datetime.strptime(t2, t_delta)
    return str(int(abs((t1-t2).total_seconds())))


for _ in range(int(input())):
    print(t_diff(input(), input()))


