number = int(input("input duration:"))
days = number // 86400
hours, minutes, seconds = 0
if days > 0:
    hours = (number - (days * 24 * 3600)) // 3600
    minutes = (number - (days * 24 * 3600) - (hours * 60) // 60
    seconds = (number - (days * 24 * 3600) - (hours * 60) - (minutes * 60)
    print(days, hours, minutes, seconds)
else:
    print()
