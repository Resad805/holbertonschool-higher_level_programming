#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = (len(sys.argv)) - 1

    if args == 0:
        print('0 argument:')
    
    elif args == 1:
        print('1 argument:')
        print(f'1: {sys.argv[1]}')

    elif args > 1:
        print(f'{args} argument:')
        for i in range(0, args +1):
            print(f'{i}: {sys.argv[i]}')