def is_leap(year):
    leap = False

    return bool(leap:=((year%4==0) & ((year%100!=0)|(year%400==0))))
