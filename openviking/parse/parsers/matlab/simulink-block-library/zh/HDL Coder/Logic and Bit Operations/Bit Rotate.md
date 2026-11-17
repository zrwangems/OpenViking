---
type: simulink-block
title: 'Bit Rotate'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitrotate'
documentation_source_path: 'ref/bitrotate.html'
language: zh-CN
chinese_source: worker-translation
---

# Bit Rotate

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

执行位旋转的输入信号。

- 最小位宽：2
- 最大位宽：128

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

经过位旋转的输出信号。输出信号的数据类型与输入信号相同。
## 参数
```yaml
parameters:
- name: Rotate Mode
  summary: 指定旋转方向，向左或向右 Rotate Left（默认）| Rotate Right
  group: ''
  block_parameter: mode
  type: string scalar | character vector
  values: '"Rotate Left" | "Rotate Right"'
- name: Rotate Length
  summary: 指定要旋转的位数 0（默认）| 大于或等于零的整数
  group: ''
  block_parameter: N
  type: string scalar | character vector
  values: 大于或等于零的整数
```

### **Rotate Mode** — 指定旋转方向，向左或向右 `Rotate Left`（默认）| `Rotate Right`

指定旋转方向，向左或向右。

#### 编程使用

|  |
| --- |
| **模块参数：** `mode` |
| **类型：** string scalar | character vector |
| **值：** `"Rotate Left"` | `"Rotate Right"` |
| **默认：** `'Rotate Left'` |

### **Rotate Length** — 指定要旋转的位数 `0`（默认）| 大于或等于零的整数

指定要旋转的位数。

#### 编程使用

|  |
| --- |
| **模块参数：** `N` |
| **类型：** string scalar | character vector |
| **值：** 大于或等于零的整数 |
| **默认：** `'0'` |
## 所属库

HDL Coder / Logic and Bit Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014a 中引入**

## 描述

按位位置旋转输入信号

Bit Rotate 模块将输入信号向左或向右旋转指定的位位置数。
