---
type: simulink-block
title: 'PS Math Function'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Functions'
documentation_page: 'psmathfunction'
documentation_source_path: 'ref/psmathfunction.html'
language: en
---

# PS Math Function

## Ports

### Input

### **I** — Input physical signal, *u*, untyped physical signal

Input port for the operand physical signal, *u*.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

## Parameters

### **Function choice** — Function to perform on the operand signal `sin(u)` (default) | `cos(u)` | `exp(u)` | `log(u)` | `10.^u` | `log10(u)` | `u.^2` | `sqrt(u)` | `1./u` | `tanh(u)` | `u.^v`

Select the function to perform. The block output is the result of the operation of
the function on the value and unit of the input signal.

### **v** — Power `1` (default) | scalar, vector, or matrix

For the `u.^v` option, the value of the output signal is
the value of the input signal, *`u`*, to the power of
**v**. If **v** is a vector or matrix, its size must
match the size of the input signal, *`u`*, or
*`u`* must be a scalar.

The unit of the output signal is the result of the operation of the function on the
input signal unit. Therefore, unless the input signal is unitless, changing the value of
**v** changes the unit of the output signal.

#### Dependencies

To enable this parameter, set **Function choice** to
`u.^v`.

## Libraries

Simscape / Foundation Library / Physical Signals / Functions

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Apply mathematical function to input physical signal

The PS Math Function block applies a mathematical function
to the value and unit of the input physical signal, *u*. The block output is
the result of the operation of the function on the input. You can select one of the following
functions from the **Function choice** parameter list.

| Function | Description | Mathematical Expression |
| --- | --- | --- |
| `sin(u)` | Sine | sin(*u*) |
| `cos(u)` | Cosine | cos(*u*) |
| `exp(u)` | Exponential | e*u* |
| `log(u)` | Natural logarithm | ln(*u*) |
| `10.^u` | Power of base 10 | 10*u* |
| `log10(u)` | Common (base 10) logarithm | log(*u*) |
| `u.^2` | Power 2 | *u*2 |
| `sqrt(u)` | Square root | *u*0.5 |
| `1./u` | Reciprocal | 1/*u* |
| `tanh(u)` | Hyperbolic tangent | tanh(*u*) |
| `u.^v` | Power | *u**v* |

The PS Math Function block issues a simulation-time error
when the input falls out of the expected domain for the particular function used. For example,
if set to `sqrt(u)`, the PS Math
Function block issues an error if it receives negative input during
simulation.

**Note**

For `u.^2`, `sqrt(u)`,
`1./u`, and `u.^v` the unit of the
output signal is the result of the operation of the function on the input signal unit. Thus
for `u.^v`, unless the input signal is unitless, changing the value
of **v** changes the unit of the output signal. For all other functions in
the list, the input signal must be unitless.
