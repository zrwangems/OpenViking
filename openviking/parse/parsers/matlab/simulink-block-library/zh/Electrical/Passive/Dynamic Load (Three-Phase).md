---
type: simulink-block
title: 'Dynamic Load (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'dynamicloadthreephase'
documentation_source_path: 'ref/dynamicloadthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Dynamic Load (Three-Phase)

## 端口

### 输入

### **P** — 有功功率，W，物理信号

与有功功率关联的物理信号端口，指定为标量。

### **Q** — 无功功率，V\*A，物理信号

与无功功率关联的物理信号端口，指定为标量。
### 守恒

### **~** — 三相电压，电气

与三相电压关联的复合三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — A 相电压，电气

与 A 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — B 相电压，电气

与 B 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — C 相电压，电气

与 C 相电压关联的扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

## 参数

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择对复合三相端口还是扩展三相端口进行建模。

当选择 `Composite three-phase ports` 时，**~** 守恒端口表示复合三相端口。

当选择 `Expanded three-phase ports` 时，**a**、**b** 和 **c** 守恒端口表示三相系统的各独立相。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

*自 R2023a 起*

额定电气频率。

### **Minimum supply voltage (phase-to-phase RMS)** — 最小电源电压 `100` `V`（默认）| 标量

电源为使模块作为动态负载运行所需的最小电压，以相间 RMS 表示。

### **Voltage time constant** — 电压动态时间常数 `0.01` `s`（默认）| 正标量

*自 R2023a 起*

与端子电压测量瞬态关联的时间常数。

### **Initial supply voltage (phase-to-phase RMS)** — 初始端子电压 `200` `V`（默认）| 正标量

*自 R2023a 起*

时间为零时的端子电压，以相间 RMS 表示。

### **Initial supply voltage angle** — 时间为零时 A 相端子电压角度 `0` `deg`（默认）| 标量

*自 R2023a 起*

时间为零时 A 相端子电压角度。

### **Parasitic conductance to electrical reference** — 对电气参考的寄生电导 `0` `S`（默认）| 非负标量

*自 R2023a 起*

对电气参考的寄生电导。

### 故障

### **Open circuit fault** — 添加开路故障的选项 `Add fault`（默认）

用于在 Dynamic Load (Three-Phase) 模块中添加开路故障的选项。

要添加故障，请单击 **Add fault** 超链接。

### **Open-circuit conductance** — 开路电导 `1e-4` `S`（默认）| 标量

开路状态期间的电导。

#### 依赖关系

要启用此参数，请通过单击 **Open circuit fault** 参数中的 **Add fault** 超链接，向 Dynamic Load (Three-Phase) 模块添加故障。

创建故障后，您可以在 **Fault Inspector** 窗口中更改属性。当您打开包含故障的模块时，将显示 **Open Fault Inspector** 超链接，而不是 **Add fault** 超链接。有关展示如何包含故障的示例，请参阅 Analyze a DC Armature Winding Fault。

### **Trigger fault at time** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **Trigger Type** 设置为 `Timed`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2023a：改进了对感性节点的支持

在 R2023a 之前，要将 Dynamic Load (Three-Phase) 模块连接到感性节点，必须提供较大的寄生电阻。从 R2023a 开始，您可以通过指定 **Rated electrical frequency**、**Voltage time constant**、**Initial supply voltage (phase-to-phase RMS)**、**Initial supply voltage angle** 和 **Parasitic conductance to the electrical reference** 参数，将此模块连接到感性节点。由于此更改，**Minimum active power** 参数已被移除。如果您的模型保存在较早版本中并包含此模块，则必须为新参数设置适当的值。

此外，该模块的 **Modeling option** 参数已重命名为 **Electrical connection**，并移至 **Main** 部分。

### R2020b：库路径更改

Dynamic Load (Three-Phase) 模块已从 **Simscape** > **Electrical** > **Passive** > **RLC Assemblies** 库移至 **Simscape** > **Electrical** > **Passive** 库。

如果您的脚本依赖于该模块的库路径或 Simscape 组件路径，请更新脚本以反映这些更改。

## 描述

平衡三相动态负载

Dynamic Load (Three-Phase) 模块为平衡三相电源建模平衡动态负载。

下表显示了该模块如何根据来自电源的电压 *V* 计算消耗的有功功率和无功功率。

| *V* 值范围 | 消耗的有功功率和无功功率 |
| --- | --- |
| V>Vmin | Pactual=PinQactual=Qin |
| V<Vmin | 该模块对阻抗等于以下值的负载进行建模：  R=Vmin2PinPin2+Qin2X=Vmin2QinPin2+Qin2Z=R2+X2 |

在这些方程中：

- *Vmin* 是 Minimum supply voltage (phase-to-phase RMS) 参数的值。
- *Pactual* 是 Dynamic Load (Three-Phase) 模块消耗的有功功率。
- *Pin* 是 Dynamic Load (Three-Phase) 模块的输入有功功率，由外部输入端口 **P** 确定。
- *Qactual* 是 Dynamic Load (Three-Phase) 模块消耗的无功功率。
- *Qin* 是 Dynamic Load (Three-Phase) 模块的输入无功功率，由外部输入端口 **Q** 确定。

Dynamic Load (Three-Phase) 模块根据输入有功功率 *Pin* 的极性消耗或生成有功功率。如果 *Pin* > 0，则该模块消耗有功功率。如果 *Pin* < 0，则该模块生成有功功率。

### 故障

要对 Dynamic Load (Three-Phase) 模块中的故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Dynamic Load (Three-Phase) 模块允许您将电气故障建模为开路。该模块可以在特定时间触发故障事件。

### 潮流分析

如果该模块所在的网络与频率-时间仿真模式兼容，则可以对该网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical 和 Frequency and Time Simulation Mode。
