import redis

r = redis.Redis()
players = {"player_1": 485,
           "player_2": 456,
           "player_3": 858,
           "player_4": 351,
           "player_5": 356,
           "player_6": 162,
           "player_7": 543,
           "player_8": 254}

# 1. Добавление результатов в таблицу:
r.zadd("players", players)
r.zadd("players", {"player_9": 278})

# 2. Удаление результатов из таблицы:
r.zrem("players", "player_9")

# 3. Изменение результата в таблице:
r.zrem("players", "player_6")
r.zadd("players", {"player_6": 208})

# 4. Полная очистка таблицы:
r.flushdb()
# r.flushall() – очистка всех имеющихся баз

# 5. Поиск данных в таблице:
print(r.zscan("players", 0, "player_1"))

# 6. Просмотр содержимого таблицы:
print(r.zrange("players", 0, -1, withscores=True))

# 7. Отображение лучшей десятки результатов:
print(r.zrevrange("players", 0, 2, withscores=True))
