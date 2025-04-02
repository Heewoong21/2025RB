if __name__ == '__main__':
    print(" I am running. My nmae is ", end='')
    print(__name__)
else:
    print("I am imported. My name is ", end='')
    print(__name__)