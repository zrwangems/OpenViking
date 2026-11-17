---
type: simulink-block
title: 'Constant Velocity Joint'
family: 'joints'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'constantvelocityjoint'
documentation_source_path: 'ref/constantvelocityjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Velocity Joint

## 端口

### Frame

### **B** — 基础坐标系 frame

与关节模块的基础坐标系关联的端口。在 CV 关节联接两个轴的典型应用中，基础坐标系的 *Z* 轴与主动轴对齐。

### **F** — 从动坐标系 frame

与关节模块的从动坐标系关联的端口。在 CV 关节联接两个轴的典型应用中，从动坐标系的 *Z* 轴与从动轴对齐。

### 输入

#### Mode Configuration

### **mode** — 关节模式控制物理信号

控制关节模式的输入端口。该信号必须是无量纲 scalar。当输入信号为 `0` 时，关节模式为 normal；当输入信号为 `-1` 时，为 disengaged；当输入信号为 `1` 时，为 locked。您可以在仿真期间随时更改模式。

该表显示了在模式之间转换期间关节的位置和速度如何变化。

| 转换 | 位置 | 速度 |
| --- | --- | --- |
| Normal 到 Locked | 关节位置保留当前值，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |
| Normal 到 Disengaged | 关节位置保留当前值，但可在转换后沿任意方向变化。 | 关节速度保留当前值，但可在转换后沿任意方向变化。 |
| Locked 到 Normal | 关节位置保留当前值，但可在转换后沿与关节自由度 (DOF) 对齐的方向变化。 | 关节速度保持为零，但可在转换后沿与关节 DOF 对齐的方向变化。 |
| Locked 到 Disengaged | 关节位置保留当前值，但可在转换后沿任意方向变化。 | 关节速度保持为零，但可在转换后沿任意方向变化。 |
| Disengaged 到 Normal | 对于与关节 DOF 对齐的方向，关节位置初始采用通过牛顿法计算的值，之后可以变化。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 对于与关节 DOF 对齐的方向，关节速度初始采用通过牛顿法计算的值，之后可以变化。在受约束方向上，关节速度变为零，并在转换后保持恒定。 |
| Disengaged 到 Locked | 对于与关节 DOF 对齐的方向，关节位置初始采用通过牛顿法计算的值，并在转换后保持恒定。在受约束方向上，关节位置变为零，并在转换后保持恒定。 | 关节速度变为零，并在转换后保持恒定。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。

### 输出

### **qb** — 弯曲角 scalar

CV 关节的弯曲角，以 scalar 形式返回。此量是模块的基础坐标系与从动坐标系的 *Z* 轴之间的角度。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Position**。

### **wb** — 弯曲角速度 scalar

CV 关节的弯曲角速度，以 scalar 形式返回。此量等于端口 **qb** 输出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Velocity**。

### **bb** — 弯曲角加速度 scalar

CV 关节的弯曲角加速度，以 scalar 形式返回。此量等于端口 **qb** 输出的信号的二阶时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Acceleration**。

### **qa** — 方位角 scalar

CV 关节的方位角，以 scalar 形式返回。此量是绕基础坐标系 *Z* 轴旋转的角度。该旋转确定弯曲角发生的平面。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Position**。

### **wa** — 方位角速度 scalar

CV 关节的方位角速度，以 scalar 形式返回。此量等于端口 **qa** 输出的信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Velocity**。

### **ba** — 方位角加速度 scalar

CV 关节的方位角加速度，以 scalar 形式返回。此量等于端口 **qa** 输出的信号的二阶时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Acceleration**。

#### Composite Force/Torque Sensing

### **fc** — 约束力，N 物理信号

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出采用 3-by-1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅力和力矩感测。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出采用 3-by-1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩感测。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

输出作用在关节上的总力的物理信号端口。总力是通过关节在连接的坐标系之间传递的所有力之和。输出采用 3-by-1 向量格式，表示沿解析坐标系的 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力 (*F*A)、内力 (*F*I) 和约束力 (*F*C)。有关详细信息，请参阅力和力矩感测。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在连接的坐标系之间传递的所有力矩之和。该力矩包括执行、内部、限制和约束力矩。输出采用 3-by-1 向量格式，表示绕解析坐标系的 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅力和力矩感测。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

### Constant Velocity Primitive (CV)

### **Internal State** — 关节的内部状态参数化 `Rotation Sequence (faster simulations)`（默认）| `Quaternion (allows zero bend angle)`

选择用于指定关节内部状态的参数化。

`Rotation Sequence (faster simulations)`
:   Constant Velocity Joint 模块使用 *Z-Y-Z* 旋转序列参数化。第二个 *Z* 轴旋转的角度是第一个 *Z* 轴旋转角度的负值。

    请尽可能使用此方法，因为使用此参数化的仿真通常比使用四元数参数化的仿真更快。但是，当弯曲角为零时，*Z-Y-Z* 旋转序列参数化具有运动学奇异性。如果需要零弯曲角，请将 **Internal State** 设置为 `Quaternion (allows zero bend angle)`。

`Quaternion (allows zero bend angle)`
:   Constant Velocity Joint 模块使用四元数参数化。为强制 CV 运动学约束，四元数的第四个分量，即向量部分的 *Z* 分量，始终为零。

    当需要零弯曲角时，请使用此方法。此方法在零弯曲角处没有运动学奇异性，但在弯曲角为 180 度时具有运动学奇异性。使用此参数化的仿真通常比使用 *Z-Y-Z* 参数化的仿真慢。

### **State Targets > Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以启用用于指定关节位置目标的参数。

### **State Targets > Specify Position Target > Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

设置位置目标的优先级。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value** — 用于指定位置目标的角度 `Bend Angle Only`（默认）| `Bend Angle and Azimuth`

是否在仿真开始时仅使用弯曲角，或使用弯曲角和方位角来指定 CV 关节的位置目标。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value > Bend Angle** — 要指定的弯曲角 45 `deg`（默认）

指定 CV 关节的弯曲角。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value > Azimuth** — 要指定的方位角 0 `deg`（默认）

指定 CV 关节的方位角。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** > **Specify Position Target** > **Value** 下，选择 **Bend Angle and Azimuth**。

### **State Targets > Specify Velocity Target** — 是否指定速度目标 `off`（默认）| `on`

选择此参数以启用用于指定关节速度目标的参数。

### **State Targets > Specify Velocity Target > Priority** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

设置速度目标的优先级。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **State Targets > Specify Velocity Target > Value** — 用于指定速度目标的参数 `Bend Angle Only`（默认）| `Bend Angle and Azimuth`

是否在仿真开始时仅使用弯曲角，或使用弯曲角和方位角来指定 CV 关节的速度目标。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **State Targets > Specify Velocity Target > Value > Bend Angle** — 要指定的弯曲角速度 0 `deg/s`（默认）

指定 CV 关节的弯曲角速度。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **State Targets > Specify Velocity Target > Value > Azimuth** — 要指定的方位角速度 0 `deg/s`（默认）

指定 CV 关节的方位角速度。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** > **Specify Velocity Target** > **Value** 下，选择 **Bend Angle and Azimuth**。

### **Sensing > Bend Angle > Position** — 是否感测弯曲角 off（默认）| on

选择此参数以启用端口 **qb**。

### **Sensing > Bend Angle > Velocity** — 是否感测弯曲角速度 off（默认）| on

选择此参数以启用端口 **wb**。

### **Sensing > Bend Angle > Acceleration** — 是否感测弯曲角加速度 off（默认）| on

选择此参数以启用端口 **bb**。

### **Sensing > Azimuth > Position** — 是否感测方位角 off（默认）| on

选择此参数以启用端口 **qa**。

### **Sensing > Azimuth > Velocity** — 是否感测方位角速度 off（默认）| on

选择此参数以启用端口 **wa**。

### **Sensing > Azimuth > Acceleration** — 是否感测方位角加速度 off（默认）| on

选择此参数以启用端口 **ba**。

### Mode Configuration

### **Mode** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | Locked 模式约束关节的所有自由度 (DOF)。在仿真期间，锁定关节保持其初始装配位置且速度为零。根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置，关节模块可以感测力或力矩。 |
| `Normal` | Normal 模式启用 DOF，并且关节的约束在仿真期间按预期工作。 |
| `Disengaged` | Disengaged 模式在整个仿真过程中释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不会影响 disengaged 关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **输入** 部分中的端口 **mode**。 |

### Composite Force/Torque Sensing

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 下的输出信号。反转方向会改变测量的符号。有关详细信息，请参阅力和力矩测量方向。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2015a 中引入**

### R2025a: 模型模式故障

您现在可以为所有关节模块建模模式故障。使用这些故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

强制两个轴之间等速运动学约束的关节

Constant Velocity Joint 模块在其基座坐标系和从动坐标系之间施加等速 (CV) 运动学约束，这两个坐标系的原点在整个仿真过程中重合。具体而言，如果基座坐标系和从动坐标系的 *Z* 轴均相对于一个公共参考坐标系固定，则这两个坐标系相对于该公共参考坐标系的角速度的 *Z* 分量相等。

该模块具有两个自由度，允许基座坐标系和从动坐标系的 *Z* 轴彼此任意定向。图中显示了一个示例。

方位角弯曲角

黑色和红色坐标系表示该模块的基座坐标系和从动坐标系。绕基座坐标系 *Z* 轴的方位角旋转确定弯曲角所在的平面。绕所得 *Y* 轴（红色 *Y* 轴）的弯曲角指定从动坐标系 *Z* 轴相对于基座坐标系 *Z* 轴的定向。

该模块有两种参数化方式：`Rotation Sequence (faster simulation)` 或 `Quaternion (allows zero bend angle)`，用于指定关节的内部状态。只要有可能，就使用旋转序列参数化，因为使用这种参数化的仿真通常比使用四元数参数化的仿真更快。有关更多信息，请参阅 Internal State。

您可以使用 **State Targets** 下的参数指定关节所需的初始状态，例如方位角和弯曲角的位置和速度。

该模块具有多种传感能力。您可以在整个仿真过程中感测方位角、弯曲角及其时间导数。此外，您还可以感测作用在关节中的力和扭矩，例如约束力和总扭矩。有关更多信息，请参阅 Composite Force/Torque Sensing 一节。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则关节变为 disengaged。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon 按钮以添加故障。您可以为关节模块添加多个故障，但关节模块在仿真期间只能有一个活动故障。

添加故障时，请在 Property Inspector 中的 **Fault** 部分下指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真处于开启状态。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
