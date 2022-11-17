def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*1


mygenerator = create_generator()
print(mygenerator)

for ii in mygenerator:
    print(ii)
