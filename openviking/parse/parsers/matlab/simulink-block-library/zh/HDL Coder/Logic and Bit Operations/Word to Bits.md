---
type: simulink-block
title: 'Word to Bits'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'wordtobits'
documentation_source_path: 'ref/wordtobits.html'
language: zh-CN
chinese_source: worker-translation
---

# Word to Bits

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Out
  summary: 输出信号 二值标量 | 二值向量
  direction: output
  data_types: ufix1
```

### 输入

### **In** — 输入信号 标量

输入信号，指定为标量。字长必须小于或等于 **Maximum Word Length** 参数。

**示例:** `72`

**示例:** `5.5`

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Out** — 输出信号 二值标量 | 二值向量

输出信号，以二值标量或向量的形式返回。在 **Maximum Word Length** 参数中设置此向量的长度。该模块将输出向量的第一个元素视为 LSB，并将后续位按升序视为下一个有效位。

**数据类型:** `ufix1`
## 参数
```yaml
parameters:
- name: Maximum Word Length
  summary: 最大输出字长 64（默认）| [1, 65535] 范围内的整数
  group: ''
  block_parameter: maxWordLength
  type: 字符向量
  values: '[1, 65535] 范围内的整数'
- name: Output bit order
  summary: 输出位顺序 LSB first（默认）| MSB first
  group: ''
  block_parameter: bitOrder
  type: 字符向量
  values: '''LSB first'' | ''MSB first'''
```

### **Maximum Word Length** — 最大输出字长 `64`（默认）| [1, 65535] 范围内的整数

最大输出字长，指定为 [1, 65535] 范围内的整数。该参数值必须大于或等于输入信号字长。

#### 编程使用

|  |
| --- |
| **模块参数:** `maxWordLength` |
| **类型:** 字符向量 |
| **值:** [1, 65535] 范围内的整数 |
| **默认:** `'64'` |

### **Output bit order** — 输出位顺序 `LSB first`（默认）| `MSB first`

定义输出信号的第一位是最高有效位 (MSB) 还是最低有效位 (LSB)。

#### 编程使用

|  |
| --- |
| **模块参数**: `bitOrder` |
| **类型**: 字符向量 |
| **值**: `'LSB first'` | `'MSB first'` |
| **默认**: `'LSB first'` |
## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**数据类型支持**

该模块支持以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 总线 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **In** | 标量 | 是 | 否 | 是 | 否 | 否 | 否 |

**限制**

- 不支持矩阵输入。

## 版本历史

**在 R2023a 中引入**

### R2024b: 最大字长为 65535 位

**Maximum Word Length** 模块参数支持最大字长 65535 位。在 R2024b 之前，最大字长为 128 位。

## 描述

将实数转换为位向量

Word to Bits 模块将字长为 *N* 的实数转换为位向量。该模块的输出是一个向量，其长度由 **Maximum Word Length** 参数指定。

该模块将输出向量的第一个元素视为最低有效位（LSB），并将后续位按升序视为次高有效位。

下图展示了当最大字长指定为 8 时，将无符号整数 72 转换为其二进制表示的过程。你也可以将有符号整数值转换为其对应的二进制向量。

Word to Bits 转换

下图展示了将非整数值 5.5 转换为其二进制表示的过程。输出是 5.5 的存储整数值的二进制表示。要确定定点实数的存储整数值，请使用 `storedInteger` 函数。

将实数转换为位向量
