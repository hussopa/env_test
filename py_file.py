import os

if 'SILLY' in os.environ and 'LITTLE' in os.environ and "STRING" in os.environ:
    print(os.environ['SILLY'])
    print(os.environ['LITTLE'])
    print(os.environ['STRING'])
else:
    print("VARIABLES not found")

