---
type: simulink-block
title: 'Uniform Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'uniformdecoder'
documentation_source_path: 'ref/uniformdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Uniform Decoder

## 端口
```yaml
ports:
- name: Input
  summary: 输入向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64
- name: Output
  summary: 解码输出向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Input** — 输入向量 | 矩阵

指定要解码的整数输入，形式为向量或矩阵。

复数输入的实部和虚部独立回绕。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**复数支持：** 是
### 输出

### **Output** — 解码输出向量 | 矩阵

解码后的浮点输出，以向量或矩阵形式返回。

有关该模块如何计算输出的详细信息，请参阅算法。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Peak
  summary: 编码输入中的最大幅度 1 （默认） | 非负标量
  group: ''
- name: Bits
  summary: 位数 3 （默认） | 范围为 [2, 32] 的整数
  group: ''
- name: Overflow mode
  summary: 溢出模式 Saturate （默认） | Wrap
  group: ''
- name: Output type
  summary: 输出数据类型 Double （默认） | Single
  group: ''
```

### **Peak** — 编码输入中的最大幅度 `1` （默认） | 非负标量

将编码输入中表示的最大幅度指定为非负标量。要正确解码使用 Uniform Encoder 模块编码的值，请将两个模块中的 **Peak** 参数设置为相同的值。

### **Bits** — 位数 `3` （默认） | 范围为 [`2`, `32`] 的整数

指定用于编码数据的输入位数 *B*。位数 *B* 可以是 2 到 32（含）之间的任意整数值。该值可以小于输入数据类型提供的总位数。要正确解码使用 Uniform Encoder 模块编码的值，请将两个模块中的 **Bits** 参数设置为相同的值。

### **Overflow mode** — 溢出模式 `Saturate` （默认） | `Wrap`

指定当整数输入超出 *B* 位可表示的范围时模块的行为。超出范围的输入可以在极值处饱和，或者回绕到范围内。

当您选择 `Saturate` 时，大于 2B−1 的*无符号*输入值在 2B−1 处饱和，大于 2B−1−1 或小于 −2B−1 的*有符号*输入值在这些限值处饱和。复数输入的实部和虚部独立饱和。

当您选择 `Wrap` 时，大于 2B−1 的*无符号*输入值 `u` 使用 mod-2B 算术回绕到范围 [0, 2B−1] 内。

```
u = mod(u,2^B)
```

大于 2B−1−1 或小于 −2B−1 的*有符号*输入值 `u` 使用 mod-2B 算术回绕到该范围内。

```
u = (mod(u+2^B/2,2^B)-(2^B/2))
```

复数输入的实部和虚部独立回绕。

### **Output type** — 输出数据类型 `Double` （默认） | `Single`

将解码后的浮点输出的精度指定为 `single` 或 `double`。您可以对六种整数输入数据类型中的任何一种使用任一输出精度级别。
## 所属库

DSP System Toolbox / Quantizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

将整数输入解码为浮点输出

Uniform Decoder 模块执行 Uniform Encoder 模块的逆操作，并从编码的整数输入重建量化的浮点值。该模块遵循 ITU-T Recommendation G.701 中规定的均匀解码定义。

有关该模块如何计算解码后的浮点输出的详细信息，请参阅算法。
