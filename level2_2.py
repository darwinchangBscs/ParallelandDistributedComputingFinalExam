
firstside = int(input("Input First Side: "))
secondside = int(input("Input Second Side: "))
thirdside = int(input("Input Third Side: "))

if firstside*firstside+secondside*secondside==thirdside*thirdside or firstside*firstside+thirdside*thirdside==secondside*secondside or thirdside*thirdside+secondside*secondside==firstside*firstside:
    print("Triangle is Right!")
else:
    print("Triangle is Not Right!")