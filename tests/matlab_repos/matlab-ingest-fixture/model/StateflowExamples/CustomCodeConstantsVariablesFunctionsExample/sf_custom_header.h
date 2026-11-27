#ifndef SF_CUSTOM_HEADER_H
#define SF_CUSTOM_HEADER_H
/* Include guard makes ensures that the header file is included 
   only once in the generated code. */

/* Constant definitions shared by the Stateflow chart and custom code*/

static const int LOW = -1;
static const int MEDIUM = 0;
static const int HIGH = 1;

/* extern declaration of the global variable defined in the source file 
   sf_custom_source.c */

extern int custom_var;

/* extern declaration of the custom function defined in the source file 
   sf_custom_source.c */

extern int custom_function(double var1, int var2); 

#endif /* SF_CUSTOM_HEADER_H */