---
type: simulink-block
title: 'Lead Screw Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'leadscrewjoint'
documentation_source_path: 'ref/leadscrewjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Lead Screw Joint

## 端口

### 坐标系

### **B** — 基础坐标系 frame

关节模块的基础坐标系。

### **F** — 从动坐标系 frame

关节模块的从动坐标系。
### 输入

#### 模式配置

### **mode** — 关节模式控制物理信号

用于控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。您可以在仿真期间随时更改模式。

下表显示了在模式之间转换时，关节的位置和速度如何变化。

| Transitions | Position | Velocity |
| --- | --- | --- |
| Normal to Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal to Disengaged | 关节位置保留当前值，但在转换后可以沿任意方向变化。 | 关节速度保留当前值，但在转换后可以沿任意方向变化。 |
| Locked to Normal | 关节位置保留当前值，但在转换后可以沿与关节自由度 (DOFs) 对齐的方向变化。 | 关节速度保持为零，但在转换后可以沿与关节 DOFs 对齐的方向变化。 |
| Locked to Disengaged | 关节位置保留当前值，但在转换后可以沿任意方向变化。 | 关节速度保持为零，但在转换后可以沿任意方向变化。 |
| Disengaged to Normal | 对于与关节 DOFs 对齐的方向，关节位置最初取通过 Newton 方法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOFs 对齐的方向，关节速度最初取通过 Newton 方法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged to Locked | 对于与关节 DOFs 对齐的方向，关节位置最初取通过 Newton 方法计算的值，并在转换后保持恒定。在约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

#### 旋转

### **q** — 关节旋转物理信号

输出从动坐标系相对于基础坐标系的旋转角的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Rotation** 下，选择 **Position**。

### **w** — 关节旋转一阶导数的物理信号

输出关节旋转一阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Rotation** 下，选择 **Velocity**。

### **b** — 关节旋转二阶导数的物理信号

输出关节旋转二阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Rotation** 下，选择 **Acceleration**。

#### 平移

### **p** — 关节平移物理信号

输出从动坐标系相对于基础坐标系的关节平移的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Translation** 下，选择 **Position**。

### **v** — 关节平移一阶导数的物理信号

输出关节平移一阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Translation** 下，选择 **Velocity**。

### **a** — 关节平移二阶导数的物理信号

输出关节平移二阶导数的物理信号端口。

#### 依赖关系

要启用此端口，请在 **Sensing** > **Translation** 下，选择 **Acceleration**。

#### 复合力/力矩传感

### **fc** — 约束力物理信号

输出作用在关节中的约束力的物理信号端口。该力维持关节的平移约束。有关详细信息，请参阅 Measure Joint Constraint Forces。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩物理信号

输出作用在关节中的约束力矩的物理信号端口。该力矩维持关节的旋转约束。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力物理信号

输出作用在关节中的总力的物理信号端口。总力是通过关节从一个坐标系传递到另一个坐标系的力之和。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩物理信号

输出作用在关节中的总力矩的物理信号端口。总力矩是通过关节从一个坐标系传递到另一个坐标系的力矩之和。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### Z 丝杠基元 (LSz)

### **Direction** — 丝杠关节的旋向 `Right-Hand` (默认) | `Left-Hand`

丝杠关节的旋向，指定为 `Right-Hand` 或 `Left-Hand`。右旋关节将正旋转转换为正线性运动，而左旋关节将正旋转转换为负线性运动。

### **Lead** — 丝杠关节的导程 1 `mm/rev` (默认) | 标量

丝杠关节的导程，指定为具有长度/角度单位的标量。导程是指从动坐标系在从动坐标系完整旋转一圈时沿基础坐标系的 *z* 轴移动的距离。

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off` (默认) | `on`

选择此参数可启用用于指定关节基元位置目标的参数。

### **Priority** — 位置目标的优先级级别 `High (desired)` (默认) | `Low (approximate)`

位置目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Position Target**。

### **Based On** — 用于指定位置目标的运动类型 `Translation` (默认) | `Rotation`

用于指定位置目标的运动类型，指定为 `Translation` 或 `Rotation`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Position Target**。

### **Value** — 旋转位置目标 0 `deg` (默认) | 具有角度单位的标量

旋转位置目标，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请在 **State Targets** > **Specify Position Target** > **Based On** 下，选择 **Rotation**。

### **Value** — 平移位置目标 0 `m` (默认) | 具有长度单位的标量

平移位置目标，指定为具有长度单位的标量。

#### 依赖关系

要启用此参数，请在 **State Targets** > **Specify Position Target** > **Based On** 下，选择 **Translation**。

### **Specify Velocity Target** — 是否指定速度目标 `off` (默认) | `on`

选择此参数可启用用于指定关节基元速度目标的参数。

### **Priority** — 速度目标的优先级级别 `High (desired)` (默认) | `Low (approximate)`

速度目标的优先级级别，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Velocity Target**。

### **Based On** — 用于指定速度目标的运动类型 `Translation` (默认) | `Rotation`

用于指定速度目标的运动类型，指定为 `Translation` 或 `Rotation`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Velocity Target**。

### **Value** — 角速度目标 0 `deg/s` (默认) | 具有角速度单位的标量

关节基元的角速度目标，指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请在 **State Targets** > **Specify Position Target** > **Based On** 下，选择 **Rotation**。

### **Value** — 线速度目标 0 `m/s` (默认) | 具有线速度单位的标量

关节基元的线速度目标，指定为具有线速度单位的标量。

#### 依赖关系

要启用此参数，请在 **State Targets** > **Specify Position Target** > **Based On** 下，选择 **Translation**。

### 模式配置

### **Mode** — 关节模式 `Normal` (默认) | `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| Mode | Description |
| --- | --- |
| `Locked` | `Locked` 模式约束关节的所有自由度 (DOFs)。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置感测力或力矩。 |
| `Normal` | `Normal` 模式启用 DOFs，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | `Disengaged` 模式在整个仿真期间将关节从所有约束中释放。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **输入** 部分中的端口 **mode**。 |

### 复合力/力矩传感

### **Direction** — 测量方向 `Follower on Base` (默认) | `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量值的坐标系 `Base` (默认) | `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2025a：对模式故障建模

现在可以为所有关节模块对模式故障建模。使用这些故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **故障** 部分。

## 描述

具有耦合旋转和平移自由度的关节

Lead Screw Joint 模块表示一个具有一个自由度的关节，并对一对耦合的旋转和平移进行建模，如图所示。

丝杠关节基元的示意图

在仿真期间，关节约束基础坐标系和从动坐标系的 *z* 轴保持对齐。从动坐标系原点可以沿基础 *z* 轴平移，而从动 *x* 轴和 *y* 轴绕基础坐标系 *z* 轴旋转。平移与旋转成比例，比例基于 **Lead** 和 **Direction** 参数的值。

要指定关节初始状态的目标，请使用 **State Targets** 下的参数。您可以基于关节坐标系之间的相对旋转或平移来指定目标。要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅 **端口** 和 **参数** 部分下的 **Mode Configuration**。

关节模块具有输出传感数据（例如位置、速度、加速度、力和力矩）的端口，您可以使用这些数据对模型执行分析任务。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为脱离状态。

要向关节模块添加模式故障，请点击该关节模块，在 **Simscape Block** 选项卡的 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以为关节模块添加多个故障，但关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真处于开启状态。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
