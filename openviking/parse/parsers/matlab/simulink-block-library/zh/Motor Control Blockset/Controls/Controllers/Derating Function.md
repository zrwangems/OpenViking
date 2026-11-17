---
type: simulink-block
title: 'Derating Function'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'deratingfunction'
documentation_source_path: 'ref/deratingfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Derating Function

## 端口
```yaml
ports:
- name: fmax
  summary: 最大参考信号限值标量
  direction: input
  data_types: single | double | fixed point
- name: ffeedback
  summary: 参考反馈信号标量
  direction: input
  data_types: single | double | fixed point
- name: y
  summary: 降额因子标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **fmax** — 最大参考信号限值标量

参考信号值的最大限值，超过该值时降额因子变为零。

**数据类型：** `single` | `double` | `fixed point`

### **ffeedback** — 参考反馈信号标量

模块用于生成降额因子的参考信号，随后可用于对控制信号进行降额。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **y** — 降额因子标量

当信号超过 **Derating threshold** 参数值时，模块根据参考信号的反馈值和最大限值生成的降额因子。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Derating threshold
  summary: 必须进行降额的阈值 0.9（默认）| [0,1) 范围内的标量
  group: ''
```

### **Derating threshold** — 必须进行降额的阈值 `0.9`（默认）| [0,1) 范围内的标量

参考信号值，超过该值时模块生成降额因子。
## 所属库

Motor Control Blockset / Controls / Controllers Motor Control Blockset HDL Support / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算降额因子

Derating Function 模块根据输入参考信号的反馈（*ffeedback*）和最大限值（*fmax*）值生成降额因子（*y*）。

降额因子：

- 当 *ffeedback* 位于 **Derating threshold** 的正值和负值之间时，保持等于一。降额因子在该范围之外根据 *ffeedback* 线性变化。
- 当参考信号超出（正值或负值）*fmax* 时，保持等于零。

因此，当参考信号超过指定的 **Derating threshold** 后，可以使用生成的降额因子对控制信号进行降额。

下图显示了使用正弦波作为 *ffeedback* 时的模块输出。

### 方程

**Derating threshold** 参数 x 表示参考信号峰值幅值的百分比。所示模块输出中的 **Derating threshold** 为 0.5，这导致阈值值为 2（对于正弦参考信号的峰值幅值 4）。

x=[0,1)

此方程描述了模块如何计算降额因子（*y*）。

Derating factor (y)=1−ffeedback−xfmax(1−x)fmax
