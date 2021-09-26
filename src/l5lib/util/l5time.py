from datetime import date, timedelta


def getDate(delta=0):
    return datetime.date.today() + timedelta(days=delta)
