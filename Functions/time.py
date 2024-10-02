import datetime

now = datetime.datetime.now().hour

print(now)

if now <= 12:
    print("good Morning!")
elif now <= 18:
    print("good Afternoon")
elif now <= 20:
    print("good Night, GO TO SLEEP!!!!!!!!") 