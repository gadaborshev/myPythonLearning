# For what time the light from the Ыun will reach the Earth

SPEED_OF_LIGHT = 299_792_458 # для удобства чтения кода можно отделять числа нижним подчеркиванием
DISTANCE_TO_THE_SUN =  150_000_000_000

time = DISTANCE_TO_THE_SUN / SPEED_OF_LIGHT
print(time)

print(f"Время, необходимое свету для достижения Земли от Солнца: {time:.2f} секунд")