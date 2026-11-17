---
type: simulink-block
title: 'Wrap To Zero'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'wraptozero'
documentation_source_path: '../simulink/slref/wraptozero.html'
language: zh-CN
chinese_source: worker-translation
---

# Wrap To Zero

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。等于或大于 `Threshold` 值的信号值被设置为零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

输出信号设置为输入信号值或零。输出的数据类型与输入的数据类型相同。

**提示**

如果输入数据类型无法表示零，则会发生参数溢出。要检测此溢出，请转到配置参数对话框的**诊断 > 数据有效性**窗格，并将**参数 > 检测溢出**设置为 `warning` 或 `error`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Threshold
  summary: 输出零的阈值 255（默认）| 标量
  group: ''
  block_parameter: Threshold
  type: 字符向量
  values: scalar
```

要编辑 Wrap to Zero 模块的参数，请双击模块图标。

### **Threshold** — 输出零的阈值 `255`（默认）| 标量

将输出值设置为零的阈值。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Threshold` |
| **类型**：字符向量 |
| **值**：`scalar` |
| **默认**：`'255'` |
## 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

输入信号和 **Threshold** 参数必须具有相同的大小。例如，如果输入是二维向量，**Threshold** 也必须是二维向量。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

如果输入高于阈值，则将输出设置为零

当输入高于 **Threshold** 值时，Wrap To Zero 模块将输出设置为零。当输入小于或等于 **Threshold** 时，输出等于输入。
