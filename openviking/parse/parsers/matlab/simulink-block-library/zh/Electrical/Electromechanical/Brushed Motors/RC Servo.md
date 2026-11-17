---
type: simulink-block
title: 'RC Servo'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Brushed Motors'
documentation_page: 'rcservo'
documentation_source_path: 'ref/rcservo.html'
language: zh-CN
chinese_source: worker-translation
---

# RC Servo

## 端口
```yaml
ports:
- name: s
  summary: 轴控制电气端口
  direction: conserving
- name: +
  summary: 正极端子电气端口
  direction: conserving
- name: '-'
  summary: 负极端子电气端口
  direction: conserving
- name: R
  summary: 转子机械旋转端口
  direction: conserving
- name: C
  summary: 壳体机械旋转端口
  direction: conserving
```

### 守恒端口

### **s** — 轴控制电气端口

与 PWM 控制信号关联的电气守恒端口。输出轴角度需求由施加到该端口的电压脉冲宽度设定。

### **+** — 正极端子电气端口

与电机正极端子关联的电气守恒端口。

### **-** — 负极端子电气端口

与电机负极端子关联的电气守恒端口。

### **R** — 转子机械旋转端口

与转子关联的机械旋转守恒端口。

### **C** — 壳体机械旋转端口

与定子（壳体）关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Stall torque
  summary: 最大负载转矩 2.4 kg*cm（默认值）
  group: 电气转矩
- name: Time to travel 60 degrees (no load)
  summary: 输出轴 60 度转动时间 0.28 s（默认值）
  group: 电气转矩
- name: Corresponding nominal voltage
  summary: 直流电源电压 4.8 V（默认值）
  group: 电气转矩
- name: Rotational range
  summary: 输出轴角度范围 [0 180] deg（默认值）
  group: 电气转矩
- name: Corresponding pulse widths
  summary: 输入脉冲宽度范围 [550 2330] us（默认值）
  group: 电气转矩
- name: Pulse threshold
  summary: 脉冲控制的阈值电压 3 V（默认值）
  group: 控制
- name: Signal input resistance
  summary: 阻抗 18 kOhm（默认值）
  group: 控制
- name: Angle resolution
  summary: 需求输出轴角度与测量输出轴角度之间允许的最小误差 0.1 deg（默认值）
  group: 控制
- name: Angle measurement error
  summary: 角度测量中的模型误差 0 deg（默认值）
  group: 控制
- name: Backdrive torque (unpowered)
  summary: 反向驱动未通电电机所需的负载转矩 0.5 kg*cm（默认值）
  group: 机械
- name: Gear reduction ratio
  summary: 从电机轴到 RC 伺服输出轴的近似减速比 320（默认值）
  group: 机械
- name: Rotor inertia
  summary: 直流电机和转子齿轮的惯量 10 g*cm^2（默认值）
  group: 机械
- name: End-stop angles
  summary: 机械角度范围 [-5 185] deg（默认值）
  group: 机械
- name: End-stop stiffness
  summary: 机械限位的刚度 1e6 N*m/rad（默认值）
  group: 机械
- name: End-stop damping
  summary: 机械限位的阻尼 0.01 N*m/(rad/s)（默认值）
  group: 机械
- name: Servo fault
  summary: 向 RC 伺服添加故障的选项 Add fault（默认值）
  group: 故障
- name: Failure mode
  summary: 选择故障类型 Fail off（默认值） | Fail forward | Fail reverse | Failed winding
  group: 故障
- name: Trigger fault at time
  summary: 进入故障状态之前的时间 0 s（默认值） | 非负标量
  group: 故障
- name: Maximum permissible current
  summary: 故障转换的电流阈值 1 A（默认值） | 正标量
  group: 故障
- name: Time to fail when exceeding maximum permissible current
  summary: 电流超过阈值的最大持续时间 1 s（默认值） | 非负标量
  group: 故障
```

### 电气转矩

### **Stall torque** — 最大负载转矩 `2.4` `kg*cm`（默认值）

RC 伺服在不失速（停止）的情况下能够移动的最大负载转矩。

### **Time to travel 60 degrees (no load)** — 输出轴 60 度转动时间 `0.28` `s`（默认值）

电机驱动空载时输出轴转动 60 度所需的时间。

### **Corresponding nominal voltage** — 直流电源电压 `4.8` `V`（默认值）

测量失速转矩和 60 度转动时间时使用的直流电源电压。

### **Rotational range** — 输出轴角度范围 `[0 180]` `deg`（默认值）

RC 伺服的输出轴角度范围。

### **Corresponding pulse widths** — 输入脉冲宽度范围 `[550 2330]` `us`（默认值）

与最小和最大输出角度对应的输入脉冲宽度，由 **Rotational range** 参数定义。超出此范围的脉冲宽度将被模块裁剪以保持在此范围内。

### 控制

### **Pulse threshold** — 脉冲控制的阈值电压 `3` `V`（默认值）

脉冲控制的阈值电压。当 s 和 - 端口之间的电压高于此水平时，输入脉冲被检测为高电平。

### **Signal input resistance** — 阻抗 `18` `kOhm`（默认值）

在 s 和 - 端口之间测得的电阻抗。

### **Angle resolution** — 需求输出轴角度与测量输出轴角度之间允许的最小误差 `0.1` `deg`（默认值）

需求输出轴角度与测量输出轴角度之间允许的最小误差。当需求输出轴角度与测量输出轴角度之间的误差降至角度分辨率以下时，电机断电。此参数模拟通常集成在 RC 伺服控制器中的迟滞，以防止在设定点附近振荡。

### **Angle measurement error** — 角度测量中的模型误差 `0` `deg`（默认值）

角度测量中的模型误差。此参数允许您模拟角度测量误差，例如可能由电位器角度传感器故障引起的情况。例如，如果您想模拟电机被驱动抵靠其中一个硬限位的情况，可以设置适当的角度测量误差来实现。

### 机械

### **Backdrive torque (unpowered)** — 反向驱动未通电电机所需的负载转矩 `0.5` `kg*cm`（默认值）

电机未通电时反向驱动电机所需的负载转矩。模块使用此值来确定齿轮摩擦参数。

### **Gear reduction ratio** — 从电机轴到 RC 伺服输出轴的近似减速比 `320`（默认值）

从直流电机轴到 RC 伺服输出轴的减速比。此参数仅影响转子惯量对输出轴等效惯量值的影响。它对空载速度没有影响。因此，该值不必精确。

### **Rotor inertia** — 直流电机和转子齿轮的惯量 `10` `g*cm^2`（默认值）

直流电机的惯量，加上折算到转子的齿轮惯量（如果齿轮是塑料的，通常很小）。

### **End-stop angles** — 机械角度范围 `[-5 185]` `deg`（默认值）

机械限位防止输出轴旋转超出指定范围。限位角度指定的范围必须大于 **Rotational range** 参数指定的范围。

### **End-stop stiffness** — 机械限位的刚度 `1e6` `N*m/rad`（默认值）

机械限位的刚度。

### **End-stop damping** — 机械限位的阻尼 `0.01` `N*m/(rad/s)`（默认值）

机械限位的阻尼。

### 故障

### **Servo fault** — 向 RC 伺服添加故障的选项 `Add fault`（默认值）

向 RC 伺服添加故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Failure mode** — 选择故障类型 `Fail off`（默认值） | `Fail forward` | `Fail reverse` | `Failed winding`

要建模的故障类型：

- `Fail off` — 无电气转矩。
- `Fail forward` — 沿正方向旋转以撞击上限位。
- `Fail reverse` — 沿负方向旋转以撞击下限位。
- `Failed winding` — 仅当电机转子与剩余两个正常工作绕组之一对齐时才施加转矩。

#### 依赖关系

要启用此参数，请通过单击 **Servo fault** 参数中的 **Add fault** 超链接向 RC Servo 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开具有故障的模块时，**Open Fault Inspector** 超链接会代替 **Add fault** 超链接出现。有关如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态之前的时间 `0` `s`（默认值） | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible current** — 故障转换的电流阈值 `1` `A`（默认值） | 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding maximum permissible current** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding maximum permissible current** — 电流超过阈值的最大持续时间 `1` `s`（默认值） | 非负标量

电流可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。
## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2023a: 使用单个参数实现故障的时间或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。您只能启用一个触发器。

如果您在早期版本中创建了模型并同时启用了时间触发器和行为触发器，现在仅启用时间触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果会有所不同。

如果您想在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果您想确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

具有基于 PWM 的角度位置跟踪和故障建模的无线电控制伺服电机

RC Servo 模块表示一个带有齿轮箱和控制电路的小型直流电机，常用于四旋翼飞行器、无线电控制飞机和直升机以及其他机电设备。RC 伺服在有限的角度范围内提供输出轴的角位置控制。角度需求由施加到端口 s 的 PWM 信号的脉冲宽度设定。

RC Servo 模块对以下效应进行建模：

- 基于直流电机方程的转矩-速度行为
- 基于输入 PWM 信号脉冲宽度的位置跟踪
- 内部齿轮减速比，包括相关的摩擦损耗
- 机械限位，以防止输出轴被负载驱动超出范围
- 位置测量误差
- 故障建模

电机方程与 DC Motor 模块使用的方程相同，但不建模电感。RC Servo 模块使用失速转矩和空载速度来确定方程参数，并进行修正以考虑反向驱动转矩。

### 故障

要在 RC Servo 模块中建模故障，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

RC Servo 模块允许您建模多种类型的故障：

- Fail off — 无电气转矩。
- Fail forward — 沿正方向旋转以撞击上限位。
- Fail reverse — 沿负方向旋转以撞击下限位。
- Failed winding — 仅当电机转子与剩余两个正常工作绕组之一对齐时才施加转矩。

模块可以触发故障事件：

- 在特定时间。
- 当电流限制被超过的时间长于特定时间间隔时。

如果您想在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果您想确定系统是否发生故障以及何时发生故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真的鲁棒性。标称值可以来自不同的来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 假设和限制

- 此模块没有可选的热端口。
- 如果您使用定步长求解器仿真模型，例如使用局部求解器，则步长必须足够小以获得所需的输入脉冲宽度分辨率。对于快速桌面仿真，请将此模块与变步长求解器一起使用。
