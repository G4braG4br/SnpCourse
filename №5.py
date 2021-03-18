import datetime

def date_in_future(integer: int):
    dt_now = datetime.datetime.now()
    if type(integer) != int:
        return f"{dt_now.date().day:>02d}-{dt_now.date().month:>02d}-{dt_now.date().year:<4d} " \
               f"{dt_now.time().hour:>02d}:{dt_now.time().minute:>02d}:{dt_now.time().second:>02d}"
    res = dt_now + datetime.timedelta(days=integer)
    #res = datetime.datetime(res.date().year, month=integer, day=res.date().day)
    return f"{res.date().day:>02d}-{res.date().month:>02d}-{res.date().year:<4d} " \
           f"{res.time().hour:>02d}:{res.time().minute:>02d}:{res.time().second:>02d}"


"""
print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
"""
