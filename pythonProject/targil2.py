def print_msg(strng, itr):
    print((strng+'\n')*itr)


message = input("please type a message:")
times = input("how many times should the message be printed? ")

if times.startswith(tuple('0123456789')):
    print_msg(message, int(times))
else:
    times = 1
    print_msg(message, times)
