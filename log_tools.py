from datetime import datetime

def logger(func):
    print('Logger on')

    def new_func(*args, **kwargs):
        start = datetime.now()
        name = func.__name__
        arguments = (args,kwargs)
        result = func(*args, **kwargs)
        with open('log.txt', 'a') as f:
            print(f'{start},{name = },{arguments = },{result = }',end='\n', file=f)
        return result

    print('Logger off')
    return new_func