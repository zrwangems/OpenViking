---
type: simulink-block
title: 'J-K Flip-Flop'
family: 'simulink-extras'
product_id: 'simulink-extras'
product_name: 'Simulink Extras'
documentation_release: R2025b
official_category: 'Flip Flops'
documentation_page: 'jkflipflop'
documentation_source_path: '../simulink/ref_extras/jkflipflop.html'
language: en
---

# J-K Flip-Flop

## Ports
```yaml
ports:
- name: J
  summary: Input signal J scalar
  direction: input
  data_types: double | Boolean
- name: CLK
  summary: Clock signal scalar
  direction: input
  data_types: double | Boolean
- name: K
  summary: Input signal K scalar
  direction: input
  data_types: double | Boolean
- name: Q
  summary: Output signal Q scalar
  direction: output
  data_types: double | Boolean
- name: '!Q'
  summary: Output signal !Q scalar
  direction: output
  data_types: double | Boolean
```

### Input

### **J** — Input signal J scalar

Input signal **J** specified as a scalar, vector, or
matrix.

#### Dependencies

The data types that the J-K Flip-Flop block accepts depend on the
setting of the **Implement logic signals as boolean data
(vs. double)** configuration parameter:

- `On` — J-K Flip-Flop block
  accepts only real scalar signals of type
  `boolean`.
- `Off` — J-K Flip-Flop
  block accepts real scalar signals of type
  `boolean` or `double`
  (both inputs must have the same type).

**Data Types:** `double` | `Boolean`

### **CLK** — Clock signal scalar

Clock signal, specified as a scalar, vector, or matrix.

#### Dependencies

The data types that the J-K Flip-Flop block accepts depend on the
setting of the **Implement logic signals as boolean data
(vs. double)** configuration parameter:

- `On` — J-K Flip-Flop block
  accepts only real scalar signals of type
  `boolean`
- `Off` — J-K Flip-Flop
  block accepts real scalar signals of type
  `boolean` or `double`
  (both inputs must have the same type).

**Data Types:** `double` | `Boolean`

### **K** — Input signal K scalar

Input signal **K** specified as a scalar, vector, or matrix.

#### Dependencies

The data types that the J-K Flip-Flop block accepts depend on the
setting of the **Implement logic signals as boolean data
(vs. double)** configuration parameter:

- `On` — J-K Flip-Flop block
  accepts only real scalar signals of type
  `boolean`
- `Off` — J-K Flip-Flop
  block accepts real scalar signals of type
  `boolean` or `double`
  (both inputs must have the same type).

**Data Types:** `double` | `Boolean`
### Output

### **Q** — Output signal Q scalar

Output signal **!Q**, with the same dimensions and
data type as the input.

**Data Types:** `double` | `Boolean`

### **!Q** — Output signal !Q scalar

Output signal **!Q**, with the same dimensions and
data type as the input.

**Data Types:** `double` | `Boolean`
## Parameters
```yaml
parameters:
- name: Initial condition (state of Q)
  summary: Initial value of output Q 0 (default) | scalar
  group: ''
  block_parameter: initial_condition
  type: character vector
  values: scalar
  default: '''0'''
```

### **Initial condition (state of Q)** — Initial value of output Q `0` (default) | scalar

Specify the initial value of the output **Q**. A nonzero
value is treated as true (`1`).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `initial_condition` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'0'` |
## Libraries

Simulink Extras / Flip Flops

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2008b**

## Description

Model a negative-edge-triggered J-K flip-flop

The J-K Flip-Flop block models a negative-edge-triggered J-K flip-flop. The
J-K flip-flop block has three inputs, **J**,
**K**, and **CLK**. On the negative (falling) edge
of the clock signal (**CLK**), the J-K Flip-Flop block
outputs **Q** and its complement, **!Q**, according to
the following truth table. In this truth table,
**Q**n-1 is the output at the previous time
step.

**Note**

The J-K Flip-Flop block treats a nonzero input as true
(`1`).

| J | K | Q n | !Q n |
| --- | --- | --- | --- |
| 0 | 0 | Q n-1 | !Q n-1 |
| 0 | 1 | 0 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | !Q n-1 | Q n-1 |

When **J** is 1 and **K** is 0, the flip-flop goes to the
set state (**Q**n is 1). When
**J** is 0 and **K** is 1, the flip-flop goes to
the reset state (**Q**n is 0). When both
**J** and **K** are 0, the flip-flop stays in the
previous state (**Q**n is
**Q**n-1). When both **J**
and **K** are 1, the flip-flop toggles
(**Q**n is the complement of
**Q**n-1).

### Logic Signals as Boolean or Double Data Types

The **Implement logic signals as boolean data (vs. double)** configuration
parameter setting affects the input and output data types of the J-K
Flip-Flop block because this block is a masked subsystem that uses the
Combinatorial Logic block. For more
information about this configuration parameter, see Implement logic signals as Boolean data (vs. double).
