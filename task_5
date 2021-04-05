import datetime

def date_in_future(integer: int=None):
    if integer is None:
        return None
    dt_now = datetime.datetime.now()
    if type(integer) != int:
        return f"{datetime.datetime.now():%d-%m-%y %H:%M:%S}"
    res = dt_now + datetime.timedelta(days=integer)
    #res = datetime.datetime(res.date().year, month=integer, day=res.date().day)
    return f"{res:%d-%m-%y %H:%M:%S}"


"""
print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
"""
