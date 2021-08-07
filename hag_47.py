import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["museum"]
exhibits = db["exhibits"]
persons = db["persons"]

exhibits_list = [
    {"type": "book", "title": "April Theses", "person": "Vladimir Lenin", "year": 1917},
    {"type": "vehicle", "title": "armored car", "person": "Vladimir Lenin", "year": 1915},
    {"type": "book", "title": "das Kapital", "person": "Karl Marx", "year": 1867},
    {"type": "vehicle", "title": "armored train", "person": "Vladimir Lenin", "year": 1912},
    {"type": "book", "title": "Selected works", "person": "Kim Il-sung", "year": 1971},
    {"type": "book", "title": "With the Century", "person": "Kim Il-sung", "year": 1992},
    {"type": "book", "title": "Selected works", "person": "Joseph Stalin", "year": 1942},
    {"type": "other", "title": "smoking pipe", "person": "Joseph Stalin", "year": 1935},
    {"type": "other", "title": "log", "person": "Vladimir Lenin", "year": 1920},
    {"type": "vehicle", "title": "personal train", "person": "Kim Il-sung", "year": 1984}]
persons_list = [
    {"name": "Kim Il-sung", "DOB": "15.04.1912", "DOD": "08.07.1994", "country": "North Korea"},
    {"name": "Vladimir Lenin", "DOB": "22.04.1870", "DOD": "21.01.1924", "country": "USSR"},
    {"name": "Karl Marx", "DOB": "05.05.1818", "DOD": "14.03.1883", "country": "Germany"},
    {"name": "Joseph Stalin", "DOB": "18.12.1878", "DOD": "05.03.1953", "country": "USSR"},
]
exhibits.insert_many(exhibits_list)
persons.insert_many(persons_list)

# 1. Добавление экспоната:
exhibits.insert_one({"type": "book", "title": "The State and Revolution", "person": "Lenin", "year": 1917})
exhibits.insert_one({"type": input("type: "), "title": input("title: "),
                      "person": input("person: "), "year": int(input("year: "))})

# 2. Удаление экспоната:
unnecessary_exhibit = {"title": "log"}
exhibits.delete_one(unnecessary_exhibit)

# 3. Редактирование информации об экспонате:
changeable_exhibit = {"title": "smoking pipe"}
new_value = {"$set": {"year": 1933}}
exhibits.update_one(changeable_exhibit, new_value)

# 4. Просмотр полной информации об экспонате:
print(exhibits.find_one({"title": "With the Century"}))

# 5. Вывод информации о всех экспонатах:
for exhibit in exhibits.find():
    print(exhibit)
    
# 6. Просмотр информации о людях, имеющих отношение к конкретному экспонату:
print(persons.find_one({"name": exhibits.find_one({"title": "armored car"}).get("person")}))

# 7. Просмотр информации об экспонатах, имеющих отношение к конкретному человеку:
for exhibit in exhibits.find({"person": "Joseph Stalin"}):
    print(exhibit)

# 8. Просмотр набора экспонатов на основе некоторого критерия:
for exhibit in exhibits.find({"type": "vehicle"}):
    print(exhibit)
    
# client.drop_database("museum")
