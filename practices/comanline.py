import sys #argparse

#parser = argparse.ArgumentParser(
#        prog='top',
#        description='show top lines from each file')
#parser.add_argument('filenames', nargs='+')
#parser.add_argument('-l', '--lines', type=int, default=10)
#args = parser.parse_args()
#print(args)

# total args
n = len(sys.argv)
print("Total args passed: ", n)

# args passed
print("\nName of py script: ", sys.argv[0])

print("\nArgs passed: ", end=' ')
for i in range(1, n):
    print(sys.argv[i], end=' ')

# Addition of numbers
sum = 0
# using argparse module
for i in range(1, n):
    sum += int(sys.argv[i])

print("\n\nresult: ", sum)
