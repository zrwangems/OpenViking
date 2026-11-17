---
type: simulink-block
title: 'Induction Machine (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Asynchronous'
documentation_page: 'inductionmachinesinglephase'
documentation_source_path: 'ref/inductionmachinesinglephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine (Single-Phase)

## 端口

### 输出

### **pu** — 电机标幺值测量物理信号 | 向量

与电机标幺值测量相关联的物理信号向量端口。向量元素为：

- pu\_torque
- pu\_velocity
- pu\_vds
- pu\_vqs
- pu\_v0s = 0
- pu\_ids
- pu\_iqs
- pu\_i0s = 0
### 守恒

### **a1** — 主绕组正极端子 电气 | 标量

与主绕组正极端子相关联的电气守恒端口。

### **a2** — 主绕组负极端子 电气 | 标量

与主绕组负极端子相关联的电气守恒端口。

### **b1** — 辅助绕组正极端子 电气 | 标量

与辅助绕组正极端子相关联的电气守恒端口。

#### 依赖关系

仅当将 **Type** 设置为 `Main
and auxiliary windings` 时，此端口才可见。

### **b2** — 辅助绕组负极端子 电气 | 标量

与辅助绕组负极端子相关联的电气守恒端口。

#### 依赖关系

仅当将 **Type** 设置为 `Main
and auxiliary windings` 时，此端口才可见。

### **R** — 电机转子机械旋转

与电机转子相关联的机械旋转守恒端口。

### **C** — 电机机壳机械旋转

与电机机壳相关联的机械旋转守恒端口。

### **HA** — 主绕组热端口 热

与定子主绕组相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。

### **HB** — 辅助绕组热端口 热

与定子辅助绕组相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

### **HR** — 转子热端口 热

与转子相关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对生成的热量和电机温度的影响进行建模。

### 主要

### **Type** — 感应电机类型 `Split-phase`（默认）| `Capacitor-start` | `Capacitor-start-capacitor-run` | `Main and auxiliary windings`

感应电机的类型。

### **Rated apparent power** — 额定视在功率 `180` `V*A`（默认）| 正标量

感应电机的额定视在功率。

### **Rated voltage** — 额定电压 `220` `V`（默认）| 正标量

RMS 电压。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

对应于额定视在功率的标称电气频率。

### **Number of pole pairs** — 极对数 `2`（默认）| 正整数

电机极对数。该值用作反电动势常数。

### **Parameterization unit** — SI 或标幺值参数化选项 `SI`（默认）| `Per unit`

用于模块参数化的单位制。

#### 依赖关系

选择：

- `SI` 会显示 SI
  **Electrical** 参数。
- `Per unit` 会显示标幺值
  **Electrical** 参数。

### 电气

对于 **Main** 设置中的 **Parameterization unit** 参数，选择 `SI` 以
显示 SI **Electrical** 参数，或选择 `Per
unit` 以显示标幺值 **Electrical**
参数。

### **Main winding stator resistance, Ras** — 主绕组定子电阻 `1.8180` `Ohm`（默认）| 正标量

主绕组的 SI 定子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Main winding stator leakage inductance, Llas** — 主绕组定子漏电感 `0.0067` `H`（默认）| 正标量

主绕组的 SI 漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Main winding rotor resistance, Rar'** — 主绕组转子电阻 `3.7080` `Ohm`（默认）| 正标量

主绕组的 SI 转子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Main winding rotor leakage inductance, Llar'** — 主绕组转子漏电感 `0.0050` `H`（默认）| 正标量

主绕组的 SI 转子漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Main winding mutual inductance, Lms** — 主绕组互感 `0.1595` `H`（默认）| 正标量

主绕组的 SI 互感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Auxiliary winding stator resistance, Rbs** — 辅助绕组定子电阻 `6.4260` `Ohm`（默认）| 正标量

辅助绕组的 SI 定子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Auxiliary winding stator leakage inductance, Llbs** — 辅助绕组定子漏电感 `0.0077` `H`（默认）| 正标量

辅助绕组的 SI 定子漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `SI`
会显示 SI
**Electrical** 参数。

### **Auxiliary/main windings turn ratio** — 匝比 `1.1`（默认）| 正标量

主绕组与辅助绕组之间的绕组比。

### **Main winding stator resistance, Ras (pu)** — 主绕组定子电阻 `0.0135`（默认）| 正标量

主绕组的标幺值定子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Main winding stator leakage inductance, Llas (pu)** — 主绕组定子漏电感 `0.0188`（默认）| 正标量

主绕组的标幺值漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Main winding rotor resistance, Rar' (pu)** — 主绕组转子电阻 `0.0276`（默认）| 正标量

主绕组的标幺值转子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Main winding rotor leakage inductance, Llar' (pu)** — 主绕组转子漏电感 `0.0140`（默认）| 正标量

主绕组的标幺值转子漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Main winding mutual inductance, Lms (pu)** — 主绕组互感 `0.4472`（默认）| 正标量

主绕组的标幺值互感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Auxiliary winding stator resistance, Rbs (pu)** — 辅助绕组定子电阻 `0.0478`（默认）| 正标量

辅助绕组的标幺值定子电阻。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Auxiliary winding stator leakage inductance, Llbs (pu)** — 辅助绕组定子漏电感 `0.0216`（默认）| 正标量

辅助绕组的标幺值定子漏电感。

#### 依赖关系

在 **Main** 设置中为
**Parameterization unit** 参数选择 `Per unit`
会显示标幺值
**Electrical** 参数。

### **Auxiliary/main windings turn ratio** — 匝比 `1.1`（默认）| 正标量

主绕组与辅助绕组之间的绕组比。

### **Capacitor-start resistance, Rs** — 启动电容电阻 `3` `Ohm`（默认）| 正标量

SI 启动电容电阻。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run` 或
`Capacitor-start`，并将
**Parameterization unit** 设置为
`SI`。

### **Capacitor-start capacitance, Cs** — 启动电容电容值 `0.00018` `F`（默认）| 正标量

SI 启动电容电容值。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run` 或
`Capacitor-start`，并将
**Parameterization unit** 设置为
`SI`。

### **Capacitor-run resistance, Rr** — 运行电容电阻 `9` `Ohm`（默认）| 正标量

SI 运行电容电阻。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为
`SI`。

### **Capacitor-run capacitance, Cr** — 运行电容电容值 `0.000015` `F`（默认）| 正标量

SI 运行电容电容值。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为
`SI`。

### **Capacitor-start resistance, Rs (pu)** — 启动电容电阻 `0.0223`（默认）| 正标量

标幺值启动电容电阻。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为 `Per
unit`。

### **Capacitor-start capacitance, Cs (pu)** — 启动电容电容值 `9.1232`（默认）| 正标量

标幺值启动电容电容值。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为 `Per
unit`。

### **Capacitor-run resistance, Rr (pu)** — 运行电容电阻 `0.0669`（默认）| 正标量

标幺值运行电容电阻。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为 `Per
unit`。

### **Capacitor-run resistance, Cr (pu)** — 运行电容电容值 `0.000015`（默认）| 正标量

标幺值运行电容电容值。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Capacitor-start-capacitor-run`，并将
**Parameterization unit** 设置为 `Per
unit`。

### **Disconnection speed (% of rated speed)** — 断开速度 `80`（默认）| 范围 [0,100] 内的标量

电容断开时的速度，以额定速度的百分比表示。该值必须介于 `0` 和
`100` 之间（含端点）。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Split-phase`、
`Capacitor-start` 或
`Capacitor-start-capacitor-run`。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认）| 正标量

转子的惯量。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认）| 标量

转子的阻尼。

### 热

这些参数仅对具有暴露热端口的模块显示。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认）| 实标量

电机参数的标称温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| 正标量

所有三个绕组的电阻与温度关系方程中的系数 α，如 Thermal Model for Actuator Blocks 中所述。默认值
`3.93e-3` 1/K 适用于铜。

### **Cage resistance temperature coefficient** — 转子温度系数 `4.4e-3`（默认）| `1/K` | 标量

转子笼型电阻与温度的关系系数。默认值
`4.4e-3` 1/K 适用于铝。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| 正标量

每个定子绕组的热质量值。热质量是将温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| 正标量

转子的热质量。热质量是将转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2021b：感应电机类型参数

从 R2021b 起，要对不同类型的感应电机进行建模，请将
**Type** 参数设置为
`Split-phase`、
`Capacitor-start`、
`Capacitor-start-capacitor-run` 或 `Main
and auxiliary windings`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Type** 参数。

## 描述

具有 SI 或 pu 基本参数化的单相感应电机

Induction Machine (Single-Phase) 模块表示具有鼠笼式转子的单相感应电机，其基本参数
以标幺值或国际单位制 (SI) 表示。

此模块对四种类型的单相感应电机进行建模：

- `Split-phase`
- `Capacitor-start`
- `Capacitor-start-capacitor-run`
- `Main and auxiliary windings`

单相感应电机由鼠笼式转子和两个定子绕组（主绕组和辅助绕组）组成。辅助绕组通常仅在启动期间
激活。然而，为提高性能，在低功率应用中辅助绕组可在运行期间保持激活。该图显示了主绕组和
辅助绕组的等效 *d* 轴和 *q* 轴电路。

下表定义了变量。

| 变量 | 定义 |
| --- | --- |
| *vqs**vds* | *d*-*q* 表示中的定子电压 |
| *iqs**ids* | *d*-*q* 表示中的定子电流 |
| *Ψqr**Ψdr* | *d*-*q* 表示中的转子磁链 |
| *⍵* | 转子电气速度 |
| *a* | 辅助/主绕组匝比 |
| *Ras* | 主绕组定子电阻 |
| *Las* | 主绕组定子漏电感 |
| *R'ar* | 主绕组转子电阻 |
| *L'lar* | 主绕组转子漏电感 |
| *Lmas* | 主绕组互感 |
| *Rbs* | 辅助绕组定子电阻 |
| *Rlbs* | 辅助绕组定子漏电感 |
| *R'br* | 辅助绕组转子电阻 |
| *L'lbr* | 辅助绕组转子漏电感 |
| *Lmbs* | 辅助绕组互感 |

### 方程

SI 模型将您在对话框中输入的 SI 值转换为用于仿真的标幺值。有关 SI 与标幺值电机参数之间关系的信息，请参阅 Per-Unit Conversion for Machine Parameters。有关标幺值参数化的信息，请参阅 Per-Unit System of Units。

这些变换通过定义相对于主绕组的等效电路，将转子电阻、转子漏电感和定子互感简化为单组值：

Lms=Lmas=1a2Lmbs

Rar'=1a2Rbr'

Llar'=1a2Llbr'

定子和转子的电压方程为：

vqs=Rasiqs+dψqsdt

vds=Rbsids+dψdsdt

0=Rar'iqr'+dψqr'dt−1aωrψdr'

0=a2Rar'idr'+dψdr'dt+aωrψqr'

ψqs=(Llas+Lms)iqs+Lmsiqr'

ψds=(Llbs+a2Lms)ids+a2Lmsidr'

ψqr'=(Llar'+Lms)iqr'+Lmsiqs

ψdr'=a2(Llar'+Lms)idr'+a2Lmsids

电磁转矩 *T* 的表达式通过应用虚位移原理 [1] 获得。

T=p(aψqr'idr'−1aψdr'iqr')

机械方程为

Jdωmdt=T−TL−Bmωm,

其中 *ωm* 是转子角速度。

在分相电机中，辅助绕组与主绕组在电气上相差 90 度，并且仅在速度达到断开速度之前运行，该速度通常为额定速度的 70% 到 80%。在此配置中，与主绕组相比，辅助绕组具有高电阻和小电抗。由此产生的相位差使电机表现得像两相电机。

电容启动电机是一种分相电机，它使用与辅助绕组串联的电容器来启动电机。在此配置中，辅助绕组和主绕组具有相同的匝数。电容器的值确保辅助线圈中的电流领先主绕组中的电流约 80 电气度。

电容启动电压为：

vc=Rsids+∫​1Csωrids.

当电容器与辅助绕组串联时，*d* 轴电压方程为

vds=Rbsids+dψdsdt−Rsids−∫​1Csωrids.

对于电容启动电容运行电机，可以立即得到扩展。在此配置中，两个电容器并联连接。

断开电容启动后的 *d* 轴电压为

vds=Rbsids+dψdsdt−Rrids−∫​1Crωrids.

### 显示选项

要在 MATLAB® Command Window 中显示电机标幺基准值，请右键单击模块，然后从 **Electrical** 菜单中选择 **Display Base Values**。

### 模拟热效应

您可以暴露热端口来模拟产生的热量和电机温度的影响。要暴露热端口和 **Thermal** 参数，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 模块包含与定子绕组相关的电气守恒端口，但不包含热端口。
- `Show thermal port` — 模块包含与定子绕组相关的扩展电气守恒端口，以及每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
