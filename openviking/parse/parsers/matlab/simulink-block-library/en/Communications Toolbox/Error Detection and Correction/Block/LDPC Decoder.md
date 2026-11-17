---
type: simulink-block
title: 'LDPC Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'ldpcdecoder'
documentation_source_path: 'ref/ldpcdecoder.html'
language: en
---

# LDPC Decoder

## Ports
```yaml
ports:
- name: In
  summary: Log-likelihood ratios column vector
  direction: input
  data_types: double
- name: Out
  summary: Decoded data column vector
  direction: output
  data_types: double | Boolean
- name: Iter
  summary: Number of executed decoding iterations positive integer
  direction: output
  data_types: double
- name: ParChk
  summary: Final parity checks column vector
  direction: output
```

### Input

### **In** — Log-likelihood ratios column vector

Log-likelihood ratios, specified as an *N*-by-1
column vector containing the soft-decision output from demodulation.
*N* is the number of bits in the LDPC codeword
before modulation. Each element is the log-likelihood ratio for a
received bit and the value is more likely to be `0` if
the log-likelihood ratio is positive. The first *K*
elements correspond to the information-part of the input message.

**Data Types:** `double`
### Output

### **Out** — Decoded data column vector

Decoded data, returned as a column vector. The **Decision
type** parameter specifies whether the block outputs hard
decisions or soft decisions (log-likelihood ratios).

- If the **Output format** parameter is set
  to `Information part`, the output includes
  only the information-part of the received codeword.
- If the **Output format** parameter is set
  to `Whole codeword`, the output includes
  the whole log-likelihood ratio vector.

**Data Types:** `double` | `Boolean`

### **Iter** — Number of executed decoding iterations positive integer

Number of executed decoding iterations, returned as a positive
integer.

#### Dependencies

To enable this port, select the **Output number of
iterations executed** parameter.

**Data Types:** `double`

### **ParChk** — Final parity checks column vector

Final parity checks after decoding the input LDPC code, returned as an
(*N*-*K*)-by-1 column vector.
*N* is the number of bits in the LDPC codeword
before modulation. *K* is the length of the uncoded
message.

#### Dependencies

To enable this port, select the **Output final parity
checks** parameter.
## Parameters
```yaml
parameters:
- name: Parity-check matrix (sparse binary (N-K)-by-N matrix)
  summary: Parity-check matrix ldpcDecoderConfig().ParityCheckMatrix (default) | sparse binary matrix | nonsparse index matrix
  group: ''
- name: Output format
  summary: Output value format Information part (default) | Whole codeword
  group: ''
- name: Decision type
  summary: Decision method Hard decision (default) | Soft decision
  group: ''
- name: Output data type
  summary: Output value data type double (default) | boolean
  group: ''
- name: Number of iterations
  summary: Maximum number of decoding iterations 50 (default) | positive integer
  group: ''
- name: Stop iterating when all parity-checks are satisfied
  summary: Condition for iteration termination off (default) | on
  group: ''
- name: Output number of iterations executed
  summary: Output number of iterations executed off (default) | on
  group: ''
- name: Output final parity-checks
  summary: Output number of iterations executed off (default) | on
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Parity-check matrix (sparse binary (N-K)-by-N matrix)** — Parity-check matrix `ldpcDecoderConfig().ParityCheckMatrix` (default) | sparse binary matrix | nonsparse index matrix

Parity-check matrix, specified as a sparse (*N* –
*K*)-by-*N* binary-valued matrix.
*N* is the length of the received signal and must be in
the range (0, 231). *K* is the
length of the uncoded message and must be less than *N*.
The last (*N* – *K*) columns in the
parity-check matrix must be an invertible matrix in the Galois field of
order 2, `gf`(2).

You can also specify the parity-check matrix as a two-column nonsparse
index matrix, `I`, that defines the row and column indices
of the `1`s in the parity-check matrix such that
`sparse(I(:,1),I(:,2),1)`.

This parameter accepts numeric data types. When you set this parameter to
a sparse binary matrix, this parameter also accepts the
`Boolean` data type.

**Example:** `ldpcDecoderConfig().ParityCheckMatrix` configures the binary
matrix as a 108-by-648 sparse logical matrix.

### **Output format** — Output value format `Information part` (default) | `Whole codeword`

Output value format, specified as one of these values:

- `Information part` — The block
  outputs a *K*-by-1 column vector containing
  only the information-part of the received log-likelihood ratio
  vector. *K* is the length of the uncoded
  message.
- `Whole codeword` — The block outputs
  an *N*-by-1 column vector containing the whole
  log-likelihood ratio vector. *N* is the length
  of the received signal.

  *N* and *K* must align with
  the dimension of the
  (*N*–*K*)-by-*K*
  parity-check matrix.

### **Decision type** — Decision method `Hard decision` (default) | `Soft decision`

Decision method used for decoding, specified as one of these values:

- `Hard decision` — The block outputs
  decoded data of data type `double` or
  `boolean`. Specify this data type using the
  **Output data type** parameter.
- `Soft decision` — The block outputs
  log-likelihood ratios of data type
  `double`.

### **Output data type** — Output value data type `double` (default) | `boolean`

Output value data type, specified as `double` or
`boolean`.

#### Dependencies

To enable this parameter, set the **Decision type**
parameter to `Hard decision`.

### **Number of iterations** — Maximum number of decoding iterations `50` (default) | positive integer

Maximum number of decoding iterations, specified as a positive
integer.

### **Stop iterating when all parity-checks are satisfied** — Condition for iteration termination `off` (default) | `on`

Select this parameter to terminate decoding after all parity checks are
satisfied. If not all parity checks are satisfied, decoding terminates after
the number of iterations specified by the **Number of
iterations** parameter.

### **Output number of iterations executed** — Output number of iterations executed `off` (default) | `on`

Select this parameter to enable the **Iter** output
port.

### **Output final parity-checks** — Output number of iterations executed `off` (default) | `on`

Select this parameter to enable the **ParChk** output
port.
## Libraries

Communications Toolbox / Error Detection and Correction / Block

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2024b: Change default parity-check matrix

With this update, the default parity-check matrix for the
LDPC Decoder block is now
`ldpcDecoderConfig().ParityCheckMatrix` instead of
`dvbs2ldpc(1/2)`.

## Description

Decode binary low-density parity-check (LDPC) code

The LDPC Decoder block uses the belief propagation algorithm to decode a binary LDPC
code, which is input to the block as the soft-decision output (log-likelihood ratio of
received bits) from demodulation. The block decodes generic binary LDPC codes where no
patterns in the parity-check matrix are assumed. For more information, see Belief Propagation Decoding.

The input and output are discrete-time signals. The ratio of the output sample time to
the input sample time is:

- *N/K* when only the information-part of the codeword is
  decoded
- 1 when the entire codeword is decoded

*N* is the length of the received signal and must be in
the range (0, 231). *K* is the length of the
uncoded message and must be less than *N*.

This icon shows all ports, including optional ports, for the LDPC Decoder block.
