---
type: simulink-block
title: 'S-Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunction'
documentation_source_path: 'slref/sfunction.html'
language: en
---

# S-Function

## Ports

### Input

### **In** — Signal input to an S-function block scalar | vector | matrix

You can configure input port using the `mdlInitializeSizes`
callback function. Use the `mdlInitializeSizes`
function to specify number of input ports, dimension of input signals,
sample time of each port, and if ports are direct feedthrough.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Out** — Signal output of an S-function block scalar | vector | matrix

You can configure output port using the `mdlInitializeSizes`
callback function. Use the `mdlInitializeSizes`
function to specify number of output ports, dimension of output signals,
and sample time of each port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **S-function name** — Name of the S-function `system` (default) | S-function name

Use this parameter to specify the name of your S-function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionName` |
| **Values:** | `'system'` (default) | S-function name in quotes |

### **S-function parameters** — Additional S-function parameters MATLAB expressions | comma-separated variables

Specify the additional S-function parameters.

The function parameters can be specified as MATLAB expressions or as variables separated by commas. For
example:

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

Although individual parameters can be enclosed in brackets, the list of
parameters must not be enclosed in brackets.

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `Parameters` |
| **Values:** | `''` (default) | S-function parameters in quotes |

### **S-function modules** — Additional files for code generation `''` (default) | filenames

This parameter applies only if this block represents a C MEX S-function
and you intend to use the Simulink
Coder™ software to generate code from the model containing the block.
If you use it, when you are ready to generate code, you must force the coder
to rebuild the top model as explained in Control Regeneration of Top Model Code (Simulink Coder).

For more information on using this parameter, see Specify Additional Source Files for an S-Function (Simulink Coder).

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `SFunctionModules` |
| **Values:** | `''` (default) | filenames in quotes |

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `yesa` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `yesa` |
| **Zero-Crossing Detection** | `yesa` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Actual code generation support depends on block implementation.
- S-functions that call into MATLAB are not supported for code generation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

- Actual data type support depends on block implementation.
- See Integrate External Code (Fixed-Point Designer) for details on using
  fixed-point data types in S-functions.

## Version History

**Introduced before R2006a**

## Description

Include S-function in model

The S-Function block allows you to integrate your S-function or system
function algorithms written in C, C++, or Fortran®, known as C MEX S-functions, into Simulink models. You can use the block
to implement Level-1 or Level-2 C MEX S-functions. To incorporate your S-function in a
model, after you compile your C MEX S-function:

1. Drag an S-function block from the **Simulink Library
   Browser** to your model.
2. Open up the **Block Parameters** dialog box and specify the
   S-function name at the **S-function name** field to provide
   functionality for the S-function block. For example, type
   `timestwo` and select **Apply**.

An *S-function* is a computer language description of a Simulink® block written in MATLAB®, C, C++, or Fortran. If you have C, C++, or Fortran S-functions, they need to be compiled as MEX files using the
`mex` utility (see Build C MEX Function). S-functions
define how a block works during different parts of simulation, such as initialization,
update, derivatives, outputs and termination. S-functions use a special calling syntax
called the S-function API that enables you to interact with the Simulink engine. This interaction is very similar to the interaction that takes
place between the engine and built-in Simulink blocks. In every step of a simulation, a method is invoked by the
simulation engine to fulfill a specific task.

For example, below is an example of a simple C MEX S-function called
`timestwo.c` that outputs twice its input.

```
#define S_FUNCTION_NAME timestwo /* Specifies the name of the S-function (timestwo) */
#define S_FUNCTION_LEVEL 2 /* Specifies that the S-function is in the Level 2 format */

#include "simstruc.h" /* Defines the data structure */
static void mdlInitializeSizes(SimStruct *S) /* Initialize the input and output ports and their size */
{
    ssSetNumSFcnParams(S, 0);
    if (ssGetNumSFcnParams(S) != ssGetSFcnParamsCount(S)) {
        return; /* Parameter mismatch reported by the Simulink engine*/
    }

    if (!ssSetNumInputPorts(S, 1)) return;
    ssSetInputPortWidth(S, 0, DYNAMICALLY_SIZED);
    ssSetInputPortDirectFeedThrough(S, 0, 1);

    if (!ssSetNumOutputPorts(S,1)) return;
    ssSetOutputPortWidth(S, 0, DYNAMICALLY_SIZED);

    ssSetNumSampleTimes(S, 1);

    /* Take care when specifying exception free code - see sfuntmpl.doc */
    ssSetOptions(S, SS_OPTION_EXCEPTION_FREE_CODE);
    }
static void mdlInitializeSampleTimes(SimStruct *S) /* Set the sample time of the S-function as inherited */
{
    ssSetSampleTime(S, 0, INHERITED_SAMPLE_TIME);
    ssSetOffsetTime(S, 0, 0.0);
}
static void mdlOutputs(SimStruct *S, int_T tid) /* Calculate the block output for each time step */
{
    int_T i;
    InputRealPtrsType uPtrs = ssGetInputPortRealSignalPtrs(S,0);
    real_T *y = ssGetOutputPortRealSignal(S,0);
    int_T width = ssGetOutputPortWidth(S,0);

    for (i=0; i<width; i++) {
        *y++ = 2.0 *(*uPtrs[i]);
    }
}
static void mdlTerminate(SimStruct *S){} /* Perform tasks at the end of the simulation */

#ifdef MATLAB_MEX_FILE /* Is this file being compiled as a MEX-file? */
#include "simulink.c" /* MEX-file interface mechanism */
#else
#include "cg_sfun.h" /* Code generation registration function */
#endif
```

S-functions follow a general form and can accommodate continuous, discrete, and hybrid
systems. You can implement an algorithm in an S-function and use the S-Function block to
add it to a Simulink model. After you write your S-function and place its name in an S-Function
block (available in the User-Defined Functions block library), you can customize the
user interface using masking. In this example, the `timestwo.c`
function is compiled using `mex timestwo.c`, and it is implemented
using the S-Function block.

Timestwo S-function is implemented using the S-Function block. The input to the block is a sine wave and the output of the block is connected to a Scope block.

The S-Function block displays the name of the specified S-function and
the number of input and output ports specified by the S-function. Signals connected to
the inputs must have the dimensions specified by the S-function for the inputs.

**Note**

Use the Level-2 MATLAB S-Function block to
include a Level-2 MATLAB S-function in a
block diagram.
