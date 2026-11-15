---
type: simulink-block
title: 'Revolute Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Assembly / Joints / Joints with One or No Primitives'
documentation_page: 'revolutejoint'
documentation_source_path: 'ref/revolutejoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Revolute Joint

## 端口

### 坐标系

### **B** — 基坐标系 frame

关节模块的基坐标系。

### **F** — 从坐标系 frame

关节模块的从坐标系。
### 输入

### **t** — 驱动力矩 physical signal

物理信号输入端口，接受关节基元的驱动力矩。该信号提供施加在关节基元的基坐标系和从坐标系上的扭矩值。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Torque** 设置为 `Provided by Input`。

### **q** — 运动曲线 physical signal

物理信号输入端口，接受关节基元的运动曲线。该信号提供从坐标系相对于基坐标系绕关节基元轴线的旋转。注意，该信号还必须包含该旋转的一阶和二阶导数。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Actuation** 下，将 **Motion** 设置为 `Provided by Input`。

#### 模式配置

### **mode** — 关节模式控制 physical signal

控制关节模式的输入端口。该信号必须是无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。可在仿真期间随时更改模式。

下表显示在模式之间转换期间关节的位置和速度如何变化。

| Transitions | Position | Velocity |
| --- | --- | --- |
| Normal to Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal to Disengaged | 关节位置保留当前值，但可在转换后沿任意方向变化。 | 关节速度保留当前值，但可在转换后沿任意方向变化。 |
| Locked to Normal | 关节位置保留当前值，但可在转换后沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但可在转换后沿与关节自由度 (DOFs) 对齐的方向变化。 |
| Locked to Disengaged | 关节位置保留当前值，但可在转换后沿任意方向变化。 | 关节速度保持为零，但可在转换后沿任意方向变化。 |
| Disengaged to Normal | 对于与关节自由度 (DOFs) 对齐的方向，关节位置初始采用通过牛顿法计算的值，之后可变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节自由度 (DOFs) 对齐的方向，关节速度初始采用通过牛顿法计算的值，之后可变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged to Locked | 对于与关节自由度 (DOFs) 对齐的方向，关节位置初始采用通过牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖项

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

### **q** — 关节基元位置 physical signal

物理信号端口，输出关节基元的位置。该值是从坐标系相对于基坐标系的旋转角。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Position**。

### **w** — 关节基元位置的一阶导数 physical signal

物理信号端口，输出关节基元位置的一阶导数。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Velocity**。

### **b** — 关节基元位置的二阶导数 physical signal

物理信号端口，输出关节基元位置的二阶导数。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Acceleration**。

### **t** — 作用在关节基元上的执行器扭矩 physical signal

物理信号端口，输出作用在关节基元上的执行器扭矩。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Actuator Torque**。

### **tll** — 下限扭矩 physical signal

物理信号端口，输出下限扭矩。当关节基元位置超过自由区域的下界时，模块会施加该扭矩。该扭矩施加到关节基元的基坐标系和从坐标系，以使位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Lower-Limit Torque**。

### **tul** — 上限扭矩 physical signal

物理信号端口，输出上限扭矩。当关节基元位置超过自由区域的上界时，模块会施加该扭矩。该扭矩施加到关节基元的基坐标系和从坐标系，以使位置加速回到自由区域。

#### 依赖项

要启用此端口，请在 **Z Revolute Primitive (Rz)** > **Sensing** 下，选择 **Upper-Limit Torque**。

#### 复合力/扭矩感测

### **fc** — 约束力，N physical signal

物理信号端口，输出作用在关节两端的约束力。这些力维持关节的平移约束。输出采用 3-by-1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅力和扭矩感测。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束扭矩，N\*m physical signal

物理信号端口，输出作用在关节两端的约束扭矩。这些扭矩维持关节的旋转约束。输出采用 3-by-1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅力和扭矩感测。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N physical signal

物理信号端口，输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力之和。输出采用 3-by-1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅力和扭矩感测。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总扭矩，N\*m physical signal

物理信号端口，输出作用在关节上的总扭矩。总扭矩是通过关节在相连坐标系之间传递的所有扭矩之和。该扭矩包括驱动力矩、内力矩、限值扭矩和约束扭矩。输出采用 3-by-1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的扭矩分量。有关详细信息，请参阅力和扭矩感测。

#### 依赖项

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

### Z Revolute Primitive (Rz)

### **State Targets > Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数可启用用于指定关节基元位置目标的参数。

### **State Targets > Specify Position Target > Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value** — 位置目标的角度 0 `deg`（默认）| 具有角度单位的标量

用于指定位置目标的角度，指定为具有角度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Velocity Target** — 是否指定速度目标 `off`（默认）| `on`

选择此参数可启用用于指定关节基元速度目标的参数。

### **State Targets > Specify Velocity Target > Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **State Targets > Specify Velocity Target > Value** — 关节基元的速度目标 0 `deg/s`（默认）| 具有角速度单位的标量

关节基元的速度目标，指定为具有角速度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **Internal Mechanics > Equilibrium Position** — 内部扭矩为零时的位置 0 `deg`（默认）| 具有角度单位的标量

弹簧扭矩为零时的位置，指定为具有角度单位的标量。该值指定从坐标系相对于基坐标系的旋转角。

### **Internal Mechanics > Spring Stiffness** — 力律的刚度 0 `N*m/deg`（默认）| 具有刚度单位的标量

关节基元内部弹簧-阻尼力律的刚度，指定为具有刚度单位的标量。

### **Internal Mechanics > Damping Coefficient** — 力律的阻尼系数 0 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

关节基元内部弹簧-阻尼力律的阻尼系数，指定为具有阻尼系数单位的标量。

### **Limits > Specify Lower Limit** — 是否指定位置下限 `off`（默认）| `on`

选择此参数可启用用于指定关节基元下限的参数。

### **Limits > Specify Lower Limit > Bound** — 自由区域的下界 -90 `deg`（默认）| 具有角度单位的标量

关节基元自由区域的下界，指定为具有角度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Spring Stiffness** — 下界处的弹簧刚度 1e4 `N*m/deg`（默认）| 具有刚度单位的标量

下界处的弹簧刚度，指定为具有刚度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Damping Coefficient** — 下界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

下界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Lower Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 0.1 `deg`（默认）| 具有角度单位的标量

用于平滑弹簧和阻尼力的区域，指定为具有角度单位的标量。

一旦穿透量达到过渡区域的宽度，力就达到完整值。区域越小，力的起始越尖锐，并且求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Lower Limit**。

### **Limits > Specify Upper Limit** — 是否指定位置上限 `off`（默认）| `on`

选择此参数可启用用于指定关节基元上限的参数。

### **Limits > Specify Upper Limit > Bound** — 自由区域的上界 90 `deg`（默认）| 具有角度单位的标量

关节基元自由区域的上界，指定为具有角度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Spring Stiffness** — 上界处的弹簧刚度 1e4 `N*m/deg`（默认）| 具有刚度单位的标量

上界处的弹簧刚度，指定为具有刚度单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Damping Coefficient** — 上界处的阻尼系数 10 `N*m/(deg/s)`（默认）| 具有阻尼系数单位的标量

上界处的阻尼系数，指定为具有阻尼系数单位的标量。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Limits > Specify Upper Limit > Transition Region Width** — 用于平滑弹簧和阻尼力的区域 0.1 `deg`（默认）| 具有角度单位的标量

用于平滑弹簧和阻尼力的区域，指定为具有角度单位的标量。

一旦穿透量达到过渡区域的宽度，力就达到完整值。区域越小，力的起始越尖锐，并且求解器所需的时间步长越小。在仿真精度和仿真速度之间的权衡中，减小过渡区域可提高精度，而扩大过渡区域可提高速度。

#### 依赖项

要启用此参数，请在 **Z Revolute Primitive (Rz)** > **Limits** 下，选择 **Specify Upper Limit**。

### **Actuation > Torque** — 提供驱动力矩的选项 `None`（默认）| `Provided by Input` | `Automatically Computed`

用于为关节基元提供驱动力矩的选项，指定为 `None`、`Provided by Input` 或 `Automatically Computed`。

| Actuation Torque Setting | 描述 |
| --- | --- |
| `None` | 无驱动力矩。 |
| `Provided by Input` | 暴露输入端口 **t**。 |
| `Automatically computed` | 为满足机构的运动输入所需的扭矩。该模块自动计算扭矩。请注意，如果将此参数设置为 `Automatically computed`，并不意味着必须对同一关节基元的 **Motion** 参数使用 `Provided by Input`。自动计算的扭矩可能是为了满足机构中其他位置的运动输入。 |

### **Actuation > Motion** — 用于提供致动运动的选项 `Automatically Computed`（默认） | `Provided by Input`

用于为关节基元提供致动运动的选项，指定为 `Automatically Computed` 或 `Provided by Input`。

| Actuation Torque Setting | 描述 |
| --- | --- |
| `Automatically computed` | 该模块基于模型动力学计算并应用关节基元运动。 |
| `Provided by Input` | 暴露输入端口 **q**。 |

### **Sensing > Position** — 是否检测关节基元位置 off（默认） | on

选择此参数以启用输出端口 **q**。

### **Sensing > Velocity** — 是否检测关节基元速度 off（默认） | on

选择此参数以启用端口 **w**。

### **Sensing > Acceleration** — 是否检测关节基元加速度 off（默认） | on

选择此参数以启用端口 **b**。

### **Sensing > Lower-Limit Torque** — 是否检测下限扭矩 off（默认） | on

选择此参数以启用端口 **tll**。

### **Sensing > Upper-Limit Torque** — 是否检测上限扭矩 off（默认） | on

选择此参数以启用端口 **tul**。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认） | `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| Mode | 描述 |
| --- | --- |
| `Locked` | `Locked` 模式约束关节的所有自由度 (DOFs)。锁定的关节在仿真期间以零速度保持其初始装配位置。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置检测力或扭矩。 |
| `Normal` | `Normal` 模式在仿真期间启用 DOF，并使关节的约束按预期工作。 |
| `Disengaged` | `Disengaged` 模式在整个仿真期间将关节从所有约束中释放。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不会影响已分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您使用输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/扭矩传感

### **Direction** — 测量方向 `Follower on Base`（默认） | `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 该模块检测从动坐标系施加在基坐标系上的力和扭矩。
- `Base on Follower` — 该模块检测基坐标系施加在从动坐标系上的力和扭矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base`（默认） | `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 该模块在基坐标系的坐标中解析测量值。
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

### R2025a：对模式故障进行建模

现在可以为所有关节模块对模式故障进行建模。使用这些故障，可以在仿真过程中更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有一个旋转基元的关节

Revolute Joint 模块对一个具有一个旋转自由度的关节建模。

Revolute Joint 的自由度

该关节将两个任意坐标系的运动约束为绕公共轴的纯旋转，这两个任意坐标系连接到关节的基坐标系和从动坐标系。旋转轴与关节基坐标系的 *z* 轴对齐。基坐标系和从动坐标系具有公共原点和 *z* 轴，并且从动坐标系绕 *z* 轴旋转，如图所示。

Revolute Joint 的旋转基元

要为关节基元指定初始状态的目标，请使用 **State Targets** 下的参数。这些目标在基坐标系中指定。还可以为目标设置优先级。如果关节无法满足所有状态目标，则优先级决定首先满足哪些目标以及满足它们的接近程度。有关示例，请参阅 How Multibody Assembly Works 的 Guiding Assembly 部分。

要为关节基元对阻尼和弹簧行为建模，请使用 **Internal Mechanics** 下的参数。使用 **Damping Coefficient** 参数对能量耗散建模，使用 **Spring Stiffness** 参数对能量存储建模。关节弹簧试图使关节基元偏离其平衡位置，关节阻尼器充当能量耗散元件。弹簧和阻尼器严格线性。

要指定关节基元的限值，请使用 **Limits** 下的参数。下限和上限定义自由区域的宽度。当位置超出边界时，该模块施加力，以将关节位置加速回自由区域。该模块使用平滑弹簧-阻尼器方法计算该力。有关平滑弹簧-阻尼器方法的详细信息，请参阅 Spatial Contact Force 模块的描述部分。

**Actuation** 部分中的 **Force**、**Torque** 和 **Motion** 参数控制仿真期间关节基元的运动。有关详细信息，请参阅 Specifying Joint Actuation Inputs。此外，关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。有关详细信息，请参阅 Sensing and Force and Torque Sensing。

要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **模式配置**。

### 故障

使用模式故障，可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为 `Disengaged` 模式。

要向关节模块添加模式故障，请单击该关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，单击 **Fault** > `Add Fault`。或者，可以单击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后单击 Add a fault on the block icon 按钮以添加故障。可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请单击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，可以使用 Simulink® 信号、Simscape™ 语言模块和 MATLAB® 工作区变量。要设置模块的活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，单击 **Faults** > `Fault Dashboard`。

要创建和修改故障，还可以使用 Simscape 和 Simulink 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls and Simscape Faults Interface 的函数部分。
