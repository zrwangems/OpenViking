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
```yaml
ports:
- name: N
  summary: 法向力物理信号
  direction: input
- name: X
  summary: 换挡连杆位置物理信号
  direction: output
- name: B
  summary: 基座机械旋转
  direction: output
- name: F
  summary: 从动件机械旋转
  direction: output
- name: H
  summary: 热流热
  direction: output
- name: S
  summary: 换挡连杆机械旋转
  direction: output
```

### 输入

### **N** — 法向力物理信号

与法向力关联的物理信号端口。该信号为正值或零。小于零的信号将被解释为零。

#### 依赖关系

仅当在**几何**设置中，**换挡连杆控制**参数设置为 `Physical signal` 时，此端口才可见。有关详细信息，请参阅换挡连杆控制和几何参数依赖关系。

### 输出

### **X** — 换挡连杆位置物理信号

与换挡连杆位置关联的物理信号端口。

#### 依赖关系

仅当在**几何**设置中，**换挡连杆控制**参数设置为 `Conserving port` 时，此端口才可见。有关详细信息，请参阅换挡连杆控制和几何参数依赖关系。

### 守恒

### **B** — 基座机械旋转

与驱动（基座）轴关联的机械旋转守恒端口。离合器运动以*滑差* *ω* = *ωF*–*ωB* 来衡量，即从动件相对于基座的角速度。

### **F** — 从动件机械旋转

与从动轴或从动件轴关联的机械旋转守恒端口

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖关系

仅当在**摩擦**设置中，**摩擦模型**参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时，此端口才可见。有关详细信息，请参阅摩擦模型和摩擦参数依赖关系。

### **S** — 换挡连杆机械旋转

与换挡连杆关联的机械旋转守恒端口。

#### 依赖关系

仅当在**几何**设置中，**换挡连杆控制**参数设置为 `Conserving port` 时，此端口才可见。有关详细信息，请参阅换挡连杆控制和几何参数依赖关系。
## 参数
```yaml
parameters:
- name: 接触面最大直径
  summary: 外径 150 mm（默认）| 正标量
  group: 几何
- name: 接触面最小直径
  summary: 内径 100 mm（默认）| 正标量
  group: 几何
- name: 锥半角
  summary: 锥半角 12 deg（默认）| 正标量
  group: 几何
- name: 换挡连杆控制
  summary: 换挡连杆模型 Physical signal（默认）| Conserving port
  group: 几何
- name: 换挡连杆后部硬限位
  summary: 硬限位选项 on（默认）| off
  group: 换挡连杆
- name: 分离时的环毂间隙
  summary: 环毂间隙 3 mm（默认）| 非负标量
  group: 换挡连杆
- name: 环挡块刚度
  summary: 环挡块刚度 10e5 N/m（默认）| 非负标量
  group: 换挡连杆
- name: 环挡块阻尼
  summary: 环挡块阻尼 1e3 N/(m/s)（默认）| 非负标量
  group: 换挡连杆
- name: 换挡连杆粘性摩擦系数
  summary: 换挡连杆粘性摩擦 100 N/(m/s)（默认）| 正标量
  group: 换挡连杆
- name: 连杆行程方向
  summary: 分离行程方向 Positive shift linkage displacement engages clutch（默认）| Negative shift linkage displacement engages clutch
  group: 换挡连杆
- name: 摩擦模型
  summary: 摩擦模型 Fixed kinetic friction coefficient（默认）| Velocity-dependent kinetic friction coefficient | Temperature-dependent
    friction coefficients | Temperature and velocity-dependent friction coefficients
  group: 摩擦
- name: 相对速度向量
  summary: 相对速度 [0, 100, 1000] rad/s（默认）| 向量
  group: 摩擦
- name: 温度向量
  summary: 温度 [280, 300, 320] K（默认）| 递增向量
  group: 摩擦
- name: 静摩擦系数
  summary: 静摩擦系数 0.35（默认）| 标量
  group: 摩擦
- name: 静摩擦系数向量
  summary: 静摩擦系数 [.4, .38, .36]（默认）| 向量
  group: 摩擦
- name: 动摩擦系数
  summary: 动摩擦系数 0.3（默认）| 正标量
  group: 摩擦
- name: 动摩擦系数向量
  summary: 动摩擦系数 [.3, .22, .19]（默认）| [.3, .28, .25] | 向量
  group: 摩擦
- name: Kinetic friction coefficient matrix
  summary: 动摩擦系数 [.34, .32, .3; .3, .28, .25; .25, .2, .15]（默认）| 矩阵
  group: 摩擦
- name: Friction coefficient interpolation method
  summary: 插值方法 Linear（默认）| Smooth
  group: 摩擦
- name: Friction coefficient extrapolation method
  summary: 外插方法 Linear（默认）| Nearest | Error
  group: 摩擦
- name: Velocity tolerance
  summary: 相对速度锁定阈值 0.001 rad/s（默认）| 标量
  group: 摩擦
- name: Threshold force
  summary: 法向接触力阈值 1 N（默认）| 标量
  group: 摩擦
- name: Viscous friction coefficient
  summary: 粘性摩擦 0（默认）| 非负标量
  group: 摩擦
- name: Initial state
  summary: 初始离合器状态 Unlocked（默认）| Locked
  group: 初始条件
- name: 离合器故障
  summary: 对摩擦故障建模的选项 添加故障
  group: 故障
- name: 发生故障时的行为
  summary: 离合器摩擦故障响应 无法传递动力（默认）| 无法解锁
  group: 故障
- name: 热质量
  summary: 热质量 50 kJ/K（默认）| 标量
  group: 热端口
- name: 初始温度
  summary: 初始温度 300 K（默认）| 标量
  group: 热端口
```

### 几何

下表显示了某些参数的可见性如何取决于您为其他参数选择的选项。

**几何参数依赖关系**

| **几何** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **接触面最大直径** | | | | | | |
| **接触面最小直径** | | | | | | |
| **锥半角** | | | | | | |
| **换挡连杆控制** | | | | | | |
| `Physical signal` | | | `Conserving port` | | | |
| 暴露物理信号输入端口 **N** | | | 暴露：  - 守恒端口   **S** - 物理信号输出端口   **X** - **换挡连杆**设置 | | | |

### **接触面最大直径** — 外径 `150` `mm`（默认）| 正标量

外锥直径 *do*。

### **接触面最小直径** — 内径 `100` `mm`（默认）| 正标量

内锥直径 *di*。

### **锥半角** — 锥半角 `12` `deg`（默认）| 正标量

锥体几何的半开角 *α*。

### **换挡连杆控制** — 换挡连杆模型 `Physical signal`（默认）| `Conserving port`

换挡连杆控制模型：

- `Physical signal` — 暴露物理信号端口 **N**（输入法向力）和 **X**（输出换挡连杆行程）。
- `Conserving port` — 暴露守恒端口 **S**，与换挡连杆控制关联。

#### 依赖关系

**换挡连杆**设置以及端口 **S**、**X** 和 **N** 的可见性取决于此设置。有关详细信息，请参阅几何参数依赖关系。

### 换挡连杆

仅当在**几何**设置中，**换挡连杆控制**参数设置为 `Conserving port` 时，这些设置才可见。有关详细信息，请参阅换挡连杆控制和几何参数依赖关系。

### **换挡连杆后部硬限位** — 硬限位选项 `on`（默认）| `off`

是否在换挡连杆后部包含硬限位。

### **分离时的环毂间隙** — 环毂间隙 `3` `mm`（默认）| 非负标量

分离时的环毂间隙

### **环挡块刚度** — 环挡块刚度 `10e5` `N/m`（默认）| 非负标量

环挡块刚度

### **环挡块阻尼** — 环挡块阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

环挡块阻尼

### **换挡连杆粘性摩擦系数** — 换挡连杆粘性摩擦 `100` `N/(m/s)`（默认）| 正标量

换挡连杆粘性摩擦系数

### **连杆行程方向** — 分离行程方向 `Positive shift linkage displacement engages clutch`（默认）| `Negative shift linkage displacement engages clutch`

使离合器分离的连杆行程方向

### 摩擦

下表显示了某些端口、参数和设置的可见性如何取决于您为其他参数选择的选项。

**摩擦参数依赖关系**

| **摩擦** | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| **摩擦模型** | | | | | | |
| `Fixed kinetic friction coefficient` | `Velocity-dependent kinetic friction coefficient` | | `Temperature-dependent friction coefficients` | | `Temperature and velocity-dependent friction coefficients` | |
| 暴露：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **热端口**设置 | | 暴露：  - 守恒端口   **H** - **摩擦**设置中的热参数 - **热端口**设置 | |
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

用于对动摩擦系数建模的参数化方法。此参数的选项和默认值取决于您为模块选择的摩擦模型。选项包括：

- `Fixed kinetic friction coefficient` — 为动摩擦系数提供固定值。
- `Velocity-dependent kinetic friction coefficient` — 基于圆盘之间的相对角速度，通过一维查表定义动摩擦系数。
- `Temperature-dependent friction coefficients` — 基于温度，通过查表定义动摩擦系数。
- `Temperature and velocity-dependent friction coefficients` — 基于温度和圆盘之间的相对角速度，通过查表定义动摩擦系数。

#### 依赖关系

摩擦模型设置会影响其他参数、设置和端口的可见性。有关详细信息，请参阅摩擦参数依赖关系。

### **相对速度向量** — 相对速度 `[0, 100, 1000]` `rad/s`（默认）| 向量

相对速度的输入值，以向量形式给出。向量中的值必须从左到右递增。最少值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **温度向量** — 温度 `[280, 300, 320]` `K`（默认）| 递增向量

温度的输入值，以向量形式给出。最少值的数量取决于您选择的插值方法。对于线性插值，每个维度至少提供两个值。对于平滑插值，每个维度至少提供三个值。向量中的值必须从左到右递增。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **静摩擦系数** — 静摩擦系数 `0.35`（默认）| 标量

摩擦系数的静态值或峰值。静摩擦系数必须大于动摩擦系数。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Fixed kinetic friction coefficient` 或 `Velocity-dependent kinetic friction coefficient` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **静摩擦系数向量** — 静摩擦系数 `[.4, .38, .36]`（默认）| 向量

摩擦系数的静态值或峰值，以向量形式给出。该向量必须与温度向量具有相同数量的元素。每个值必须大于动摩擦系数向量中对应元素的值。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **动摩擦系数** — 动摩擦系数 `0.3`（默认）| 正标量

动摩擦系数或库仑摩擦系数。该系数必须大于零。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Fixed kinetic friction coefficient` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **动摩擦系数向量** — 动摩擦系数 `[.3, .22, .19]`（默认）| `[.3, .28, .25]` | 向量

动摩擦系数的输出值，以向量形式给出。所有值必须大于零。

如果**摩擦模型**参数设置为

- `Velocity-dependent kinetic friction coefficient` — 该向量必须与相对速度向量具有相同数量的元素。
- `Temperature-dependent friction coefficients` — 该向量必须与温度向量具有相同数量的元素。

#### 依赖关系

此参数仅在**摩擦模型**参数设置为 `Velocity-dependent kinetic friction coefficient` 或 `Temperature-dependent friction coefficients` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **Kinetic friction coefficient matrix** — 动摩擦系数 `[.34, .32, .3; .3, .28, .25; .25, .2, .15]`（默认）| 矩阵

动摩擦系数的输出值，以矩阵形式表示。所有值必须大于零。矩阵的大小必须等于温度向量 × 动摩擦系数相对速度向量所得矩阵的大小。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient interpolation method** — 插值方法 `Linear`（默认）| `Smooth`

当输入值位于两个连续网格点之间时，用于逼近输出值的插值方法：

- `Linear` —
  选择此选项以获得最佳性能。
- `Smooth` —
  选择此选项以生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Friction coefficient extrapolation method** — 外插方法 `Linear`（默认）| `Nearest` | `Error`

当输入值位于参数列表中指定的范围之外时，用于确定输出值的外插方法：

- `Linear` —
  选择此选项以生成在外插区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` —
  选择此选项以生成不高于数据中最高点或不低于数据中最低点的外插。
- `Error` —
  当您希望数据位于表格范围内时，选择此选项以避免进入外插模式。如果输入信号超出表格范围，仿真将停止并生成错误。

有关外插算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

此参数仅在 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`、`Temperature-dependent friction coefficients` 或 `Temperature and velocity-dependent friction coefficients` 时可见。有关详细信息，请参阅 Friction Parameter Dependencies。

### **Velocity tolerance** — 相对速度锁定阈值 `0.001` `rad/s`（默认）| 标量

两个表面可以锁定的相对速度下限。如果 **B** 和 **F** 旋转端口上的扭矩小于有效半径、静摩擦系数和所施加法向力的乘积，则表面锁定。

### **Threshold force** — 法向接触力阈值 `1` `N`（默认）| 标量

施加到物理信号端口 **N** 的法向力仅在力的大小超过 **Threshold force** 参数的值时才施加到接触点。低于 **Threshold force** 的力不会被施加，因此不会传递摩擦力矩。

### **Viscous friction coefficient** — 粘性摩擦 `0`（默认）| 非负标量

粘性摩擦系数。

### 初始条件

### **Initial state** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：锁定和解锁。锁定的离合器约束基轴和从动轴以相同速度旋转，即作为一个整体旋转。解锁的离合器允许两个轴以不同速度旋转，从而导致离合器片之间发生滑移。

### 故障

要修改故障，请创建一个故障，然后在模块对话框中点击 **打开故障属性**。在属性检查器中，点击 **故障行为** 链接以打开故障。

### **离合器故障** — 对摩擦故障建模的选项 `添加故障`

是否在模块中对故障建模。要添加故障，请点击 **添加故障** 超链接。

### **发生故障时的行为** — 离合器摩擦故障响应 `无法传递动力`（默认）| `无法解锁`

故障响应。您可以将离合器故障选择为以下任一选项：

- `无法传递动力`
- `无法解锁`

#### 依赖关系

要启用此参数，请通过点击 **添加故障** 超链接为模块启用故障。

### 热端口

**热端口** 设置仅在 **摩擦** 设置中的 **摩擦模型** 参数设置为 `温度相关摩擦系数` 或 `温度和速度相关摩擦系数` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **热质量** — 热质量 `50` `kJ/K`（默认）| 标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

此参数仅在 **摩擦** 设置中的 **摩擦模型** 参数设置为 `温度相关摩擦系数` 或 `温度和速度相关摩擦系数` 时可见。有关详细信息，请参阅摩擦参数依赖关系。

### **初始温度** — 初始温度 `300` `K`（默认）| 标量

仿真开始时组件的温度。初始温度会根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损失。

#### 依赖关系

此参数仅在 **摩擦** 设置中的 **摩擦模型** 参数设置为 `温度相关摩擦系数` 或 `温度和速度相关摩擦系数` 时可见。有关详细信息，请参阅摩擦参数依赖关系。
## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：参数名称变更

**粘性阻力矩系数** 参数现在为 **粘性摩擦系数** 参数。

### R2025a：枚举更新

**换挡连杆后端的硬限位** 参数现在使用复选框。此参数在之前的版本中使用下拉菜单。

### R2024a：使用 Simscape 故障接口对故障建模

Cone Clutch 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

## 描述

当法向力超过阈值时，带有摩擦片的锥形离合器接合

锥形离合器模块表示具有锥形接触界面的摩擦离合器。锥形界面通过在离合器组件（锥体和锥杯）之间产生楔入作用，降低了离合器接合所需的法向力。锥形离合器的应用包括同步啮合变速箱，它通过同步主动轴和从动轴的转速，使变速器齿轮之间能够更平稳地接合。

锥杯组件与主动轴刚性连接，作为一个整体随之旋转。锥体组件与从动轴刚性连接，从动轴与主动轴轴向对齐。当锥体向锥杯滑动并紧压其内表面时，离合器接合。锥体-锥杯接触界面处的摩擦力使离合器能够在主动轴和从动轴之间传递旋转动力。该模块的摩擦模型包括静摩擦和动摩擦两种贡献，后者会导致锥体和锥杯组件之间打滑时的功率耗散。

锥形离合器模块基于基础摩擦离合器模块。有关完整的摩擦离合器模型，请参见基础摩擦离合器。本节讨论锥形离合器模块中实现的专用模型。

当您施加法向力 *FN* 时，锥形离合器模块可以对传动系运动施加两种摩擦力：动摩擦和静摩擦。离合器仅当一条传动系轴线相对于另一条传动系轴线旋转时才施加动摩擦力矩。当两条传动系轴线锁定并一起旋转时，离合器施加静摩擦力矩。该模块通过多步测试迭代来确定何时锁定和解锁离合器。

### 离合器几何结构与变量

下图展示了锥形离合器的几何结构。

**离合器变量**

| 参数 | 定义 | 含义 |
| --- | --- | --- |
| *d*o | 锥形接触表面的外径 | *参见上图* |
| *d*i | 锥形接触表面的内径 | *参见上图* |
| *α* | 锥体半角 | *参见上图* |
| *ω* | 相对角速度（打滑） | *ω*F – *ω*B |
| *ω*Tol | 离合器锁定的打滑容差 | *参见以下模型* |
| *F*N | 施加在锥形表面上的法向力 | 施加的法向力，若大于阈值：*F*N > *F*th |
| *α* | 锥体半角 | *参见上图* |
| *r*eff | 有效力矩半径 | 离合器摩擦力的有效力臂 |
| *k*K | 动摩擦系数 | 锥形摩擦表面的无量纲动摩擦系数。是 *ω* 的函数。 |
| *k*S | 静摩擦系数 | 锥形摩擦表面的无量纲静摩擦系数。 |
| *τ*K | 动摩擦力矩 | *参见以下模型* |
| *τ*S | 静摩擦力矩极限 | （静摩擦峰值因子）·（*ω* → 0 时的动摩擦力矩）（*参见以下模型*） |

### 与基本摩擦离合器之间的关系

Cone Clutch 模块基于 Fundamental Friction Clutch 模块。Cone Clutch 模块不需要将动摩擦和静摩擦极限转矩作为输入信号，而是根据离合器参数和输入法向力信号 *FN* 计算动摩擦和静摩擦。

**动摩擦**

动摩擦力矩是四个因子的乘积：

τK=kK⋅FN⋅reff⋅sgn(ω)

动摩擦力矩与相对滑移方向相反，并以整体负号施加。当 *ω* 改变符号时，它也会改变符号。

您可以将动摩擦系数 *kK* 指定为常数，或指定为相对角速度 *ω* 的表格化离散函数。假定该表格化函数对于相对角速度的正值和负值是对称的。因此，只需为 *ω* 的正值指定 *k*K。

有效转矩半径 *reff* 是从传动系轴线测量的有效半径，动摩擦力在该半径处施加于摩擦表面。它与锥形摩擦表面的几何形状关系为：

reff=13sinαdo3−di3do2−di2

*do* 和 *di* 分别是接触表面的最大直径和最小直径。

**静摩擦**

静摩擦极限与动摩擦相关，将 *ω* 设为零，并将动摩擦系数替换为静摩擦系数：

TS=kS⋅FN⋅reff≥0

*k*S > *k*K，因此在 *ω* = 0 时，克服静摩擦以解锁离合器所需的转矩 *τ* 大于解锁瞬间的动摩擦。

静摩擦极限定义对称的*静摩擦力矩极限*为：

τS≡τS+=−τS−

范围 [*τ*S–, *τ*S+] 由 Fundamental Friction Clutch 使用。

**接合与锁定条件**

当锥形摩擦表面受到正法向力并产生动摩擦时，离合器接合（传递转矩）：*F*N > 0 且 *τK* > 0。

当且仅当离合器接合，且滑移小于速度容差时，离合器锁定：|*ω*| < *ω*Tol。

**离合器耗散的功率**

离合器耗散的功率为 |*ω*·*τK*|。仅当离合器同时处于滑移状态（ω ≠ 0）并施加动摩擦（*τK* > 0）时，离合器才耗散功率。

### 速度相关模型

您可以通过选择速度相关模型来建模旋转速度变化的影响。要选择速度相关模型，请在 **Friction** 设置中将 **Friction model** 参数设置为 `Velocity-dependent kinetic friction coefficient`。有关同时依赖于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

### 热模型

您可以通过选择温度相关模型来建模热流和温度变化的影响。要选择温度相关模型，请在 **Friction** 设置中将 **Friction model** 参数设置为 `Temperature-dependent friction coefficients`。有关同时依赖于速度和温度的摩擦模型的信息，请参阅 Thermal, Velocity-Dependent Model。

### 热、速度相关模型

您可以通过选择速度相关且温度相关模型来建模旋转速度变化和热流的影响。要选择同时依赖于速度和温度的模型，请在 **Friction** 设置中将 **Friction model** 参数设置为 `Temperature and velocity-dependent friction coefficients`。

### 故障

要对 Cone Clutch 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块将在仿真的剩余时间内根据 **Behavior when faulted** 参数的设置进行响应。故障选项包括：

- `Cannot transmit power`
- `Cannot unlock`
