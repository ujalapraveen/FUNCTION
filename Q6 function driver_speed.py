def driver(speed):
    speed1=speed-70
    point=speed1//5
    if speed<=70:
        print("ok")
    elif point>12:
        print("license suspended")
    elif speed>70:
        print(point,"point")
speed =int(input("enter a speed"))
driver(speed)
