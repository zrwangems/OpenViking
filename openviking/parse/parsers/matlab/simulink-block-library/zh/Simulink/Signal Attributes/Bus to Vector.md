---
type: simulink-block
title: 'Bus to Vector'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'bustovector'
documentation_source_path: 'slref/bustovector.html'
language: zh-CN
chinese_source: worker-translation
---

# Bus to Vector

## 端口
```yaml
ports:
- name: Port_1
  summary: 要转换为向量的总线 标量 | 向量 | 总线
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: Port_1
  summary: 输出向量 向量
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
```

### 输入

### **Port\_1** — 要转换为向量的总线 标量 | 向量 | 总线

输入总线必须由具有相同数据类型、信号类型和采样模式的标量或一维、行或列向量组成。如果输入是非总线信号，该模块不执行任何转换。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** 是
### 输出

### **Port\_1** — 输出向量 向量

输出向量的维度取决于输入总线元素的维度。如果输入总线包含行向量或列向量，则模块输出分别为行向量或列向量。否则，输出为一维向量。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
**复数支持：** 是
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅 Buses (HDL Coder) 和 Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2007a 中引入**

## 描述

将虚拟总线转换为向量

Bus to Vector 模块将虚拟总线转换为向量。仅当要用显式转换替换隐式总线到向量转换时，才使用 Bus to Vector 模块。

不接受总线的模块可能会隐式地将总线转换为向量。当总线被视为向量时，总线元素将变得不可访问。要识别并修正被用作向量的总线，请使用 Model Advisor 检查 Check bus signals treated as vectors 或函数 `Simulink.BlockDiagram.addBusToVector`。
