import os

if 'SILLY' in os.environ:
    print(os.environ['SILLY'])
else:
    print("SILLY not found")

