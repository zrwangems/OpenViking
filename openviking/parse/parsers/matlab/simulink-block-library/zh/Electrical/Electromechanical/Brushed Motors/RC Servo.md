---
type: simulink-block
title: 'RC Servo'
family: 'electromechanical'
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

### 守恒

### **s** — 轴控制电气

与 PWM 控制信号相关的电气守恒端口。输出轴角度需求由施加到该端口的电压脉冲宽度设定。

### **+** — 正极端子电气

与电机正极端子相关的电气守恒端口。

### **-** — 负极端子电气

与电机负极端子相关的电气守恒端口。

### **R** — 转子机械旋转

与转子相关的机械旋转守恒端口。

### **C** — 壳体机械旋转

与定子（壳体）相关的机械旋转守恒端口。

## 参数

### 电气转矩

### **Stall torque** — 最大负载转矩 `2.4` `kg*cm`（默认）

RC 伺服在不失速（停止）的情况下可以移动的最大负载转矩。

### **Time to travel 60 degrees (no load)** — 输出轴 60 度转动时间 `0.28` `s`（默认）

电机空载驱动时，输出轴转动 60 度所需的时间。

### **Corresponding nominal voltage** — 直流电源电压 `4.8` `V`（默认）

测量失速转矩和转动 60 度时间时使用的直流电源电压。

### **Rotational range** — 输出轴角度范围 `[0 180]` `deg`（默认）

RC 伺服的输出轴角度范围。

### **Corresponding pulse widths** — 输入脉冲宽度范围 `[550 2330]` `us`（默认）

对应于最小和最大输出角度的输入脉冲宽度，由 **Rotational range** 参数定义。超出此范围的脉冲宽度将被该模块裁剪，以保持在此范围内。

### 控制

### **Pulse threshold** — 脉冲控制阈值电压 `3` `V`（默认）

脉冲控制的阈值电压。当 s 和 - 端口之间的电压高于此电平时，输入脉冲被检测为高电平。

### **Signal input resistance** — 阻抗 `18` `kOhm`（默认）

在 s 和 - 端口之间测得的电阻抗。

### **Angle resolution** — 要求输出轴角度与测得输出轴角度之间允许的最小误差 `0.1` `deg`（默认）

要求输出轴角度与测得输出轴角度之间允许的最小误差。当要求输出轴角度与测得输出轴角度之间的误差降到角度分辨率以下时，电机断电。此参数对 RC 伺服控制器中通常包含的滞回进行建模，以防止在设定点附近抖动。

### **Angle measurement error** — 角度测量中的模型误差 `0` `deg`（默认）

角度测量中的模型误差。此参数允许您对角度测量误差进行建模，例如可能由故障电位器角度传感器引起的误差。例如，如果要对电机被驱动到其中一个硬限位的情况建模，可以设置适当的角度测量误差来实现。

### 机械

### **Backdrive torque (unpowered)** — 反向驱动未通电电机所需的负载转矩 `0.5` `kg*cm`（默认）

反向驱动未通电电机所需的负载转矩。该模块使用此值来确定齿轮摩擦参数。

### **Gear reduction ratio** — 从电机轴到 RC 伺服输出轴的近似减速比 `320`（默认）

从直流电机轴到 RC 伺服输出轴的减速比。此参数仅影响转子惯量对输出轴等效惯量值的影响。它不影响空载速度。因此，该值不必精确。

### **Rotor inertia** — 直流电机和转子齿轮传动的惯量 `10` `g*cm^2`（默认）

直流电机的惯量，加上折算到转子的齿轮传动惯量（如果齿轮为塑料齿轮，通常很小）。

### **End-stop angles** — 机械角度范围 `[-5 185]` `deg`（默认）

机械端挡可防止输出轴旋转超出指定范围。端挡角度指定的范围必须大于 **Rotational range** 参数指定的范围。

### **End-stop stiffness** — 机械端挡的刚度 `1e6` `N*m/rad`（默认）

机械端挡的刚度。

### **End-stop damping** — 机械端挡的阻尼 `0.01` `N*m/(rad/s)`（默认）

机械端挡的阻尼。

### 故障

### **Servo fault** — 向 RC 伺服添加故障的选项 `Add fault`（默认）

向 RC 伺服添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Failure mode** — 选择故障类型 `Fail off`（默认） | `Fail forward` | `Fail reverse` | `Failed winding`

要建模的故障类型：

- `Fail off` — 无电气转矩。
- `Fail forward` — 沿正方向旋转以撞到上端挡。
- `Fail reverse` — 沿负方向旋转以撞到下端挡。
- `Failed winding` — 仅当电机转子与剩余两个正常工作的绕组之一对齐时才施加转矩。

#### 依赖关系

要启用此参数，请点击 **Servo fault** 参数中的 **Add fault** 超链接，向 RC Servo 模块添加故障。

创建故障后，可以在 **Fault Inspector** 窗口中更改属性。当您打开存在故障的模块时，会显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认） | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

### **Maximum permissible current** — 故障转换的电流阈值 `1` `A`（默认） | 正标量

故障转换的电流阈值。如果电流超过此值的时间长于 **Time to fail when exceeding maximum permissible current** 参数值，则模块进入故障状态。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

### **Time to fail when exceeding maximum permissible current** — 电流超过阈值的最大持续时间 `1` `s`（默认） | 非负标量

电流可以超过最大允许值而不触发故障的最长时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Behavioral`。

## 所属库

Simscape / Electrical / Electromechanical / Brushed Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2023a：使用单个参数为故障实现时间触发或行为触发

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已被移除，并由 **Fault trigger** 参数替代。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。只能启用一个触发器。

如果您在较早版本中创建了模型并同时启用了时间触发和行为触发，现在只会启用时间触发。因此，如果行为触发在您的模型中导致故障，仿真结果会有所不同。

如果要在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果要确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

具有基于 PWM 的角位置跟踪和故障建模功能的无线电控制伺服电机

RC Servo 模块表示带有齿轮箱和控制电路的小型直流电机，常用于四轴飞行器、无线电遥控飞机和直升机以及其他机电设备。RC 伺服在有限角度范围内提供输出轴的角位置控制。角度需求由施加到端口 s 的 PWM 信号脉冲宽度设定。

RC Servo 模块对以下效应建模：

- 基于直流电机方程的转矩-速度行为
- 基于输入 PWM 信号脉冲宽度的位置跟踪
- 内部齿轮减速比，包括相关摩擦损耗
- 机械端挡，用于防止负载将输出轴驱动到范围之外
- 位置测量误差
- 故障建模

电机方程与 DC Motor 模块使用的方程相同，但不建模电感。RC Servo 模块使用失速转矩和空载速度确定方程参数，并进行校正以考虑反向驱动转矩。

### 故障

要在 RC Servo 模块中对故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

RC Servo 模块允许您对多种类型的故障建模：

- Fail off — 无电气转矩。
- Fail forward — 沿正方向旋转以撞到上端挡。
- Fail reverse — 沿负方向旋转以撞到下端挡。
- Failed winding — 仅当电机转子与剩余两个正常工作的绕组之一对齐时才施加转矩。

该模块可以触发故障事件：

- 在特定时间。
- 当电流限值被超过的时间长于特定时间间隔时。

如果要在特定时间触发故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Timed`。如果要确定系统是否发生故障以及何时发生故障，请在 **Fault Inspector** 窗口中，将 **Trigger type** 设置为 `Behavioral`。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 假设和限制

- 此模块没有可选的热端口。
- 如果使用固定步长求解器（例如使用局部求解器）仿真模型，则步长必须足够小，以获得所需的输入脉冲宽度分辨率。为了快速进行桌面仿真，请将此模块与可变步长求解器一起使用。
