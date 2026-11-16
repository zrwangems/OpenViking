---
type: simulink-block
title: 'PTC Thermistor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'ptcthermistor'
documentation_source_path: 'ref/ptcthermistor.html'
language: zh-CN
chinese_source: worker-translation
---

# PTC Thermistor

## 端口

### 守恒

### **A** — 热质量热

与热质量相关联的热守恒端口。

### **+** — 正极端子（电气）

与正极端子相关联的电气守恒端口。

### **-** — 负极端子（电气）

与负极端子相关联的电气守恒端口。

## 参数

### 电气

### **热敏电阻参数化类型** — 热敏电阻类型 `Switching Thermistor`（默认）| `RTD (Callendar - Van Dusen coefficients)`

*自 R2024a 起*

热敏电阻类型。此参数决定模块用于将电阻计算为温度函数的方程。选择以下选项之一：

- `Switching Thermistor` — 对开关型热敏电阻建模。指定标称温度和参考温度下的温度系数与电阻。
- `RTD (Callendar - Van Dusen coefficients)` — 对电阻温度检测器建模。指定 Callendar–Van Dusen 系数以及 0 degC 下的标称电阻。

### **标称温度 T0 下的标称电阻 R0** — 标称温度下的电阻 `1000` `Ohm`（默认）| 正标量

标称温度下的电阻。数据手册通常将 25 摄氏度下的标称电阻列为 R25。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **标称温度 T0 下的温度系数 alpha0** — 标称温度下的温度系数 `-0.01` `1/K`（默认）| 负标量

标称温度下的温度系数。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **标称温度 T0** — 标称温度 `298.15` `K`（默认）| 正标量

引用标称电阻时的温度。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **参考温度 T1 下的参考电阻 R1** — 参考温度下的电阻 `10000` `Ohm`（默认）| 正标量

参考温度下的电阻。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **参考温度 T1 下的温度系数 alpha1** — 参考温度下的温度系数 `1` `1/K`（默认）| 正标量

参考温度下的温度系数。

### **参考温度 T1** — 参考温度 `398.15` `K`（默认）| 标量

引用参考电阻时的温度。此温度必须处于 PTC 区。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **0 degC 下的标称电阻 R0** — 标称温度下的电阻 `100` `Ohm`（默认）| 正标量

*自 R2024a 起*

0 摄氏度标称温度下的电阻。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### **A 系数 [degC^-1]** — `A` 系数 `3.9083e-3`（默认）| 正标量

*自 R2024a 起*

Callendar–Van Dusen 方程中的 `A` 系数。默认值对于铂 RTD 是典型的。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### **B 系数 [degC^-2]** — `B` 系数 `-5.775e-7`（默认）| 标量

*自 R2024a 起*

Callendar–Van Dusen 方程中的 `B` 系数。默认值对于铂 RTD 是典型的。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### **C 系数 [degC^-4]** — `C` 系数 `-4.183e-12`（默认）| 标量

*自 R2024a 起*

Callendar–Van Dusen 方程中的 `C` 系数。默认值对于铂 RTD 是典型的。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### 温度工作限值

### **启用温度工作限值** — 用于指定温度工作限值的选项 `No`（默认）| `Yes`

*自 R2024a 起*

用于指定温度工作限值的选项。

#### 依赖关系

要启用此参数，请将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`。

### **超出工作限值时的报告方式** — 温度超出工作范围时的报告方式 `Warn`（默认）| `Error`

*自 R2024a 起*

温度超出工作限值时的报告方式。选择以下选项之一：

- `Warn` — Simulink 显示警告，仿真继续。
- `Error` — Simulink 显示错误并终止仿真。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`，并将 **启用温度工作限值** 设置为 `Yes`。
- 将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### **最低工作温度** — 工作温度范围的下限 `223.15` `K`（默认）| 标量

*自 R2024a 起*

工作温度范围的下限。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`，并将 **启用温度工作限值** 设置为 `Yes`。
- 将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### **最高工作温度** — 工作温度范围的上限 `428.15` `K`（默认）| 标量

*自 R2024a 起*

工作温度范围的上限。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **热敏电阻参数化类型** 设置为 `Switching Thermistor`，并将 **启用温度工作限值** 设置为 `Yes`。
- 将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。

### 热

### **热时间常数** — 热时间常数 `5.0` `s`（默认）| 正标量

当环境温度发生阶跃变化时，热敏电阻温度变化达到最终温度变化的 63% 所需的时间。

### **耗散系数** — 耗散系数 `0.75e-3` `W/K`（默认）| 正标量

使热敏电阻温度升高 1 K 所需的热功率。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2024a：对电阻温度检测器建模

现在可以对电阻温度检测器（RTD）建模。模块使用 Callendar–Van Dusen 方程计算电阻随温度的变化。要启用此选项，请将 **热敏电阻参数化类型** 参数设置为 `RTD (Callendar – Van Dusen coefficients)`。

如果对 RTD 建模，则必须指定工作温度限值。如果对开关型热敏电阻建模，现在可以选择指定工作温度限值。

### R2024a：对自热建模

PTC Thermistor 模块现在对自热建模。以下方程描述模块的热行为：

\[
Q=K_d t_c \frac{dT}{dt}-I^2R.
\]

有关每个变量的定义，请参阅描述。

在 2024a 之前，模块使用的方程不包含 *I*²*R* 项。此更改提高了建模精度，而不会减慢仿真。

由于此更改，不得将模块连接到理想电流源，因为这种配置会形成正反馈回路，导致热失控。

## 描述

正温度系数 (PTC) 热敏电阻

PTC Thermistor 模块对正温度系数 (PTC) 热敏电阻建模。要对开关型 PTC 热敏电阻或电阻温度检测器 (RTD) 建模，请使用此模块。要对非开关型线性 PTC 热敏电阻建模，请使用 Thermal Resistor 模块。

模块的热行为使用方程

\[
Q=K_d t_c \frac{dT}{dt}-I^2R,
\]

其中：

- *Q* 是流入 **A** 端口的净热流。
- *K*d 是 **耗散系数** 参数值。
- *t*c 是 **热时间常数** 参数值。
- *dT/dt* 是温度相对于时间的变化率。
- *I* 是电流。
- *R* 是电阻。

**注意**

不得将 PTC Thermistor 模块连接到理想电流源。这种配置会形成正反馈回路，导致热失控，因为：

- 温度升高会增加电阻
- 在理想电流源下，电阻增加会增加电压
- 电压增加会增加耗散功率
- 耗散功率增加会升高温度，从而闭合回路

### 温度工作限值

*自 R2024a 起*

如果将 **热敏电阻参数化类型** 参数设置为 `Switching Thermistor`，则可以通过 **启用温度工作限值** 参数选择是否指定工作温度范围。如果将 **热敏电阻参数化类型** 参数设置为 `RTD (Callendar - Van Dusen coefficients)`，则必须指定工作温度范围。

分别通过设置 **最低工作温度** 和 **最高工作温度** 参数来指定温度工作限值的下限和上限。请在数据手册中查找这些值。如果温度超出工作限值：

- 如果将 **超出工作限值时的报告方式** 设置为 `Warn`，Simulink® 会显示警告，仿真继续。
- 如果将 **超出工作限值时的报告方式** 设置为 `Error`，Simulink 会显示错误并终止仿真。

### 开关型热敏电阻

要对开关型 PTC 热敏电阻建模，请将 **热敏电阻参数化类型** 参数设置为 `Switching Thermistor`。此类热敏电阻的电阻随温度升高而降低，直至居里温度 *T*c。高于居里温度时，电阻随温度升高而快速增加。此图中 *T*c 右侧的区域称为 *PTC 区*。

以下方程定义温度 *T* 下的电阻 *R*，

\[
R=\begin{cases}
R_0 e^{\alpha_0 (T-T_0)} & \text{for } T \le T_c\\
R_1 e^{\alpha_1 (T-T_1)} & \text{for } T \ge T_c
\end{cases}
\]

\[
T_c=\frac{\log(R_1)-\log(R_0)+\alpha_0 T_0-\alpha_1 T_1}{\alpha_0-\alpha_1}
\]

其中：

- *R*0 是标称温度下的电阻。
- *R*1 是参考温度下的电阻。
- *α*0 是标称温度下的温度系数。
- *α*1 是参考温度下的温度系数。
- *T*0 是标称温度，即引用标称电阻时的温度，通常为室温。*T*0 必须小于居里温度。
- *T*1 是参考温度，即引用参考电阻时的温度。*T*1 必须处于 PTC 区。

### 电阻温度检测器

*自 R2024a 起*

要对 RTD 建模，请将 **热敏电阻参数化类型** 设置为 `RTD (Callendar - Van Dusen coefficients)`。Callendar–Van Dusen 方程定义温度 *T* 下的电阻 *R*。此方程使用以 degC 测量的 *T*，

\[
R=\begin{cases}
R_0(1+AT+BT^2+C(T-100)T^3) & \text{for } T \le 0\\
R_0(1+AT+BT^2) & \text{for } T \ge 0
\end{cases}
\]

其中：

- *R*0 是 0 degC 标称温度下的电阻。
- *A*、*B* 和 *C* 是 Callendar–Van Dusen 系数。

可以在数据手册中找到这些系数。模块使用的默认参数值对于铂 RTD 是典型的。*R*-*T* 特性在工作温度范围内近似线性，因此请选择比 *A* 小几个数量级的 *B* 和 *C* 值。

Simulink 显示警告 if 电阻在工作温度范围内不是单调增加。如果将 **超出工作限值时的报告方式** 参数设置为 `Warn`，且温度超出工作范围，则模块使用线性外推计算电阻随温度的变化。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
