#include <stdio.h>
#include <string.h>
#include "cprog.h"

int (*python_function)(float float_n);

int main ( int argc, char *argv[] )
{
    printf("call from main\n");
 
    return 0;
}

int plus_one(int a)
{
    printf("call plus_one\n");
    return a+(1*CONST);
}

void set_callback(int (*func)(float))
{
    python_function = func;
    printf("calling py func\n");
    python_function(1.3);
}

