---
type: simulink-block
title: 'Weld Joint'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Joints'
documentation_page: 'weldjoint'
documentation_source_path: 'ref/weldjoint.html'
language: zh-CN
chinese_source: worker-translation
---

# Weld Joint

## 端口
```yaml
ports:
- name: B
  summary: 基坐标系 frame
  direction: input
- name: F
  summary: 从坐标系 frame
  direction: input
- name: mode
  summary: 关节模式控制 physical signal
  direction: input
- name: fc
  summary: 约束力，N physical signal
  direction: output
- name: tc
  summary: 约束力矩，N\*m physical signal
  direction: output
- name: ft
  summary: 总力，N physical signal
  direction: output
- name: tt
  summary: 总力矩，N\*m physical signal
  direction: output
```

### 坐标系

### **B** — 基坐标系 frame

关节模块的基坐标系。

### **F** — 从坐标系 frame

关节模块的从坐标系。
### 输入

#### 模式配置

### **mode** — 关节模式控制 physical signal

用于控制关节模式的输入端口。该信号必须为无量纲标量。当输入信号为 `0` 时，关节模式为正常；当输入信号为 `-1` 时，关节模式为分离。您可以在仿真过程中的任意时刻更改模式。

下表显示了关节在模式切换期间位置和速度的变化。

| 切换 | 位置 | 速度 |
| --- | --- | --- |
| 正常到分离 | 关节位置保持为零，但在切换后可沿任意方向变化。 | 关节速度保持为零，但在切换后可沿任意方向变化。 |
| 分离到正常 | 关节位置变为零，并在切换后保持不变。 | 关节速度变为零，并在切换后保持不变。 |

#### 依赖关系

要启用此端口，请在**模式配置**下，将**模式**设置为 `Provided by Input`。
### 输出

#### 复合力/力矩传感

### **fc** — 约束力，N physical signal

输出作用在关节上的约束力的物理信号端口。这些力维持关节的平移约束。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**约束力**。

### **tc** — 约束力矩，N\*m physical signal

输出作用在关节上的约束力矩的物理信号端口。这些力矩维持关节的旋转约束。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**约束力矩**。

### **ft** — 总力，N physical signal

输出作用在关节上的总力的物理信号端口。总力是通过关节在连接坐标系之间传递的所有力之和。输出为 3×1 向量格式，表示沿解算坐标系 `x`、`y` 和 `z` 轴的力分量。

为了演示作用在关节上的总力，该图显示了一个使用 Prismatic Joint 模块的模型。

总力示意图

总力包括执行器力（*F*A）、内力（*F*I）和约束力（*F*C）。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力**。

### **tt** — 总力矩，N\*m physical signal

输出作用在关节上的总力矩的物理信号端口。总力矩是通过关节在连接坐标系之间传递的所有力矩之和。该力矩包括执行、内部、限位和约束力矩。输出为 3×1 向量格式，表示关于解算坐标系 `x`、`y` 和 `z` 轴的力矩分量。有关详细信息，请参阅 Force and Torque Sensing。

#### 依赖关系

要启用此端口，请在**复合力/力矩传感**下，选择**总力矩**。
## 参数
```yaml
parameters:
- name: Mode
  summary: 关节模式 Normal（默认）| Disengaged | Provided by Input
  group: 模式配置
- name: Direction
  summary: 测量方向 Follower on Base（默认）| Base on Follower
  group: Composite Force/Torque Sensing
- name: Resolution Frame
  summary: 用于解析测量的坐标系 Base（默认）| Follower
  group: Composite Force/Torque Sensing
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink Toolstrip 的**仿真**选项卡上，在**准备**库中，选择 **Property Inspector**。

### 模式配置

### **Mode** — 关节模式 `Normal`（默认）| `Disengaged` | `Provided by Input`

用于仿真的关节模式，指定为以下值之一：

| 模式 | 描述 |
| --- | --- |
| `Normal` | 正常模式使关节约束在仿真期间按预期工作。 |
| `Disengaged` | 分离模式在整个仿真期间释放关节的所有约束。**Internal Mechanics**、**Limits** 和 **Actuation** 参数的设置不影响分离的关节。所有输出端口输出零。 |
| `Provided by Input` | `Provided by Input` 选项允许您通过输入信号指定关节模式。有关详细信息，请参阅 **Input** 部分中的端口 **mode**。 |

### Composite Force/Torque Sensing

### **Direction** — 测量方向 `Follower on Base`（默认）| `Base on Follower`

测量方向，指定为以下值之一：

- `Follower on Base` — 模块感测从动坐标系施加在基础坐标系上的力和力矩。
- `Base on Follower` — 模块感测基础坐标系施加在从动坐标系上的力和力矩。

此参数仅影响 **Composite Force/Torque Sensing** 部分下的输出信号。反转方向会改变测量值的符号。有关详细信息，请参阅 Force and Torque Measurement Direction。

### **Resolution Frame** — 用于解析测量的坐标系 `Base`（默认）| `Follower`

用于解析测量的坐标系，指定为以下值之一：

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

**在 R2012a 中引入**

### R2025a：模型模式故障

您现在可以为所有关节模块建模模式故障。使用故障，您可以在仿真期间更改关节模式，而无需更改模型设计。有关详细信息，请参阅描述中的 **Faults** 部分。

## 描述

零原语的关节

此模块表示具有零自由度的关节。它不包含任何关节原语。基础坐标系和从动坐标系各自连接到一个单独的刚体，并且在所有时间都重合。模块对话框提供约束力和总力与力矩的感测选项。

**关节自由度**

### 故障

使用模式故障，您可以在仿真期间更改关节模式，而无需修改模型设计。故障注入会覆盖模式设置。例如，如果某个关节的 **Mode** 参数设置为 `Locked`，且 **Fault behavior** 参数设置为 `Disengaged`，则该关节变为分离状态。

要向关节模块添加模式故障，请点击该关节模块，在 **Simscape Block** 选项卡和 **Faults** 部分中，点击 **Fault** > `Add Fault`。或者，您可以点击该关节模块，将鼠标悬停在省略号上以打开操作栏，然后点击 Add a fault on the block icon Button 以添加故障。您可以向一个关节模块添加多个故障，但该关节模块在仿真期间只能有一个活动故障。

在添加故障时，请在 Property Inspector 中的 **Fault** 部分下，指定故障的行为和触发类型。要定义故障行为，请点击 **Fault Behavior** 旁边的链接。此关节支持 `Normal` 或 `Disengaged` 模式。关节模块支持以下触发类型：`Always on`、`Timed`、`Manual` 和 `Conditional`。有关这些触发类型的更多详细信息，请参阅 Set Fault Triggers。要触发条件故障，您可以使用 Simulink 信号、Simscape 语言模块和 MATLAB 工作区变量。要为模块设置活动故障，请使用 Fault Table。有关更多详细信息，请参阅 Access the Fault Table and Fault Dashboard。

要启用故障仿真，请在 **Simscape Block** 选项卡和 **Faults** 部分中，打开 **Fault Simulation** 按钮。当按钮为绿色且状态为 **on** 时，故障仿真已开启。仿真会记录触发状态数据。要查看数据，请使用 Simulation Data Inspector。此外，您可以在 Fault Dashboard 中查看故障状态和已触发故障的摘要。要打开 Fault Dashboard，请在 **Simscape Block** 选项卡中，点击 **Faults** > `Fault Dashboard`。

要创建和修改故障，您还可以使用 Simscape™ 和 Simulink® 故障函数。有关更多详细信息，请参阅 Simulink Fault Controls 和 Simscape Faults Interface 的函数部分。
