---
type: simulink-block
title: 'Revolute Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'revolutejoint'
documentation_source_path: 'ref/revolutejoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Revolute Joint

## 端口

### 坐标系

### **B** — 基坐标系 坐标系

关节模块的基坐标系。

### **F** — 从坐标系 坐标系

关节模块的从坐标系。
### 输入

### **t** — 驱动力矩 物理信号

物理信号输入端口，接受关节基元的驱动力矩。该信号提供施加在关节基元和从坐标系上的力矩值。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`。

### **q** — 运动轮廓 物理信号

物理信号输入端口，接受关节基元的运动轮廓。该信号提供从坐标系相对于基坐标系绕关节基元轴的旋转。请注意，该信号还必须包含旋转的一阶和二阶导数。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制 物理信号

控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为脱离；当输入信号为 `1` 时，关节模式为锁定。您可以在仿真过程中的任何时间更改模式。

下表显示了在模式之间转换期间关节位置和速度的变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保持当前值，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |
| 正常到脱离 | 关节位置保持当前值，但转换后可以在任何方向上变化。 | 关节速度保持当前值，但转换后可以在任何方向上变化。 |
| 锁定到正常 | 关节位置保持当前值，但转换后可以在与关节自由度（DOF）对齐的方向上变化。 | 关节速度保持为零，但转换后可以在与关节自由度对齐的方向上变化。 |
| 锁定到脱离 | 关节位置保持当前值，但转换后可以在任何方向上变化。 | 关节速度保持为零，但转换后可以在任何方向上变化。 |
| 脱离到正常 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在转换后保持不变。 | 对于与关节自由度对齐的方向，关节速度初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在转换后保持不变。 |
| 脱离到锁定 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，并在转换后保持不变。在约束方向上，关节位置变为零，并在转换后保持不变。 | 关节速度变为零，并在转换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

### **q** — 关节基元的位置 物理信号

输出关节基元位置的物理信号端口。该值是从坐标系相对于基坐标系的旋转角度。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Position**。

### **w** — 关节基元位置的一阶导数物理信号

输出关节基元位置一阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Velocity**。

### **b** — 关节基元位置的二阶导数物理信号

输出关节基元位置二阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Acceleration**。

### **t** — 作用于关节基元的执行器力矩物理信号

输出作用于关节基元的执行器力矩的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Actuator Torque**。

### **tll** — 下限力矩物理信号

输出下限力矩的物理信号端口。当关节基元位置超出自由区域的下界时，模块施加该力矩。该力矩施加到关节基元的基座坐标系和从动坐标系上，以将位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Lower-Limit Torque**。

### **tul** — 上限力矩物理信号

输出上限力矩的物理信号端口。当关节基元位置超出自由区域的上界时，模块施加该力矩。该力矩施加到关节基元的基座坐标系和从动坐标系上，以将位置加速回自由区域。

#### 依赖关系

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解算坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕解算坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在连接坐标系之间传递的所有力的总和。输出为 3×1 向量格式，表示沿解算坐标系的 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，该图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在连接坐标系之间传递的所有力矩之和。该力矩包括驱动力矩、内力矩、限位力矩和约束力矩。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力与力矩传感。

#### 依赖关系

要启用此端口，请在 **复合力/力矩传感** 下，选择 **总力矩**。

## 参数

### Z 转动基元 (Rz)

### **状态目标 > 指定位置目标** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元位置目标的参数。

### **状态目标 > 指定位置目标 > 优先级** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **Z 转动基元 (Rz)** > **状态目标** 下，选择 **指定位置目标**。

### **状态目标 > 指定位置目标 > 值** — 位置目标的角度 0 `deg`（默认）| 具有角度单位的标量

用于指定位置目标的角度，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z 转动基元 (Rz)** > **状态目标** 下，选择 **指定位置目标**。

### **状态目标 > 指定速度目标** — 是否指定速度目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元速度目标的参数。

### **状态目标 > 指定速度目标 > 优先级** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **Z 转动基元 (Rz)** > **状态目标** 下，选择 **指定速度目标**。

### **状态目标 > 指定速度目标 > 值** — 关节基元的速度目标 0 `deg/s`（默认）| 具有角速度单位的标量

关节基元的速度目标，指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z 转动基元 (Rz)** > **状态目标** 下，选择 **指定速度目标**。

### **内部力学 > 平衡位置** — 内部力矩为零的位置 0 `deg`（默认）| 具有角度单位的标量

弹簧力矩为零的位置，指定为具有角度单位的标量。该值指定从动坐标系相对于基础坐标系的旋转角度。

### **内部力学 > 弹簧刚度** — 力律的刚度 0 `N*m/deg`（默认）| 具有刚度单位的标量

关节基元的内部弹簧-阻尼力律的刚度，指定为具有刚度单位的标量。

### **内部力学 > 阻尼系数** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

关节基元的内部弹簧-阻尼力律的阻尼系数，指定为具有阻尼系数单位的标量。

### **限位 > 指定下限** — 是否指定下限位置 `off`（默认）| `on`

选择此参数以启用用于指定关节基元下限的参数。

### **限位 > 指定下限 > 边界** — 自由区域的下界 -90 `deg`（默认）| 具有角度单位的标量

关节基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z 转动基元 (Rz)** > **限位** 下，选择 **指定下限**。

### **Limits > Specify Lower Limit > Spring Stiffness** — 下界处弹簧的刚度 1e4 `N*m/deg`（默认）| 具有刚度单位的标量

下界处弹簧的刚度，指定为具有刚度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

下界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 0.1 `deg`（默认）| 具有角度单位的标量

用于平滑弹簧和阻尼力的区域，指定为具有角度单位的标量。

一旦侵入量达到过渡区域的宽度，力就会达到完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Upper Limit** — 是否指定上位置限 `off`（默认）| `on`

选择此参数以启用用于指定关节基元上限的参数。

### **Limits > Specify Upper Limit > Bound** — 自由区域的上界 90 `deg`（默认）| 具有角度单位的标量

关节基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Spring Stiffness** — 上界处弹簧的刚度 1e4 `N*m/deg`（默认）| 具有刚度单位的标量

上界处弹簧的刚度，指定为具有刚度单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 0.1 `deg`（默认）| 具有角度单位的标量

用于平滑弹簧和阻尼力的区域，指定为具有角度单位的标量。

一旦侵入量达到过渡区域的宽度，力就会达到完整值。该区域越小，力的起始越尖锐，求解器所需的时间步长也越小。在仿真精度与仿真速度的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖关系

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Actuation > Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

为关节基元提供驱动力矩的选项，指定为 `None`、`Provided by Input` 或 `Automatically Computed`。

| 驱动力矩设置 | 描述 |
| --- | --- |
| `None` | 无驱动力矩。 |
| `Provided by Input` | 暴露输入端口 **t**。 |
| `Automatically computed` | 满足机构运动输入所需的力矩。模块自动计算力矩。请注意，如果将此参数设置为 `Automatically computed`，并不意味着必须对同一关节基元的 **Motion** 参数使用 `Provided by Input`。自动计算的力矩可能是为了满足机构中其他位置的运动输入。 |

### **Actuation > Motion** — 提供驱动运动的选项 `Automatically Computed`（默认）| `Provided by Input`

为关节基元提供驱动运动的选项，指定为 `Automatically Computed` 或 `Provided by Input`。

| 驱动力矩设置 | 描述 |
| --- | --- |
| `Automatically computed` | 模块根据模型动力学计算并施加关节基元运动。 |
| `Provided by Input` | 暴露输入端口 **q**。 |

### **Sensing > Position** — 是否检测关节基元位置 off（默认）| on

选择此参数以启用输出端口 **q**。

### **Sensing > Velocity** — 是否检测关节基元速度 off（默认）| on

选择此参数以启用端口 **w**。

### **Sensing > Acceleration** — 是否检测关节基元加速度 off（默认）| on

选择此参数以启用端口 **b**。

### **Sensing > Lower-Limit Torque** — 是否检测下限力矩 off（默认）| on

选择此参数以启用端口 **tll**。

### **Sensing > Upper-Limit Torque** — 是否检测上限力矩 off（默认）| on

选择此参数以启用端口 **tul**。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置来检测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，约束按预期在仿真期间工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩检测

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块检测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块检测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 该模块在基座坐标系的坐标中解析测量值。
- `Follower` — 该模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### R2025a：模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

具有一个转动基元的关节

Revolute Joint 模块对一个具有一个旋转自由度的关节进行建模。

Revolute Joint 的自由度

该关节将连接到关节基座坐标系和从动坐标系的任意两个坐标系的运动约束为绕公共轴的纯旋转。旋转轴与关节基座坐标系的 *z* 轴对齐。基座坐标系和从动坐标系具有公共原点和 *z* 轴，并且从动坐标系绕 *z* 轴旋转，如图所示。

Revolute Joint 的转动基元

要指定关节基元初始状态的目标，请使用 **State Targets** 下的参数。目标在基座坐标系中指定。您还可以设置目标的优先级。如果关节无法满足所有状态目标，优先级将确定首先满足哪些目标以及满足它们的接近程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元建模阻尼和弹簧行为，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数来建模能量耗散，使用 **Spring Stiffness** 参数来建模能量存储。关节弹簧试图使关节基元偏离其平衡位置，而关节阻尼器充当能量耗散元件。弹簧和阻尼器严格为线性。

要指定关节基元的限值，请使用 **Limits** 下的参数。下限和上限定义自由区域的宽度。当位置超过边界时，该模块施加力以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼器方法计算力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing 和 Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **Ports** 和 **Parameters** 部分下的 **Mode Configuration**。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink® 信号、Simscape™ 语言模块和 MATLAB® 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape 和 Simulink 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
