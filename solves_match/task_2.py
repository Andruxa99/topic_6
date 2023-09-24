a = int(input())

# match a:
#     case _ if a < 42:
#         print('Less')
#     case _ if a == 42:
#         print('The answer')
#     case _ if a > 42:
#         print('Greater')

match [a < 42, a == 42]:
    # match [False, False]:

    case [True, False]:
        print('Меньше')
    case [_, True]:
        print('Ответ')
    case [False, False]:
        print('Больше')
