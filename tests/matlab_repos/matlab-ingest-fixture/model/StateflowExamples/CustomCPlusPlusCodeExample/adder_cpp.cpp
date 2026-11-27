/* Copyright 2003-2022 The MathWorks, Inc. */

#include "adder_cpp.h"

/***************************************/
/**** Class instance global storage ****/
/***************************************/

adder *adderVar;

/**********************************/
/**** Class method definitions ****/
/**********************************/

adder::adder()
{
	int_state = 0;
}

int adder::add_one(int increment)
{
	int_state += increment;
    return int_state;
}

int adder::get_val()
{
	return int_state;
}

