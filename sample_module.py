def sample_function(msg: str):
    print(f'{sample_function.__name__}: {msg}')


def main():
    sample_function('Hello!')

if __name__ == '__main__':
    main()
