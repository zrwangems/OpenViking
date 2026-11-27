#include "sf_custom_header.h"

/* Definition of the global variable */

int custom_var = 0;

/* Definition of the custom function */

int custom_function(double var1, int var2)
{
    if(var1 > var2 + custom_var) {
        return(HIGH);
    }else if(var1 < var2 - custom_var) {
        return(LOW);
    }
    return(MEDIUM);
}
