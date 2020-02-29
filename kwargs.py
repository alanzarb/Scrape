""" Pass **kwargs to a function.
    Iterate through the args
    """


def greet_me(**kwargs):
    # print(kwargs)
    print(len(kwargs))
    # if kwargs is not None:
    print(f"kwargs len is  {len(kwargs.items())}")
    for key, value in kwargs.items():
        print(f"Key: {key}  \tValue: {value} ")


greet_me(aa="AAA",
         bb="BBBB",
         cc="CCCC",
         bob="Robert",
         k456="Fourhundred",
         m23="MMM23")

greet_me()