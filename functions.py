def nameFunction(name):
    print(f'My name is {name}')

nameFunction('kaeneth')

def foodFunc(*args, **kwargs):
    print(kwargs['food'])
    print(f'I would like {args[1]} {kwargs['food']}')

foodFunc(20, 30, 40, animal= 'dog', food='eggs')