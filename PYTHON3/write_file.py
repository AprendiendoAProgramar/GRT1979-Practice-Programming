# numbers = [1, 2, 3]
# file = open("file_write.txt", 'w')
# for item in numbers:
#     file.write(str(item)+'\n')
# file.close()


temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
file = open("file_temp_write.txt", 'w')
for t in temperatures:
    if t >= -273.15:
        file.write(str(c_to_f(t))+'\n')

file.close()
