from easydict import EasyDict

def random_normal_initializer(*args, **kargs):
    return ("rni", args, kargs)


class Scope:
    cur_scope = []

    @classmethod
    def get_scope(cls):
        return cls.cur_scope[-1].scope

    def __init__(self, subscope, reuse=None):
        if len(self.cur_scope) > 0:
            self.scope = self.cur_scope[-1].scope + [subscope]
        else:
            self.scope = [subscope]
        print('init', subscope)

    def __enter__(self):
        self.cur_scope.append(self)
        print('entered', self.get_scope())
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exited', self.get_scope())
        self.cur_scope.pop()


nn = EasyDict({'relu': 'relu','tanh': 'tanh'})

add = 'add!'

variable_scope = Scope
