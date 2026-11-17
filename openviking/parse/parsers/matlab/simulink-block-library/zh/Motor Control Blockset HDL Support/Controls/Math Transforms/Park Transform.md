---
type: simulink-block
title: 'Park Transform'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'parktransform'
documentation_source_path: '../mcb/ref/parktransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Park Transform

## 端口
```yaml
ports:
- name: α
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: β
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: αβ0
  summary: 轴分量 标量
  direction: input
  data_types: single | double | fixed point
- name: sin θe
  summary: 旋转角正弦值 标量
  direction: input
  data_types: single | double | fixed point
- name: cos θe
  summary: 旋转角余弦值 标量
  direction: input
  data_types: single | double | fixed point
- name: d
  summary: 轴分量 标量
  direction: output
  data_types: single | double | fixed point
- name: q
  summary: 轴分量 标量
  direction: output
  data_types: single | double | fixed point
- name: dq0
  summary: 轴分量 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **α** — 轴分量 标量

静止 *αβ* 参考系中的 alpha 轴分量 *α*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **β** — 轴分量 标量

静止 *αβ* 参考系中的 beta 轴分量 *β*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **αβ0** — 轴分量 标量

静止 *αβ* 参考系中的多路复用 alpha 轴分量 *α*、beta 轴分量 *β* 和 `0` 分量。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **sin θe** — 旋转角正弦值 标量

变换角 *θe* 的正弦值。*θe* 是旋转参考系与 *α* 轴之间的夹角。

**数据类型：** `single` | `double` | `fixed point`

### **cos θe** — 旋转角余弦值 标量

变换角 *θe* 的余弦值。*θe* 是旋转参考系与 *α* 轴之间的夹角。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **d** — 轴分量 标量

旋转 *dq* 参考系中的直轴分量 *d*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **q** — 轴分量 标量

旋转 *dq* 参考系中的交轴分量 *q*。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Two inputs`。

**数据类型：** `single` | `double` | `fixed point`

### **dq0** — 轴分量 标量

旋转 *dq* 参考系中的多路复用直轴分量 *d*、交轴分量 *q* 和 *0* 分量。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为 `Three inputs`。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of inputs
  summary: 模块输入数量 Two inputs（默认）| Three inputs
  group: ''
- name: Alpha (phase-a) axis alignment
  summary: '*dq* 参考系对齐 D-axis（默认）| Q-axis'
  group: ''
- name: Theta input
  summary: 位置输入类型 Sine and Cosine electrical position（默认）| Electrical position
  group: ''
- name: Theta units
  summary: 电位置输入的单位 Per-unit（默认）| Radians | Degrees
  group: ''
- name: Number of data points for lookup table
  summary: 查找表数组的大小 1024（默认）| 标量
  group: ''
```

### **Number of inputs** — 模块输入数量 `Two inputs`（默认）| `Three inputs`

选择可以指定的输入数量：

- `Two inputs` — 将模块配置为接受两个独立的输入信号 *α* 和 *β*。该模块生成两个独立的输出信号 *d* 和 *q*。
- `Three inputs` — 将模块配置为接受包含 *α*、*β* 和 *0* 信号的多路复用输入。该模块生成包含 *d*、*q* 和 *0* 信号的多路复用输出。

### **Alpha (phase-a) axis alignment** — *dq* 参考系对齐 `D-axis`（默认）| `Q-axis`

将旋转参考系的 *d* 轴或 *q* 轴与静止参考系的 *α* 轴对齐。

### **Theta input** — 位置输入类型 `Sine and Cosine electrical position`（默认）| `Electrical position`

位置（theta）输入的类型：

- `Sine and Cosine electrical position` — 将模块配置为直接接受 *sinθe* 和 *cosθe* 输入。
- `Electrical position` — 将模块配置为接受电位置（*θe*）输入。该模块根据 *θe* 输入在内部计算 *sinθe* 和 *cosθe* 信号。

### **Theta units** — 电位置输入的单位 `Per-unit`（默认）| `Radians` | `Degrees`

电位置输入（*θe*）的单位。

#### 依赖

要启用此参数，请将 **Theta input** 设置为 `Electrical position`。

### **Number of data points for lookup table** — 查找表数组的大小 `1024`（默认）| 标量

该模块用于根据 *θe* 输入计算 *sinθe* 和 *cosθe* 信号的查找表数组的大小。可以指定 125 到 4095 之间的值。

#### 依赖

要启用此参数，请将 **Theta input** 设置为 `Electrical position`。
## 所属库

Motor Control Blockset / Controls / Math Transforms Motor Control Blockset HDL Support / Controls / Math Transforms

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除 Park Transform 模块层级。默认值为 `inherit`。另请参阅 FlattenHierarchy (HDL Coder)。 如果您正在对 Park Transform 模块使用资源共享优化（通过将 **SharingFactor** 属性设置为大于 0 的值），请将该模块的 **FlattenHierarchy** 属性设置为 `on`。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

实现 αβ 到 dq 变换

Park Transform 模块计算静止 *αβ* 参考系中两相正交分量（*α*、*β*）或多路复用 *αβ0* 分量的 Park 变换。

该模块接受以下输入：

- 静止参考系中的 *α-β* 轴分量或多路复用分量 *αβ0*。使用 **Number of inputs** 参数选择使用两个或三个输入。
- 对应变换角度的正弦和余弦值。

使用双输入配置时，该模块输出旋转 *dq* 参考系中的正交直轴（*d*）和交轴（*q*）分量。使用三输入配置时，它输出多路复用分量 *dq0*。

对于平衡系统，零分量等于零。

您可以将模块配置为在时间 *t* = 0 时使 *d* 轴或 *q* 轴与 *α* 轴对齐。

这些图显示了在以下情况下 *αβ* 参考系和旋转 *dq* 参考系中的 *α-β* 轴分量：

- *d* 轴与 *α* 轴对齐。
- *q* 轴与 *α* 轴对齐。

  在两种情况下，角度 *θ = ωt*，其中：

  - *θ* 是 *d* 轴对齐时 *α* 轴与 *d* 轴之间的角度，或 *q* 轴对齐时 *α* 轴与 *q* 轴之间的角度。它表示旋转 *dq* 参考系相对于 *α* 轴的角位置。
  - *ω* 是 *d-q* 参考系的旋转速度。
  - *t* 是从初始对齐开始的时间，以秒为单位。

这些图显示了在以下情况下 *αβ* 和 *dq* 参考系各分量的时间响应：

- *d* 轴与 *α* 轴对齐。
- *q* 轴与 *α* 轴对齐。

### 方程

如果**输入数量**参数设置为 `Two
inputs`，以下方程描述该模块如何实现 Park 变换。

- 当 *d* 轴与 *α* 轴对齐时。

  [fdfq]= [cosθsinθ−sinθcosθ][fαfβ]
- 当 *q* 轴与 *α* 轴对齐时。

  [fdfq]= [sinθ−cosθcosθsinθ][fαfβ]

其中：

- fα 和 fβ 是静止 *αβ* 参考坐标系中的两相正交分量。
- fd 和 fq 是旋转 *dq* 参考坐标系中的直轴和交轴正交分量。

如果**输入数量**参数设置为 `Three
inputs`，以下方程描述该模块如何实现 Park 变换：

- Clarke to Park Angle Transform 模块针对 *a* 相到 *q* 轴对齐实现如下变换：

  [dq0]=[sin(θ)−cos(θ)0cos(θ)sin(θ)0001][αβ0]

  其中：

  - *α* 和 *β* 是静止参考坐标系中两相系统的 alpha 轴和 beta 轴分量。
  - *0* 是零分量。
  - *d* 和 *q* 是旋转参考坐标系中双轴系统的直轴和交轴分量。
- 对于 *a* 相到 *d* 轴对齐，该模块使用以下方程实现变换：

  [dq0]=[cos(θ)sin(θ)0−sin(θ)cos(θ)0001][αβ0]
