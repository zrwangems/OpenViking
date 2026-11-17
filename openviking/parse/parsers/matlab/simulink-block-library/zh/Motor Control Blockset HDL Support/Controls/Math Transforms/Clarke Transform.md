---
type: simulink-block
title: 'Clarke Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'clarketransform'
documentation_source_path: '../mcb/ref/clarketransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Clarke Transform

## 端口
```yaml
ports:
- name: a
  summary: 相分量标量
  direction: input
  data_types: single | double | fixed point
- name: b
  summary: 相分量标量
  direction: input
  data_types: single | double | fixed point
- name: abc
  summary: 相分量标量
  direction: input
  data_types: single | double | fixed point
- name: α
  summary: 轴分量标量
  direction: output
  data_types: single | double | fixed point
- name: β
  summary: 轴分量标量
  direction: output
  data_types: single | double | fixed point
- name: αβ0
  summary: 轴分量标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **a** — 相分量标量

*abc* 参考坐标系中三相系统的分量。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **b** — 相分量标量

*abc* 参考坐标系中三相系统的分量。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **abc** — 相分量标量

*abc* 参考坐标系中三相系统的多路复用相分量 *a*、*b* 和 *c*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **α** — 轴分量标量

静止 *αβ* 参考坐标系中的 alpha 轴分量 *α*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **β** — 轴分量标量

静止 *αβ* 参考坐标系中的 beta 轴分量 *β*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **αβ0** — 轴分量标量

静止 *αβ* 参考坐标系中多路复用的 alpha 轴分量 *α*、beta 轴分量 *β* 和 `0` 分量。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 模块输入数量 Two inputs（默认）| Three inputs
  group: ''
- name: Power invariant
  summary: 启用功率不变性 off（默认）| on
  group: ''
```

### **Number of inputs** — 模块输入数量 `Two inputs`（默认）| `Three inputs`

选择可以指定的输入数量：

- `Two inputs` — 将模块配置为接受两个独立的输入信号 *a* 和 *b*。该模块生成两个独立的输出信号 *α* 和 *β*。
- `Three inputs` — 将模块配置为接受包含 *a*、*b* 和 *c* 信号的多路复用输入。该模块生成包含 *α*、*β* 和 *0* 信号的多路复用输出。

### **Power invariant** — 启用功率不变性 `off`（默认）| `on`

要在模块输出中启用功率不变性属性，请选中此参数。要在模块输出中禁用功率不变性（启用幅值不变性），请清除此参数。
## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

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

实现 ab 到 αβ 变换

Clarke Transform 模块计算 *abc* 参考系中平衡三相分量的 Clarke 变换，并输出静止 *αβ* 参考系中的平衡两相正交分量。
或者，该模块可以计算三相分量 *a*、*b* 和 *c* 的 Clarke 变换，并输出分量 *α*、*β* 和 `0`。对于平衡系统，零分量等于零。使用 **Number of inputs** 参数选择使用两个还是三个输入。

当使用双输入配置时，该模块接受三相（*abc*）中的两个信号，自动计算第三个信号，并输出 *αβ* 参考系中的对应分量。

例如，该模块可以接受 *a* 和 *b* 输入值，也可以接受多路复用输入值 *abc*，其中 phase-*a* 轴与 *α* 轴对齐。

- 该图显示了 *abc* 参考系和静止 *αβ* 参考系中定子绕组磁轴的方向。
- 该图显示了静止 *αβ* 参考系中的等效 *α* 和 *β* 分量。
- 等效平衡 *abc* 和 *αβ* 系统各分量的时间响应。

### 方程

以下方程描述了 Clarke 变换计算：

[fαfβf0]=(23)×[1−12−120 32−3212 12 12][fafbfc]

对于像电机这样的平衡系统，零序分量计算始终为零。例如，电机的电流可以表示为，

ia+ib+ic=0

因此，在三相电机驱动中，你可以只使用两个电流传感器，其中第三相可以计算为，

ic=−(ia+ib)

通过使用这些方程，该模块将 Clarke 变换实现为，

[fαfβ]= [1013  23][fafb]

其中：

- fa、fb 和 fc 是 *abc* 参考系中的平衡三相分量。
- fα 和 fβ 是静止 *αβ* 参考系中的平衡两相正交分量。
- f0 是静止 *αβ* 参考系中的零分量。
