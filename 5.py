from datetime import datetime

def sort_dates(arr, order):
    dates = list(map(lambda x: datetime.strptime(x, '%d-%m-%Y_%H:%M'), arr))
    dates.sort(key=lambda d: d.strftime('%Y%m%d%H%M'))
    if order == 'DSC': dates.reverse()
    return list(map(lambda d:  d.strftime('%d-%m-%Y_%H:%M'), dates))
    

print('sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC") ->', sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "ASC"))
print('sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC") ->', sort_dates(["10-02-2018_12:30", "10-02-2016_12:30", "10-02-2018_12:15"], "DSC"))
print('sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC") ->', sort_dates(["09-02-2000_10:03", "10-02-2000_18:29", "01-01-1999_00:55"], "ASC"))
