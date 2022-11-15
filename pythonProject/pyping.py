import sys
import os

print(f"First Argument: {sys.argv[0]}")
list_of_host = sys.argv[1:]
print(list_of_host)


for h in list_of_host:
    print(f"ping {h}")
    print(os.system("ping -c 1 " + h))
