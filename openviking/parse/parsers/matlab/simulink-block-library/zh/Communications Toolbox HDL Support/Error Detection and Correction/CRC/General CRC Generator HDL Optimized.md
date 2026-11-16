---
type: simulink-block
title: 'General CRC Generator HDL Optimized'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction / CRC'
documentation_page: 'generalcrcgeneratorhdloptimized'
documentation_source_path: '../comm/ref/generalcrcgeneratorhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# General CRC Generator HDL Optimized

## 端口

### 输入

### **dataIn** — 输入数据 标量 | 向量

输入数据，指定为以下选项之一。

- 标量 – 指定表示若干位的整数。对于这种情况，模块支持无符号整数（`uint8`、
  `uint16` 或 `uint32`）或 `fixdt(0,N,0)` 数据类型。
- 向量 – 指定二进制值向量。对于这种情况，模块支持 `double` 或
  `Boolean` 数据类型。

数据宽度必须小于或等于 CRC 长度，且 CRC 长度必须能被数据宽度整除。对于 CRC-CCITT/CRC-16，有效的数据宽度为
16、8、4、2 和 1。

**示例：** `uint8` 向量输入 `[0 0 0 1 0 0 1
1]` 等效于 `19`。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `fixed point` | `Boolean`

### **startIn** — 输入帧起始指示符 布尔标量

输入帧起始指示符，指定为布尔标量。

**数据类型：** `Boolean`

### **endIn** — 输入帧结束指示符 布尔标量

输入帧结束指示符，指定为布尔标量。

**数据类型：** `Boolean`

### **validIn** — 有效输入数据指示符 布尔标量

有效输入数据指示符，指定为布尔标量。

这是一个控制信号，用于指示 **dataIn** 端口上的数据是否有效。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出数据 标量 | 向量

附加校验和后的输出数据，以标量或向量形式返回。输出数据类型和大小与输入数据相同。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **startOut** — 输出帧起始指示符 标量

输出帧起始指示符，以布尔标量形式返回。

**数据类型：** `Boolean`

### **endOut** — 输出帧结束指示符 标量

输出帧结束指示符，以布尔标量形式返回。

**数据类型：** `Boolean`

### **validOut** — 有效输出数据指示符 标量

有效输出数据指示符，以布尔标量形式返回。

此端口是一个控制信号，用于指示 **dataOut** 端口上的数据是否有效。

**数据类型：** `Boolean`

## 参数

### **Polynomial** — 生成多项式 `[1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1]`（默认）| 二进制向量

将生成多项式指定为系数按幂次降序排列的二进制向量。向量长度等于多项式的次数加
1。

### **Initial state** — 移位寄存器的初始条件 `0`（默认）| 二进制标量 | 二进制向量

将内部移位寄存器的初始条件指定为二进制、双精度或单精度标量或向量。对于向量输入，初始状态的长度必须等于生成多项式的次数。

### **Direct method** — 计算校验和的方法 `off`（默认）| `on`

指定用于计算校验和的直接或间接方法。

- 选中此参数时，模块使用直接算法进行 CRC 校验和计算。
- 清除此参数时，模块使用非直接算法进行 CRC 校验和计算。

有关直接和非直接算法的详细信息，请参阅 Cyclic Redundancy Check Codes。

### **Reflect input** — 输入字节顺序 `off`（默认）| `on`

指定输入字节顺序。

- 选中此参数时，模块在输入数据进入移位寄存器之前翻转每个输入字节。
- 清除此参数时，模块将消息数据原样传递到移位寄存器。

输入数据宽度必须是 8 的倍数。

### **Reflect CRC checksum** — 校验和字节顺序 `off`（默认）| `on`

指定校验和字节顺序。

- 选中此参数时，模块在将每个校验和字节传递到最终 XOR 级之前翻转该字节。
- 清除此参数时，模块将校验和字节原样传递到最终 XOR 级。

输入数据宽度必须是 8 的倍数。

### **Final XOR value** — 校验和 `0`（默认）| 二进制标量 | 二进制向量

将校验和指定为二进制、双精度或单精度数据类型的标量或向量。模块将 CRC 校验和与此值执行 XOR 运算，然后将其附加到输入数据。

如果指定向量输入，向量长度必须等于生成多项式的次数。

## 所属库

Communications Toolbox HDL Support / Error Detection and Correction / CRC

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2012a 中引入**

## 描述

生成 CRC 码位并将其附加到输入数据

General CRC Generator HDL Optimized 模块与
General CRC Generator 模块类似，生成循环冗余校验（CRC）校验和并将其附加到输入消息。General CRC Generator HDL Optimized 模块
的处理针对 HDL 代码生成进行了优化。该模块不是一次处理整个帧，而是接收并返回带有随附控制信号的数据样本流。
控制信号指示样本的有效性和帧的边界。为了实现更高的吞吐量，该模块接受最大为 CRC 长度的向量数据，并实现
并行架构。
