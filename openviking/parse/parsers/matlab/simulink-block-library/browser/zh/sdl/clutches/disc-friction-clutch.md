---
type: simulink-block
title: 'Disc Friction Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'discfrictionclutch'
documentation_source_path: 'ref/discfrictionclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Disc Friction Clutch

## 端口

### 输入

### **P** — 压力物理信号

离合器片之间所施加压力的物理信号输入端口，单位为 Pascals。该模块将小于零的信号饱和为零。
### 守恒

### **B** — 基础机械旋转

与驱动轴（或称基座轴）相关联的旋转守恒端口。

### **F** — 从动机械旋转

与从动轴（或称跟随轴）相关联的旋转守恒端口。

### **H** — 热流热

与热流相关联的热守恒端口。

#### 依赖关系

仅当在 **Friction** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此端口才可见。有关详细信息，请参阅摩擦参数依赖关系和 Friction model。

## 参数

### 几何

### **Geometry model** — 几何参数化方法 `Define effective radius`（默认） | `Define annular region`

用于对离合器摩擦几何进行建模的参数化方法。

#### 依赖关系

**Effective torque radius** 参数仅当此参数设置为 `Define effective radius` 时可见：

这些参数仅当此参数设置为 `Define annular region` 时可见：

- **Friction surface outside diameter**
- **Friction surface inside diameter**

### **Effective torque radius** — 力矩臂半径 `130``mm`（默认） | 正标量

有效力矩臂半径 *reff*，用于确定离合器内部的动摩擦转矩。

#### 依赖关系

仅当 **Geometry model** 参数设置为 `Define effective radius` 时，此参数才可见。

### **Friction surface outside diameter** — 摩擦表面外径 `150` `mm`（默认） | 正标量

沿摩擦盘环形区域外边缘的直径 2*ro*。

#### 依赖关系

仅当 **Geometry model** 参数设置为 `Define annular region` 时，此参数才可见。

### **Friction surface inside diameter** — 摩擦表面内径 `100` `mm`（默认） | 非负标量

沿摩擦盘环形区域内边缘的直径 2*ri*。

#### 依赖关系

仅当 **Geometry model** 参数设置为 `Define annular region` 时，此参数才可见。

### **Number of friction surfaces** — 摩擦表面数量 `4`（默认） | 正标量整数

离合器内部产生摩擦的接触表面数量 *N*。

### **Engagement piston area** — 压力作用面积 `0.001` `m^2`（默认） | 正标量

当活塞向离合器施加压力时，离合器活塞的有效面积 *A*。

### **Directionality** — 允许的滑移方向 `Bidirectional`（默认） | `Unidirectional`

离合器允许其片之间滑移的方向。双向离合器允许正和负滑移速度。单向离合器仅允许正滑移速度。

单向离合器等效于一个摩擦离合器与一个单向离合器并联，后者仅在滑移速度变为正时分离。要对负方向滑移的单向离合器建模，请反向连接基座端口和从动端口。

### 摩擦

下表显示了某些端口、参数和设置的可见性如何取决于您为其他参数选择的选项。

**摩擦参数依赖关系**

| **摩擦** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **Friction model** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 公开：  - 守恒端口 **H** - **Thermal Port** 设置 | | 公开：  - 守恒端口 **H** - **Thermal Port** 设置 | |
| - | **Relative velocity vector** | | - | | **Relative velocity vector** | |
| - | - | | **Temperature vector** | | **Temperature vector** | |
| **Static friction coefficient** | **Static friction coefficient** | | **Static friction coefficient vector** | | **Static friction coefficient vector** | |
| **Kinetic friction coefficient** | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient vector** | | **Kinetic friction coefficient matrix** | |
| - | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | | **Friction coefficient interpolation method** | |
| - | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | | **Friction coefficient extrapolation method** | |
| **De-rating factor** | **De-rating factor** | | **De-rating factor** | | **De-rating factor** | |
| **Clutch velocity tolerance** | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | | **Clutch velocity tolerance** | |
| **Engagement threshold pressure** | **Engagement threshold pressure** | | **Engagement threshold pressure** | | **Engagement threshold pressure** | |

### **Friction model** — 摩擦模型 `Fixed kinetic friction coefficient`（默认） | `Velocity-dependent kinetic friction coefficient` | `Temperature-dependent friction coefficients` | `Temperature and velocity-dependent friction coefficients`

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅摩擦参数依赖关系。

### **Relative velocity vector** — 相对速度 `[0, 100, 1000]` `rad/s`（默认） | 向量

相对速度的输入值，以向量形式给出。向量中的值必须从左到右递增。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Temperature vector** — 温度 `[280, 300, 320]` `K`（默认） | 递增向量

温度的输入值，以向量形式给出。最小值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Static friction coefficient** — 静摩擦系数 `0.35`（默认） | 正标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Static friction coefficient vector** — 静摩擦系数 `[.4, .38, .36]`（默认） | 向量

摩擦系数的静态值或峰值，以向量形式给出。该向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient** — 动摩擦系数 `0.3`（默认） | 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Fixed kinetic friction coefficient` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient vector** — 动摩擦系数 `[.3, .22, .19]`（默认） | `[.3, .28, .25]` | 正向量

动摩擦系数的输出值，以向量形式给出。所有值必须大于零。

如果 **Friction model** 参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认） | 正矩阵

动摩擦系数的输出值，以矩阵形式给出。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Friction coefficient interpolation method** — 外推方法 `Linear`（默认） | `Smooth`

当输入值介于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Friction coefficient extrapolation method** — 插值方法 `Linear`（默认） | `Nearest` | `Error`

当输入值超出参数列表中指定的范围时，用于确定输出值的外推方法：

- `Linear` — 选择此选项以生成一条在外推区域以及与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当您希望数据位于表范围内时，选择此选项以避免进入外推模式。如果输入信号超出表的范围，仿真将停止并生成错误。

有关外推算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

仅当 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **De-rating factor** — 降额系数 `1`（默认） | 正标量

无量纲降额系数 *D*，通过按比例降低离合器摩擦来考虑离合器盘磨损。

### **Clutch velocity tolerance** — 相对速度锁定阈值 `0.001` `rad/s`（默认） | 非负标量

离合器可以锁止的最大滑移速度。滑移速度是基座轴与从动轴角速度之间的带符号差值，即 w=wF−wB。如果动摩擦转矩非零，且传递转矩在静摩擦转矩限值内，则当实际滑移速度低于速度容差时，离合器锁止。

### **Engagement threshold pressure** — 法向接触力阈值 `100` `Pa`（默认） | 非负标量

离合器接合所需的最小压力 *Pth*。如果压力输入信号低于此阈值，离合器会自动分离。

### 粘性损失

### **Viscous friction coefficient** — 粘性摩擦 `0` `N*m/(rad/s)`（默认） | 非负标量

施加于基座轴与从动轴之间相对滑移 *ω* 的粘性摩擦系数 *μ*。

### 初始条件

### **Initial state** — 初始离合器状态 `Unlocked`（默认） | `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：锁止和解锁。锁止的离合器约束基座轴和从动轴以相同速度旋转，即作为一个整体。解锁的离合器允许两轴以不同速度旋转，导致离合器片之间发生滑移。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在属性检查器中，点击 **Fault behavior** 链接以打开故障。

### **Friction fault** — 对离合器故障建模的选项 `Add fault`

是否在模块中对离合器故障建模。要添加故障，请点击 **Add fault** 超链接。

### **Behavior when faulted** — 离合器故障响应 `Cannot transmit power`（默认） | `Cannot unlock`

触发故障时的离合器响应。您可以将离合器故障选择为以下任一项：

- `Cannot transmit power`
- `Cannot unlock`

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接为模块启用故障。

### 热端口

**Thermal Port** 设置仅当在 **Friction** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Thermal mass** — 热质量 `50` `kJ/K`（默认） | 标量

使组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

仅当在 **Friction** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此参数才可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

组件在仿真开始时的温度。初始温度会根据你指定的效率向量改变组件效率，从而影响启动时的啮合损失或摩擦损失。默认值为 `300`
`K`。

#### 依赖项

仅当在 **摩擦** 设置中将 **Friction model** 参数设置为 `Temperature-dependent
friction coefficients` 或 `Temperature
and velocity-dependent friction coefficients` 时，此参数才可见。有关更多信息，请参阅摩擦参数依赖项。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称更改

**Viscous drag torque coefficient** 参数现在是 **Viscous friction coefficient** 参数。

### R2024a：使用 Simscape 故障接口对故障建模

Disc Friction Clutch 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

## 描述

当板压力超过阈值时接合的摩擦离合器盘片

Disc Friction Clutch 模块表示一个摩擦离合器，其两组扁平摩擦片接触以接合。当施加的板压力超过接合阈值压力时，离合器接合。一旦接合，盘片会受到摩擦转矩，从而能够在基座和从动驱动轴之间传递功率。

离合器可以是双向或单向的。双向离合器可以在正方向和负方向打滑。单向离合器只能在正方向打滑。如果从动轴比基轴旋转得更快，则打滑方向为正；如果打滑更慢，则为负。模块将打滑速度定义为差值

ω=ωF−ωB,

其中：

- *ω* 是相对角速度或打滑速度。
- *ωF* 是从动驱动轴的角速度。
- *ωB* 是基座驱动轴的角速度。

模块为离合器盘片之间的施加压力提供物理信号输入端口 **P**。施加压力必须大于或等于零。如果输入信号低于零，模块将板压力视为零。

### 方程

Disc Friction Clutch 模块是 Fundamental Friction Clutch 模块的简化实现。Fundamental Friction Clutch 需要动摩擦和静摩擦极限转矩作为输入信号。Disc Friction Clutch 不需要输入数据。相反，模块根据离合器参数和输入压力信号 *P* 计算动摩擦和静摩擦。

当你施加高于阈值的压力信号，使得施加压力等于或超过压力阈值，即 P≥Pth 时，模块可以对传动系运动施加两种摩擦：动摩擦和静摩擦。仅当一个传动系轴线相对于另一个传动系轴线旋转时，离合器才施加动摩擦转矩。当两个传动系轴线锁定并一起旋转时，离合器施加静摩擦转矩。模块通过多步测试进行迭代，以确定何时锁定和解锁离合器。

**动摩擦**

动摩擦转矩阻碍相对打滑，并带总体负号施加。在数学上，动摩擦是粘性阻力和表面接触摩擦转矩的正值之和：

τk=μ⋅ω+τcontact.

- *τK* 是动摩擦转矩。
- *μ* 是粘性阻力系数。
- *ω* 是相对角速度，或打滑速度。
- *τcontact* 是接触转矩。

接触摩擦是六个因子的乘积，使得

τcontact=kK⋅D⋅N⋅reff⋅Pfric⋅A≥0,

其中：

- *kK* 是离合器盘的无量纲动摩擦系数，它是 *ω* 的函数。
- *D* 是离合器降额因子。
- *N* 是摩擦表面数量。
- *reff* 是有效转矩半径，即离合器摩擦力的有效力臂。
- *Pfric* 是离合器摩擦容量，使得 Pfric=max[(P−Pth),0]。
- *A* 是接合表面积。

你将动摩擦系数 *kK* 指定为常数或相对角速度 *ω* 的表格离散函数。假定表格函数对于相对角速度的正值和负值是对称的。因此，仅针对 *ω* 的正值指定 *kK*。

离合器在其活塞上施加的法向力为离合器摩擦容量 *Pfric* 与接合表面积 *A* 的乘积，作用于 *N* 个摩擦表面中的每一个。压力信号 *P* 应为非负。如果 *P* 小于压力阈值 *Pth*，则离合器完全不施加摩擦。

*有效转矩半径* *reff* 是离合器摩擦力的有效力臂，从传动系轴线测量，是动摩擦力施加在摩擦表面上的力臂。它与摩擦表面的几何形状相关：

reff=23ro3−ri3ro2−ri2,

其中，对于建模为环形盘的摩擦表面：

- *ro* 是外盘半径。
- *ri* 是内盘半径。

*离合器降额因子* *D* 考虑了离合器磨损。对于新离合器，*D* 为 1。对于接近*均匀磨损*状态的离合器：

D→34(ro+ ​ri)2ro2+rori+ ​ri2.

**静摩擦**

静摩擦限制与动摩擦相关，将 *ω* 设为零，并用静摩擦系数替换动摩擦系数：

τS=kS⋅D⋅N⋅reff⋅Pfric⋅A≥0.

其中：

- *τS* 是静摩擦转矩限制，它是静摩擦峰值因子与动摩擦转矩在 *ω* 趋近 0 时的乘积。
- *kK* 是离合器盘的无量纲静摩擦系数。
- *D* 是离合器降额因子。
- *N* 是摩擦表面数量。
- *reff* 是有效转矩半径，即离合器摩擦力的有效力臂。
- *Pfric* 是离合器摩擦容量，使得 Pfric=max[(P−Pth),0]。
- *A* 是接合表面积。

kS>kK，因此通过克服静摩擦解锁离合器所需的跨离合器转矩 *τ* 大于解锁瞬间（ω=0..）的动摩擦。

*静摩擦转矩范围*或限制随后对称定义为

τS≡τS+=−τS−.

**Wait 状态：锁定和解锁**

Disc Friction Clutch 的 Wait 状态与 Fundamental Friction Clutch 的 Wait 状态相同，只是将正动摩擦条件 τK>0 替换为正离合器摩擦容量条件，即施加压力等于或超过压力阈值，P≥Pth。

**离合器耗散的功率**

离合器耗散的功率是打滑速度 *ω* 与动摩擦转矩 *τK* 乘积的绝对值，即 |ω⋅τK|。仅当离合器同时打滑 ω≠0 并施加动摩擦 τk>0 时，它才耗散功率。

### 速度相关和温度相关的摩擦模型

**速度相关模型**

你可以通过选择速度相关模型来建模旋转速度变化的影响。要选择速度相关模型，请在 **摩擦** 设置中将 **Friction model** 参数设置为 `Velocity-dependent kinetic
friction coefficient`。有关同时取决于速度和温度的摩擦模型的信息，请参阅热、速度相关模型。

对于速度相关模型，以下相关参数将在 **摩擦** 设置中变为可见：

- **Relative velocity vector**
- **Kinetic friction coefficient vector**
- **Friction coefficient interpolation
  method**
- **Friction coefficient extrapolation
  method**

**热模型**

你可以通过选择温度相关模型来建模热流和温度变化的影响。要选择温度相关模型，请在 **摩擦** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction
coefficients`。有关同时取决于速度和温度的摩擦模型的信息，请参阅热、速度相关模型。

**热、速度相关模型**

你可以通过选择速度相关且温度相关的模型来建模旋转速度变化和热流的影响。要选择同时取决于速度和温度的模型，请在 **摩擦** 设置中将 **Friction model** 参数设置为 `Temperature and
velocity-dependent friction coefficients`。

### 故障

要建模 Disc Friction Clutch 模块中的故障，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障** 超链接。有关故障建模的更多信息，请参阅故障行为建模和故障触发。

你可以为模块故障选择以下一个或两个设置。当你触发故障时，模块会在仿真的剩余时间内根据 **Behavior when faulted** 参数的设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`
