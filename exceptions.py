# from math import tan, radians
# angle = int(input('Enter integral angle in degrees: '))
#
# # We must be sure that angle != 90 + k * 180
# assert angle % 180 != 90
# print(tan(radians(angle)))



list = [1, 2, 3, 4, 5]
indx = 0
flag = True

while flag:
    try:
        print(list[indx])
        indx += 1
    except IndexError:
        flag = False

print("Out of loop")
