# kwargs

obj = {
    'name':'kevin',
    'age':'20',
    'sxe':'boy',
}

def forObj (obj):
    for k,v in obj.items():
        print(k,':',v)

# forObj(obj)


def kwarg (**kwargs):
    for key,value in kwargs.items():
        print(key,':',value)

kwarg(name='kevin',age='20')


