# **kwargs
# *args

def typeof (*args,**kwargs):
    print(type(args))  # tuple
    print(type(kwargs)) # dict

typeof(7)


obj = {
    'name':'kevin',
    'sex':'boy',
    'age':'20',
    'height':'179cm'
}

def forObj(obj):
    for k,v in obj.items():
        print(k,':',v)

forObj(obj) 

def kwargs_(**kwargs):
    for key,v in kwargs.items():
        print(key,':',v)

kwargs_(name='kevin')