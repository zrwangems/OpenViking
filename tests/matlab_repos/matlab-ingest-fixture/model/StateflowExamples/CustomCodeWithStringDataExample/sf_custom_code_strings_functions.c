#include "sf_custom_code_strings_functions.h"

extern void searchfun(int* nout, char* strin)
{
    nout[0] = strspn(strin,"0");
    nout[1] = strcspn(strin,".e");
    nout[2] = strcspn(strin,"e");
    nout[3] = strlen(strin);
}

extern void mergefun(char* strout, char* strin, int in0, double in1, double in2) 
{
    sprintf(strout, "%s means %1.*f times ten to the %dth power", strin, in0, in1, (int) in2);
}
