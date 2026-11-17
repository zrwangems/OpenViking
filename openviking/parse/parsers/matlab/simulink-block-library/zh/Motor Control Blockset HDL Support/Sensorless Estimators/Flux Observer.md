---
type: simulink-block
title: 'Flux Observer'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'fluxobserver'
documentation_source_path: '../mcb/ref/fluxobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux Observer

## 端口
```yaml
ports:
- name: Vα
  summary: '*α* 轴电压标量'
  direction: input
  data_types: single | double | fixed point
- name: Vβ
  summary: '*β* 轴电压标量'
  direction: input
  data_types: single | double | fixed point
- name: Iα
  summary: '*α* 轴电流标量'
  direction: input
  data_types: single | double | fixed point
- name: Iβ
  summary: '*β* 轴电流标量'
  direction: input
  data_types: single | double | fixed point
- name: Rst
  summary: 复位模块标量
  direction: input
  data_types: single | double | fixed point
- name: ParameterBus
  summary: 磁链观测器总线的计算参数
  direction: input
  data_types: single | double
- name: θe
  summary: 电机电角度位置标量
  direction: output
  data_types: single | double | fixed point
- name: Ψ
  summary: 电机转子磁链标量
  direction: output
  data_types: single | double | fixed point
- name: Te
  summary: 电机电磁转矩标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Vα** — *α* 轴电压标量

静止 *αβ* 参考坐标系中沿 *α* 轴的电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vβ** — *β* 轴电压标量

静止 *αβ* 参考坐标系中沿 *β* 轴的电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Iα** — *α* 轴电流标量

静止 *αβ* 参考坐标系中沿 *α* 轴的电流。

**数据类型：** `single` | `double` | `fixed point`

### **Iβ** — *β* 轴电流标量

静止 *αβ* 参考坐标系中沿 *β* 轴的电流。

**数据类型：** `single` | `double` | `fixed point`

### **Rst** — 复位模块标量

复位模块算法的脉冲（真值）。

**数据类型：** `single` | `double` | `fixed point`

### **ParameterBus** — 磁链观测器总线的计算参数

Flux Observer 模块的计算参数。该输入端口接受以下参数：

- **极对数**
- **定子电阻 (ohm)**
- **定子 d 轴电感 (H)**
- **定子漏电感 (H)**
- **转子漏电感 (H)**
- **励磁电感 (H)**
- **截止频率 (Hz)**

将此端口与 Compute Parameter 模块配合使用，以在运行时最优地更新前述模块参数。

#### 依赖

要启用此端口，请选择 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `single` | `double`
### 输出

### **θe** — 电机电角度位置标量

模块估计的转子电角度位置。

#### 依赖

要启用此端口，请在 **Block output** 参数中选择 **Position** 选项。

**数据类型：** `single` | `double` | `fixed point`

### **Ψ** — 电机转子磁链标量

模块估计的转子磁通量。

#### 依赖

要启用此端口，请在 **Block output** 参数中选择 **Flux** 选项。

**数据类型：** `single` | `double` | `fixed point`

### **Te** — 电机电磁转矩标量

模块估计的电机电磁转矩。

#### 依赖

要启用此端口，请在 **Block output** 参数中选择 **Torque** 选项。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Motor selection
  summary: 电机类型 PMSM（默认）| ACIM
  group: 参数
- name: Support 16-bit fixedpoint datatype
  summary: 支持 16 位定点数据类型 off（默认）| on
  group: 参数
- name: Input unit
  summary: 电压和电流输入的单位 SI unit（默认）| Per-unit
  group: 参数
- name: Base voltage (V)
  summary: 对应一个标幺值的标称电压 13.86（默认）| 标量
  group: 参数
- name: Base current (A)
  summary: 对应一个标幺值的标称电流 19.3（默认）| 标量
  group: 参数
- name: 模块输出
  summary: 模块输出选项 位置 | 磁通 | 转矩
  group: 参数
- name: 极对数
  summary: 电机中可用的极对数 4（默认）| 标量
  group: 参数
- name: 定子电阻 (ohm)
  summary: 定子绕组电阻 0.36（默认）| 标量
  group: 参数
- name: 定子 d 轴电感 (H)
  summary: 沿 *d* 轴的定子绕组电感 0.2e-3（默认）| 标量
  group: 参数
- name: 定子漏电感 (H)
  summary: 定子绕组的漏电感 0.0068（默认）| 标量
  group: 参数
- name: 转子漏电感 (H)
  summary: 转子绕组的漏电感 0.0068（默认）| 标量
  group: 参数
- name: 励磁电感 (H)
  summary: 感应电机的励磁电感 0.0300（默认）| 标量
  group: 参数
- name: 截止频率 (Hz)
  summary: 内部高通滤波器的截止频率 3.1863（默认）| 标量
  group: 参数
- name: 离散步长 (s)
  summary: 连续模块执行之间的间隔 50e-6（默认）| 标量
  group: 参数
- name: Use input port for computed parameters (run-time motor swap)
  summary: 用于启用输入端口以接受计算参数的选项 off（默认）| on
  group: 参数
- name: Position unit
  summary: 电位置输出的单位 Radians（默认）| Degrees | Per-unit
  group: Datatypes
- name: Position datatype
  summary: 电位置输出的数据类型 single（默认）| double | fixed point
  group: Datatypes
- name: Flux unit
  summary: 磁通量输出的单位 Weber（默认）| Per-unit
  group: Datatypes
- name: Per unit flux (Wb)
  summary: 对应一个 per-unit 的磁通量 0.1（默认）| scalar
  group: Datatypes
- name: Flux datatype
  summary: 磁通量输出的数据类型 single（默认）| double | fixed point
  group: Datatypes
- name: Torque unit
  summary: 电磁转矩输出的单位 Nm（默认）| Per-unit
  group: Datatypes
- name: Per unit torque (Nm)
  summary: 对应一个 per-unit 的转矩 100（默认）| scalar
  group: Datatypes
- name: Torque datatype
  summary: 电磁转矩输出的数据类型 single（默认）| double | fixed point
  group: Datatypes
```

### 参数

### **Motor selection** — 电机类型 `PMSM`（默认）| `ACIM`

从模块支持的电机类型中选择电机类型。

### **Support 16-bit fixedpoint datatype** — 支持 16 位定点数据类型 `off`（默认）| `on`

要处理 16 位定点输入并使用 16 位定点数据类型执行计算，请选择此参数。要使用 16 位定点以外的数据类型，请清除此参数。

如果选择此参数：

- 模块将 **Input unit** 参数设置为 `Per-unit`。
- 模块在 **Block output** 参数中选择 **Position** 选项，因为在使用 16 位数据类型时不支持磁链和转矩计算。

### **Input unit** — 电压和电流输入的单位 `SI unit`（默认）| `Per-unit`

选择 *α* 轴和 *β* 轴电压和电流输入值的单位。

### **Base voltage (V)** — 对应一个标幺值的标称电压 `13.86`（默认）| 标量

施加到电机的最大相电压。有关详细信息，请参阅 Per-Unit System。

#### 依赖

要启用此参数，请将 **Input unit** 设置为 `Per-unit`。

### **Base current (A)** — 对应一个标幺值的标称电流 `19.3`（默认）| 标量

供应到电机的最大可测量电流。有关详细信息，请参阅 Per-Unit System。

#### 依赖

要启用此参数，请将 **Input unit** 设置为 `Per-unit`。

### **模块输出** — 模块输出选项 **位置** | **磁通** | **转矩**

选择您希望模块计算并在模块输出中显示的一个或多个量。

**注意**

您必须至少选择一个值。如果在未选择任何值的情况下点击 **确定** 或 **应用**，模块将显示错误消息。

### **极对数** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数：

- 在 **模块输出** 参数中选择 **转矩** 选项。
- 清除 **高级选项** 部分中提供的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **定子电阻 (ohm)** — 定子绕组电阻 `0.36`（默认）| 标量

电机的定子相绕组电阻，单位为欧姆。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **定子 d 轴电感 (H)** — 沿 *d* 轴的定子绕组电感 `0.2e-3`（默认）| 标量

电机沿 *d* 轴的定子绕组电感，单位为亨利。

#### 依赖关系

要启用此参数：

- 将 **电机选择** 设置为 `PMSM`。
- 清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **定子漏电感 (H)** — 定子绕组的漏电感 `0.0068`（默认）| 标量

感应电机定子绕组的漏电感，单位为亨利。

#### 依赖关系

要启用此参数：

- 将 **电机选择** 设置为 `ACIM`。
- 清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **转子漏电感 (H)** — 转子绕组的漏电感 `0.0068`（默认）| 标量

感应电机转子绕组的漏电感，单位为亨利。

#### 依赖关系

要启用此参数：

- 将 **电机选择** 设置为 `ACIM`。
- 清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **励磁电感 (H)** — 感应电机的励磁电感 `0.0300`（默认）| 标量

感应电机的励磁电感，单位为亨利。

#### 依赖关系

要启用此参数：

- 将 **电机选择** 设置为 `ACIM`。
- 清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **截止频率 (Hz)** — 内部高通滤波器的截止频率 `3.1863`（默认）| 标量

内部高通滤波器（用于滤除噪声）的截止频率，单位为赫兹。

Flux Observer 模块使用内部一阶 IIR 高通滤波器。将此滤波器的 **截止频率 (Hz)** 设置为低于电机最低速度对应电气频率的值。例如，您可以输入电机电流最低频率十分之一的值。但是，您可以调整此值以确定更准确的截止频率，从而生成所需的模块输出。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中的 **使用输入端口获取计算参数（运行时电机切换）** 参数。

### **离散步长 (s)** — 连续模块执行之间的间隔 `50e-6`（默认）| 标量

两次连续模块执行实例之间的固定时间间隔，单位为秒。

### **Use input port for computed parameters (run-time motor swap)** — 用于启用输入端口以接受计算参数的选项 `off`（默认）| on

选择此参数以启用 **ParameterBus** 输入端口，并禁用以下参数：

- **Pole pairs**
- **Stator resistance (ohm)**
- **Stator d-axis inductance (H)**
- **Stator leakage inductance (H)**
- **Rotor leakage inductance (H)**
- **Magnetizing inductance (H)**
- **Cutoff frequency (Hz)**

此参数使您能够将输入端口与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。

### Datatypes

### **Position unit** — 电位置输出的单位 `Radians`（默认）| `Degrees` | `Per-unit`

电位置输出的单位。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Position** 选项。

### **Position datatype** — 电位置输出的数据类型 `single`（默认）| `double` | `fixed point`

电位置输出的数据类型。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Position** 选项。

### **Flux unit** — 磁通量输出的单位 `Weber`（默认）| `Per-unit`

磁通量输出的单位。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Flux** 选项。

### **Per unit flux (Wb)** — 对应一个 per-unit 的磁通量 `0.1`（默认）| scalar

对应一个 per-unit 的磁通量值（以 weber 为单位）。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数：

- 在 **Block output** 参数中选择 **Flux** 选项。
- 将 **Flux unit** 参数设置为 `Per-unit`。

### **Flux datatype** — 磁通量输出的数据类型 `single`（默认）| `double` | `fixed point`

磁通量输出的数据类型。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Flux** 选项。

### **Torque unit** — 电磁转矩输出的单位 `Nm`（默认）| `Per-unit`

电磁转矩输出的单位。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Torque** 选项。

### **Per unit torque (Nm)** — 对应一个 per-unit 的转矩 `100`（默认）| scalar

对应一个 per-unit 的转矩值（以 Nm 为单位）。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数：

- 在 **Block output** 参数中选择 **Torque** 选项。
- 将 **Torque unit** 参数设置为 `Per-unit`。

### **Torque datatype** — 电磁转矩输出的数据类型 `single`（默认）| `double` | `fixed point`

电磁转矩输出的数据类型。

#### 依赖关系

要启用此参数，请在 **Block output** 参数中选择 **Torque** 选项。
## 所属库

Motor Control Blockset HDL Support / Sensorless Estimators Motor Control Blockset / Sensorless Estimators

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
| **ConstrainedOutputPipeline** | 通过在设计内部移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅 Resource Sharing (HDL Coder)。 |

**限制**

- 仅当您将 **Motor selection** 参数设置为 `PMSM` 时，该模块才支持 HDL 代码生成。
- 在以下情况下，该模块不支持 HDL 代码生成：

  - 输入或输出信号具有混合数据类型。
  - 选中参数 **Support 16-bit fixedpoint datatype**。
  - 输入或输出信号具有大小小于 16 位的定点数据类型。
- 该模块需要原生浮点库来支持具有 HDL 代码生成的定点数据类型。
- 如果您运行第三方 (3p) 仿真，由于使用浮点数据类型的内部三角函数，该模块可能会在仿真结果中显示轻微不匹配（约为 `1e-7` 量级）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算转子的电位置、磁通量和电磁转矩

Flux Observer 模块使用静止 *αβ* 参考坐标系中沿 *α-* 和 *β*-轴的单位电压和电流值，计算表面贴装永磁同步电机 (SPMSM) 或感应电机的电位置、磁通量和电磁转矩。

该模块还接受 16 位定点数据类型输入。为了对 16 位定点数据类型信号执行数学运算，该模块使用方程的优化实现来保持尽可能最佳的精度。

此外，您可以使用高级选项启用 **ParameterBus** 输入端口，您可以将其与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。当电机参数可能随时间变化时，例如在构建可能需要在运行时更换电机的应用时，您可以使用此功能。

### 方程

这些方程描述了模块如何在 *αβ* 参考坐标系中计算 SPMSM 的电气位置、磁通量和电磁转矩。

ψα= ∫​(Vα−IαR)dt− (Ls⋅Iα)

ψβ= ∫​(Vβ−IβR)dt− (Ls⋅Iβ)

如果 (Vα−IαR)=v1(t) 且 (Vβ−IβR)=v2(t)

那么，以下拉普拉斯变换表示 *Ψα* 和 *Ψβ* 中可用的积分项：

L(∫​v1(t)dt)=1sL(v1(t))=1sv1(s)L(∫​v2(t)dt)=1sL(v2(t))=1sv2(s)

模块使用基于低通滤波器 (LPF) 的积分器来计算这些积分项。

如果电机的输入电气速度 (*ωe*) 远大于基于 LPF 的积分器截止频率对应的速度 (*ωc*)，则

L(∫​v1(t)dt)=1(s+ωc)v1(s)L(∫​v2(t)dt)=1(s+ωc)v2(s)

基于 LPF 的积分器不允许任何直流偏移（在模块输入中）使模块输出斜坡上升。例如，考虑一个对应于阶跃输入 *x(t) = k\*u(t)* 的输入函数 *X(s)=k/s*。使用前述基于 LPF 的积分器传递函数 G(s)=1(s+ωc)，我们得到：

Y(s)=G(s)X(s)=ks(s+ωc)=kωc(1s)−kωc(1s+ωc)Y(t)=kωcu(t)−kωcexp(−ωct)u(t)

根据前述方程，LPF 积分器的阶跃响应渐近稳定到一个直流值（该值取决于阶跃输入的幅值）。而纯积分器的阶跃响应是斜坡函数。在 LPF 积分器输出端使用高通滤波器可以完全消除（输入中存在的）直流偏移。

ψ= ψα2+ψβ2

Te=32P(ψαIβ−ψβIα)

θe= tan−1ψβψα

这些方程描述了模块如何计算感应电机的转子电气位置、转子磁通量和电磁转矩。

ψα=LrLm (∫​(Vα−IαR)dt− σLsIα)

ψβ=LrLm (∫​(Vβ−IβR)dt− σLsIβ)

σ=1−Lm2Lr⋅Ls

ψ= ψα2+ψβ2

Te=32⋅P⋅LmLr(ψαIβ−ψβIα)

θe= tan−1ψβψα

其中：

- Vα 和 Vβ 是 *α* 轴和 *β* 轴电压（伏特）。
- Iα 和 Iβ 是 *α* 轴和 *β* 轴电流（安培）。
- R 是电机的定子电阻（欧姆）。
- Ls 是电机的定子电感（亨利）。
- Lr 是电机的转子电感（亨利）。
- Lm 是电机的励磁电感（亨利）。
- σ 是感应电机的总漏磁系数。
- P 是电机极对数。
- ψ 是转子磁通量（韦伯）。
- ψα 和 ψβ 是沿 *α* 轴和 *β* 轴的转子磁通量（韦伯）。
- Te 是转子的电磁转矩（Nm）。
- θe 是转子的电气位置（弧度）。
