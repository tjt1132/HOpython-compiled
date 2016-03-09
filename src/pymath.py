# file: pymath.py

import ctypes as C

__CLIB = C.CDLL('./libmath.so')
__CLIB.add_float.argtypes = [ C.c_float, C.c_float ]
__CLIB.add_float.restype = C.c_float
__CLIB.add_int.argtypes = [ C.c_int, C.c_int ]
__CLIB.add_int.restype = C.c_int
__CLIB.dot_product.restype = C.c_float


'''
add_two.c
'''
def add_float( float_a, float_b ):
    return __CLIB.add_float( float_a, float_b)

def add_int( int_a, int_b ):
    return __CLIB.add_int( int_a, int_b )

def add_float_ref( float_a, float_b ):
    float_res = C.c_float()

    __CLIB.add_float_ref( C.byref(C.c_float(float_a)),
                          C.byref(C.c_float(float_b)),
                          C.byref(float_res) )

    return float_res.value

def add_int_ref( int_a, int_b ):
    int_res = C.c_int()

    __CLIB.add_int_ref( C.byref(C.c_int(int_a)),
                        C.byref(C.c_int(int_b)),
                        C.byref(int_res) )

    return int_res.value

'''
arrays.c
'''
def add_int_array( array_a, array_b, n ):
    c_int_array_a = ( C.c_int * n ) (*tuple( array_a[:n] ))
    c_int_array_b = ( C.c_int * n ) (*tuple( array_b[:n] ))
    c_int_array_res = ( C.c_int * n ) ()
    __CLIB.add_int_array( C.byref(c_int_array_a),
                          C.byref(c_int_array_b),
                          C.byref(c_int_array_res),
                          C.c_int(n))

    return [c_int_array_res[i] for i in range(n)]

def dot_product( array_a, array_b, n ):
    c_int_array_a = ( C.c_float * n ) (*tuple( array_a[:n] ))
    c_int_array_b = ( C.c_float * n ) (*tuple( array_b[:n] ))

    return __CLIB.dot_product( C.byref(c_int_array_a),
                               C.byref(c_int_array_b),
                               C.c_int(n))
