---
type: simulink-block
title: 'DC Motor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Brushed Motors'
documentation_page: 'dcmotor'
documentation_source_path: 'ref/dcmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# DC Motor

## 端口

### 守恒

### **+** — 正端子电气

与直流电机正端子关联的电气守恒端口。

### **-** — 负端子电气

与直流电机负端子关联的电气守恒端口。

### **C** — 电机外壳机械

与直流电机外壳关联的机械旋转守恒端口。

### **R** — 电机转子机械

与直流电机转子关联的机械旋转守恒端口。

### **F+** — 正励磁电气

与正励磁绕组关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **磁场类型** 设置为 `Wound`。

### **F-** — 负励磁电气

与负励磁绕组关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **磁场类型** 设置为 `Wound`。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### **选定部件** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商组件的选项。点击 **<click to select>** 超链接以打开模块参数化管理器窗口。有关模块参数化管理器的详细信息，请参阅加载预定义参数化。

### 电气转矩

### **磁场类型** — 磁场类型 `Permanent Magnet`（默认）| `Wound`

选择以下磁场类型方法之一：

- `Permanent Magnet` — 使用永磁体生成 DC Motor 磁场。
- `Wound` — 使用流经绕组的电流生成 DC Motor 磁场。

### **模型参数化** — 模块参数化 `By equivalent circuit parameters`（默认）| `By stall torque & no-load speed` | `By rated load and speed`

选择以下模块参数化方法之一：

- `By equivalent circuit parameters` — 为电机的等效电路模型提供电气参数。
- `By stall torque & no-load speed` — 提供转矩和速度参数，模块会将其转换为电机的等效电路模型。
- `By rated load and speed` — 提供功率和速度参数，模块会将其转换为电机的等效电路模型。

#### 依赖关系

要启用此参数，请将 **磁场类型** 设置为 `Permanent magnet`。

### **励磁电阻** — 励磁电阻 `100` `Ohm`（默认）

磁场的电阻。

#### 依赖关系

要启用此参数，请将 **磁场类型** 设置为 `Wound`。

### **励磁电感** — 励磁电感 `1` `H`（默认）

磁场的电感。

#### 依赖关系

要启用此参数，请将 **磁场类型** 设置为 `Wound`。

### **励磁-电枢互感** — 励磁-电枢互感 `0.15` `H`（默认）

磁场与电机导电部分之间的互感。

#### 依赖关系

要启用此参数，请将 **磁场类型** 设置为 `Wound`。

### **初始励磁电流** — 初始励磁电流 `0` `A`（默认）

初始励磁电流。

#### 依赖关系

要启用此参数，请将 **磁场类型** 设置为 `Wound`。

### **电枢电阻** — 电枢电阻 `3.9` `Ohm`（默认）

电机导电部分的电阻。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By equivalent circuit parameters`。

### **电枢电感** — 电枢电感 `12e-6` `H`（默认）

电机导电部分的电感。如果您没有关于此电感的信息，请将此参数的值设置为一个小的非零数值。

### **定义反电动势或转矩常数** — 常数指定 `Specify back-emf constant`（默认）| `Specify torque constant`

指示您将指定电机的反电动势常数还是转矩常数。当以 SI 单位指定时，这些常数具有相同的值，因此您只需在模块对话框中指定其中之一。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By equivalent circuit parameters`。

### **反电动势常数** — 反电动势常数 `0.072e-3`（默认）| `V/rpm`

电机产生的电压与电机旋转速度之比。

#### 依赖关系

要启用此参数，请将 **定义反电动势或转矩常数** 设置为 `Specify back-emf constant`。

### **转矩常数** — 转矩常数 `6.876e-4` `N*m/A`（默认）

电机产生的转矩与输送给它的电流之比。

#### 依赖关系

要启用此参数，请将 **定义反电动势或转矩常数** 设置为 `Specify torque constant`。

### **堵转转矩** — 堵转转矩 `0.24e-3` `N*m`（默认）

当速度近似为零时电机产生的转矩量。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By stall torque & no-load speed`。

### **空载速度** — 空载速度 `19100` `rpm`（默认）

电机未驱动负载时的速度。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By stall torque & no-load speed` 或 `By rated load and speed`。

### **额定速度（额定负载时）** — 额定速度 `15000` `rpm`（默认）

电机在额定机械功率水平下的速度。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By rated load and speed`。

### **额定负载（机械功率）** — 额定负载 `0.08` `W`（默认）

电机设计为在额定速度下输出的机械功率。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By rated load and speed`。

### **额定直流电源电压** — 额定直流电源电压 `1.5` `V`（默认）

电机额定运行时的电压。

#### 依赖关系

要启用此参数，请将 **模型参数化** 设置为 `By stall torque & no-load speed` 或 `By rated load and speed`。

### **转子阻尼参数化** — 转子阻尼参数化 `By damping value`（默认）| `By no-load current`

选择以下方法之一来指定转子阻尼：

- `By damping value` — 通过使用 **机械** 参数中的 **转子阻尼** 参数直接指定转子阻尼的值。
- `By no-load current` — 模块根据您为 **空载电流** 和 **测量空载电流时的直流电源电压** 参数指定的值计算转子阻尼。如果选择此选项，则 **转子阻尼** 参数在 **机械** 参数中不可用。

### **空载电流** — 空载电流 `0` `A`（默认）

指定用于计算转子阻尼的空载电流值。

#### 依赖关系

要启用此参数，请将 **转子阻尼参数化** 设置为 `By no-load current`。

### **测量空载电流时的直流电源电压** — 测量空载电流时的直流电源电压 `1.5` `V`（默认）

指定与空载电流值对应的直流电源电压，用于计算转子阻尼。

#### 依赖关系

要启用此参数，请将 **转子阻尼参数化** 设置为 `By no-load current`。

### 机械

### **转子惯量** — 转子惯量 `0.01` `g*cm^2`（默认）

转子对电机运动变化的抵抗能力。该值可以为零。

### **转子阻尼** — 转子耗散的能量 `0` `N*m/(rad/s)`（默认）

转子耗散的能量。该值可以为零。

#### 依赖关系

要启用此参数，请将 **电气转矩** 设置中的 **转子阻尼参数化** 参数设置为 `By damping value`。

### **初始转子速度** — 初始转子速度 `0` `rpm`（默认）

仿真开始时转子的速度。

### 温度依赖性

此选项卡仅对具有外露热端口的模块显示。

### **电阻温度系数** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻温度系数。

### **测量温度** — 测量温度 `25` `degC`（默认）

定义电机参数所对应的温度。

### 热端口

此选项卡仅对具有外露热端口的模块显示。

### **热质量** — 热质量 `100` `J/K`（默认）

热质量是将温度升高一度所需的能量。

### **初始温度** — 初始温度 `25` `degC`（默认）

仿真开始时热端口的温度。

### 故障

### **电枢绕组故障** — 添加电枢绕组故障的选项 `Add fault`（默认）

用于向 DC Motor 模块的电枢绕组添加故障的选项。

要添加故障，请点击 **添加故障** 超链接。

### **电枢开路期间的旋转比例** — 电枢开路期间的旋转比例 `1/3`（默认）

直流电机旋转过程中电枢绕组发生故障且电压源观测到开路的那部分比例。有关详细信息，请参阅故障部分。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接。

### **故障电枢绕组开路电导** — 故障电枢绕组的开路电导 `1e-5` `S`（默认）

电枢绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接。

### **触发类型** — 触发类型 `Always on`（默认）| `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **在时间点触发故障** 参数指定的值时，故障注入。
- `Behavioral` — 故障在仿真期间因故障参数值而注入。将 **触发类型** 设置为 `Behavioral` 会启用用于定义故障条件的模块参数。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项，然后点击 **打开故障属性** 超链接，以在属性检查器中将 **触发类型** 设置为以下值之一：

  - `Conditional` — 故障因反映与信号关联行为的条件而注入。条件在每个时间步计算 **条件** 参数中的布尔表达式。要对不可逆故障建模，请在属性检查器中选择 **触发激活后保持开启** 参数。当触发条件首次变为 true 时，模块进入故障状态，并在仿真的剩余时间内保持故障状态。要对可逆故障建模，请清除 **触发激活后保持开启** 参数。当触发条件为 true 时，模块进入故障状态；当触发条件为 false 时，模块进入无故障状态。要了解详细信息，请参阅创建和管理条件。
  - `Manual` — 当您在 **故障仪表板** 窗格中切换状态时，故障注入或清除。要了解详细信息，请参阅在模型中手动触发故障。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接。

### **在时间点触发故障** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Timed`。

### **最大允许电枢绕组电流** — 最大允许电枢绕组电流 `inf` `A`（默认）

开路电枢绕组故障的负载电流上限阈值。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Behavioral`。

### **超过电枢绕组电流时的失效时间** — 超过电枢绕组电流时的失效时间 `1` `s`（默认）

在触发行为故障之前，绕组电流必须持续超过最大允许电枢绕组电流的时间量。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Behavioral`。

### **触发配置** — 启用附加触发类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发类型的选项。要将 **触发类型** 参数设置为 `Conditional` 或 `Manual`，请点击 **打开故障属性** 超链接，并在属性检查器中设置 **触发类型**。

#### 依赖关系

要启用此参数，请点击 **电枢绕组故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Behavioral`。

### **励磁绕组故障** — 添加励磁绕组故障的选项 `Add fault`（默认）

用于向 DC Motor 模块的励磁绕组添加故障的选项。

要添加故障，请点击 **添加故障** 超链接。

#### 依赖关系

要启用此参数，请在 **电气转矩** 设置中将 **磁场类型** 设置为 `Wound`。

### **故障励磁绕组开路电导** — 故障励磁绕组的开路电导 `1e-5` `S`（默认）

励磁绕组发生故障时的开路电导。

#### 依赖关系

要启用此参数：

- 在 **电气转矩** 设置中，将 **磁场类型** 设置为 `Wound`。
- 点击 **励磁绕组故障** 参数的 **添加故障** 超链接。

### **Trigger type** — 触发类型 `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **Trigger fault at time** 参数指定的值时，故障注入。
- `Behavioral` — 故障根据仿真期间的故障参数值注入。将 **Trigger type** 设置为 `Behavioral` 会启用定义故障条件的模块参数。
- `Additional triggers` — 故障根据模块对话框中不可用的额外触发器注入。选择此选项并单击 **Open fault properties** 超链接，以在 Property Inspector 中将 **Trigger type** 设置为以下值之一：

  - `Conditional` — 故障由反映与信号关联行为的条件导致而注入。条件会在每个时间步计算 **Condition** 参数中的布尔表达式。要对不可逆故障建模，请在 Property Inspector 中选择 **Trigger stays on once activated** 参数。该模块在触发条件首次变为 true 时进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。该模块在触发条件为 true 时进入故障状态，在触发条件为 false 时进入未故障状态。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障会注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models.

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque**
  设置中，将 **Field type** 设置为
  `Wound`。
- 单击 **Field winding fault**
  参数的 **Add fault** 超链接。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s` (default) | 非负标量

模块进入故障状态时的仿真时间。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque**
  设置中，将 **Field type** 设置为
  `Wound`。
- 单击 **Field winding fault**
  参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为
  `Timed`。

### **Maximum permissible field winding current** — 最大允许励磁绕组电流 `inf` `A` (default)

开路励磁绕组故障的负载电流上限阈值。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque**
  设置中，将 **Field type** 设置为
  `Wound`。
- 单击 **Field winding fault**
  参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为
  `Behavioral`。

### **Time to fail when exceeding field winding current** — 超过励磁绕组电流后的故障时间 `1` `s` (default)

在触发行为故障之前，绕组电流必须连续超过最大允许励磁绕组电流的时间量。

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque**
  设置中，将 **Field type** 设置为
  `Wound`。
- 单击 **Field winding fault**
  参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为
  `Behavioral`。

### **Trigger configuration** — 启用额外触发类型的选项 `Open fault properties`

#### 依赖关系

要启用此参数：

- 在 **Electrical Torque**
  设置中，将 **Field type** 设置为
  `Wound`。
- 单击 **Field winding fault**
  参数的 **Add fault** 超链接。
- 将 **Trigger type** 设置为
  `Additional
  triggers`。

## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2025a：对可逆条件故障建模

您现在可以通过清除 **Trigger stays on once activated** 参数，在 DC Motor 模块中对可逆条件故障建模。该模块在触发条件为 true 时进入故障状态，在触发条件为 false 时进入未故障状态。

在 R2025a 之前，该模块在触发条件首次变为 true 时进入故障状态，并在仿真剩余时间内保持故障状态。

如果您在 R2025a 之前创建模型并在 DC Motor 模块中启用条件故障，则该模块现在默认选择 **Trigger stays on once activated** 参数，以实现向后兼容。

## 描述

具有电气和转矩特性以及故障建模的 DC motor 模型

DC Motor 模块使用此等效电路模型表示 DC motor 的电气和转矩特性。

DC motor 模型

当您将 **Model parameterization** 参数设置为 `By equivalent circuit parameters` 时，您需要为此模型指定等效电路参数。电阻 *R* 对应于您在 **Armature resistance** 参数中指定的电阻。电感 L 对应于您在 **Armature inductance** 参数中指定的电感。

您可以通过将 **Field type** 参数设置为所需选项来指定如何生成 DC motor 的磁场。电机中的永磁体在电枢中感应出以下反电动势 *vb*：

vb=kvω

其中 *kv* 是 **Back-emf constant**，*ω* 是角速度。电机产生以下转矩，该转矩与电机电流 *i* 成正比：

TE=kti

其中 *kt* 是 **Torque constant**。DC Motor 模块假设没有电磁损耗。这意味着机械功率等于电枢中反电动势耗散的电气功率。令这两项相等，得到：

TEω=vbiktiω=kvωikv=kt

因此，您在模块参数中指定 *kv* 或 *kt*。

如果磁场由流过绕组的电流产生，则 **Back-emf constant** 取决于励磁电流 *If*：

kv=LafIf

其中 *Laf* 是 **Field-armature mutual inductance**。

DC Motor 模块的转矩-速度特性与上图参数相关。当您将 **Model parameterization** 参数设置为 `By stall torque & no-load speed` 或 `By rated load and speed` 时，该模块按如下方式求解等效电路参数：

1. 对于稳态转矩-速度关系，*L* 没有影响。
2. 对回路电压求和并重新整理求 *i*：

   i=V−vbR=V−kvωR
3. 将此 *i* 的值代入转矩方程：

   TE=ktR(V−kvω)

   当您将 **Model parameterization** 参数设置为
   `By stall torque & no-load speed` 时，该模块使用堵转转矩和空载速度来确定
   *R* 和 *kt*
   （以及等效的 *kv*）的值。

   当您将 **Model parameterization** 参数设置为
   `By rated load and speed` 时，该模块使用
   额定速度和功率计算额定转矩。该模块使用
   额定转矩和空载速度值来确定
   *R* 和
   *kt* 的值。

对于 **Model parameterization** 参数的所有值，该模块都对电机惯量 *J* 和阻尼 *λ* 建模。模块两端的合成转矩为：

T=ktR(V−kvω)−Jω˙−λω

并不总是能够测量转子阻尼，且制造商数据表中并不总是提供转子阻尼。另一种方法是使用空载电流推断转子阻尼值。

对于空载，电产生的机械转矩必须等于转子阻尼转矩：

ktinoload=λωnoload

其中 *i*noload 是空载电流。如果您为 **Rotor damping parameterization** 参数选择 `By no-load current`，则除了转矩-速度方程外，还使用此方程确定 *λ* 和其他方程系数的值。

在确定 **Model parameterization** 选项 `By stall torque and no-load speed` 和 `By rated load and speed` 的等效电路参数时，会考虑转子阻尼的值，无论它是直接指定还是根据空载电流指定。

当正电流从电气 **+** 端口流向 **-** 端口时，正转矩从机械 **C** 端口作用于 **R** 端口。

**注意**

Simscape™ Electrical™ 包含多个可对同一类型电机或执行器建模的模块。选择一个对需要回答的工程设计问题具有足够建模细节的模块。不要使用建模细节超过所需程度的模块，因为更高保真度的模型会减慢仿真速度，并且参数化更复杂。

像 DC Motor 模块这样的模块使用简单等效电路对具有固定系数或参数相关系数的电机建模。这些模型具有中等保真度。使用此模块可为执行应用（如机器人技术和机电一体化）中的控制或系统进行设计，并在饱和和谐波仅对损耗产生微弱影响时进行效率预测。有关选择合适模块以合适保真度对电机建模的更多信息，请参阅 Choose Blocks to Model Motors or Actuators。

### 故障

要对 DC Motor 模块中的故障建模，请在 **Faults** 部分中，单击您要建模的故障旁边的 **Add fault**。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

DC Motor 模块允许您对两种类型的故障建模：

- 电枢绕组故障 — 电枢绕组失效并变为开路。
- 励磁绕组故障 — 产生磁场的励磁绕组失效并变为开路。

此图显示了具有电刷、电枢、换向器及其绕组的 DC motor 的一般表示：

当电枢失效时，连接到此模块的电压源在电机总转数的一部分中观察到开路，该部分由 **Fraction of revolution during which armature is open-circuit** 参数 `rev_faulted` 指定。此图说明了在整个转数周期内某个 `rev_faulted` 的电路状态行为：

**故障触发**

您通过使用 **Trigger type** 参数指定故障的发生方式和时间。

如果将 **Trigger type** 设置为 `Behavioral`，则当绕组电流连续超过阈值的时间长于特定时间间隔时，DC Motor 模块会触发故障：

- 当绕组电流连续超过 **Maximum permissible armature winding current** 参数的值，且持续时间长于 **Time to fail when exceeding armature winding current** 参数的值时，会发生电枢绕组故障。
- 当绕组电流超过 **Maximum permissible field winding current** 参数的值，且持续时间长于 **Time to fail when exceeding field winding current** 参数的值时，会发生励磁绕组故障。

如果将 **Trigger type** 设置为 `Conditional`，您可以选择 DC Motor 模块中的故障是否可逆 *（自 R2025a 起）*。要对不可逆故障建模，请单击 **Open fault properties** 以打开 Property Inspector，并选择 **Trigger stays on once activated** 参数。该模块在触发条件首次变为 true 时进入故障状态，并在仿真剩余时间内保持故障状态。要对可逆故障建模，请清除 **Trigger stays on once activated** 参数。该模块在触发条件为 true 时进入故障状态，在触发条件为 false 时进入未故障状态。

有关向模块添加故障和指定故障触发的更多信息，请参阅 Introduction to Simscape Faults。

### 预定义参数化

永磁 DC Motor 模块有多个可用的内置参数化。要选择参数化，请将 **Model Parameterization** 参数设置为 `By equivalent circuit parameters`。

此预参数化数据允许您设置该模块以表示特定供应商的组件。这些 DC motor 的参数化与制造商数据表匹配。要加载预定义参数化，请双击 DC Motor 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源获取参数值。使用工程判断和简化假设来填补缺失数据。因此，预计仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

有关预参数化的更多信息以及可用组件列表，请参阅 List of Pre-Parameterized Components。

### 对热效应建模

您可以公开热端口，以对将功率转换为热量的损耗效应建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

有关在执行器模块中使用热端口的更多信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
