---
type: simulink-block
title: 'Cone Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'coneclutch'
documentation_source_path: 'ref/coneclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Cone Clutch

## 端口

### 输入

### **N** — 法向力物理信号

与法向力关联的物理信号端口。该信号为正或零。小于零的信号解释为零。

#### 依赖关系

仅当在 **几何** 设置中将 **换挡机构控制** 参数设置为 `Physical signal` 时，此端口才可见。有关详细信息，请参阅 换挡机构控制 和 几何参数依赖关系。

### 输出

### **X** — 换挡机构位置物理信号

与换挡机构位置关联的物理信号端口。

#### 依赖关系

仅当在 **几何** 设置中将 **换挡机构控制** 参数设置为 `Conserving port` 时，此端口才可见。有关详细信息，请参阅 换挡机构控制 和 几何参数依赖关系。

### 守恒

### **B** — 基础机械旋转

与驱动（基础）轴关联的机械旋转守恒端口。离合器运动以 *slip* *ω* = *ωF*–*ωB* 衡量，即从动件相对于基础件的角速度。

### **F** — 从动件机械旋转

与从动或从动件轴关联的机械旋转守恒端口

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

仅当在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此端口才可见。有关详细信息，请参阅 摩擦模型 和 摩擦参数依赖关系。

### **S** — 换挡机构机械旋转

与换挡机构关联的机械旋转守恒端口。

#### 依赖关系

仅当在 **几何** 设置中将 **换挡机构控制** 参数设置为 `Conserving port` 时，此端口才可见。有关详细信息，请参阅 换挡机构控制 和 几何参数依赖关系。

## 参数

### 几何

该表显示了某些参数的可见性如何取决于为其他参数选择的选项。

**几何参数依赖关系**

| **几何** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **接触表面最大直径** | | | | | | |
| **接触表面最小直径** | | | | | | |
| **锥半角** | | | | | | |
| **换挡机构控制** | | | | | | |
| `Physical signal` | | | `Conserving port` | | | |
| 公开物理信号输入端口 **N** | | | 公开：  - 守恒端口   **S** - 物理信号输出端口   **X** - **换挡机构** 设置 | | | |

### **接触表面最大直径** — 外径 `150` `mm`（默认）| 正标量

外锥直径 *do*。

### **接触表面最小直径** — 内径 `100` `mm`（默认）| 正标量

内锥直径 *di*。

### **锥半角** — 锥半角 `12` `deg`（默认）| 正标量

锥几何形状的半开角 *α*。

### **换挡机构控制** — 换挡机构模型 `Physical signal`（默认）| `Conserving port`

换挡机构控制模型：

- `Physical signal`
  — 公开物理信号端口
  **N**（输入法向力）和 **X**（输出
  换挡机构行程）。
- `Conserving port`
  — 公开守恒端口
  **S**，其与
  换挡机构控制关联。

#### 依赖关系

**换挡机构** 设置以及端口
**S**、**X**
和 **N** 的可见性取决于此设置。
有关详细信息，请参阅 几何参数依赖关系。

### 换挡机构

仅当在
**几何** 设置中将 **换挡机构控制** 参数设置为
`Conserving port` 时，这些设置才可见。有关
详细信息，请参阅 换挡机构控制 和 几何参数依赖关系。

### **换挡机构后部硬限位** — 硬限位选项 `on`（默认）| `off`

是否在换挡机构后部包含硬限位。

### **分离时环毂间隙** — 环毂间隙 `3` `mm`（默认）| 非负标量

分离时环毂间隙

### **环挡块刚度** — 环挡块刚度 `10e5` `N/m`（默认）| 非负标量

环挡块刚度

### **环挡块阻尼** — 环挡块阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

环挡块阻尼

### **换挡机构粘性摩擦系数** — 换挡机构粘性摩擦 `100` `N/(m/s)`（默认）| 正标量

换挡机构粘性摩擦
系数

### **连杆行程方向** — 分离行程方向 `Positive shift linkage displacement engages clutch`（默认）| `Negative shift linkage displacement engages clutch`

使离合器分离的连杆行程方向

### 摩擦

该表显示了某些端口、参数和设置的可见性如何取决于为其他参数选择的选项。

**摩擦参数依赖关系**

| **摩擦** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **摩擦模型** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 公开：  - 守恒端口   **H** - **摩擦** 设置中的热参数 - **热端口** 设置 | | 公开：  - 守恒端口   **H** - **摩擦** 设置中的热参数 - **热端口** 设置 | |
| - | - | | **温度向量** | | **温度向量** | |
| - | **相对速度向量** | | - | | **相对速度向量** | |
| **静摩擦系数** | **静摩擦系数** | | **静摩擦系数向量** | | **静摩擦系数向量** | |
| **动摩擦系数** | **动摩擦系数向量** | | **动摩擦系数向量** | | **动摩擦系数矩阵** | |
| - | **摩擦系数插值方法** | | **摩擦系数插值方法** | | **摩擦系数插值方法** | |
| - | **摩擦系数外推方法** | | **摩擦系数外推方法** | | **摩擦系数外推方法** | |
| **速度容差** | **速度容差** | | **速度容差** | | **速度容差** | |
| **阈值力** | **阈值力** | | **阈值力** | | **阈值力** | |
| **粘性摩擦系数** | **粘性摩擦系数** | | **粘性摩擦系数** | | **粘性摩擦系数** | |

### **摩擦模型** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于建模动摩擦系数的参数化方法。此参数的选项和默认值取决于为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅 摩擦参数依赖关系。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，以向量形式表示。向量中的值必须从左到右递增。最小值数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式表示。最小值数量取决于所选的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静值或峰值，以向量形式表示。该向量的元素数量必须与温度向量相同。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Fixed kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式表示。所有值必须大于零。

如果 **摩擦模型** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **动摩擦系数矩阵** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **摩擦系数插值方法** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` —
  选择此选项可获得最佳性能。
- `Smooth` —
  选择此选项可生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **摩擦系数外推方法** — 外推方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表中指定范围之外时，用于确定输出值的外推方法：

- `Linear` —
  选择此选项可生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` —
  选择此选项可生成不高于数据中最高点或不低于数据中最低点的外推。
- `Error` —
  当希望数据位于表范围内时，选择此选项可避免进入外推模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **速度容差** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可锁定时的相对速度下限。如果 **B** 和 **F** 旋转端口上的扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则表面锁定。

### **阈值力** — 法向接触力阈值 `1` `N`（默认）| 标量

施加到物理信号端口 **N** 的法向力仅在力的大小超过 **阈值力** 参数值时才会施加到接触面。低于 **阈值力** 的力不会施加，因此不会传递摩擦扭矩。

### **粘性摩擦系数** — 粘性摩擦 `0`（默认）| 非负标量

粘性摩擦系数。

### 初始条件

### **初始状态** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时的离合器状态。离合器可处于两种状态之一：锁定和解锁。锁定的离合器约束基础轴和从动轴以相同速度旋转，即作为一个整体旋转。解锁的离合器允许两个轴以不同速度旋转，从而导致离合器片之间打滑。

### 故障

要修改故障，请创建一个故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **离合器故障** — 用于建模摩擦故障的选项 `Add fault`

是否在模块中对故障建模。要添加故障，请点击 **Add fault** 超链接。

### **发生故障时的行为** — 离合器摩擦故障响应 `Cannot transmit power`（默认）| `Cannot unlock`

故障响应。您可以选择将离合器故障设置为：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### 热端口

**热端口** 设置仅在 **摩擦** 设置中的 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **热质量** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗越强。

#### 依赖关系

仅当在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

### **初始温度** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的组件温度。初始温度会根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

#### 依赖关系

仅当在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 摩擦参数依赖关系。

## 库

Simscape / Driveline / Clutches

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称变更

**粘性阻力矩系数** 参数现在为 **粘性摩擦系数** 参数。

### R2025a：枚举更新

**换挡机构后部硬限位** 参数现在使用复选框。在之前的版本中，此参数使用下拉列表。

### R2024a：使用 Simscape faults 接口对故障建模

Cone Clutch 模块现在支持 Simscape faults 接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 说明

当法向力超过阈值时接合的锥形离合器板

Cone Clutch 模块表示具有锥形接触界面的摩擦离合器。锥形界面通过在离合器组件（一个锥体和一个杯体）之间产生楔入作用，减少离合器接合所需的正压力。锥形离合器应用包括同步啮合变速箱，它同步驱动轴和从动轴的速度，以实现变速箱齿轮之间更平稳的接合。

杯体组件刚性连接到驱动轴，并作为一个整体与其旋转。锥体组件刚性连接到从动轴，从动轴与驱动轴轴向对齐。当锥体向杯体滑动并紧压其内表面时，离合器接合。锥体-杯体接触界面处的摩擦使离合器能够在驱动轴和从动轴之间传递旋转功率。此模块的摩擦模型同时包含静摩擦和动摩擦贡献，后者在锥体和杯体组件之间打滑时导致功率耗散。

Cone Clutch 模块基于 Fundamental Friction Clutch 模块。有关完整的摩擦离合器模型，请参阅 Fundamental Friction Clutch。本节讨论 Cone Clutch 模块中实现的专用模型。

当施加法向力 *FN* 时，Cone Clutch 模块可以对传动系统运动施加两种摩擦：动摩擦和静摩擦。仅当一个传动系统轴相对于另一个传动系统轴旋转时，离合器才施加动摩擦扭矩。当两个传动系统轴锁定并一起旋转时，离合器施加静摩擦扭矩。该模块通过多步测试进行迭代，以确定何时锁定和解锁离合器。

### 离合器几何与变量

该图显示了锥形离合器几何形状。

**离合器变量**

| 参数 | 定义 | 含义 |
| --- | --- | --- |
| *d*o | 锥形接触表面的外径 | *见上图* |
| *d*i | 锥形接触表面的内径 | *见上图* |
| *α* | 锥半角 | *见上图* |
| *ω* | 相对角速度（滑差） | *ω*F – *ω*B |
| *ω*Tol | 用于离合器锁定的滑差容差 | *见以下模型* |
| *F*N | 施加到锥形表面的法向力 | 如果大于阈值，则施加法向力：*F*N > *F*th |
| *α* | 锥半角 | *见上图* |
| *r*eff | 有效扭矩半径 | 离合器摩擦力的有效力臂 |
| *k*K | 动摩擦系数 | 锥形摩擦表面的无量纲动摩擦系数。*ω* 的函数。 |
| *k*S | 静摩擦系数 | 锥形摩擦表面的无量纲静摩擦系数。 |
| *τ*K | 动摩擦扭矩 | *见以下模型* |
| *τ*S | 静摩擦扭矩限值 | (静摩擦峰值因子)·(*ω* → 0 时的动摩擦扭矩)  (*见以下模型*) |

### 与 Fundamental Friction Clutch 的关系

Cone Clutch 模块基于 Fundamental Friction Clutch 模块。Cone Clutch 模块不是要求将动摩擦和静摩擦限值扭矩作为输入信号，而是根据离合器参数和输入法向力信号 *FN* 计算动摩擦和静摩擦。

**动摩擦**

动摩擦扭矩是四个因子的乘积：

τK=kK⋅FN⋅reff⋅sgn(ω)

动摩擦扭矩阻碍相对滑差，并以整体负号施加。当 *ω* 改变符号时，它也会改变符号。

您可以将动摩擦系数 *kK* 指定为常数，或指定为相对角速度 *ω* 的表格化离散函数。对于相对角速度的正值和负值，假定表格化函数是对称的。因此，只需为 *ω* 的正值指定 *k*K。

有效扭矩半径 *reff* 是从传动系统轴测量的有效半径，动摩擦力在该半径处施加到摩擦表面。它与锥形摩擦表面几何形状的关系为：

reff=13sinαdo3−di3do2−di2

*do* 和 *di* 分别是接触表面的最大直径和最小直径。

**静摩擦**

静摩擦限值与动摩擦相关：将 *ω* 设置为零，并将动摩擦系数替换为静摩擦系数：

TS=kS⋅FN⋅reff≥0

*k*S
>
*k*K，因此在解锁瞬间，当 *ω* = 0 时，克服静摩擦以解锁离合器所需的扭矩 *τ* 大于动摩擦。

静摩擦限值定义对称的 *静摩擦扭矩限值* 如下：

τS≡τS+=−τS−

范围
[*τ*S–,
*τ*S+]
由 Fundamental Friction Clutch 使用。

**接合与锁定条件**

当锥形摩擦表面受到正法向力并产生动摩擦时，离合器接合（传递扭矩）：*F*N
> 0 且 *τK*>
0。

当且仅当离合器接合，并且滑差小于速度容差时，离合器锁定：|*ω*| <
*ω*Tol。

**离合器耗散的功率**

离合器耗散的功率为
|*ω*·*τK*|。
仅当离合器既打滑（ω ≠ 0）又施加动摩擦（*τK*
> 0）时，它才耗散功率。

### 速度相关模型

您可以通过选择速度相关模型来建模旋转速度变化的影响。要选择速度相关模型，请在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Velocity-dependent kinetic friction coefficient`。有关同时取决于速度和温度的摩擦模型的信息，请参阅 热、速度相关模型。

### 热模型

您可以通过选择温度相关模型来建模热流和温度变化的影响。要选择温度相关模型，请在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Temperature-dependent friction coefficients`。有关同时取决于速度和温度的摩擦模型的信息，请参阅 热、速度相关模型。

### 热、速度相关模型

您可以通过选择速度相关且温度相关的模型来建模旋转速度变化和热流的影响。要选择同时取决于速度和温度的模型，请在 **摩擦** 设置中将 **摩擦模型** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

### 故障

要在 Cone Clutch 模块中对故障建模，请在 **故障** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块会在仿真的剩余时间内根据 **发生故障时的行为** 参数的设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`
