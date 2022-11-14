

xmen_file = open('D:/DevOps_2022/Texts/xmen.txt')

new_xmen = open('D:/DevOps_2022/Texts/new_xmen.txt', 'r+')

new_xmen.write(xmen_file.read())

new_xmen.close()

new_xmen = open('D:/DevOps_2022/Texts/new_xmen.txt', 'r')

print(new_xmen.read())
