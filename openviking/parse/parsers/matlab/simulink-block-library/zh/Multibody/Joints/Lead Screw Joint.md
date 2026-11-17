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
```yaml
ports:
- name: B
  summary: 基础坐标系 坐标系
  direction: input
- name: F
  summary: 从动坐标系 坐标系
  direction: input
- name: mode
  summary: 关节模式控制 物理信号
  direction: input
- name: q
  summary: 关节旋转 物理信号
  direction: output
- name: w
  summary: 关节旋转的一阶导数 物理信号
  direction: output
- name: b
  summary: 关节旋转的二阶导数 物理信号
  direction: output
- name: p
  summary: 关节平移 物理信号
  direction: output
- name: v
  summary: 关节平移的一阶导数 物理信号
  direction: output
- name: a
  summary: 关节平移物理信号的二阶导数
  direction: output
- name: fc
  summary: 约束力物理信号
  direction: output
- name: tc
  summary: 约束力矩物理信号
  direction: output
- name: ft
  summary: 总力物理信号
  direction: output
- name: tt
  summary: 总力矩物理信号
  direction: output
```

### 坐标系

### **B** — 基础坐标系 坐标系

关节模块的基础坐标系。

### **F** — 从动坐标系 坐标系

关节模块的从动坐标系。
### 输入

#### 模式配置

### **mode** — 关节模式控制 物理信号

控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离；当输入信号为 `1` 时，关节模式为锁定。您可以在仿真过程中的任意时刻更改模式。

下表显示了在模式之间切换时关节位置和速度的变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到锁定 | 关节位置保持当前值，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |
| 正常到分离 | 关节位置保持当前值，但在切换后可沿任意方向变化。 | 关节速度保持当前值，但在切换后可沿任意方向变化。 |
| 锁定到正常 | 关节位置保持当前值，但在切换后可沿与关节自由度（DOF）对齐的方向变化。 | 关节速度保持为零，但在切换后可沿与关节自由度对齐的方向变化。 |
| 锁定到分离 | 关节位置保持当前值，但在切换后可沿任意方向变化。 | 关节速度保持为零，但在切换后可沿任意方向变化。 |
| 分离到正常 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节位置变为零，并在切换后保持不变。 | 对于与关节自由度对齐的方向，关节速度初始采用通过牛顿法计算的值，此后可以变化。在约束方向上，关节速度变为零，并在切换后保持不变。 |
| 分离到锁定 | 对于与关节自由度对齐的方向，关节位置初始采用通过牛顿法计算的值，并在切换后保持不变。在约束方向上，关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在 **模式配置** 下，将 **模式** 设置为 `Provided by Input`。
### 输出

#### 旋转

### **q** — 关节旋转 物理信号

物理信号端口，输出从动坐标系相对于基础坐标系的旋转角度。

#### 依赖关系

要启用此端口，请在 **传感** > **旋转** 下，选择 **位置**。

### **w** — 关节旋转的一阶导数 物理信号

物理信号端口，输出关节旋转的一阶导数。

#### 依赖关系

要启用此端口，请在 **传感** > **旋转** 下，选择 **速度**。

### **b** — 关节旋转的二阶导数 物理信号

物理信号端口，输出关节旋转的二阶导数。

#### 依赖关系

要启用此端口，请在 **传感** > **旋转** 下，选择 **加速度**。

#### 平移

### **p** — 关节平移 物理信号

物理信号端口，输出从动坐标系相对于基础坐标系的关节平移。

#### 依赖关系

要启用此端口，请在 **传感** > **平移** 下，选择 **位置**。

### **v** — 关节平移的一阶导数 物理信号

物理信号端口，输出关节平移的一阶导数。

#### 依赖关系

要启用此端口，请在 **传感** > **平移** 下，选择 **速度**。

### **a** — 关节平移物理信号的二阶导数

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
```yaml
parameters:
- name: Direction
  summary: 丝杠关节的旋向 Right-Hand（默认）| Left-Hand
  group: Z Lead Screw Primitive (LSz)
- name: Lead
  summary: 丝杠关节的导程 1 mm/rev（默认）| 标量
  group: Z Lead Screw Primitive (LSz)
- name: Specify Position Target
  summary: 是否指定位置目标 off（默认）| on
  group: Z Lead Screw Primitive (LSz)
- name: Priority
  summary: 位置目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Lead Screw Primitive (LSz)
- name: Based On
  summary: 用于指定位置目标的运动类型 Translation（默认）| Rotation
  group: Z Lead Screw Primitive (LSz)
- name: Value
  summary: 旋转位置目标 0 deg（默认）| 具有角度单位的标量
  group: Z Lead Screw Primitive (LSz)
- name: Value
  summary: 平移位置目标 0 m（默认）| 具有长度单位的标量
  group: Z Lead Screw Primitive (LSz)
- name: 指定速度目标
  summary: 是否指定速度目标 off（默认）| on
  group: Z Lead Screw Primitive (LSz)
- name: 优先级
  summary: 速度目标的优先级 High (desired)（默认）| Low (approximate)
  group: Z Lead Screw Primitive (LSz)
- name: 基于
  summary: 用于指定速度目标的运动类型 Translation（默认）| Rotation
  group: Z Lead Screw Primitive (LSz)
- name: 值
  summary: 角速度目标 0 deg/s（默认）| 具有角速度单位的标量
  group: Z Lead Screw Primitive (LSz)
- name: 值
  summary: 线速度目标 0 m/s（默认）| 具有线速度单位的标量
  group: Z Lead Screw Primitive (LSz)
- name: 模式
  summary: 关节模式 Normal（默认）| Locked | Disengaged | Provided by Input
  group: 模式配置
- name: 方向
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: 复合力/力矩感测
- name: 解析坐标系
  summary: 用于解析测量值的坐标系 Base（默认）| Follower
  group: 复合力/力矩感测
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### Z Lead Screw Primitive (LSz)

### **Direction** — 丝杠关节的旋向 `Right-Hand`（默认）| `Left-Hand`

丝杠关节的旋向，指定为 `Right-Hand` 或 `Left-Hand`。右旋关节将正旋转转换为正线性运动，而左旋关节将正旋转转换为负线性运动。

### **Lead** — 丝杠关节的导程 1 `mm/rev`（默认）| 标量

丝杠关节的导程，指定为具有长度/角度单位的标量。导程是指跟随坐标系在基坐标系 *z* 轴方向上随跟随坐标系完整旋转一圈所移动的距离。

#### 状态目标

### **Specify Position Target** — 是否指定位置目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元位置目标的参数。

### **Priority** — 位置目标的优先级 `High (desired)`（默认）| `Low (approximate)`

位置目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Position Target**。

### **Based On** — 用于指定位置目标的运动类型 `Translation`（默认）| `Rotation`

用于指定位置目标的运动类型，指定为 `Translation` 或 `Rotation`。

#### 依赖关系

要启用此参数，请在 **State Targets** 下，选择 **Specify Position Target**。

### **Value** — 旋转位置目标 0 `deg`（默认）| 具有角度单位的标量

旋转位置目标，指定为具有角度单位的标量。

#### 依赖关系

要启用此参数，请在 **State Targets** > **Specify Position Target** > **Based On** 下，选择 **Rotation**。

### **Value** — 平移位置目标 0 `m`（默认）| 具有长度单位的标量

平移位置目标，指定为具有长度单位的标量。

#### 依赖关系

要启用此参数，请在 **状态目标** > **指定位置目标** > **基于** 下，选择 **平移**。

### **指定速度目标** — 是否指定速度目标 `off`（默认）| `on`

选择此参数以启用用于指定关节基元速度目标的参数。

### **优先级** — 速度目标的优先级 `High (desired)`（默认）| `Low (approximate)`

速度目标的优先级，指定为 `High (desired)` 或 `Low (approximate)`。

#### 依赖关系

要启用此参数，请在 **状态目标** 下，选择 **指定速度目标**。

### **基于** — 用于指定速度目标的运动类型 `Translation`（默认）| `Rotation`

用于指定速度目标的运动类型，指定为 `Translation` 或 `Rotation`。

#### 依赖关系

要启用此参数，请在 **状态目标** 下，选择 **指定速度目标**。

### **值** — 角速度目标 0 `deg/s`（默认）| 具有角速度单位的标量

关节基元的角速度目标，指定为具有角速度单位的标量。

#### 依赖关系

要启用此参数，请在 **状态目标** > **指定位置目标** > **基于** 下，选择 **旋转**。

### **值** — 线速度目标 0 `m/s`（默认）| 具有线速度单位的标量

关节基元的线速度目标，指定为具有线速度单位的标量。

#### 依赖关系

要启用此参数，请在 **状态目标** > **指定位置目标** > **基于** 下，选择 **平移**。

### 模式配置

### **模式** — 关节模式 `Normal`（默认）| `Locked` | `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Locked` | 锁定模式约束关节的所有自由度（DOF）。锁定的关节在仿真期间保持其初始装配位置且速度为零。关节模块可以根据 **内部力学**、**限制** 和 **驱动** 参数的设置来感测力或力矩。 |
| `Normal` | 正常模式启用关节的自由度，关节的约束在仿真期间按预期工作。 |
| `Disengaged` | 脱离模式在整个仿真过程中释放关节的所有约束。**内部力学**、**限制** 和 **驱动** 参数的设置不影响脱离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参见 **输入** 部分中的端口 **mode**。 |

### 复合力/力矩感测

### **方向** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **复合力/力矩感测** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参见力和力矩测量方向。

### **解析坐标系** — 用于解析测量值的坐标系 `Base`（默认）| `Follower`

用于解析测量值的坐标系，指定为以下值之一：

- `Base` — 模块在基础坐标系的坐标中解析测量值。
- `Follower` — 模块在从动坐标系的坐标中解析测量值。

此参数仅影响 **复合力/力矩感测** 部分下的输出信号。
## 所属库

Simscape / Multibody / Joints

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2025a: 模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的**故障**部分。

## 描述

具有耦合旋转和平移自由度的关节

Lead Screw Joint 模块表示一个具有一个自由度的关节，并建模一对耦合的旋转和平移，如图所示。

丝杠关节基元的示意图

在仿真期间，该关节约束基座坐标系和从动坐标系的 *z* 轴对齐。从动坐标系原点可以沿基座 *z* 轴平移，而从动 *x* 轴和 *y* 轴绕基座坐标系 *z* 轴旋转。平移与旋转成比例，比例取决于 **Lead** 和 **Direction** 参数的值。

要指定关节初始状态的目标，请使用 **State Targets** 下的参数。您可以基于关节坐标系之间的相对旋转或平移来指定目标。要指定关节模式配置，请使用 **Mode** 参数。有关更多详细信息，请参阅**端口**和**参数**部分下的**模式配置**。

该关节模块具有输出传感数据的端口，例如位置、速度、加速度、力和扭矩，您可以使用这些数据对模型执行分析任务。

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果一个关节的 **Mode** 参数设置为 `Locked`，并且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击用于添加故障的 Add a fault on the block icon 按钮。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。该关节支持 `Locked`、`Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要设置模块的活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
