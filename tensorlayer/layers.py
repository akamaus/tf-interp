from tensorflow import Scope

class CommonLayer:
    def __init__(self, layer_type, args, kargs):
        self.args = args
        self.kargs = kargs
        print(layer_type, args, kargs, 'scope', Scope.get_scope())


def BatchNormLayer(*args, **kargs):
    return CommonLayer('BatchNormLayer', args, kargs)


def Conv2d(*args, **kargs):
    return CommonLayer('Conv2d', args, kargs)


def ElementwiseLayer(*args, **kargs):
    return CommonLayer('BatchNormLayer', args, kargs)


def InputLayer(*args, **kargs):
    return CommonLayer('InputLayer', args, kargs)


def SubpixelConv2d(*args, **kargs):
    return CommonLayer('Conv2d', args, kargs)

def set_name_reuse(*args):
    print("set_name_reuse", args)
