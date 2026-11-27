
#include "adder_wrapper.h"
#include "adder_cpp.h"

//********************************************************
//**** Wrappers for methods called by Stateflow chart ****
//********************************************************

adder *createAdder()
{
	return new adder;
}

void deleteAdder(adder *obj)
{
	delete obj;
}

double adderOutput(adder *obj, int increment)
{
	obj->add_one(increment);
	return obj->get_val();
}
