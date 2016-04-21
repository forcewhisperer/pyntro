class Hello:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def hello(name):
        print "hello " + name

    def say_hello(self):
        Hello.hello(self.name)


def main():
    hello = Hello('Fran')
    hello.say_hello()

if __name__ == '__main__':
    main()
