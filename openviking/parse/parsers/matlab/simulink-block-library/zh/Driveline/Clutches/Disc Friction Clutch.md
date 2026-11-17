---
type: simulink-block
title: 'Disc Friction Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'discfrictionclutch'
documentation_source_path: 'ref/discfrictionclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Disc Friction Clutch

## 端口
```yaml
ports:
- name: P
  summary: 压力物理信号
  direction: input
- name: B
  summary: 基础机械旋转
  direction: input
- name: F
  summary: 从动机械旋转
  direction: input
- name: H
  summary: 热流热
  direction: input
```

### 输入

### **P** — 压力物理信号

用于施加在离合器片之间的压力的物理信号输入端口，单位为帕斯卡。该模块将小于零的信号饱和为零。
### 守恒

### **B** — 基础机械旋转

与驱动轴（即基础轴）关联的旋转守恒端口。

### **F** — 从动机械旋转

与从动轴（即从动轴）关联的旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

此端口仅在 **Friction** 设置中 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies 和 Friction model。
## 参数
```yaml
parameters:
- name: Geometry model
  summary: 几何参数化方法 Define effective radius（默认）| Define annular region
  group: 几何
- name: Effective torque radius
  summary: 力臂半径 130 mm（默认）| 正标量
  group: 几何
- name: Friction surface outside diameter
  summary: 摩擦面外径 150 mm（默认）| 正标量
  group: 几何
- name: Friction surface inside diameter
  summary: 摩擦面内径 100 mm（默认）| 非负标量
  group: 几何
- name: Number of friction surfaces
  summary: 摩擦面数量 4（默认）| 正标量整数
  group: 几何
- name: Engagement piston area
  summary: 压力施加面积 0.001 m^2（默认）| 正标量
  group: 几何
- name: Directionality
  summary: 允许的滑移方向 Bidirectional（默认）| Unidirectional
  group: 几何
- name: Friction model
  summary: 摩擦模型 Fixed kinetic friction coefficient（默认）| Velocity-dependent kinetic friction coefficient | Temperature-dependent
    friction coefficients | Temperature and velocity-dependent friction coefficients
  group: 摩擦
- name: Relative velocity vector
  summary: 相对速度 [0, 100, 1000] rad/s（默认）| 向量
  group: 摩擦
- name: Temperature vector
  summary: 温度 [280, 300, 320] K（默认）| 递增向量
  group: 摩擦
- name: Static friction coefficient
  summary: 静摩擦系数 0.35（默认）| 正标量
  group: 摩擦
- name: Static friction coefficient vector
  summary: 静摩擦系数 [.4, .38, .36]（默认）| 向量
  group: 摩擦
- name: Kinetic friction coefficient
  summary: 动摩擦系数 0.3（默认）| 正标量
  group: 摩擦
- name: Kinetic friction coefficient vector
  summary: 动摩擦系数 [.3, .22, .19]（默认）| [.3, .28, .25] | 正向量
  group: 摩擦
- name: Kinetic friction coefficient matrix
  summary: 动摩擦系数 [.34, .32, .3; .3, .28, .25; .25, .2, .15]（默认）| 正矩阵
  group: 摩擦
- name: Friction coefficient interpolation method
  summary: 外推方法 Linear（默认）| Smooth
  group: 摩擦
- name: Friction coefficient extrapolation method
  summary: 插值方法 Linear（默认）| Nearest | Error
  group: 摩擦
- name: De-rating factor
  summary: 降额系数 1（默认）| 正标量
  group: 摩擦
- name: Clutch velocity tolerance
  summary: 相对速度锁定阈值 0.001 rad/s（默认）| 非负标量
  group: 摩擦
- name: Engagement threshold pressure
  summary: 法向接触力阈值 100 Pa（默认）| 非负标量
  group: 摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦 0 N*m/(rad/s)（默认）| 非负标量
  group: 粘性损耗
- name: Initial state
  summary: 初始离合器状态 Unlocked（默认）| Locked
  group: 初始条件
- name: Friction fault
  summary: 用于建模离合器故障的选项 Add fault
  group: 故障
- name: Behavior when faulted
  summary: 离合器故障响应 Cannot transmit power（默认）| Cannot unlock
  group: 故障
- name: Thermal mass
  summary: 热质量 50 kJ/K（默认）| 标量
  group: 热端口
- name: Initial temperature
  summary: 初始温度 300 K（默认）| 标量
  group: 热端口
```

### 几何

### **Geometry model** — 几何参数化方法 `Define effective radius`（默认）| `Define annular region`

用于建模离合器摩擦几何的参数化方法。

#### 依赖关系

**Effective torque radius** 参数仅在此参数设置为 `Define effective radius` 时可见：

以下参数仅在此参数设置为 `Define annular region` 时可见：

- **Friction surface outside diameter**
- **Friction surface inside diameter**

### **Effective torque radius** — 力臂半径 `130` `mm`（默认）| 正标量

有效力臂半径 *reff*，用于确定离合器内部的动摩擦力矩。

#### 依赖关系

此参数仅在 **Geometry model** 参数设置为 `Define effective radius` 时可见。

### **Friction surface outside diameter** — 摩擦面外径 `150` `mm`（默认）| 正标量

摩擦盘环形区域外边缘的直径 2*ro*。

#### 依赖关系

此参数仅在 **Geometry model** 参数设置为 `Define annular region` 时可见。

### **Friction surface inside diameter** — 摩擦面内径 `100` `mm`（默认）| 非负标量

摩擦盘环形区域内边缘的直径 2*ri*。

#### 依赖关系

此参数仅在 **Geometry model** 参数设置为 `Define annular region` 时可见。

### **Number of friction surfaces** — 摩擦面数量 `4`（默认）| 正标量整数

离合器内部产生摩擦的接触面数量 *N*。

### **Engagement piston area** — 压力施加面积 `0.001` `m^2`（默认）| 正标量

当活塞在离合器上施加压力时，离合器活塞的有效面积 *A*。

### **Directionality** — 允许的滑移方向 `Bidirectional`（默认）| `Unidirectional`

离合器允许其片之间滑移的方向。双向离合器允许正和负滑移速度。单向离合器仅允许正滑移速度。

单向离合器等效于一个摩擦离合器与一个仅在滑移速度变为正时分离的单向离合器并联。要对负方向滑移的单向离合器建模，请反转基础端口和从动端口的连接。

### 摩擦

下表显示了某些端口、参数和设置的可见性如何取决于您为其他参数选择的选项。

**Friction Parameter Dependencies**

| **Friction** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 显示：  - 守恒端口 **H** - **Thermal Port** 设置 | | 显示：  - 守恒端口 **H** - **Thermal Port** 设置 | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **De-rating factor** | **De-rating factor** | | **De-rating factor** | | **De-rating factor** | |
| **Clutch velocity tolerance** | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | |
| **Engagement threshold pressure** | **Engagement threshold pressure** | | **Engagement threshold pressure** | | **Engagement threshold pressure** | |

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient`（默认）| `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于建模动摩擦系数的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Relative velocity vector** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，以向量形式表示。向量中的值必须从左到右递增。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式表示。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认）| 正标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，以向量形式表示。该向量的元素数量必须与温度向量相同。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数（即库仑摩擦系数）。该系数必须大于零。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 正向量

动摩擦系数的输出值，以向量形式表示。所有值必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量的元素数量必须与相对速度向量相同。
- `Temperature-dependent friction coefficients` — 该向量的元素数量必须与温度向量相同。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 正矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient interpolation method** — 外推方法 `Linear`（默认）| `Smooth`

当输入值介于两个连续网格点之间时，用于近似输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient extrapolation method** — 插值方法 `Linear`（默认）| `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成在外推区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不高于数据中最高点或不低于数据中最低点的外推。
- `Error` — 当您希望数据在表格范围内时，选择此选项以避免进入外推模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **De-rating factor** — 降额系数 `1`（默认）| 正标量

无量纲降额系数 *D*，通过按比例降低离合器摩擦来考虑离合器盘磨损。

### **Clutch velocity tolerance** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 非负标量

离合器可以锁定的最大滑移速度。滑移速度是基础轴和从动轴角速度之间的有符号差值，即 w=wF−wB。如果动摩擦力矩非零且传递的力矩在静摩擦力矩限值内，则当实际滑移速度低于速度容差时，离合器锁定。

### **Engagement threshold pressure** — 法向接触力阈值 `100` `Pa`（默认）| 非负标量

离合器接合的最小压力 *Pth*。如果压力输入信号低于此阈值，离合器将自动分离。

### 粘性损耗

### **Viscous friction coefficient** — 粘性摩擦 `0` `N*m/(rad/s)`（默认）| 非负标量

施加于基础轴和从动轴之间相对滑移 *ω* 的粘性摩擦系数 *μ*。

### 初始条件

### **Initial state** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：锁定和解锁。锁定的离合器约束基础轴和从动轴以相同速度旋转，即作为一个整体旋转。解锁的离合器允许两个轴以不同速度旋转，从而在离合器片之间产生滑移。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在 Property Inspector 中，点击 **Fault behavior** 链接以打开故障。

### **Friction fault** — 用于建模离合器故障的选项 `Add fault`

是否在模块中建模离合器故障。要添加故障，请点击 **Add fault** 超链接。

### **Behavior when faulted** — 离合器故障响应 `Cannot transmit power`（默认）| `Cannot unlock`

触发故障时离合器的响应。您可以选择将离合器故障设置为：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### 热端口

**Thermal Port** 设置仅在 **Friction** 设置中 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

此参数仅在 **Friction** 设置中 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的部件温度。初始温度会根据您指定的效率向量改变部件效率，从而影响起始啮合损失或摩擦损失。默认值为 `300`
`K`。

#### 依赖关系

仅当在 **Friction** 设置中，**Friction model** 参数设置为 `Temperature-dependent
friction coefficients` 或 `Temperature
and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅 Friction Parameter Dependencies。
## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称变更

**Viscous drag torque coefficient** 参数现在为
**Viscous friction coefficient** 参数。

### R2024a：使用 Simscape faults 接口对故障建模

Disc Friction Clutch 模块现在支持 Simscape faults 接口。要了解详细信息，
请参阅 Introduction to Simscape Faults。

## 描述

当片压力超过阈值时，带片式摩擦片啮合的摩擦离合器

Disc Friction Clutch 模块表示一个带有两组扁平摩擦片组的摩擦
离合器，这两组摩擦片接触以啮合。当施加的片压力超过啮合阈值压力时，离合器
啮合。一旦啮合，摩擦片会承受摩擦力矩，使其能够在基座驱动轴和从动驱动轴之间传递动力。

离合器可以是双向或单向的。双向离合器可以在正方向和负方向上打滑。单向离合器只能在
正方向上打滑。如果从动轴比基座轴旋转得更快，则打滑方向为正；如果打滑更慢，则为负。该模块将打滑速度
定义为差值

ω=ωF−ωB，

其中：

- *ω* 是相对角速度或打滑
  速度。
- *ωF* 是从动驱动轴的角速度。
- *ωB* 是基座驱动轴的角速度。

该模块提供一个物理信号输入端口 **P**，用于离合器片之间的施加
压力。施加压力必须大于或等于零。如果输入信号降至零以下，该模块将片压力视为
零。

### 方程

Disc Friction Clutch 模块是 Fundamental Friction Clutch 模块的简化
实现。Fundamental Friction Clutch 需要动摩擦和静摩擦极限力矩作为输入信号。Disc Friction
Clutch 不需要这些输入数据。相反，该模块
根据离合器参数和输入压力信号 *P* 计算动摩擦和静摩擦。

当您施加高于阈值的压力信号，使得施加压力等于或超过压力阈值，即 P≥Pth 时，该模块可以对传动系运动施加两种摩擦力：动摩擦和静摩擦。离合器仅当一条传动系轴相对于另一条传动系轴旋转时才施加动摩擦力矩。当两条传动系轴锁定并一起旋转时，离合器施加
静摩擦力矩。该模块通过多步测试进行迭代，以确定何时锁定和解锁
离合器。

**动摩擦**

动摩擦力矩与相对打滑方向相反，并以整体负号施加。在数学上，动摩擦是黏性阻力矩和表面接触摩擦力矩的正和：

τk=μ⋅ω+τcontact。

- *τK* 是动摩擦力矩。
- *μ* 是黏性阻力系数。
- *ω* 是相对角速度，或打滑
  速度。
- *τcontact* 是接触力矩。

接触摩擦是六个因子的乘积，因此

τcontact=kK⋅D⋅N⋅reff⋅Pfric⋅A≥0，

其中：

- *kK* 是离合器片的无量纲动摩擦系数，它是 *ω* 的函数。
- *D* 是离合器降额因子。
- *N* 是摩擦表面数量。
- *reff* 是有效力矩半径，即离合器摩擦力有效力臂。
- *Pfric* 是离合器摩擦能力，使得 Pfric=max[(P−Pth),0]。
- *A* 是啮合表面积。

您将动摩擦系数 *kK* 指定为常数或相对角速度 *ω* 的表格化离散函数。
假定该表格化函数对于相对角速度的正值和负值是对称的。因此，仅针对 *ω* 的正值指定 *kK*。

离合器在其每个 *N* 摩擦表面上施加来自其活塞的法向力，该力为离合器摩擦能力 *Pfric* 和啮合表面积 *A* 的乘积。压力信号 *P* 应为非负。如果 *P* 小于压力阈值 *Pth*，则离合器完全不施加摩擦。

*有效力矩半径* *reff* 是离合器摩擦力的有效力臂，从传动系轴线测量，动摩擦力在摩擦表面处施加于该力臂。它与摩擦表面的几何形状关系为：

reff=23ro3−ri3ro2−ri2，

其中，对于建模为环形圆盘的摩擦表面：

- *ro* 是外盘半径。
- *ri* 是内盘半径。

*离合器降额因子* *D* 考虑了离合器磨损。对于新离合器，*D* 为 1。对于接近*均匀磨损*状态的离合器：

D→34(ro+ ​ri)2ro2+rori+ ​ri2。

**静摩擦**

静摩擦极限与动摩擦相关，将 *ω* 设为零，并将动摩擦系数替换为静摩擦系数：

τS=kS⋅D⋅N⋅reff⋅Pfric⋅A≥0。

其中：

- *τS* 是静摩擦力矩极限，它是静摩擦峰值因子与当 *ω* 趋近 0 时的动摩擦力矩的乘积。
- *kK* 是离合器片的无量纲静摩擦系数。
- *D* 是离合器降额因子。
- *N* 是摩擦表面数量。
- *reff* 是有效力矩半径，即离合器摩擦力有效力臂。
- *Pfric* 是离合器摩擦能力，使得 Pfric=max[(P−Pth),0]。
- *A* 是啮合表面积。

kS>kK，因此在 ω=0 时，通过克服静摩擦来解锁离合器所需的跨离合器力矩 *τ* 大于解锁瞬间的动摩擦。

*静摩擦力矩范围*或极限随后对称定义为

τS≡τS+=−τS−。

**等待状态：锁定和解锁**

Disc Friction Clutch 的等待状态与 Fundamental Friction Clutch 的等待状态相同，只是将正动摩擦条件 τK>0 替换为正离合器摩擦能力条件，即施加压力等于或超过压力阈值，即 P≥Pth。

**离合器耗散的功率**

离合器耗散的功率是打滑速度 *ω* 与动摩擦力矩 *τK* 的乘积的绝对值，即 |ω⋅τK|。仅当离合器既打滑 ω≠0 又施加动摩擦 τk>0 时，它才耗散功率。

### 速度相关和温度相关摩擦模型

**速度相关模型**

您可以通过选择速度相关模型来对旋转速度变化的影响进行建模。要选择速度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Velocity-dependent kinetic
friction coefficient`。有关同时取决于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

对于速度相关模型，以下相关参数会在 **Friction** 设置中变为可见：

- **Relative velocity vector**
- **Kinetic friction coefficient vector**
- **Friction coefficient interpolation
  method**
- **Friction coefficient extrapolation
  method**

**热模型**

您可以通过选择温度相关模型来对热流和温度变化的影响进行建模。要选择温度相关模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature-dependent friction
coefficients`。有关同时取决于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

**热、速度相关模型**

您可以通过选择速度相关且温度相关模型来对旋转速度变化和热流的影响进行建模。要选择同时取决于速度和温度的模型，请在 **Friction** 设置中，将 **Friction model** 参数设置为 `Temperature and
velocity-dependent friction coefficients`。

### 故障

要对 Disc Friction Clutch 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

您可以为模块故障选择以下设置中的任一项或两项。当您触发故障时，该模块会在仿真的剩余时间内根据 **Behavior when faulted** 参数的设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`
