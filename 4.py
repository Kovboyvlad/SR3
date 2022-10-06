time_minute = 5
hours_day = 8
years = int(input("Введите количество лет: "))
print('Вы сможете посмотеть', int(60/time_minute*hours_day*365*years),'экспонатов')
quantity = int(input('Введите количество эксопнатов: '))
print("Просмотр займет", quantity/(60/time_minute*hours_day), 'дней')