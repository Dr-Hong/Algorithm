count = 1
earth, sun, moon = 1, 1, 1
years = list(map(int, input().split()))

def earthCount():
    global earth
    earth += 1
    if earth == 16:
        earth = 1
    return earth

def sunCount():
    global sun
    sun += 1
    if sun == 29:
        sun = 1
    return sun

def moonCount():
    global moon
    moon += 1
    if moon == 20:
        moon = 1
    return moon

while True:
    if earth == years[0] and sun == years[1] and moon == years[2]:
        break
    else:
        earthCount()
        sunCount()
        moonCount()
        count += 1

print(count)