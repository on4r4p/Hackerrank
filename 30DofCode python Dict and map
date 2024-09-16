n = int(input())
phoneBook = {}

for i in range(n):
    name, number = input().split(" ")
    phoneBook[name.lower()] = number

for _ in phoneBook:
    try:
        search_name = input()
        if search_name.lower() in phoneBook:
            print(f"{search_name.lower()}={phoneBook[search_name.lower()]}")
        else:
            print("Not found")
    except:
        break
