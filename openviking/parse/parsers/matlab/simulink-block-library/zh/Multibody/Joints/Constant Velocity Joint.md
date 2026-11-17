---
type: simulink-block
title: 'Constant Velocity Joint'
family: 'sm'
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

### **B** — 基座坐标系 frame

与关节模块的基座坐标系关联的端口。在 CV 关节连接两根轴的典型应用中，基座坐标系的 *Z* 轴与主动轴对齐。

### **F** — 从动坐标系 frame

与关节模块的从动坐标系关联的端口。在 CV 关节连接两根轴的典型应用中，从动坐标系的 *Z* 轴与从动轴对齐。
### 输入

#### 模式配置

### **mode** — 关节模式控制物理信号

控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。您可以在仿真过程中的任意时刻更改模式。

下表显示了关节在模式切换期间位置和速度的变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保持当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| 正常到分离 | 关节位置保持当前值，但切换后可在任意方向上变化。 | 关节速度保持当前值，但切换后可在任意方向上变化。 |
| 锁定到正常 | 关节位置保持当前值，但切换后可在与关节自由度（DOF）对齐的方向上变化。 | 关节速度保持为零，但切换后可在与关节自由度对齐的方向上变化。 |
| 锁定到分离 | 关节位置保持当前值，但切换后可在任意方向上变化。 | 关节速度保持为零，但切换后可在任意方向上变化。 |
| 分离到正常 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节自由度对齐的方向，关节速度初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在切换后保持不变。 |
| 分离到锁定 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，并在切换后保持不变。在约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **Mode Configuration** 下，将 **Mode** 设置为 `Provided by Input`。
### 输出

### **qb** — 弯曲角 标量

CV 关节的弯曲角，以标量形式返回。该量是模块基座坐标系和从动坐标系 *Z* 轴之间的夹角。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Position**。

### **wb** — 弯曲角速度 标量

CV 关节弯曲角的速度，以标量形式返回。该量等于端口 **qb** 输出信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Velocity**。

### **bb** — 弯曲角加速度 标量

CV 关节弯曲角的加速度，以标量形式返回。该量等于端口 **qb** 输出信号的二阶时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Bend Angle** 下，选择 **Acceleration**。

### **qa** — 方位角标量

CV 关节的方位角，以标量形式返回。该量是绕基座坐标系 *Z* 轴旋转的角度。该旋转确定了发生弯曲角的平面。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Position**。

### **wa** — 方位角速度标量

CV 关节方位角的速度，以标量形式返回。该量等于端口 **qa** 输出信号的时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Velocity**。

### **ba** — 方位角加速度标量

CV 关节方位角的加速度，以标量形式返回。该量等于端口 **qa** 输出信号的二阶时间导数。

#### 依赖关系

要启用此端口，请在 **Constant Velocity Primitive (CV)** > **Sensing** > **Azimuth** 下，选择 **Acceleration**。

#### 复合力/力矩传感

### **fc** — 约束力，N 物理信号

物理信号端口，输出作用在关节上的约束力。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿求解坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参见 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Force**。

### **tc** — 约束力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的约束力矩。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示绕求解坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参见 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Constraint Torque**。

### **ft** — 总力，N 物理信号

物理信号端口，输出作用在关节上的总力。总力是通过关节在相连坐标系之间传递的所有力之和。输出为 3×1 向量格式，表示沿求解坐标系 `x`、`y` 和 `z` 轴的力分量。

为演示作用在关节上的总力，该图展示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参见 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Force**。

### **tt** — 总力矩，N\*m 物理信号

物理信号端口，输出作用在关节上的总力矩。总力矩是通过关节在相连坐标系之间传递的所有力矩之和。力矩包括驱动、内力、限位和约束力矩。输出为 3×1 向量格式，表示绕求解坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参见 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在 **Composite Force/Torque Sensing** 下，选择 **Total Torque**。

## 参数

### Constant Velocity Primitive (CV)

### **Internal State** — 关节 `Rotation Sequence (faster simulations)`（默认）| `Quaternion (allows zero bend angle)` 的内部状态参数化

选择用于指定关节内部状态的参数化方式。

`Rotation Sequence (faster simulations)`
:   Constant Velocity Joint 模块使用 *Z-Y-Z* 旋转序列参数化。第二次 *Z* 轴旋转的角度是第一次 *Z* 轴旋转角度的负值。

    尽可能使用此方法，因为使用此参数化的仿真通常比使用四元数参数化的仿真更快。然而，*Z-Y-Z* 旋转序列参数化在弯曲角为零时存在运动学奇异。如果需要零弯曲角，请将 **Internal State** 设置为 `Quaternion (allows zero bend angle)`。

`Quaternion (allows zero bend angle)`
:   Constant Velocity Joint 模块使用四元数参数化。为强制满足 CV 运动学约束，四元数的第四个分量，即向量部分的 *Z* 分量，始终为零。

    当需要零弯曲角时使用此方法。此方法在零弯曲角处没有运动学奇异，但在弯曲角为 180 度时存在运动学奇异。使用此参数化的仿真通常比使用 *Z-Y-Z* 参数化的仿真更慢。

### **State Targets > Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以启用用于指定关节位置目标的参数。

### **State Targets > Specify Position Target > Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

设置位置目标的优先级。有关详细信息，请参阅 Guiding Assembly。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Position Target**。

### **State Targets > Specify Position Target > Value** — 用于指定位置目标的角度 `Bend Angle Only`（默认）| `Bend Angle and Azimuth`

是否在仿真开始时仅使用弯曲角或弯曲角和方位角来指定 CV 关节的位置目标。

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

### **状态目标 > 指定速度目标 > 值** — 用于指定速度目标的参数 `Bend Angle Only`（默认）| `Bend Angle and Azimuth`

是否在仿真开始时仅使用弯曲角度或弯曲角度和方位角来指定 CV 关节的速度目标。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **状态目标 > 指定速度目标 > 值 > 弯曲角度** — 要指定的弯曲角速度 0 `deg/s`（默认）

指定 CV 关节的弯曲角速度。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** 下，选择 **Specify Velocity Target**。

### **状态目标 > 指定速度目标 > 值 > 方位角** — 要指定的方位角速度 0 `deg/s`（默认）

指定 CV 关节的方位角速度。

#### 依赖关系

要启用此参数，请在 **Constant Velocity Primitive (CV)** > **State Targets** > **Specify Velocity Target** > **Value** 下，选择 **Bend Angle and Azimuth**。

### **传感 > 弯曲角度 > 位置** — 是否检测弯曲角度 off（默认）| on

选择此参数以启用端口 **qb**。

### **传感 > 弯曲角度 > 速度** — 是否检测弯曲角度的速度 off（默认）| on

选择此参数以启用端口 **wb**。

### **传感 > 弯曲角度 > 加速度** — 是否检测弯曲角度的加速度 off（默认）| on

选择此参数以启用端口 **bb**。

### **传感 > 方位角 > 位置** — 是否检测方位角 off（默认）| on

选择此参数以启用端口 **qa**。

### **传感 > 方位角 > 速度** — 是否检测方位角的速度 off（默认）| on

选择此参数以启用端口 **wa**。

### **传感 > 方位角 > 加速度** — 是否检测方位角的加速度 off（默认）| on

选择此参数以启用端口 **ba**。

### 模式配置

### **模式** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置来检测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，并且关节的约束按预期在仿真期间工作。 |
| `Disengaged` | 分离模式在整个仿真过程中将关节从所有约束中释放。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不会影响分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### 复合力/力矩传感

### **方向** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块检测从动坐标系施加在基坐标系上的力和力矩。
- `Base on Follower` — 模块检测基坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

- `Base` — 该模块在基座坐标系的坐标中解析测量值。
- `Follower` — 该模块在从动坐标系坐标中解析测量值。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。

## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2025a：模式故障建模

现在您可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

在两个轴之间施加恒定速度运动学约束的关节

Constant Velocity Joint 模块在其基座坐标系和从动坐标系之间施加恒定速度（CV）运动学约束，这两个坐标系的原点在整个仿真过程中重合。具体而言，如果基座坐标系和从动坐标系的 *Z* 轴均相对于一个共同参考坐标系固定，则这两个坐标系相对于该共同参考坐标系的角速度的 *Z* 分量相等。

该模块具有两个自由度，允许基座坐标系和从动坐标系的 *Z* 轴相对于彼此任意取向。图中显示了一个示例。

方位角 弯曲角

黑色和红色坐标系分别表示该模块的基座坐标系和从动坐标系。绕基座坐标系 *Z* 轴的方位角旋转确定了弯曲角所在的平面。绕所得 *Y* 轴（红色 *Y* 轴）的弯曲角指定了从动坐标系 *Z* 轴相对于基座坐标系 *Z* 轴的取向。

该模块有两种参数化方式：`Rotation Sequence (faster simulation)` 或 `Quaternion (allows zero bend angle)`，用于指定关节的内部状态。请尽可能使用旋转序列参数化，因为使用此参数化的仿真通常比使用四元数参数化的仿真更快。有关详细信息，请参阅 Internal State。

您可以使用 **State Targets** 下的参数指定关节的期望初始状态，例如方位角和弯曲角的位置和速度。

该模块具有多种传感能力。您可以在整个仿真过程中感测方位角、弯曲角及其时间导数。此外，您还可以感测作用在关节中的力和力矩，例如约束力和总力矩。有关详细信息，请参阅 Composite Force/Torque Sensing 部分。

### 故障

使用模式故障，您可以在仿真过程中更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡中的 **Faults** 部分，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以用于添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
