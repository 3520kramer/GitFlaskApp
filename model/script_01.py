'''
def makebold(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            return "<b>" + fn(*args, **kwargs) + "</b>"
        return wrapped

    def makeitalic(fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            return "<i>" + fn(*args, **kwargs) + "</i>"
        return wrapped

    @makebold
    @makeitalic
    def hello():
        return "hello world"
'''

def makebold(func):
    def wrapped(*args):
        return '13', func(*args)
    return wrapped

def makeitalic(func):
    def wrapped(*args):
        return '12', func(*args)
    return wrapped

@makebold

def hello():
    print('yes')

    
