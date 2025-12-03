#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = (len(sys.argv)) - 1

    if args == 0:
        print('0 arguments')
    
    elif args == 1:
        print('1 arguments')
        print(f'1: {sys.argv[1]}')

    elif args > 1:
        print(f'{sys.argv[argv]} arguments')
        for i in range(0, args):
            print(f'{i}: {sys.argv[i]}')