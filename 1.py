def calculate_speed(coordinates: str) -> str:
    #"Ваш код"
    l = coordinates.split(',')
    for i in range(len(l)):
        l[i] = float(l[i])
    result = ''
    for i in range(len(l)-1):
        result += str(round(((l[i] - l[i+1]) * -10.0), 2)) + ','
    return result

time_period = 0.1
coordinates = "0.1,0.2,0.3,0.4,0.5"
# Ожидаемый результат
# 1.0,1.0,1.0,1.0

#coordinates = input()

speeds = calculate_speed(coordinates)

print(speeds)