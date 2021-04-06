import datetime

def date_in_future(integer: int=None):
    if integer is None:
        return f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
    dt_now = datetime.datetime.now()
    if type(integer) != int:
        return f"{datetime.datetime.now():%d-%m-%Y %H:%M:%S}"
    res = dt_now + datetime.timedelta(days=integer)
    return f"{res:%d-%m-%Y %H:%M:%S}"


"""
print(date_in_future([])) # => текущая дата
print(date_in_future(2)) # => текущая дата + 2 дня
"""
