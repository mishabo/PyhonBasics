# Необходимо считать любой текстовый файл на вашем ПК (можно создать новый) и
# создать на его основе новый файл, где содержимое будет записано в обратном порядке.
# В конце программы вывести на экран оба файла - старый в неизменном виде
# и новый в обратном порядке.

def print_file(f_name):
    f = open(f_name)
    data = f.readlines()
    print(f_name + ' content: ')
    print(data)


f_in = open('data.in', 'r')
lines = ''
while line := f_in.readline():
    lines += line
f_in.close

lines_length = len(lines)
lines_reverse = lines[lines_length::-1]

f_out = open('data.out', 'w')
f_out.writelines(lines_reverse)
f_out.close()

print_file('data.in')
print_file('data.out')
