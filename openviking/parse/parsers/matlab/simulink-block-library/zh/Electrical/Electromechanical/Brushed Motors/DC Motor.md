---
type: simulink-block
title: 'DC Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'dcmotor'
documentation_source_path: 'ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

### 守恒端口

### **+** — 正极端子电气

与 DC Motor 正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与 DC Motor 负极端子关联的电气守恒端口。

### **C** — 电机外壳机械

与 DC Motor 外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与 DC Motor 转子关联的机械旋转守恒端口。

### **F+** — 正励磁电气

与正励磁绕组关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Field type** 设置为 `Wound`。

### **F-** — 负励磁电气

与负励磁绕组关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Field type** 设置为 `Wound`。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### **Selected part** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商组件的选项。点击 **<click to select>** 超链接以打开 Block Parameterization Manager 窗口。有关 Block Parameterization Manager 的详细信息，请参阅 Load Predefined Parameterizations。

### 电磁转矩

### **Field type** — 励磁类型 `Permanent Magnet`（默认）| `Wound`

选择以下励磁类型方法之一：

- `Permanent Magnet` — 使用永磁体生成 DC Motor 磁场。
- `Wound` — 使用流经绕组的电流生成 DC Motor 磁场。

### **Model parameterization** — 模块参数化 `By equivalent circuit parameters`（默认）| `By stall torque & no-load speed` | `By rated load and speed`

选择以下模块参数化方法之一：

- `By equivalent circuit parameters` — 为电机的等效电路模型提供电气参数。
- `By stall torque & no-load speed` — 提供转矩和转速参数，模块将其转换为电机的等效电路模型。
- `By rated load and speed` — 提供功率和转速参数，模块将其转换为电机的等效电路模型。

#### 依赖关系

要启用此参数，请将 **Field type** 设置为 `Permanent magnet`。

### **Field resistance** — 励磁电阻 `100` `Ohm`（默认）

磁场的电阻。

#### 依赖关系

要启用此参数，请将 **Field type** 设置为 `Wound`。

### **Field inductance** — 励磁电感 `1` `H`（默认）

磁场的电感。

#### 依赖关系

要启用此参数，请将 **Field type** 设置为 `Wound`。

### **Field-armature mutual inductance** — 励磁-电枢互感 `0.15` `H`（默认）

磁场与电机导电部分之间的互感。

#### 依赖关系

要启用此参数，请将 **Field type** 设置为 `Wound`。

### **Initial field current** — 初始励磁电流 `0` `A`（默认）

初始励磁电流。

#### 依赖关系

要启用此参数，请将 **Field type** 设置为 `Wound`。

### **Armature resistance** — 电枢电阻 `3.9` `Ohm`（默认）

电机导电部分的电阻。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By equivalent circuit parameters`。

### **Armature inductance** — 电枢电感 `12e-6` `H`（默认）

电机导电部分的电感。如果没有关于此电感的信息，请将此参数的值设置为一个较小的非零数。

### **Define back-emf or torque constant** — 常数指定 `Specify back-emf constant`（默认）| `Specify torque constant`

指示您将指定电机的反电动势常数还是转矩常数。当以 SI 单位指定时，这些常数具有相同的值，因此您只需在模块对话框中指定其中之一。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By equivalent circuit parameters`。

### **Back-emf constant** — 反电动势常数 `0.072e-3`（默认）| `V/rpm`

电机产生的电压与电机旋转速度之比。

#### 依赖关系

要启用此参数，请将 **Define back-emf or torque constant** 设置为 `Specify back-emf constant`。

### **Torque constant** — 转矩常数 `6.876e-4` `N*m/A`（默认）

电机产生的转矩与供给电机的电流之比。

#### 依赖关系

要启用此参数，请将 **Define back-emf or torque constant** 设置为 `Specify torque constant`。

### **Stall torque** — 堵转转矩 `0.24e-3` `N*m`（默认）

当速度近似为零时电机产生的转矩量。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By stall torque & no-load speed`。

### **No-load speed** — 空载转速 `19100` `rpm`（默认）

电机不驱动负载时的转速。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By stall torque & no-load speed` 或 `By rated load and speed`。

### **Rated speed (at rated load)** — 额定转速 `15000` `rpm`（默认）

在额定机械功率水平下的电机转速。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By rated load and speed`。

### **Rated load (mechanical power)** — 额定负载 `0.08` `W`（默认）

电机设计为在额定转速下输出的机械功率。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By rated load and speed`。

### **Rated DC supply voltage** — 额定直流电源电压 `1.5` `V`（默认）

电机额定工作电压。

#### 依赖关系

要启用此参数，请将 **Model parameterization** 设置为 `By stall torque & no-load speed` 或 `By rated load and speed`。

### **Rotor damping parameterization** — 转子阻尼参数化 `By damping value`（默认）| `By no-load current`

选择以下指定转子阻尼的方法之一：

- `By damping value` — 通过 **Mechanical** 参数中的 **Rotor damping** 参数直接指定转子阻尼值。
- `By no-load current` — 模块根据您为 **No-load current** 和 **DC supply voltage when measuring no-load current** 参数指定的值计算转子阻尼。如果选择此选项，**Mechanical** 参数中的 **Rotor damping** 参数将不可用。

### **No-load current** — 空载电流 `0` `A`（默认）

指定空载电流值，用于计算转子阻尼。

#### 依赖关系

要启用此参数，请将 **Rotor damping parameterization** 设置为 `By no-load current`。

### **DC supply voltage when measuring no-load current** — 测量空载电流时的直流电源电压 `1.5` `V`（默认）

指定与空载电流值对应的直流电源电压，用于计算转子阻尼。

#### 依赖关系

要启用此参数，请将 **Rotor damping parameterization** 设置为 `By no-load current`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `g*cm^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子耗散能量 `0` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

#### 依赖关系

要启用此参数，请将 **Electrical Torque** 设置中的 **Rotor damping parameterization** 参数设置为 `By damping value`。

### **Initial rotor speed** — 初始转子速度 `0` `rpm`（默认）

仿真开始时转子的速度。

### 温度依赖性

此选项卡仅对具有暴露热端口的模块显示。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻温度系数。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

定义电机参数时的温度。

### 热端口

此选项卡仅对具有暴露热端口的模块显示。

### **Thermal mass** — 热质量 `100` `J/K`（默认）

热质量是将温度升高一度所需的能量。

### **Initial temperature** — 初始温度 `25` `degC`（默认）

仿真开始时热端口的温度。

### 故障

### **Armature winding fault** — 添加电枢绕组故障的选项 `Add fault`（默认）

向 DC Motor 模块的电枢绕组添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Fraction of revolution during which armature is open-circuit** — 电枢开路期间的旋转比例 `1/3`（默认）

DC Motor 旋转过程中电枢绕组发生故障且电压源观察到开路的比例。有关详细信息，请参阅 Faults 部分。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Faulted armature winding open-circuit conductance** — 故障电枢绕组的开路电导 `1e-5` `S`（默认）

电枢绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障在仿真期间根据故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障根据模块对话框中不可用的附加触发器注入。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障根据反映信号相关行为的条件注入。条件在每个时间步评估 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为真时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为真时，模块进入故障状态；当触发条件为假时，模块进入非故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible armature winding current** — 最大允许电枢绕组电流 `inf` `A`（默认）

电枢绕组开路故障的负载电流上限阈值。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding armature winding current** — 超过电枢绕组电流时的故障时间 `1` `s`（默认）

在触发行为故障之前，绕组电流必须持续超过最大允许电枢绕组电流的时间量。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **Trigger type** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **Trigger type**。

#### 依赖关系

要启用此参数，请点击 **Armature winding fault** 参数的 **Add fault** 超链接，并将 **Trigger type** 设置为 `Behavioral`。

### **Field winding fault** — 添加励磁绕组故障的选项 `Add fault`（默认）

向 DC Motor 模块的励磁绕组添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请在 **Electrical Torque** 设置中将 **Field type** 设置为 `Wound`。

### **Faulted field winding open-circuit conductance** — 故障励磁绕组的开路电导 `1e-5` `S`（默认）

励磁绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。

### **Trigger type** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 故障在仿真时间达到 **Trigger fault at time** 参数指定的值时注入。
- `Behavioral` — 故障根据仿真期间的故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障根据模块对话框中不可用的附加触发器注入。选择此选项并点击 **Open fault properties** 超链接，在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障根据反映信号相关行为的条件注入。条件在每个时间步对 **Condition** 参数中的布尔表达式求值。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时模块进入无故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Timed`。

### **Maximum permissible field winding current** — 最大允许励磁绕组电流 `inf` `A`（默认）

励磁绕组开路故障的负载电流上限阈值。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Time to fail when exceeding field winding current** — 超过励磁绕组电流时的失效时间 `1` `s`（默认）

在触发行为故障之前，绕组电流必须持续超过最大允许励磁绕组电流的时间量。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Behavioral`。

### **Trigger configuration** — 启用附加触发类型的选项 `Open fault properties`

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque** 设置中，将 **Field type** 设置为 `Wound`。
- 点击 **Field winding fault** 参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为 `Additional triggers`。

## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2025a：对可逆条件故障建模

您现在可以通过清除 **Trigger stays on once activated** 参数，在 DC Motor 模块中对可逆条件故障建模。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时模块进入无故障状态。

在 R2025a 之前，当触发条件首次变为 true 时模块进入故障状态，并在仿真剩余时间内保持故障状态。

如果您在 R2025a 之前创建了模型并在 DC Motor 模块中启用了条件故障，则模块现在默认选择 **Trigger stays on once activated** 参数以保持向后兼容性。

## 描述

具有电气和转矩特性以及故障建模的直流电机模型

DC Motor 模块使用此等效电路模型表示直流电机的电气和转矩特性。

直流电机模型

当您将 **Model parameterization** 参数设置为 `By equivalent circuit parameters` 时，您需要为该模型指定等效电路参数。电阻 *R* 对应于您在 **Armature resistance** 参数中指定的电阻。电感 L 对应于您在 **Armature inductance** 参数中指定的电感。

您可以通过将 **Field type** 参数设置为所需选项来指定如何生成直流电机的磁场。电机中的永磁体在电枢中感应出以下反电动势 *vb*：

vb=kvω

其中 *kv* 是 **Back-emf constant**，*ω* 是角速度。电机产生以下转矩，与电机电流 *i* 成正比：

TE=kti

其中 *kt* 是 **Torque constant**。DC Motor 模块假设没有电磁损耗。这意味着机械功率等于电枢中反电动势耗散的电气功率。将这两项相等可得：

TEω=vbiktiω=kvωikv=kt

因此，您在模块参数中指定 *kv* 或 *kt* 之一。

如果磁场由流过绕组的电流产生，则 **Back-emf constant** 取决于励磁电流 *If*：

kv=LafIf

其中 *Laf* 是 **Field-armature mutual inductance**。

DC Motor 模块的转矩-速度特性与上图中的参数相关。当您将 **Model parameterization** 参数设置为 `By stall torque & no-load speed` 或 `By rated load and speed` 时，模块按如下方式求解等效电路参数：

1. 对于稳态转矩-速度关系，*L* 没有影响。
2. 对回路电压求和并整理求 *i*：

   i=V−vbR=V−kvωR
3. 将此 *i* 值代入转矩方程：

   TE=ktR(V−kvω)

   当您将 **Model parameterization** 参数设置为 `By stall torque & no-load speed` 时，模块使用堵转转矩和空载速度来确定 *R* 和 *kt*（以及等效的 *kv*）的值。

   当您将 **Model parameterization** 参数设置为 `By rated load and speed` 时，模块使用额定速度和功率计算额定转矩。模块使用额定转矩和空载速度值来确定 *R* 和 *kt* 的值。

对于 **Model parameterization** 参数的所有值，模块都对电机惯量 *J* 和阻尼 *λ* 建模。模块上的合成转矩为：

T=ktR(V−kvω)−Jω˙−λω

转子阻尼并不总是可以测量，制造商数据表中也不总是提供转子阻尼。另一种方法是使用空载电流来推断转子阻尼的值。

对于空载，电气产生的机械转矩必须等于转子阻尼转矩：

ktinoload=λωnoload

其中 *i*noload 是空载电流。如果您为 **Rotor damping parameterization** 参数选择 `By no-load current`，则此方程与转矩-速度方程一起用于确定 *λ* 和其他方程系数的值。

转子阻尼的值，无论是直接指定还是以空载电流表示，在确定 **Model parameterization** 选项 `By stall torque and no-load speed` 和 `By rated load and speed` 的等效电路参数时都会被考虑在内。

当正电流从电气 **+** 端口流向 **-** 端口时，正转矩从机械 **C** 端口作用于 **R** 端口。

**注意**

Simscape™ Electrical™ 包含多个可以对同一类型电机或执行器建模的模块。请选择具有足够建模细节的模块来回答您需要解决的工程设计问题。不要使用建模细节超过您需要的模块，因为高保真模型会减慢仿真速度并且参数化更复杂。

像 DC Motor 模块这样的模块使用简单等效电路对具有固定或参数相关系数的电机建模。这些模型具有中等保真度。使用此模块来设计机器人技术和机电一体化等执行应用中的控制器或系统，以及在饱和和谐波对损耗影响较弱时进行效率预测。有关选择正确模块以适当保真度对电机建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 故障

要对 DC Motor 模块中的故障建模，请在 **Faults** 部分中，点击您要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

DC Motor 模块允许您对两种类型的故障建模：

- 电枢绕组故障 — 电枢绕组失效并变为开路。
- 励磁绕组故障 — 产生磁场的励磁绕组失效并变为开路。

下图显示了直流电机的通用表示，包括电刷、电枢、换向器及其绕组：

当电枢失效时，连接到此模块的电压源在电机总旋转的一部分时间内观察到开路，该时间由 **Fraction of revolution during which armature is open-circuit** 参数 `rev_faulted` 指定。下图说明了在整个旋转周期内某个 `rev_faulted` 的电路状态行为：

**故障触发器**

您使用 **Trigger type** 参数指定故障发生的方式和时间。

如果您将 **Trigger type** 设置为 `Behavioral`，DC Motor 模块在绕组电流持续超过阈值时间超过特定时间间隔时触发故障：

- 电枢绕组故障在绕组电流持续超过 **Maximum permissible armature winding current** 参数的值且持续时间超过 **Time to fail when exceeding armature winding current** 参数的值时发生。
- 励磁绕组故障在绕组电流超过 **Maximum permissible field winding current** 参数的值且持续时间超过 **Time to fail when exceeding field winding current** 参数的值时发生。

如果您将 **Trigger type** 设置为 `Conditional`，您可以选择 DC Motor 模块中的故障是否可逆*（自 R2025a 起）*。要对不可逆故障建模，请点击 **Open fault properties** 打开 Property Inspector 并选择 **Trigger stays on once activated** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。当触发条件为 true 时模块进入故障状态，当触发条件为 false 时模块进入无故障状态。

有关向模块添加故障和指定故障触发器的更多信息，请参阅 Introduction to Simscape Faults。

### 预定义参数化

永磁 DC Motor 模块有多个可用的内置参数化。要选择参数化，请将 **Model Parameterization** 参数设置为 `By equivalent circuit parameters`。

此预参数化数据允许您将模块设置为代表特定供应商的组件。这些直流电机的参数化与制造商数据表匹配。要加载预定义参数化，请双击 DC Motor 模块，点击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择您要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源获取参数值。工程判断和简化假设用于填补缺失数据。因此，预期仿真行为与实际物理行为之间存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。

### 对热效应建模

您可以暴露热端口来对将功率转换为热量的损耗效应建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
