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
    null_safe_get()

if __name__ == '__main__':
    main()
