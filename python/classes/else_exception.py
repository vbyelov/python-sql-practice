# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print("Division failed")
#         return None
#     else:
#         print("Everything went fine")
#         return n
#
#
# print(reciprocal(2))
# print(reciprocal(0))
def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("Division failed")
        n = None
    else:
        print("Everything went fine")
    finally:
        print("It's time to say goodbye")
        return n


print(reciprocal(2))
print(reciprocal(0))
