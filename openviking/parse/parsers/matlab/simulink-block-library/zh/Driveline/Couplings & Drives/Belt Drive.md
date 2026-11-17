---
type: simulink-block
title: 'Belt Drive'
family: 'sdl'
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
```yaml
ports:
- name: A
  summary: 带轮 A 轴机械旋转
  direction: conserving
- name: B
  summary: 带轮 B 轴机械旋转
  direction: conserving
```

### 守恒端口

### **A** — 带轮 A 轴机械旋转

与带轮 A 轴相关联的机械旋转守恒端口。

### **B** — 带轮 B 轴机械旋转

与带轮 B 轴相关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Drive type
  summary: 皮带传动配置 Open belt（默认）| Crossed belt
  group: 皮带
- name: Belt type
  summary: 皮带参数化 Ideal - No slip（默认）| Flat belt | V-belt
  group: 皮带
- name: Compliance
  summary: 柔量选项 No compliance - Suitable for HIL simulation（默认）| Specify stiffness and damping
  group: 皮带
- name: V-belt sheave angle
  summary: 带轮槽角 30 deg（默认）| 非负标量
  group: 皮带
- name: Number of V-belts
  summary: 皮带数量 1（默认）| 正标量整数
  group: 皮带
- name: Centrifugal force
  summary: 离心力选项 Do not model centrifugal force - Suitable for HIL simulation（默认）| Model centrifugal force
  group: 皮带
- name: Belt mass per unit length
  summary: 单位长度质量 0.6 kg/m（默认）| 正标量
  group: 皮带
- name: Longitudinal stiffness
  summary: 皮带有效刚度 1e4 N/m（默认）| 非负标量
  group: 皮带
- name: Longitudinal damping
  summary: 皮带有效阻尼 1e3 N/(m/s)（默认）| 非负标量
  group: 皮带
- name: Pre-tension
  summary: 静止皮带张力 100 N（默认）| 正标量
  group: 皮带
- name: Maximum tension
  summary: 张力阈值选项 No maximum tension（默认）| Specify maximum tension
  group: 皮带
- name: Belt maximum tension
  summary: 最大张力阈值 1e5 N（默认）| 正标量
  group: 皮带
- name: Pulley radius
  summary: 带轮半径 .15 m（默认）| 正标量
  group: 带轮 A
- name: Bearing viscous friction coefficient
  summary: 轴承粘性摩擦 0 N*m/(rad/s)（默认）| 标量
  group: 带轮 A
- name: Inertia
  summary: 转动惯量 No inertia（默认）| Specify inertia and initial velocity
  group: 带轮 A
- name: Pulley inertia
  summary: 带轮惯量 0.01 kg*m^2（默认）| 正标量
  group: 带轮 A
- name: Pulley initial velocity
  summary: 带轮初始旋转速度 0 rad/s（默认）| 标量
  group: 带轮 A
- name: Pulley radius
  summary: 带轮半径 .30 m（默认）| 正标量
  group: 带轮 B
- name: Bearing viscous friction coefficient
  summary: 轴承粘性摩擦 0.001 N*m/(rad/s)（默认）| 标量
  group: 带轮 B
- name: Inertia
  summary: 转动惯量 No inertia（默认）| Specify inertia and initial velocity
  group: 带轮 B
- name: Pulley inertia
  summary: 带轮惯量 0.03 kg*m^2（默认）| 正标量
  group: 带轮 B
- name: Pulley initial velocity
  summary: 带轮初始旋转速度 0 rad/s（默认）| 标量
  group: 带轮 B
- name: Friction model
  summary: 摩擦方法选择 Modal（默认）| Continuous
  group: 接触
- name: Pulley A initial state
  summary: 带轮 A 初始状态 Unlocked（默认）| Locked
  group: 接触
- name: Pulley B initial state
  summary: 带轮 B 初始状态 Unlocked（默认）| Locked
  group: 接触
- name: Static friction coefficient
  summary: 静摩擦系数 0.5（默认）| 正标量
  group: 接触
- name: Kinetic friction coefficient
  summary: 动摩擦系数 0.42（默认）| 正标量
  group: 接触
- name: Contact friction coefficient
  summary: 接触摩擦系数 0.5（默认）| 正标量
  group: 接触
- name: Wrap angle calculation
  summary: 角度计算类型 Specify pulley center separation（默认）| Specify wrap angles
  group: 接触
- name: Pulley center separation
  summary: 带轮中心距 0.5 m（默认）| 正标量
  group: 接触
- name: Pulley A wrap angle
  summary: 带轮包角 145 deg（默认）| 标量
  group: 接触
- name: Pulley B wrap angle
  summary: 带轮包角 215 deg（默认）| 标量
  group: 接触
- name: Velocity threshold
  summary: 接触阈值 0.001 m/s（默认）| 正标量
  group: 接触
- name: Force threshold
  summary: 力阈值 0.01 N（默认）| 正标量
  group: 接触
```

### 皮带

### **Drive type** — 皮带传动配置 `Open belt`（默认）| `Crossed belt`

皮带传动配置。有关详细信息，请参阅 Belt Drive Diagrams。

### **Belt type** — 皮带参数化 `Ideal - No slip`（默认）| `Flat belt` | `V-belt`

皮带类型选择。皮带类型影响打滑条件

- `Ideal - No slip` — 参数化理想皮带，其相对于带轮不打滑。
- `Flat belt` — 参数化具有矩形横截面的皮带。
- `V-belt`— 参数化具有 V 形横截面的皮带。

### **Compliance** — 柔量选项 `No compliance - Suitable for HIL simulation`（默认）| `Specify stiffness and damping`

用于模拟柔量的选项。

- `No compliance - Suitable for HIL simulation` — 模拟非柔性皮带，其在受到力时不会弹性变形。若要优先考虑性能，请选择此选项。
- `Specify stiffness and damping` — 模拟柔性皮带，其在受到力时会弹性变形。若要优先考虑保真度，请选择此选项。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Ideal - No slip`。

### **V-belt sheave angle** — 带轮槽角 `30` `deg`（默认）| 非负标量

V 形皮带的带轮槽角。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Number of V-belts** — 皮带数量 `1`（默认）| 正标量整数

V 形皮带的数量。

该模块将非整数值舍入到最接近的整数。增加皮带数量会增加摩擦力、单位长度有效质量和最大允许张力。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Centrifugal force** — 离心力选项 `Do not model centrifugal force - Suitable for HIL simulation`（默认）| `Model centrifugal force`

用于包含离心力效应的选项。如果将此参数设置为 `Model centrifugal force`，离心力将饱和至每条皮带端部力值的大约 90%。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Belt mass per unit length** — 单位长度质量 `0.6` `kg/m`（默认）| 正标量

以线密度表示的离心力贡献。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`，并将 **Centrifugal force** 设置为 `Model centrifugal force`。

### **Longitudinal stiffness** — 皮带有效刚度 `1e4` `N/m`（默认）| 非负标量

皮带的有效刚度。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Ideal - No slip` 并将 **Compliance** 设置为 `Specify stiffness and damping`，或将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Longitudinal damping** — 皮带有效阻尼 `1e3` `N/(m/s)`（默认）| 非负标量

皮带的有效阻尼。

要启用此参数，请设置

- **Belt type** 为 `Ideal - No slip` 并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- **Belt type** 为 `Flat belt` 或 `V-belt`

### **Pre-tension** — 静止皮带张力 `100` `N`（默认）| 正标量

皮带和带轮静止时皮带中的张力。该值必须为正。

要启用此参数，请设置

- **Belt type** 为 `Ideal - No slip` 并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- **Belt type** 为 `Flat belt` 或 `V-belt`

### **Maximum tension** — 张力阈值选项 `No maximum tension`（默认）| `Specify maximum tension`

用于指定最大张力的选项。如果将此参数设置为 `Specify maximum tension`，并且皮带任一端上的皮带张力达到或超过为 **Belt maximum tension** 参数指定的值，仿真将停止并生成断言错误。

#### 依赖关系

要启用此参数，请设置

- **Belt type** 为 `Ideal - No slip` 并将 **Compliance** 设置为 `Specify stiffness and damping`，或
- **Belt type** 为 `Flat belt` 或 `V-belt`

### **Belt maximum tension** — 最大张力阈值 `1e5` `N`（默认）| 正标量

每条皮带的最大允许张力。当皮带任一端上的张力达到或超过此值时，仿真将停止并生成断言错误。

要启用此参数，请设置

- **Belt type** 为 `Ideal - No slip`，**Compliance** 为 `Specify stiffness and damping`，并将 **Maximum tension** 设置为 `Specify maximum tension`，或
- **Belt type** 为 `Flat belt` 或 `V-belt`，并将 **Maximum tension** 设置为 `Specify maximum tension`

### 带轮 A

### **Pulley radius** — 带轮半径 `.15` `m`（默认）| 正标量

带轮的半径。

### **Bearing viscous friction coefficient** — 轴承粘性摩擦 `0` `N*m/(rad/s)`（默认）| 标量

与支撑带轮轴的轴承相关联的粘性摩擦。

### **Inertia** — 转动惯量 `No inertia`（默认）| `Specify inertia and initial velocity`

用于通过初始速度参数化转动惯量的选项。

### **Pulley inertia** — 带轮惯量 `0.01` `kg*m^2`（默认）| 正标量

带轮的转动惯量。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley initial velocity** — 带轮初始旋转速度 `0` `rad/s`（默认）| 标量

带轮的初始旋转速度。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### 带轮 B

### **Pulley radius** — 带轮半径 `.30` `m`（默认）| 正标量

带轮的半径。

### **Bearing viscous friction coefficient** — 轴承粘性摩擦 `0.001` `N*m/(rad/s)`（默认）| 标量

与支撑带轮轴的轴承相关联的粘性摩擦。

### **Inertia** — 转动惯量 `No inertia`（默认）| `Specify inertia and initial velocity`

用于通过初始速度参数化转动惯量的选项。

### **Pulley inertia** — 带轮惯量 `0.03` `kg*m^2`（默认）| 正标量

带轮的转动惯量。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley initial velocity** — 带轮初始旋转速度 `0` `rad/s`（默认）| 标量

带轮的初始旋转速度。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### 接触

要启用这些设置，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Friction model** — 摩擦方法选择 `Modal`（默认）| `Continuous`

用于参数化连续摩擦或模态摩擦的选项。

### **Pulley A initial state** — 带轮 A 初始状态 `Unlocked`（默认）| `Locked`

用于以带轮 A 锁定或解锁状态初始化仿真的选项。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Pulley B initial state** — 带轮 B 初始状态 `Unlocked`（默认）| `Locked`

用于以带轮 B 锁定或解锁状态初始化仿真的选项。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Static friction coefficient** — 静摩擦系数 `0.5`（默认）| 正标量

保持静态接触时的皮带摩擦。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.42`（默认）| 正标量

打滑时的皮带摩擦。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Contact friction coefficient** — 接触摩擦系数 `0.5`（默认）| 正标量

皮带与带轮表面之间的库仑摩擦系数。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Continuous`。

### **Wrap angle calculation** — 角度计算类型 `Specify pulley center separation`（默认）| `Specify wrap angles`

用于通过带轮中心距计算包角或直接指定这些值的选项。

- `Specify pulley center separation` — 该模块使用带轮半径、中心距和传动类型计算皮带在带轮上的包角。
- `Specify wrap angles` — 该模块使用您指定的包角。

### **Pulley center separation** — 带轮中心距 `0.5` `m`（默认）| 正标量

带轮中心之间的距离。

#### 依赖关系

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify pulley center separation`。

### **Pulley A wrap angle** — 带轮包角 `145` `deg`（默认）| 标量

连接到端口 **A** 的带轮与皮带之间的接触角。

#### 依赖关系

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify wrap angles`。

### **Pulley B wrap angle** — 带轮包角 `215` `deg`（默认）| 标量

连接到端口 **B** 的带轮与皮带之间的接触角。

#### 依赖关系

要启用此参数，请将 **Wrap angle calculation** 设置为 `Specify wrap angles`。

### **Velocity threshold** — 接触阈值 `0.001` `m/s`（默认）| 正标量

接触中达到峰值动摩擦所需的相对速度。摩擦速度阈值通过确保速度方向改变时力是连续的，从而提高仿真的数值稳定性。

### **Force threshold** — 力阈值 `0.01` `N`（默认）| 正标量

接触中达到峰值动摩擦所需的相对力。

#### 依赖关系

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

连接两个带轮的张紧皮带动力传输系统

Belt Drive 模块表示一对通过柔性理想、扁平或 V 形皮带连接的带轮。当将 **Belt type** 设置为 `Ideal - No slip` 时，皮带相对于带轮表面不打滑。

该模块考虑柔性皮带与带轮周边之间的摩擦。如果摩擦力不足以驱动负载，该模块允许打滑。主动分支和从动分支中的张力之间的关系符合欧拉-埃特尔魏因方程（也称为绞盘方程）。该模块考虑柔性皮带中的离心载荷、带轮惯量和轴承摩擦。

Belt Drive 模块是基于 Simscape™ Driveline™ Belt Pulley 模块以及 Simscape Translational Spring 和 Translational Damper 模块的结构组件。

Translational Spring 和 Translational Damper 模块模拟皮带的柔量。有关支配皮带与带轮之间接触动力学的方程，请参阅 Belt Pulley 模块。该图显示了 Belt Drive 模块的功能框图。

要了解有关该模块构造的更多信息，请参阅 About Composite Components 以及各个组件模块的参考页。

### 方程

这些图显示了开口式和交叉式皮带传动配置。当将 **Drive type** 设置为 `Open belt` 时，两个带轮倾向于沿相同方向旋转，较大的带轮具有较大的皮带包角。当将 **Drive type** 设置为 `Crossed belt` 时，带轮倾向于沿相反方向旋转并具有相同的包角。

**Belt Drive Diagrams**

图和方程涉及以下量：

- *θA* 是带轮 A 的包角。
- *θB* 是带轮 B 的包角。
- *RA* 是带轮 A 的有效半径。
- *RB* 是带轮 B 的有效半径。
- *C* 是带轮 A 和 B 中心之间的距离。

**开口式皮带**

当将 **Drive type** 设置为 `Open belt` 时，该模块计算皮带围绕每个带轮的包角为：

θA=π+2∗sin−1RA−RBC,θB=π−2∗sin−1RA−RBC

该图显示了包角和参数。

**交叉式皮带**

当将 **Drive type** 设置为 `Crossed belt` 时，两个包角相等，皮带围绕每个带轮的包角为：

θA=θB=π+2∗sin−1RA+RBC.

该图显示了包角和参数。
