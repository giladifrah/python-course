import linecache


def check_avilable(day_avilable, names):
    day_success = []
    c = len(day_avilable)
    length1 = len(day_avilable)
    print("length1 = ", length1)
    while (c >= len(names)):
        print("#################################################################")
        print("day avilable =", day_avilable)
        print("end_success at start = ", end_success)
        flag2 = 1  # כדי לשמור את הערך של FIRST פעם אחת בארגומנט גם אחרי שהסרנו אותו
        name_count = []
        day_equal = []
        i = 0
        length1 = len(day_avilable)
        while (int(length1) != i):
            print("=====================")
            if (flag2 == 1):  # מאכלס פעם 1 את האיבר שאנחנו משתמשים בו בארגומנט
                argument = day_avilable[0]
                print("argument = ", argument)
                flag2 = 0
                day_avilable.pop(0)  # pop the first argument
                length1 = length1 - 1
                print("length1 = ", length1)
                print("i = ", i)
                name_count.append(argument[0])
            if (day_avilable != []):
                print("day runninng = ", day_avilable[i])
                if (argument == day_avilable[i]):  # all arguments equal pop the argument
                    print("all the same poping =", day_avilable[i])
                    day_avilable.pop(i)
                    length1 = length1 - 1
                    print("length1 =", length1)
                    print("i = ", i)
                elif day_avilable[i][1] == argument[1] and day_avilable[i][2] == argument[2]:  # only day,hour equal
                    add = [day_avilable[i][1], day_avilable[i][2]]  # add = day,hour that equal to first argument
                    print("same -->success")
                    print("day_equal=", day_equal)
                    if add not in day_equal:
                        day_equal.append(add)
                    if day_avilable[i][0] not in name_count:
                        name_count.append(day_avilable[i][0])
                        print("name count = ", name_count)
                    day_avilable.pop(i)
                    length1 = length1 - 1
                else:
                    print("not the same")
                    print("i = ", i)
                    print("length1 = ", length1)
                    i += 1

        if len(name_count) == len(names):
            day_success.append(day_equal)
        print("name_count= ", name_count)
        print("names = ", names)
        print("end day avilable=", day_avilable)
        print("day success = ", day_success)
        yard = []
        print("**********************")
        print(len(day_equal))
        if day_success != []:
            while (len(day_success) > 0):
                    for x in yard_avilable:
                        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                        print("day success = ,", day_success)
                        print("x = ", x)
                        yard = [x[1], x[2]]
                        print("yard = ", yard)
                        if day_success != [[]] and yard == day_success[0][0]:
                            print("day and yard equal possible to meet at this day")
                            print(x)
                            end_success.append(x)
                            print("end success = !! ", end_success)
                        else:
                            print("yard day/hour not the same = ", x)
                    day_success.pop(0)
        else:
            print("day_success is empty")
        print("&&&&&&&&&&&&&&&")
        print("end success = ", end_success)
        c=c-1
    print("!@# = ", end_success)
    return (end_success)


with open("log.txt", "a") as myfile:
    myfile.write("\nFinish_Sample: I can do Finish at 11:00")

with open('log.txt', 'r', encoding='utf-8') as file:
    line_count = len(file.readlines())
    print(line_count)
    day_avilable = []
    yard_avilable = []
    end_success = []
    names = []
    start_block = 0
    end_block = 0
    for x in range(1, line_count + 1):
            print("first names", names)
            line_block=list(linecache.getline('log.txt ', x).split())
            if line_block != []:
                print("name11=",line_block[0])
                if line_block[0] not in names:
                    names.append(str(line_block[0]))
                    print("names = ", names)
                if line_block[1] == "I":
                    if start_block == 2:
                        start_block = 1
                        end_block = 0
                        print("^^%%^^ = ", day_avilable)
                        print("^^%%^^ = ", yard_avilable)
                        end_success = check_avilable(day_avilable,names)
                        day_avilable = []
                        yard_avilable = []
                        names = []
                        if line_block[0] not in names:
                            names.append(str(line_block[0]))
                            print("names = ", names)
                        print("new block starting , start_block = ", start_block)
                    elif start_block == 0:
                            start_block=1
                    combaind_days = [str(line_block[0]), str(line_block[4]), line_block[6]]
                    day_avilable.append(combaind_days)
                    print("$$day$$ = ", day_avilable)
                    print("Names + Day + Hour , start block = ", start_block)
                if line_block[1] == "My":
                    combaind_yard = [str(line_block[0]), str(line_block[5]), line_block[7]]
                    yard_avilable.append(combaind_yard)
                    print("$$yard$$ = ",yard_avilable)
                    if start_block == 1:
                        start_block = 2
                    print("Yard checking , start block = ", start_block)

print("names end =", names)
print("All the possible days to meet = ", end_success)
