#file: main.py
import pymath

def main():

    #add_float
    print "add_float( 5.3, 4.7 )"
    print pymath.add_float( 3.3, 4.7 )

    #add_int
    print "add_int( 3, 4 )"
    print pymath.add_int( 3, 4 )

    #add_float_ref
    print "add_float_ref( 3.5, 4.5 )"
    print pymath.add_float_ref( 3.5, 4.5 )

    #add_int_ref
    print "add_int_ref( 2, 10 )"
    print pymath.add_int_ref( 2, 10 )

    #add_int_array add n first integers
    int_array_a = [1,2,3,4,5]
    int_array_b = [3,4,5,6,7]
    n = 4
    print "add_int_array( a, b, n)"
    print pymath.add_int_array( int_array_a, int_array_b, n )

    #dot_product
    int_array_a = [1,2,3,4,5]
    int_array_b = [3,4,5,6,7]
    n = 3
    print "dot_product( a, b, n)"
    print pymath.dot_product( int_array_a, int_array_b, n )

if __name__ == "__main__":
    main()
