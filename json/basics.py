import json

data = {
    'username': 'Rob',
    'password': 'test',
    'crack': 1
}

def main():
    print('--------------')
    x = json.dumps(data)
    print(x)

if __name__ == '__main__':
    main()