---
type: simulink-block
title: 'Quantizer'
family: 'simulink-extras'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'quantizer'
documentation_source_path: '../simulink/slref/quantizer.html'
language: en
---

# Quantizer

## Ports

### Input

### **Port\_1** — Input signal to quantize scalar | vector

Input signal to the quantization algorithm.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Quantized output signal scalar | vector

Output signal composed of discrete values, quantized with a
round-to-nearest
approach:

```
y = q * round(u/q)
```

where `y` is the output, `u` is the
input, and `q` is the **Quantization
interval**.

**Data Types:** `single` | `double`

## Parameters

### **Quantization interval** — Interval that defines quantization levels for the output signal `0.5` (default) | scalar | vector

Specify the quantization interval used in the algorithm. Quantization
levels for the Quantizer block output are integer multiples
of the **Quantization interval**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `QuantizationInterval` |
| **Type**: character vector |
| **Value**: Any real or complex value |
| **Default**: `'0.5'` |

### **Treat as gain when linearizing** — Specify the gain value `on` (default) | `off`

The linearization commands in Simulink® software treat this block as a gain in state space. Select this parameter
to cause the commands to treat the gain as 1. Clear this parameter to have the commands
treat the gain as 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearizeAsGain` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

## Libraries

Simulink / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Discretize input at given interval

The Quantizer block discretizes the input signal using a quantization
algorithm. The block uses a round-to-nearest method to map signal values to quantized
values at the output that are defined by the **Quantization interval**.
A smooth input signal can take on a stair-step shape after quantization.

This equation mathematically describes the round-to-nearest method:

```
y = q * round(u/q)
```

where `y` is the quantized output, `u` is the input, and
`q` is the **Quantization interval**.
