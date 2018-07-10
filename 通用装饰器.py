def function(fn):
    def inner(*args, **kwargs):
        print('装饰器已经执行')
        ret = fn(*args, **kwargs)
        return ret 
    return inner
@function
def test(a, b):
    return a+b

print(test(3,2))