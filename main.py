from someregistrar import SomeRegistrar


def main():
    """Register account on some cite and print it email and password"""
    email, password = SomeRegistrar.register_one()
    print(f'{email=}, {password=}')


if __name__ == '__main__':
    main()
