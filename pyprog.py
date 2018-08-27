import cffi
import _cprog


@_cprog.ffi.def_extern()
def py_func(float_n):
    print("call from py_func: " + str(float_n))
    return int(float_n+1)


r = _cprog.lib.plus_one(_cprog.ffi.cast("int",3))
print(r)

r = _cprog.lib.py_func
_cprog.lib.set_callback(r)

