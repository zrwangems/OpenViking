---
type: simulink-block
title: 'Extract Bits'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'extractbits'
documentation_source_path: 'slref/extractbits.html'
language: zh-CN
chinese_source: worker-translation
---

# Extract Bits

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 提取的位 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。
浮点输入将原样通过模块传递。
`boolean` 输入被视为
`uint8` 信号。

**注意**

对有符号整数执行位操作比较困难。你可以通过将输入
信号的数据类型转换为无符号整数类型来避免困难。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 提取的位 标量 | 向量 | 矩阵 | N 维数组

提取位的连续选择，指定为标量、向量、
矩阵或 N 维数组。浮点输入将原样通过模块
传递。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Bits to extract
  summary: 提取位的方法 Upper half（默认） | Lower half | Range starting with most significant bit | Range ending with least significant
    big | Range of bits
  group: ''
  block_parameter: bitsToExtract
  type: character vector
  values: '''Upper half'' | ''Lower half'' | ''Range starting with most significant bit'' | ''Range ending with least significant
    bit'' | ''Range of bits'''
  default: '''Upper half'''
- name: Number of bits
  summary: 要输出的位数 8（默认） | 标量正整数
  group: ''
  block_parameter: numBits
  type: character vector
  values: scalar positive integer
  default: '''8'''
- name: Bit indices
  summary: 要输出的连续位范围 [0 7]（默认） | 二元素向量 | 标量正整数
  group: ''
  block_parameter: bitIdxRange
  type: character vector
  values: two-element vector | scalar positive integer
  default: '''[0 7]'''
- name: Output scaling mode
  summary: 输出定标模式 Preserve fixed-point scaling（默认） | Treat bit field as an integer
  group: ''
  block_parameter: outScalingMode
  type: character vector
  values: '''Preserve fixed-point scaling'' | ''Treat bit field as an integer'''
  default: '''Preserve fixed-point scaling'''
```

### **Bits to extract** — 提取位的方法 `Upper half`（默认） | `Lower half` | `Range starting with most significant bit` | `Range ending with least significant big` | `Range of bits`

选择从输入信号中提取位的方法。

考虑一个用二进制表示为
`110111001` 的输入信号：

- 如果为 **Bits
  to extract** 参数选择 `Upper half`，则输出为
  二进制 `11011`。
- 如果为 **Bits
  to extract** 参数选择 `Lower half`，则输出为
  二进制 `11001`。
- 如果为 **Bits to extract**
  参数选择 `Range starting with most significant
  bit`，并为 **Number
  of bits** 参数指定 `3`，则输出为
  二进制 `110`。
- 如果为 **Bits to extract**
  参数选择 `Range ending with least significant
  bit`，并为 **Number
  of bits** 参数指定 `8`，则输出为
  二进制 `10111001`。
- 如果为
  **Bits to extract** 参数选择 `Range of bits`，并为 **Bit indices** 参数指定
  `[4 7]`，则输出为二进制 `1011`。

#### 编程使用

|  |
| --- |
| **模块参数**：`bitsToExtract` |
| **类型**：character vector |
| **值**：`'Upper half' | 'Lower half' | 'Range starting with most significant bit' | 'Range ending with least significant bit' | 'Range of bits'` |
| **默认值**：`'Upper half'` |

### **Number of bits** — 要输出的位数 `8`（默认） | 标量正整数

将要从输入信号输出的位数指定为标量
正整数。

#### 依赖关系

要启用此参数，请将 **Bits to extract** 设置为
`Range starting with most significant bit` 或
`Range ending with least significant bit`。

#### 编程使用

|  |
| --- |
| **模块参数**：`numBits` |
| **类型**：character vector |
| **值**：scalar positive integer |
| **默认值**：`'8'` |

### **Bit indices** — 要输出的连续位范围 [0 7]（默认） | 二元素向量 | 标量正整数

将要输出的输入信号位指定为二元素向量，其元素为
标量正整数。以 `[start
end]` 格式指定范围。

#### 依赖关系

要启用此参数，请将 **Bits to extract** 设置为
`Range of bits`。

#### 编程使用

|  |
| --- |
| **模块参数**：`bitIdxRange` |
| **类型**：character vector |
| **值**：two-element vector | scalar positive integer |
| **默认值**：`'[0 7]'` |

### **Output scaling mode** — 输出定标模式 `Preserve fixed-point scaling`（默认） | `Treat bit field as an integer`

选择要用于输出位选择的定标模式：

- 当你选择 `Preserve fixed-point
  scaling` 时，输入的定点定标将用于在数据类型
  转换期间确定输出定标。
- 当你选择 `Treat bit field as an
  integer` 时，输入的定点定标将被忽略，仅使用存储整数来计算
  输出数据类型。

#### 编程使用

|  |
| --- |
| **模块参数**：`outScalingMode` |
| **类型**：character vector |
| **值**：`'Preserve fixed-point scaling' | 'Treat bit field as an integer'` |
| **默认值**：`'Preserve fixed-point scaling'` |
## 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL
实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

从输入信号中输出连续位的选择

Extract Bits 模块允许你从输入信号的存储整数值中输出连续选择的
位。使用 **Bits to
extract** 参数定义选择输出位的方法。

- 选择 `Upper half` 以输出包含最高有效位的输入位的一半。如果输入
  信号中的位数为奇数，则输出位数由以下公式给出

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Lower half` 以输出包含最低有效位的输入位的一半。如果输入
  信号中的位数为奇数，则输出位数由以下公式给出

  ```
  number of output bits = ceil(number of input bits/2)
  ```
- 选择 `Range starting with most significant bit` 以输出输入信号的
  一定数量的最高有效位。在 **Number of
  bits** 参数中指定要输出的最高有效位数。
- 选择 `Range ending with least significant bit` 以输出输入信号的
  一定数量的最低有效位。在 **Number of
  bits** 参数中指定要输出的最低有效位数。
- 选择 `Range of bits` 以在 **Bit indices** 参数中指示要输出的输入
  的一系列连续位。你以 `[start end]` 格式指示范围，输入位的索引
  从最低有效位的 0 开始连续标记。

此模块在仿真期间不会报告溢出回绕警告。要报告
这些警告，请参阅 `Simulink.restoreDiagnostic` 参考
页。此模块确实会报告由于溢出回绕导致的错误。
