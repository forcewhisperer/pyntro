

def format_file(old, new):

    original = open(old, 'r')
    formatted = open(new, 'w')

    for line in original:
        formatted.write(line.replace('\\n', "\n"))


def main():
    format_file('cert.txt', 'cert.pem')
    format_file('pk.txt', 'pk.pem')
    format_file('chain.txt', 'chain.pem')


if __name__ == '__main__':
    main()
