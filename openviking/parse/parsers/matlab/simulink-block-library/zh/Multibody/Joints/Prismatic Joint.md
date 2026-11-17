---
type: simulink-block
title: 'Prismatic Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'prismaticjoint'
documentation_source_path: 'ref/prismaticjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Prismatic Joint

## 端口

### 坐标系

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 随动坐标系 frame

关节模块的随动坐标系。
### 输入

### **f** — 驱动力 physical signal

物理信号输入端口，接受关节原语的驱动力。该信号提供施加在关节原语的基础坐标系和随动坐标系上的力值。

#### 依赖

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Force** 设置为 `Provided by Input`。

### **p** — 运动轮廓 physical signal

物理信号输入端口，接受关节原语的运动轮廓。该信号提供随动坐标系相对于基础坐标系沿关节原语轴的位移。注意，该信号还必须包含位移的一阶和二阶导数。

#### 依赖

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制 physical signal

控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，为脱离；当输入信号为 `1` 时，为锁定。您可以在仿真过程中的任何时间更改模式。

下表显示了关节在模式转换期间位置和速度的变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保持当前值，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |
| 正常到脱离 | 关节位置保持当前值，但转换后可以在任何方向上变化。 | 关节速度保持当前值，但转换后可以在任何方向上变化。 |
| 锁定到正常 | 关节位置保持当前值，但转换后可以在与关节自由度（DOF）对齐的方向上变化。 | 关节速度保持为零，但转换后可以在与关节自由度对齐的方向上变化。 |
| 锁定到脱离 | 关节位置保持当前值，但转换后可以在任何方向上变化。 | 关节速度保持为零，但转换后可以在任何方向上变化。 |
| 脱离到正常 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在转换后保持不变。 | 对于与关节自由度对齐的方向，关节速度初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在转换后保持不变。 |
| 脱离到锁定 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，并在转换后保持不变。在约束方向上，关节位置变为零，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |

#### 依赖

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

### **p** — 原语位置 physical signal

输出原语位置的物理信号端口。该值为随动坐标系相对于基础坐标系的位移。

#### 依赖

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Position**。

### **v** — 原语速度 physical signal

输出原语速度的物理信号端口。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Velocity**。

### **a** — 基元物理信号的加速度

输出基元加速度的物理信号端口。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Acceleration**。

### **f** — 作用在关节基元上的致动力物理信号

输出作用在关节基元上的致动力的物理信号端口。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Actuator Force**。

### **fll** — 下限力物理信号

输出下限力的物理信号端口。当关节基元位置小于自由区域的下界时，该模块施加此力。该力施加到关节基元的基座和从动框架上，以将位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Lower-Limit Force**。

### **ful** — 上限力物理信号

输出上限力的物理信号端口。当关节基元位置超过自由区域的上界时，该模块施加此力。该力施加到关节基元的基座和从动框架上，以将位置加速回自由区域。

#### 依赖项

要启用此端口，请在 **Z Prismatic Primitive (Pz)** > **Sensing** 下，选择 **Upper-Limit Force**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在相连框架之间传递的所有力之和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，下图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括致动力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在相连框架之间传递的所有力矩之和。该力矩包括致动力矩、内力矩、极限力矩和约束力矩。输出为 3×1 向量格式，表示绕解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

### Z Prismatic Primitive (Pz)

### **State Targets > Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元位置目标的参数。

### **State Targets > Specify Position Target > Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **State Targets** 下选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value** — 位置目标 0 `m`（默认）| 以长度单位为单位的标量

关节基元的位置目标，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **State Targets** 下选择 **Specify Position Target**。

### **State Targets > Specify Velocity Target** — 是否指定速度目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元速度目标的参数。

### **State Targets > Specify Velocity Target > Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **State Targets** 下选择 **Specify Velocity Target**。

### **State Targets > Specify Velocity Target > Value** — 关节基元的速度目标 0 `m/s`（默认）| 以线速度单位为单位的标量

关节基元的速度目标，指定为以线速度单位为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **State Targets** 下选择 **Specify Velocity Target**。

### **Internal Mechanics > Equilibrium Position** — 内力为零时的位置 0 `m`（默认）| 以长度单位为单位的标量

弹簧力为零时的位置，指定为以长度单位为单位的标量。该值指定基元的位置。

### **Internal Mechanics > Spring Stiffness** — 力律的刚度 0 `N/m`（默认）| 以线性刚度为单位的标量

关节基元的内部弹簧-阻尼力律的刚度，指定为以线性刚度为单位的标量。

### **Internal Mechanics > Damping Coefficient** — 力律的阻尼系数 0 `N(m/s)`（默认）| 以线性阻尼系数为单位的标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为以线性阻尼系数为单位的标量。

### **Limits > Specify Lower Limit** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以启用用于指定关节基元下限的参数。

### **Limits > Specify Lower Limit > Bound** — 自由区域的下界 -1 `m`（默认）| 以长度单位为单位的标量

关节基元自由区域的下界，指定为以长度单位为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Spring Stiffness** — 下界处的弹簧刚度 1e6 `N/m`（默认）| 以线性刚度为单位的标量

下界处的弹簧刚度，指定为以线性刚度为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Damping Coefficient** — 下界处的阻尼系数 1e3 `N/(m/s)`（默认）| 以线性阻尼系数为单位的标量

下界处的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 以长度单位为标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为标量。

当穿透量达到过渡区域的宽度时，模块施加该力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Upper Limit** — 是否指定上限位置 `off`（默认）| `on`

选择此参数以启用用于指定关节基元上限的参数。

### **Limits > Specify Upper Limit > Bound** — 自由区域的上界 1 `m`（默认）| 以长度单位为标量

关节基元自由区域的上界，指定为以长度单位为标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Spring Stiffness** — 上界处弹簧的刚度 1e6 `N/m`（默认）| 以线性刚度为单位的标量

上界处弹簧的刚度，指定为以刚度为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Damping Coefficient** — 上界处的阻尼系数 1e3 `N/(m/s)`（默认）| 以线性阻尼系数为单位的标量

上界处的阻尼系数，指定为以线性阻尼系数为单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 1e-4 `m`（默认）| 以长度单位为标量

用于平滑弹簧和阻尼力的区域，指定为以长度单位为标量。

当穿透量达到过渡区域的宽度时，模块施加该力的完整值。区域越小，力的起始越尖锐，求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请在 **Z Prismatic Primitive (Pz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Actuation > Force** — 提供致动力的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供致动力的选项，指定为表中的值。

| 致动力设置 | 描述 |
| --- | --- |
| `None` | 无致动力。 |
| `Provided by Input` | 输入端口 **f** 指定关节基元的致动力。 |
| `Automatically computed` | 模块自动计算满足机构运动输入所需的力的大小。请注意，如果将此参数设置为 `Automatically computed`，并不意味着必须对同一关节基元的 **Motion** 参数使用 `Provided by Input`。自动计算的力可能是为了满足机构中其他位置的运动输入。 |

### **Actuation > Motion** — 提供驱动运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供驱动运动的选项，指定为表中的值。

| 驱动运动设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 输入端口 **p** 指定关节基元的驱动运动。 |

### **Sensing > Position** — 是否检测关节基元位置 关（默认）| 开

选择此参数以启用输出端口 **p**。

### **Sensing > Velocity** — 是否检测关节基元速度 关（默认）| 开

选择此参数以启用端口 **v**。

### **Sensing > Acceleration** — 是否检测关节基元加速度 关（默认）| 开

选择此参数以启用端口 **a**。

### **Sensing > Actuator Force** — 是否检测关节执行器力 关（默认）| 开

选择此参数以启用端口 **f**。

### **Sensing > Lower-Limit force** — 是否检测下限力 关（默认）| 开

选择此参数以启用端口 **fll**。

### **Sensing > Upper-Limit force** — 是否检测上限力 关（默认）| 开

选择此参数以启用端口 **ful**。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置检测力或力矩。 |
| `Normal` | 正常模式启用自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩检测

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块检测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块检测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base`（默认）| `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障建模

现在可以为所有关节模块建模模式故障。利用这些故障，您可以在仿真过程中更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的**故障**部分。

## 描述

允许沿单轴相对运动的关节

Prismatic Joint 模块建模了一种连接，该连接将两个坐标系之间的相对运动限制为一个平移自由度。这种运动类型常见于液压缸或气缸中。

棱柱关节的自由度

Prismatic Joint 模块只有一个棱柱基元，沿基坐标系的 *z* 轴方向。在仿真过程中，基坐标系和从坐标系的 *z* 轴对齐，从坐标系沿 *z* 轴相对于基坐标系移动，如图所示。

棱柱关节的棱柱基元

同时，从坐标系的 *x* 轴和 *y* 轴分别保持与基坐标系的 *x* 轴和 *y* 轴平行。

要为关节基元指定初始状态的目标，请使用**状态目标**下的参数。目标在基坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将决定先满足哪些目标以及满足的程度。有关示例，请参阅多体装配工作原理中的引导装配部分。

要为关节基元建模阻尼和弹簧行为，请使用**内部力学**下的参数。使用**阻尼系数**参数建模能量耗散，使用**弹簧刚度**参数建模能量存储。关节弹簧试图将关节基元从其平衡位置移开，关节阻尼器充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限制，请使用**限制**下的参数。下限和上限定义了自由区域的宽度。当位置超出边界时，模块施加力将关节位置加速回自由区域。模块使用平滑弹簧-阻尼方法计算力。有关平滑弹簧-阻尼方法的详细信息，请参阅空间接触力模块的描述部分。

**驱动**部分中的**力**、**力矩**和**运动**参数控制仿真过程中关节基元的运动。有关详细信息，请参阅指定关节驱动输入。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和力矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅传感以及力和力矩传感。

要指定关节模式配置，请使用**模式**参数。有关更多详细信息，请参阅**端口**和**参数**部分下的**模式配置**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡中的 **Faults** 部分，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
