---
type: simulink-block
title: 'ACIM Torque Estimator'
family: 'motor-control-blockset-hdl-support'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'acimtorqueestimator'
documentation_source_path: 'ref/acimtorqueestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# ACIM Torque Estimator

## 端口
```yaml
ports:
- name: Isd
  summary: '*d* 轴定子电流标量'
  direction: input
  data_types: single | double | fixed point
- name: Isq
  summary: '*q* 轴定子电流标量'
  direction: input
  data_types: single | double | fixed point
- name: ωm
  summary: 转子机械速度标量
  direction: input
  data_types: single | double | fixed point
- name: Te
  summary: 机电转矩标量
  direction: output
  data_types: single | double | fixed point
- name: Pe
  summary: 机电功率标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Isd** — *d* 轴定子电流标量

沿旋转 *dq* 参考坐标系的 *d* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Isq** — *q* 轴定子电流标量

沿旋转 *dq* 参考坐标系的 *q* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械速度标量

转子的机械速度。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Te** — 机电转矩标量

转子的机电转矩。

**数据类型：** `single` | `double` | `fixed point`

### **Pe** — 机电功率标量

转子的机电功率。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Number of pole pairs
  summary: 电机中可用的极对数 2（默认）| 标量
  group: ''
- name: Motor parameter input method
  summary: 电机参数类型 Linear model with lumped parameters（默认）| Non-linear model with D,Q-flux linkage LUTs
  group: ''
- name: Stator leakage inductance (H)
  summary: 定子绕组的漏电感 6.81e-3（默认）| 标量
  group: ''
- name: Rotor leakage inductance (H)
  summary: 转子绕组的漏电感 6.81e-3（默认）| 标量
  group: ''
- name: Magnetizing Inductance (H)
  summary: 感应电机的励磁电感 30e-3（默认）| 标量
  group: ''
- name: Rated Flux (Wb)
  summary: 电机额定磁通 38.2e-3（默认）| 标量
  group: ''
- name: D-axis current breakpoint vector, id (A)
  summary: '*d* 轴电流查找向量 [0, 150, 350, 500]（默认）| 向量'
  group: ''
- name: Q-axis current breakpoint vector, id (A)
  summary: '*q* 轴电流查找向量 [0, 250, 500]（默认）| 向量'
  group: ''
- name: D-axis flux linkage LUT, FluxD (id,iq) (Wb)
  summary: 参考 *d* 轴磁链查找数据 4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)（默认）| 向量
  group: ''
- name: Q-axis flux linkage LUT, FluxD (id,iq) (Wb)
  summary: 参考 *q* 轴磁链查找数据 2.1e-3 * repmat([0, 250, 500], 4, 1)（默认）| 向量
  group: ''
- name: Input units
  summary: 输入值的单位 Per-Unit (PU)（默认）| SI Units
  group: ''
- name: Base Voltage (V)
  summary: 标幺制系统的基准电压 24/sqrt(3)（默认）| 标量
  group: ''
- name: Base Current (A)
  summary: 标幺制系统的基准电流 5.3611（默认）| 标量
  group: ''
- name: Base Speed (rpm)
  summary: 标幺制系统的基准转速 1500（默认）| 标量
  group: ''
- name: Base torque (Nm)
  summary: 标幺制系统的基准转矩 0.50072（默认）| 标量
  group: ''
- name: Base power (W)
  summary: 标幺制系统的基准功率 111.4284（默认）| 标量
  group: ''
```

### **Number of pole pairs** — 电机中可用的极对数 `2`（默认）| 标量

感应电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `Non-linear model with D,Q-flux linkage LUTs`

*自 R2025a 起*

模块用于生成功率和转矩估计的电机参数。将该参数设置为以下值之一：

- `Linear model with lumped parameters` — 使用电机电感
  *Ls*、*Lr*、*Lm* 的集中电路值和额定磁通来生成转矩
  和功率估计。
- `Non-linear model with D,Q-flux linkage LUTs` —
  使用 *d* 轴和
  *q* 轴磁链查找表来生成转矩和功率估计。

### **Stator leakage inductance (H)** — 定子绕组的漏电感 `6.81e-3`（默认）| 标量

与定子绕组交链的漏磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Linear model with lumped
parameters`。

### **Rotor leakage inductance (H)** — 转子绕组的漏电感 `6.81e-3`（默认）| 标量

与转子绕组交链的漏磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Linear model with lumped
parameters`。

### **Magnetizing Inductance (H)** — 感应电机的励磁电感 `30e-3`（默认）| 标量

励磁磁通引起的电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Linear model with lumped
parameters`。

### **Rated Flux (Wb)** — 电机额定磁通 `38.2e-3`（默认）| 标量

感应电机的额定磁通（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Linear model with lumped
parameters`。

### **D-axis current breakpoint vector, id (A)** — *d* 轴电流查找向量 `[0, 150, 350, 500]`（默认）| 向量

*自 R2025a 起*

用于磁链查找表的 *d* 轴电流查找向量（以百分比表示）。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Non-linear model with D,Q-flux linkage
LUTs`。

### **Q-axis current breakpoint vector, id (A)** — *q* 轴电流查找向量 `[0, 250, 500]`（默认）| 向量

*自 R2025a 起*

用于磁链查找表的 *q* 轴电流查找向量（以百分比表示）。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 参数设置为 `Non-linear model with D,Q-flux linkage
LUTs`。

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 *d* 轴磁链查找数据 `4.4e-2 * repmat([0, 150, 350, 500]', 1, 3)`（默认）| 向量

*自 R2025a 起*

*d* 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 *q* 轴磁链查找数据 `2.1e-3 * repmat([0, 250, 500], 4, 1)`（默认）| 向量

*自 R2025a 起*

*q* 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

输入值的单位。

### **Base Voltage (V)** — 标幺制系统的基准电压 `24/sqrt(3)`（默认）| 标量

标幺制系统的基准电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base Current (A)** — 标幺制系统的基准电流 `5.3611`（默认）| 标量

标幺制系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base Speed (rpm)** — 标幺制系统的基准转速 `1500`（默认）| 标量

标幺制系统的基准转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base torque (Nm)** — 标幺制系统的基准转矩 `0.50072`（默认）| 标量

标幺制系统的基准转矩（单位：Nm）。有关更多详细信息，请参阅 Per-Unit System 页面。

此参数不可配置，使用由其他参数内部计算得出的值。

#### 依赖关系

要显示此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base power (W)** — 标幺制系统的基准功率 `111.4284`（默认）| 标量

标幺制系统的基准功率（单位：W）。有关更多详细信息，请参阅 Per-Unit System 页面。

此参数不可配置，使用由其他参数内部计算得出的值。

#### 依赖关系

要显示此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。
## 所属库

Motor Control Blockset / Controls / Control Reference Motor Control Blockset HDL Support / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

### R2025a：使用新的模块参数计算功率和转矩估计值

模块参数对话框现在包含一些参数，使您能够根据磁链查找表数据计算功率和转矩估计值。

## 描述

估计机电转矩和功率

ACIM Torque Estimator 模块为感应电机生成机电转矩和功率估计值。该模块针对恒定电机参数输出数学计算得到的机电转矩。若要测量准确的转矩值，我们建议您使用物理传感器。

该模块接受 *d* 轴和 *q* 轴定子电流以及机械转速的反馈值作为输入。

### 方程

如果您在 **Input units** 参数中选择 `Per-Unit (PU)`，则该模块在执行任何计算之前会将输入转换为 SI 单位。在计算输出之后，该模块会将输出转换回标幺值。

这些方程描述了该模块对机电转矩和功率估计值的计算。

Te=32p(LmLr)λrdisq

Pe=Te⋅ωm

有关详细的方程组和假设，请参阅 Mathematical Model of Induction Motor。

其中：

- p 是电机中可用的极对数。
- Lm 是电机的励磁电感（亨利）。
- Lr 是转子电感（亨利）。
- λrd 是转子的 *d* 轴磁链（韦伯）。
- isq 是定子 *q* 轴电流（安培）。
- ωm 是转子的机械转速（弧度/秒）。
