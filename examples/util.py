import os


def os_options():
    print 'os.getcwd() = ' + os.getcwd()
    print 'os.name = ' + os.name
    print 'os.curdir = ' + os.curdir
    print 'os.environ = ' + str(os.environ)
    print 'os.getlogin() = ' + os.getlogin()


def null_safe_get():
    event = ({
            "Name": "name",
            "Info": {
                "Phone": "222-2222",
                "Address": {
                    "Street": "Main",
                    "Number": "555",
                    "Zip": "77777"
                }
            }
        })

    name = event.get('Job', {}).get('Name')

    print name


def main():
    os_options()

if __name__ == '__main__':
    main()
