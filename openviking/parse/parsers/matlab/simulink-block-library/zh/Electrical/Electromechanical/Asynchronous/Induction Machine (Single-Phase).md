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

### **pu** — 电机标幺值测量 physical signal | vector

与电机标幺值测量关联的 physical signal 向量端口。向量元素为：

- pu\_torque
- pu\_velocity
- pu\_vds
- pu\_vqs
- pu\_v0s = 0
- pu\_ids
- pu\_iqs
- pu\_i0s = 0

### 守恒

### **a1** — 主绕组正极端子 electrical | scalar

与主绕组正极端子关联的 electrical 守恒端口。

### **a2** — 主绕组负极端子 electrical | scalar

与主绕组负极端子关联的 electrical 守恒端口。

### **b1** — 辅助绕组正极端子 electrical | scalar

与辅助绕组正极端子关联的 electrical 守恒端口。

#### 依赖关系

仅当将 **Type** 设置为 `Main and auxiliary windings` 时，此端口可见。

### **b2** — 辅助绕组负极端子 electrical | scalar

与辅助绕组负极端子关联的 electrical 守恒端口。

#### 依赖关系

仅当将 **Type** 设置为 `Main and auxiliary windings` 时，此端口可见。

### **R** — 电机转子 mechanical rotational

与电机转子关联的 mechanical rotational 守恒端口。

### **C** — 电机机壳 mechanical rotational

与电机机壳关联的 mechanical rotational 守恒端口。

### **HA** — 主绕组热端口 thermal

与定子主绕组关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设置为 `Show thermal port`。

### **HB** — 辅助绕组热端口 thermal

与定子辅助绕组关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设置为 `Show thermal port`。

### **HR** — 转子热端口 thermal

与转子关联的 thermal 守恒端口。

#### 依赖关系

要启用此端口，将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并模拟生成热量和电机温度的影响。

### 主

### **Type** — 感应电机类型 `Split-phase`（默认）| `Capacitor-start` | `Capacitor-start-capacitor-run` | `Main and auxiliary windings`

感应电机的类型。

### **Rated apparent power** — 额定视在功率 `180` `V*A`（默认）| positive scalar

感应电机的额定视在功率。

### **Rated voltage** — 额定电压 `220` `V`（默认）| positive scalar

RMS 电压。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| positive scalar

对应于额定视在功率的标称电气频率。

### **Number of pole pairs** — 极对数 `2`（默认）| positive integer

电机极对数。该值用作反电动势常数。

### **Parameterization unit** — SI 或标幺值参数化选项 `SI`（默认）| `Per unit`

用于模块参数化的单位制。

#### 依赖关系

选择：

- `SI` 会显示 SI **Electrical** 参数。
- `Per unit` 会显示标幺值 **Electrical** 参数。

### 电气

对于 **Main** 设置中的 **Parameterization unit** 参数，选择 `SI` 会显示 SI **Electrical** 参数，或选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Main winding stator resistance, Ras** — 主绕组定子电阻 `1.8180` `Ohm`（默认）| positive scalar

主绕组的 SI 定子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Main winding stator leakage inductance, Llas** — 主绕组定子漏电感 `0.0067` `H`（默认）| positive scalar

主绕组的 SI 漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Main winding rotor resistance, Rar'** — 主绕组转子电阻 `3.7080` `Ohm`（默认）| positive scalar

主绕组的 SI 转子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Main winding rotor leakage inductance, Llar'** — 主绕组转子漏电感 `0.0050` `H`（默认）| positive scalar

主绕组的 SI 转子漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Main winding mutual inductance, Lms** — 主绕组互感 `0.1595` `H`（默认）| positive scalar

主绕组的 SI 互感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Auxiliary winding stator resistance, Rbs** — 辅助绕组定子电阻 `6.4260` `Ohm`（默认）| positive scalar

辅助绕组的 SI 定子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Auxiliary winding stator leakage inductance, Llbs** — 辅助绕组定子漏电感 `0.0077` `H`（默认）| positive scalar

辅助绕组的 SI 定子漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `SI` 会显示 SI **Electrical** 参数。

### **Auxiliary/main windings turn ratio** — 匝数比 `1.1`（默认）| positive scalar

主绕组和辅助绕组之间的绕组比。

### **Main winding stator resistance, Ras (pu)** — 主绕组定子电阻 `0.0135`（默认）| positive scalar

主绕组的标幺值定子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Main winding stator leakage inductance, Llas (pu)** — 主绕组定子漏电感 `0.0188`（默认）| positive scalar

主绕组的标幺值漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Main winding rotor resistance, Rar' (pu)** — 主绕组转子电阻 `0.0276`（默认）| positive scalar

主绕组的标幺值转子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Main winding rotor leakage inductance, Llar' (pu)** — 主绕组转子漏电感 `0.0140`（默认）| positive scalar

主绕组的标幺值转子漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Main winding mutual inductance, Lms (pu)** — 主绕组互感 `0.4472`（默认）| positive scalar

主绕组的标幺值互感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Auxiliary winding stator resistance, Rbs (pu)** — 辅助绕组定子电阻 `0.0478`（默认）| positive scalar

辅助绕组的标幺值定子电阻。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Auxiliary winding stator leakage inductance, Llbs (pu)** — 辅助绕组定子漏电感 `0.0216`（默认）| positive scalar

辅助绕组的标幺值定子漏电感。

#### 依赖关系

在 **Main** 设置中为 **Parameterization unit** 参数选择 `Per unit` 会显示标幺值 **Electrical** 参数。

### **Auxiliary/main windings turn ratio** — 匝数比 `1.1`（默认）| positive scalar

主绕组和辅助绕组之间的绕组比。

### **Capacitor-start resistance, Rs** — 电容器启动电阻 `3` `Ohm`（默认）| positive scalar

SI 电容器启动电阻。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run` 或 `Capacitor-start`，并将 **Parameterization unit** 设置为 `SI`。

### **Capacitor-start capacitance, Cs** — 电容器启动电容 `0.00018` `F`（默认）| positive scalar

SI 电容器启动电容。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run` 或 `Capacitor-start`，并将 **Parameterization unit** 设置为 `SI`。

### **Capacitor-run resistance, Rr** — 电容器运行电阻 `9` `Ohm`（默认）| positive scalar

SI 电容器运行电阻。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `SI`。

### **Capacitor-run capacitance, Cr** — 电容器运行电容 `0.000015` `F`（默认）| positive scalar

SI 电容器运行电容。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `SI`。

### **Capacitor-start resistance, Rs (pu)** — 电容器启动电阻 `0.0223`（默认）| positive scalar

标幺值电容器启动电阻。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `Per unit`。

### **Capacitor-start capacitance, Cs (pu)** — 电容器启动电容 `9.1232`（默认）| positive scalar

标幺值电容器启动电容。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `Per unit`。

### **Capacitor-run resistance, Rr (pu)** — 电容器运行电阻 `0.0669`（默认）| positive scalar

标幺值电容器运行电阻。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `Per unit`。

### **Capacitor-run resistance, Cr (pu)** — 电容器运行电容 `0.000015`（默认）| positive scalar

标幺值电容器运行电容。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Capacitor-start-capacitor-run`，并将 **Parameterization unit** 设置为 `Per unit`。

### **Disconnection speed (% of rated speed)** — 断开速度 `80`（默认）| scalar in range [0,100]

电容器断开时的速度，以额定速度的百分比表示。该值必须介于 `0` 和 `100`（含）之间。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Split-phase`、`Capacitor-start` 或 `Capacitor-start-capacitor-run` 之一。

### 机械

### **Rotor inertia** — 转子惯量 `0.01` `kg*m^2`（默认）| positive scalar

转子的惯量。

### **Rotor damping** — 转子阻尼 `0` `N*m/(rad/s)`（默认）| scalar

转子的阻尼。

### 热

这些参数仅对暴露热端口的模块显示。

### **Measurement temperature** — 额定温度 `298.15` `K`（默认）| real scalar

引用电机参数时所对应的温度。

### **Resistance temperature coefficient** — 温度系数 `3.93e-3` `1/K`（默认）| positive scalar

如 Thermal Model for Actuator Blocks 中所述，将全部三个绕组的电阻与温度关联的方程中的系数 α。默认值 `3.93e-3` 1/K 适用于铜。

### **Cage resistance temperature coefficient** — 转子温度系数 `4.4e-3`（默认）| `1/K` | scalar

将转子笼型电阻与温度关联的系数。默认值 `4.4e-3` 1/K 适用于铝。

### **Thermal mass for each stator winding** — 绕组热质量 `100` `J/K`（默认）| positive scalar

每个定子绕组的热质量值。热质量是使温度升高一度所需的能量。

### **Rotor thermal mass** — 转子热质量 `200` `J/K`（默认）| positive scalar

转子的热质量。热质量是使转子温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Asynchronous

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2021b：感应电机类型参数

从 R2021b 起，要对不同类型的感应电机进行建模，将 **Type** 参数设置为 `Split-phase`、`Capacitor-start`、`Capacitor-start-capacitor-run` 或 `Main and auxiliary windings` 之一。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Type** 参数。

## 描述

具有 SI 或 pu 基本参数化的单相感应电机

Induction Machine (Single-Phase) 模块表示具有鼠笼式转子的单相感应电机，其基本参数以标幺值或国际单位制 (SI) 表示。

此模块可对四种类型的单相感应电机进行建模：

- `Split-phase`
- `Capacitor-start`
- `Capacitor-start-capacitor-run`
- `Main and auxiliary windings`

单相感应电机由鼠笼式转子和两个定子绕组（主绕组和辅助绕组）组成。辅助绕组通常仅在启动期间有效。但是，为提高性能，对于低功率应用，辅助绕组可在运行期间有效。图中显示了主绕组和辅助绕组的等效 *d* 轴和 *q* 轴电路。

下表定义了这些变量。

| 变量 | 定义 |
| --- | --- |
| *vqs**vds* | 在 *d*-*q* 表示中的定子电压 |
| *iqs**ids* | 在 *d*-*q* 表示中的定子电流 |
| *Ψqr**Ψdr* | 在 *d*-*q* 表示中的转子磁链 |
| *⍵* | 转子电气速度 |
| *a* | 辅助/主绕组匝数比 |
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

SI 模型将您在对话框中输入的 SI 值转换为用于仿真的标幺值。有关 SI 与电机标幺参数之间关系的信息，请参阅电机参数的标幺值转换。有关标幺值参数化的信息，请参阅标幺值单位制。

这些变换通过相对于主绕组定义等效电路，将转子电阻、转子漏电感和定子互感归并为一组值：

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

在分相电机中，辅助绕组与主绕组在电气上相差 90 电角度，并且仅运行到转速达到断开速度为止；该速度通常为额定速度的 70% 到 80%。在此配置中，与主绕组相比，辅助绕组具有高电阻和小电抗。由此产生的相位差使电机表现得像两相电机。

电容启动电机是一种分相电机，它使用与辅助绕组串联的电容器来启动电机。在此配置中，辅助绕组和主绕组具有相同的匝数。电容器的值确保辅助线圈中的电流超前主绕组中的电流约 80 电角度。

电容启动电压为：

vc=Rsids+∫​1Csωrids.

当电容器与辅助绕组串联时，*d* 轴电压方程为

vds=Rbsids+dψdsdt−Rsids−∫​1Csωrids.

对于电容启动-电容运行电机，可立即得到其扩展形式。在此配置中，两个电容器并联连接。

断开启动电容器后的 *d* 轴电压为

vds=Rbsids+dψdsdt−Rrids−∫​1Crωrids.

### 显示选项

要在 MATLAB® 命令窗口中显示电机的标幺基准值，请右键点击该模块，然后从 **Electrical** 菜单中选择 **Display Base Values**。

### 模拟热效应

您可以暴露热端口，以模拟产生的热量和电机温度的影响。要暴露热端口和 **Thermal** 参数，请将 **Modeling option** 参数设置为以下任一值：

- `No thermal port` — 该模块包含与定子绕组关联的电气守恒端口，但不包含热端口。
- `Show thermal port` — 该模块包含与定子绕组关联的扩展电气守恒端口，以及针对每个绕组和转子的热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅模拟旋转和平移执行器中的热效应。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真的鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅基于标称值的系统缩放。
