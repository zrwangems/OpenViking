---
type: simulink-block
title: 'General CRC Syndrome Detector HDL Optimized'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction / CRC'
documentation_page: 'generalcrcsyndromedetectorhdloptimized'
documentation_source_path: '../comm/ref/generalcrcsyndromedetectorhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# General CRC Syndrome Detector HDL Optimized

## 端口
```yaml
ports:
- name: dataIn
  summary: 输入数据 标量 | 向量
  direction: input
  data_types: double | uint8 | uint16 | uint32 | fixed point | Boolean
- name: startIn
  summary: 输入帧起始指示 标量
  direction: input
  data_types: Boolean
- name: endIn
  summary: 输入帧结束指示 标量
  direction: input
  data_types: Boolean
- name: validIn
  summary: 有效输入数据指示 标量
  direction: input
  data_types: Boolean
- name: dataOut
  summary: 输出数据 标量 | 向量
  direction: output
  data_types: double | uint8 | uint16 | uint32 | Boolean | fixed point
- name: startOut
  summary: 输出帧起始指示 标量
  direction: output
  data_types: Boolean
- name: endOut
  summary: 输出帧结束指示 标量
  direction: output
  data_types: Boolean
- name: validOut
  summary: 有效输出数据指示 标量
  direction: output
  data_types: Boolean
- name: err
  summary: 错误指示 标量
  direction: output
  data_types: Boolean
```

### 输入

### **dataIn** — 输入数据 标量 | 向量

输入数据，指定为以下选项之一。

- 标量 – 指定表示若干位的整数。在这种情况下，该模块支持无符号整数（`uint8`、`uint16` 或 `uint32`）或 `fixdt(0,N,0)` 数据类型。
- 向量 – 指定二进制值向量。在这种情况下，该模块支持 `double` 或 `Boolean` 数据类型。

数据宽度必须小于或等于 CRC 长度，并且 CRC 长度必须能被数据宽度整除。对于 CRC-CCITT/CRC-16，有效的数据宽度为 16、8、4、2 和 1。

**示例：** `uint8` 向量输入 `[0 0 0 1 0 0 1 1]` 等效于 `19`。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `fixed point` | `Boolean`

### **startIn** — 输入帧起始指示 标量

输入帧起始指示，指定为布尔标量。

**数据类型：** `Boolean`

### **endIn** — 输入帧结束指示 标量

输入帧结束指示，指定为布尔标量。

**数据类型：** `Boolean`

### **validIn** — 有效输入数据指示 标量

有效输入数据指示，指定为布尔标量。

这是一个控制信号，用于指示 **dataIn** 端口上的数据是否有效。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出数据 标量 | 向量

输出数据，以标量或向量形式返回。输出数据类型和大小与输入数据相同。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **startOut** — 输出帧起始指示 标量

输出帧起始指示，以布尔标量形式返回。

**数据类型：** `Boolean`

### **endOut** — 输出帧结束指示 标量

输出帧结束指示，以 `Boolean` 标量形式返回。

**数据类型：** `Boolean`

### **validOut** — 有效输出数据指示 标量

有效输出数据指示，以布尔标量形式返回。

这是一个控制信号，用于指示 **dataOut** 端口上的数据是否有效。

**数据类型：** `Boolean`

### **err** — 错误指示 标量

接收数据损坏的错误指示，以布尔标量形式返回。

当该值为 `1` 时，消息包含至少一个错误。
当该值为 `0` 时，消息包含零个错误。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Polynomial
  summary: 生成多项式 [1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1]（默认）| 二进制向量
  group: ''
- name: Initial state
  summary: 移位寄存器初始条件 0（默认）| 二进制标量 | 二进制向量
  group: ''
- name: Direct method
  summary: 校验和计算方法 off（默认）| on
  group: ''
- name: Reflect input
  summary: 输入字节顺序 off（默认）| on
  group: ''
- name: Reflect CRC checksum
  summary: 校验和字节顺序 off（默认）| on
  group: ''
- name: Final XOR value
  summary: 校验和 0（默认）| 二进制标量 | 二进制向量
  group: ''
```

### **Polynomial** — 生成多项式 `[1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1]`（默认）| 二进制向量

将生成多项式指定为系数按幂次降序排列的二进制向量。向量长度等于多项式的阶数加 1。

### **Initial state** — 移位寄存器初始条件 `0`（默认）| 二进制标量 | 二进制向量

将内部移位寄存器的初始条件指定为二进制、双精度或单精度标量或向量。对于向量输入，初始状态的长度必须等于生成多项式的阶数。

### **Direct method** — 校验和计算方法 `off`（默认）| `on`

将校验和的计算方法指定为布尔标量。

- 选择此参数以使用直接算法进行 CRC 校验和计算。
- 清除此参数以使用非直接算法进行 CRC 校验和计算。

要了解直接算法和非直接算法，请参阅 Cyclic Redundancy Check Codes。

### **Reflect input** — 输入字节顺序 `off`（默认）| `on`

指定输入字节顺序。

- 选择此参数，使该模块在每位输入字节进入移位寄存器之前将其翻转。
- 清除此参数，使该模块将消息数据原样传递到移位寄存器。

输入数据宽度必须是 8 的倍数。

### **Reflect CRC checksum** — 校验和字节顺序 `off`（默认）| `on`

指定校验和字节顺序。

- 选择此参数，使该模块在将每个校验和字节传递到最终 XOR 级之前将其翻转。
- 清除此参数，使该模块将校验和字节原样传递到最终 XOR 级。

输入数据宽度必须是 8 的倍数。

### **Final XOR value** — 校验和 `0`（默认）| 二进制标量 | 二进制向量

将校验和指定为二进制、双精度或单精度数据类型的标量或向量。该模块在将 CRC 校验和附加到输入数据之前，使用此值对 CRC 校验和执行 XOR 运算。

如果指定向量输入，向量长度必须等于生成多项式的阶数。
## 所属库

Communications Toolbox HDL Support / Error Detection and Correction / CRC

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2012b 中引入**

## 描述

使用 CRC 检测输入数据中的错误

General CRC Syndrome Detector HDL Optimized 模块对数据执行循环冗余校验（CRC），并将生成的校验和与附加的校验和进行比较。General CRC Syndrome Detector HDL Optimized 模块的处理针对 HDL 代码生成进行了优化。如果两个校验和不匹配，该模块会报告错误。该模块不是一次处理整个帧，而是接受并返回带有伴随控制信号的数据样本流。控制信号指示样本的有效性和帧的边界。为实现更高的吞吐量，该模块接受长度不超过 CRC 长度的向量数据，并实现并行架构。
