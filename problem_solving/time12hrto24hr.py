def timeConversion(s):
    # Write your code here
    hour=int(s[0:2])
    time = s[3:8]
    meridian=s[-2:]
    if meridian == "AM" and hour == 12:
        hour = "00"
    elif meridian == "PM" and hour < 12:
        hour = hour + 12
    elif hour>12:
        return "This cannot be converted to 24 hr format"
    return "{:0>2}:{}".format(hour, time)
    

if __name__ == '__main__':
    s=input("enter the time in format: 00:00:00:AM or 00:00:00:PM \n")
    result = timeConversion(s)
    print(result)

