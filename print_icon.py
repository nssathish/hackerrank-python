#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((" " * (thickness // 2)) + (c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*3))

#Middle Belt
for i in range((thickness+1)//2):
    print((" " * (thickness // 2)) + (c*thickness*5).ljust(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((" " * (thickness // 2)) + (c*thickness).ljust(thickness*2)+(c*thickness).rjust(thickness*3))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust((thickness * 5)-1)+c+(c*(thickness-i-1)).rjust(thickness-i-1)).ljust(thickness*6))

