---
type: simulink-block
title: 'LDPC Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'ldpcencoder'
documentation_source_path: 'ref/ldpcencoder.html'
language: en
---

# LDPC Encoder

## Ports

### Input

### **In** — Input message binary column vector

Input message, specified as a *K*-by-1 column vector
containing binary-valued elements. *K* is the length of
the uncoded message.

**Data Types:** `double` | `Boolean`
### Output

### **Out** — LDPC codeword column vector

LDPC codeword, returned as an *N*-by-1 column vector.
*N* is the number of bits in the LDPC codeword. The
output signal inherits its data type from the input signal. The LDPC
codeword output is a solution to the parity-check equation. The input
message comprises the first *K* bits of the LDPC
codeword output, and the parity check comprises the remaining
(*N* – *K*) bits.

**Data Types:** `double` | `Boolean`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Parity-check matrix (sparse binary (N-K)-by-N matrix)** — Parity-check matrix `ldpcEncoderConfig().ParityCheckMatrix` (default) | sparse binary matrix | nonsparse index matrix

Parity-check matrix, specified as a sparse (*N* –
*K*)-by-*N* binary-valued matrix.
*N* is the length of the output LDPC codeword and must
be in the range (0, 231). *K* is
the length of the uncoded message and must be less than
*N*. The last (*N* – *K*)
columns in the parity-check matrix must be an invertible matrix in the
Galois field of order 2, `gf`(2).

You can also specify the parity-check matrix as a two-column nonsparse
index matrix, `I`, that defines the row and column indices
of the `1`s in the parity-check matrix such that
`sparse(I(:,1),I(:,2),1)`.

This parameter accepts numeric data types. When you set this parameter to
a sparse binary matrix, this parameter also accepts the
`Boolean` data type.

**Note**

- When the last (*N* –
  *K*) columns of the parity-check matrix
  form a triangular matrix, forward or backward substitution
  is performed to solve the parity-check equation.
- When the last (*N* –
  *K*) columns of the parity-check matrix do
  not form a triangular matrix, a matrix inversion is
  performed to solve the parity-check equation. If a large
  matrix needs to be inverted, initializations or updates take
  more time.

**Example:** `ldpcEncoderConfig().ParityCheckMatrix` configures the binary
matrix as a 108-by-648 sparse logical matrix.

## Libraries

Communications Toolbox / Error Detection and Correction / Block

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2024b: Change default parity-check matrix

With this update, the default parity-check matrix for the
LDPC Encoder block is now
`ldpcEncoderConfig().ParityCheckMatrix` instead of
`dvbs2ldpc(1/2)`.

## Description

Encode binary low-density parity-check (LDPC) code

The LDPC Encoder block applies LDPC coding to a binary input message. LDPC codes are
linear error control codes with sparse parity-check matrices and long block lengths that
can attain performance near the Shannon limit.

The input and output are discrete-time signals. The ratio of the output sample time to
the input sample time is *K/N*, where:

- *N* is the length of the received signal and must be in
  the range (0, 231).
- *K* is the length of the uncoded message and must be less
  than *N*.
