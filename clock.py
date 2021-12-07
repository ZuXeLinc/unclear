import time
a = time.localtime()
time = time.strftime("%H часов : %M  минут : %S секунд", a)
print("Текущее время: ", time) 
