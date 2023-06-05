#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n%2!=0:
    print("Weird")
elif n%2==0 and n>2 and n<5:
    print("Not Weird")
elif n%2==0 and n>6 and n<20:
    print("Weird")
elif n%2==0 and n> 20:
    print ("Not Weird")
##The above code fails test case 7
##The code below passes all the test cases

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    oddcheck = (n % 2) != 0
    if oddcheck or (n > 100) or (n < 1) or (n >= 6 and n <= 20):
        print("Weird")
    else:
        print("Not Weird")
