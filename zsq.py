def a(fn):
    def inner():
        return '<div>'+fn()+'</div>'
    return inner
def b(fn):
    def inner():
        return '<a>'+fn()+'</a>'
    return inner

@a
@b
def c():
    return 'hello 装饰器'

print(c())