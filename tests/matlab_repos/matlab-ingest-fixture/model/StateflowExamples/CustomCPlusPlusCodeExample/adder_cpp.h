/* Copyright 2003-2022 The MathWorks, Inc. */

#ifndef _ADDER_CPP_
#define _ADDER_CPP_

class adder {
private:
	int int_state;
public:
	adder();
	int add_one(int increment);
	int get_val();
};

// External declaration for class instance global storage
extern adder *adderVar;

#endif /* _ADDER_CPP_ */


