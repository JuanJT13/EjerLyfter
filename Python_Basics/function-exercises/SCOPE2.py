def local_scope():

    x = 10

    print(x)


local_scope()




z = 5


def change_z():

    z = 10

    print(z)


change_z()

print(z)



y = 5


def global_scope():

    global y

    y = 20

    print(y)


global_scope()

print(y)
