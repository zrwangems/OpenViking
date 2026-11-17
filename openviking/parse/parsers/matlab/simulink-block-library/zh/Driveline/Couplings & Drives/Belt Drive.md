---
type: simulink-block
title: 'Belt Drive'
family: 'couplings-drives'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'beltdrive'
documentation_source_path: 'ref/beltdrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Belt Drive

## 端口

### 守恒

### **A** — 带轮 A 轴机械旋转

与带轮 A 的轴关联的机械旋转守恒端口。

### **B** — 带轮 B 轴机械旋转

与带轮 B 的轴关联的机械旋转守恒端口。

## 参数

### 皮带

### **Drive type** — 皮带传动配置 `Open belt`（默认）| `Crossed belt`

皮带传动配置。有关更多信息，请参阅 Belt Drive 示意图。

### **Belt type** — 皮带参数化 `Ideal - No slip`（默认）| `Flat belt` | `V-belt`

皮带类型选择。皮带类型影响滑动条件

- `Ideal - No slip` — 参数化理想皮带，该皮带不会相对于带轮滑动。
- `Flat belt` — 参数化具有矩形横截面的皮带。
- `V-belt`— 参数化具有 V 形横截面的皮带。

### **Compliance** — 柔量选项 `No compliance - Suitable for HIL simulation`（默认）| `Specify stiffness and damping`

仿真柔量的选项。

- `No compliance - Suitable for HIL simulation` — 仿真在受力时不会弹性屈服的非柔量皮带。要优先考虑性能，请选择此选项。
- `Specify stiffness and damping` — 仿真在受力时确实会弹性屈服的柔量皮带。要优先考虑保真度，请选择此选项。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `Ideal - No slip`。

### **V-belt sheave angle** — 槽轮角度 `30` `deg`（默认）| nonnegative scalar

V-belt 的槽轮角度。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Number of V-belts** — 皮带数量 `1`（默认）| positive scalar integer

V-belt 的数量。

该模块将非整数值舍入到最接近的整数。增加皮带数量会增加摩擦力、每单位长度的有效质量和最大允许张力。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Centrifugal force** — 离心力选项 `Do not model centrifugal force - Suitable for HIL simulation`（默认）| `Model centrifugal force`

包含离心力影响的选项。如果您将此参数设置为 `Model centrifugal force`，离心力会饱和到每个皮带端上的力的值的大约 90%。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Belt mass per unit length** — 每单位长度质量 `0.6` `kg/m`（默认）| positive scalar

以线密度表示的离心力贡献。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`，并将 **Centrifugal force** 设置为 `Model centrifugal force`。

### **Longitudinal stiffness** — 皮带有效刚度 `1e4` `N/m`（默认）| nonnegative scalar

皮带的有效刚度。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `Ideal - No slip`，并将 **Compliance** 设置为 `Specify stiffness and damping`，或将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Longitudinal damping** — 皮带有效阻尼 `1e3` `N/(m/s)`（默认）| nonnegative scalar

皮带的有效阻尼。

要启用此参数，请设置以下任一项：

- 将 **Belt type** 设置为 `Ideal - No slip`，并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- 将 **Belt type** 设置为 `Flat belt` 或 `V-belt`

### **Pre-tension** — 静止皮带张力 `100` `N`（默认）| positive scalar

皮带和带轮静止时皮带中的张力。该值必须为正。

要启用此参数，请设置以下任一项：

- 将 **Belt type** 设置为 `Ideal - No slip`，并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- 将 **Belt type** 设置为 `Flat belt` 或 `V-belt`

### **Maximum tension** — 张力阈值选项 `No maximum tension`（默认）| `Specify maximum tension`

指定最大张力的选项。如果您将此参数设置为 `Specify maximum tension`，并且皮带任一端的皮带张力达到或超过您为 **Belt maximum tension** 参数指定的值，仿真将停止并生成断言错误。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **Belt type** 设置为 `Ideal - No slip`，并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- 将 **Belt type** 设置为 `Flat belt` 或 `V-belt`

### **Belt maximum tension** — 最大张力阈值 `1e5` `N`（默认）| positive scalar

每条皮带的最大允许张力。当皮带任一端的张力达到或超过此值时，仿真将停止并生成断言错误。

要启用此参数，请设置以下任一项：

- 将 **Belt type** 设置为 `Ideal - No slip`，将 **Compliance** 设置为 `Specify stiffness and damping`，并将 **Maximum tension** 设置为 `Specify maximum tension`，或
- 将 **Belt type** 设置为 `Flat belt` 或 `V-belt`，并将 **Maximum tension** 设置为 `Specify maximum tension`

### Pulley A

### **Pulley radius** — 带轮半径 `.15` `m`（默认）| positive scalar

带轮的半径。

### **Bearing viscous friction coefficient** — 轴承粘性摩擦 `0` `N*m/(rad/s)`（默认）| scalar

与支撑带轮轴的轴承相关的粘性摩擦。

### **Inertia** — 转动惯量 `No inertia`（默认）| `Specify inertia and initial velocity`

使用初始速度参数化转动惯量的选项。

### **Pulley inertia** — 带轮转动惯量 `0.01` `kg*m^2`（默认）| positive scalar

带轮的转动惯量。

#### 依赖项

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley initial velocity** — 带轮初始旋转速度 `0` `rad/s`（默认）| scalar

带轮的初始旋转速度。

#### 依赖项

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### Pulley B

### **Pulley radius** — 带轮半径 `.30` `m`（默认）| positive scalar

带轮的半径。

### **Bearing viscous friction coefficient** — 轴承粘性摩擦 `0.001` `N*m/(rad/s)`（默认）| scalar

与支撑带轮轴的轴承相关的粘性摩擦。

### **Inertia** — 转动惯量 `No inertia`（默认）| `Specify inertia and initial velocity`

使用初始速度参数化转动惯量的选项。

### **Pulley inertia** — 带轮转动惯量 `0.03` `kg*m^2`（默认）| positive scalar

带轮的转动惯量。

#### 依赖项

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley initial velocity** — 带轮初始旋转速度 `0` `rad/s`（默认）| scalar

带轮的初始旋转速度。

#### 依赖项

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### 接触

要启用这些设置，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Friction model** — 摩擦方法选择 `Modal`（默认）| `Continuous`

参数化连续摩擦或模态摩擦的选项。

### **Pulley A initial state** — 带轮 A 的初始状态 `Unlocked`（默认）| `Locked`

使用带轮 A 锁定或解锁来初始化仿真的选项。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Pulley B initial state** — 带轮 B 的初始状态 `Unlocked`（默认）| `Locked`

使用带轮 B 锁定或解锁来初始化仿真的选项。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Static friction coefficient** — 静摩擦系数 `0.5`（默认）| positive scalar

保持静态接触时的皮带摩擦。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.42`（默认）| positive scalar

滑动时的皮带摩擦。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Contact friction coefficient** — 接触摩擦系数 `0.5`（默认）| positive scalar

皮带与带轮表面之间的库仑摩擦系数。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Continuous`。

### **Wrap angle calculation** — 角度计算类型 `Specify pulley center separation`（默认）| `Specify wrap angles`

通过带轮中心距计算包角或直接指定这些值的选项。

- `Specify pulley center separation` — 该模块使用带轮半径、中心距和传动类型计算皮带在带轮上的包角。
- `Specify wrap angles` — 该模块使用您指定的包角。

### **Pulley center separation** — 带轮中心分离距离 `0.5` `m`（默认）| positive scalar

两个带轮中心之间的距离。

#### 依赖项

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify pulley center separation`。

### **Pulley A wrap angle** — 带轮包角 `145` `deg`（默认）| scalar

皮带与连接到端口 **A** 的带轮之间的接触角。

#### 依赖项

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify wrap angles`。

### **Pulley B wrap angle** — 带轮包角 `215` `deg`（默认）| scalar

皮带与连接到端口 **B** 的带轮之间的接触角。

#### 依赖项

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify wrap angles`。

### **Velocity threshold** — 接触阈值 `0.001` `m/s`（默认）| positive scalar

接触中达到峰值动摩擦所需的相对速度。摩擦速度阈值通过确保速度方向改变时力连续，提高仿真的数值稳定性。

### **Force threshold** — 力阈值 `0.01` `N`（默认）| positive scalar

接触中达到峰值动摩擦所需的相对力。

#### 依赖项

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

使用张紧皮带连接两个带轮的动力传输系统

Belt Drive 模块表示一对通过柔性理想、扁平或 V 形皮带连接的带轮。当您将 **Belt type** 设置为 `Ideal - No slip` 时，皮带不会相对于带轮表面滑动。

该模块考虑柔性皮带与带轮周边之间的摩擦。如果摩擦力不足以驱动负载，该模块允许滑动。主动分支与从动分支中的张力关系遵循绞盘方程，也称为 Euler-Eytelwein 方程。该模块考虑柔性皮带中的离心载荷、带轮转动惯量和轴承摩擦。

Belt Drive 模块是一个结构组件，基于 Simscape™ Driveline™ Belt Pulley 模块以及 Simscape Translational Spring 和 Translational Damper 模块。

Translational Spring 和 Translational Damper 模块仿真皮带的柔量。有关支配皮带与带轮之间接触动力学的方程，请参阅 Belt Pulley 模块。该图显示 Belt Drive 模块的功能框图。

要详细了解该模块的构造，请参阅 About Composite Components 以及各组件模块的参考页。

### 方程

这些图显示开式和交叉式皮带传动配置。当您将 **Drive type** 设置为 `Open belt` 时，两个带轮倾向于沿相同方向旋转，并且较大的带轮具有较大的皮带包角。当您将 **Drive type** 设置为 `Crossed belt` 时，带轮倾向于沿相反方向旋转，并具有相同的包角。

**Belt Drive 示意图**

图和方程参考以下量：

- *θA* 是带轮 A 的包角。
- *θB* 是带轮 B 的包角。
- *RA* 是带轮 A 的有效半径。
- *RB* 是带轮 B 的有效半径。
- *C* 是带轮 A 和 B 的中心之间的距离。

**Open Belt**

当您将 **Drive type** 设置为 `Open belt` 时，该模块按如下方式计算皮带绕每个带轮的包角：

θA=π+2∗sin−1RA−RBC,θB=π−2∗sin−1RA−RBC

该图显示包角和参数。

**Crossed Belt**

当您将 **Drive type** 设置为 `Crossed belt` 时，两个包角相等，并且皮带绕每个带轮的包角：

θA=θB=π+2∗sin−1RA+RBC.

该图显示包角和参数。
