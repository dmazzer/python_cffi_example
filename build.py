from cffi import FFI
import os
ffibuilder = FFI()

PATH = os.path.dirname(__file__)

ffibuilder.cdef("""
#define CONST   1
int plus_one(int a);
extern "Python" int py_func(float);
void set_callback(int (*func)(float));
""")

ffibuilder.set_source("_cprog",
"""
     #include "cprog.h"
""",
     libraries=['m',],
     sources=['cprog.c',])


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)