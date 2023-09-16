#Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
#в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов,
#то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает
#в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”,
#если с ритмом все не в порядке
#Пример:
#Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
#Вывод: Парам пам-пам

# Моё решение

song = input('Input the song: ').lower().split()
def song_rhythm(song):
    list_ = []
    for word in song:
        result = 0
        for letter in word:
            if letter in 'аеёиоуыэюя':
                result += 1
        list_.append(result)
    return len(list_) == list_.count(list_[0])

if song_rhythm(song):
    print('Парам пам-пам')
else:
    print('Пам парам')


# Решение как на разборе, но немного по своему :)

# song = input('Input the song: ').lower().split()
# counts = list(map(lambda word: [letter for letter in word if letter in 'аеёиоуыэюя'], song))
# result = set(map(len, counts))
# print('Парам пам-пам' if len(result) == 1 else 'Пам парам')
