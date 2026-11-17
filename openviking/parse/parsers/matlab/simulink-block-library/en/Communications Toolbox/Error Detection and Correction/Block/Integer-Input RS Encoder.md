---
type: simulink-block
title: 'Integer-Input RS Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integerinputrsencoder'
documentation_source_path: 'ref/integerinputrsencoder.html'
language: en
---

# Integer-Input RS Encoder

## Ports
```yaml
ports:
- name: In
  summary: Message integer column vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Out
  summary: Reed-Solomon codeword integer column vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### Input

### **In** — Message integer column vector

Message, specified as one of the following:

- When there is no message shortening, a
  (*N*C×*K*)-by-1 integer column
  vector.
- When there is message shortening, a
  (*N*C×*S*)-by-1 integer column
  vector.

*N*C is the number of message words,
*K* is the **Message length K**, and *S*
is the **Shortened message length S**.

**Note**

The number of decoded message words equals the number of codewords.

For more information, see Input and Output Signal Length in RS Blocks.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Out** — Reed-Solomon codeword integer column vector

Reed-Solomon codeword, returned as an
(*N*C×(*N* – *K* +
*S* – *P*)-by-1 integer column vector.
*N*C is the number of codewords,
*N* is the **Codeword length N**, *K* is
the **Message length K**, *S* is the **Shortened
message length S**, *P* is the number of punctures per codeword.

For more information, see Input and Output Signal Length in RS Blocks.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

For more information, see Supported Data Types.
## Parameters
```yaml
parameters:
- name: Codeword length N
  summary: Codeword length 7 (default) | integer
  group: ''
- name: Message length K
  summary: Message word length 3 (default) | integer
  group: ''
- name: Shortened message length S
  summary: Shortened message word length 3 (default) | integer
  group: ''
- name: Generator polynomial
  summary: Generator polynomial rsgenpoly(7, 3, [], [], 'double') (default) | polynomial character vector | binary row vector
    | binary Galois row vector
  group: ''
- name: Primitive polynomial
  summary: Primitive polynomial 'X^3 + X + 1' (default) | polynomial character vector | binary row vector
  group: ''
- name: Puncture vector
  summary: Puncture vector [ones(2,1); zeros(2,1)] (default) | binary column vector
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Codeword length N** — Codeword length `7` (default) | integer

Codeword length, specified as an integer.

For more information, see Restrictions on M and the Codeword Length N and Input and Output Signal Length in RS Blocks.

### **Message length K** — Message word length `3` (default) | integer

Message word length, specified as an integer in the range [1, *N*–2],
where *N* is the codeword length.

### **Shortened message length S** — Shortened message word length `3` (default) | integer

Shortened message word length, specified as an integer, such that *S* ≤
*K*. When **Shortened message length S** <
**Message length K**, the Reed-Solomon code is shortened.

You still specify *N* and *K* values for the
full-length (*N*, *K*) code but the decoding is shortened to
an (*N*–*K*+*S*, *S*)
code.

#### Dependencies

To enable this parameter, select **Specify shortened message length**.

### **Generator polynomial** — Generator polynomial `rsgenpoly(7, 3, [], [], 'double')` (default) | polynomial character vector | binary row vector | binary Galois row vector

Generator polynomial with values in the range [0 to
2*M*–1], in order of descending power, specified
as one of the following:

- A polynomial character vector. For more information, see Representation of Polynomials in Communications Toolbox.
- An integer row vector that represents the coefficients of the generator polynomial in
  order of descending power.
- An integer Galois row vector that represents the coefficients of the generator
  polynomial in order of descending power.

Each coefficient is an element of the Galois field defined by the primitive
polynomial. For more information, see Specify the Generator Polynomial.

**Example:** `[1 3 1 2 3]`, which is equivalent to
`rsgenpoly(7,3)`

#### Dependencies

To enable this parameter, select **Specify generator polynomial**.

### **Primitive polynomial** — Primitive polynomial `'X^3 + X + 1'` (default) | polynomial character vector | binary row vector

Primitive polynomial in order of descending power. This polynomial is of order
*M* and defines the finite Galois field GF(2M)
corresponding to the integers that form message words and codewords. Specify the primitive
polynomial as one of the following:

- A polynomial character vector. For more information, see Representation of Polynomials in Communications Toolbox.
- A binary row vector that represents the coefficients of the generator
  polynomial.

For more information, see Specify the Primitive Polynomial.

**Example:** `'X^3 + X + 1'`, which is the primitive polynomial used for a
(7,3) code, `ppoly = primpoly(3,'nodisplay'); int2bit(ppoly,ceil(log2(max(ppoly))))'`

#### Dependencies

To enable this parameter, select **Specify primitive polynomial**.

### **Puncture vector** — Puncture vector `[ones(2,1); zeros(2,1)]` (default) | binary column vector

Puncture vector, specified as an (*N*–*K*)-by-1 binary
column vector. Element indices with `1`s represent data
*symbol* indices that pass through the block unaltered. Element indices
with `0`s represent data *symbol* indices that get
punctured, or removed, from the data stream. For more information, see Puncturing and Erasures.

**Note**

If the encoder is processing multiple codewords per frame, then the same puncture
pattern holds for all codewords.

#### Dependencies

To enable this parameter, select **Puncture
code**.
## Libraries

Communications Toolbox / Error Detection and Correction / Block

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Create Reed-Solomon code from integer vector data

The Integer-Input RS Encoder block creates a Reed-Solomon code.

The symbols for the code are integers between 0 and
2*M*-1, which represent elements of the finite field
*GF*(2*M*). The default value of
*M* is the smallest integer that is greater than or equal to
log2(*N*+1), that is, `ceil(log2(N+1))`. You can change the
default value of *M* by specifying the primitive polynomial for
*GF*(2*M*), as described in Specify the Primitive Polynomial below. Restrictions on
*M* and *N* are described in Restrictions on M and the Codeword Length N.

The input and output are integer-valued signals that represent messages and codewords,
respectively. For more information, see Input and Output Signal Length in RS Blocks.

An (*N*, *K*) Reed-Solomon code can correct up to
`floor((N-K)/2)` symbol errors (not bit errors) in each codeword.

Suppose M = 3, N = 23-1 = 7, and K = 5. Then a message is a
vector of length 5 whose entries are integers between 0 and 7. A corresponding codeword is a
vector of length 7 whose entries are integers between 0 and 7. The following figure illustrates
possible input and output signals to this block when **Codeword length N** is
set to `7`, **Message length K** is set to
`5`, and the default primitive and generator polynomials are used.
