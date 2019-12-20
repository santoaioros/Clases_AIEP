import random
import datetime
number = random.randint(1, 15)
user_result = 0
result = number ** 2
first_time = datetime.datetime.now()
while(result != user_result):
    user_result = int(input('indique {} al cuadrado: '.format(number)))

last_time = datetime.datetime.now()
seconds = last_time - first_time
print(seconds)
solo_seconds = round(seconds.total_seconds(),1)
print(solo_seconds)

if (solo_seconds < 60):
    print('Felicidades has acertado en el resultado en {} segundos'.format(solo_seconds))
else:
    minutes = solo_seconds / 60
    print(minutes)
    print('Felicidades has acertado en el resultado en {} minutos'.format(round(minutes),1))