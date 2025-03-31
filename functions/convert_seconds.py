def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return hours, minutes


result = convert_seconds(12672)
print(result)
