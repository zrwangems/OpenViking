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

### **P** — 有功功率，W 物理信号

与有功功率相关联的物理信号端口，指定为标量。

### **Q** — 无功功率，V\*A 物理信号

与无功功率相关联的物理信号端口，指定为标量。

### 守恒

### **~** — 三相电压 电气

与三相电压相关联的复合三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — A 相电压 电气

与 A 相电压相关联的展开式三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — B 相电压 电气

与 B 相电压相关联的展开式三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — C 相电压 电气

与 C 相电压相关联的展开式三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

### 主

### **电气连接** — 电气连接 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合三相端口或展开式三相端口进行建模。

当您选择 `Composite three-phase ports` 时，**~** 守恒端口表示复合三相端口。

当您选择 `Expanded three-phase ports` 时，**a**、**b** 和 **c** 守恒端口表示三相系统的各相。

### **额定电气频率** — 额定电气频率 `60` `Hz`（默认） | 正标量

*自 R2023a 起*

额定电气频率。

### **最小电源电压（相间 RMS）** — 最小电源电压 `100` `V`（默认） | 标量

电源为使模块作为动态负载运行所需的最小电压（相间 RMS）。

### **电压时间常数** — 电压动态时间常数 `0.01` `s`（默认） | 正标量

*自 R2023a 起*

与端子电压测量的瞬态相关联的时间常数。

### **初始电源电压（相间 RMS）** — 初始端子电压 `200` `V`（默认） | 正标量

*自 R2023a 起*

时间零点的端子电压（相间 RMS）。

### **初始电源电压角度** — 时间零点时 A 相的端子电压角度 `0` `deg`（默认） | 标量

*自 R2023a 起*

时间零点时 A 相的端子电压角度。

### **对电气参考的寄生电导** — 对电气参考的寄生电导 `0` `S`（默认） | 非负标量

*自 R2023a 起*

对电气参考的寄生电导。

### 故障

### **开路故障** — 添加开路故障的选项 `Add fault`（默认）

用于在 Dynamic Load (Three-Phase) 模块中添加开路故障的选项。

要添加故障，请单击 **添加故障** 超链接。

### **开路电导** — 开路电导 `1e-4` `S`（默认） | 标量

开路状态期间的电导。

#### 依赖关系

要启用此参数，请通过单击 **开路故障** 参数中的 **添加故障** 超链接，向 Dynamic Load (Three-Phase) 模块添加故障。

创建故障后，您可以在 **故障检查器** 窗口中更改属性。当您打开存在故障的模块时，将显示 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关展示如何包含故障的示例，请参阅《分析直流电枢绕组故障》。

### **在指定时间触发故障** — 进入故障状态之前的时间 `0` `s`（默认） | 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请将 **触发类型** 设置为 `Timed`。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2023a：改进了对感性节点的支持

在 R2023a 之前，要将 Dynamic Load (Three-Phase) 模块连接到感性节点，必须提供较大的寄生电阻。从 R2023a 起，您可以通过指定 **额定电气频率**、**电压时间常数**、**初始电源电压（相间 RMS）**、**初始电源电压角度** 和 **对电气参考的寄生电导** 参数，将该模块连接到感性节点。由于此更改，**最小有功功率** 参数已删除。如果您的模型保存在较早版本中并包含此模块，则必须为新参数设置适当的值。

此外，该模块的 **建模选项** 参数已重命名为 **电气连接**，并移至 **主** 部分。

### R2020b：库路径更改

Dynamic Load (Three-Phase) 模块已从 **Simscape** > **Electrical** > **Passive** > **RLC Assemblies** 库移至 **Simscape** > **Electrical** > **Passive** 库。

如果您的脚本依赖于该模块的库路径或 Simscape 组件路径，请更新脚本以反映这些更改。

## 描述

平衡三相动态负载

Dynamic Load (Three-Phase) 模块为平衡三相电源建模平衡动态负载。

此表显示该模块如何根据来自电源的电压 *V* 计算消耗的有功功率和无功功率。

| *V* 值范围 | 消耗的有功功率和无功功率 |
| --- | --- |
| V>Vmin | Pactual=PinQactual=Qin |
| V<Vmin | 模块将负载建模为阻抗等于：  R=Vmin2PinPin2+Qin2X=Vmin2QinPin2+Qin2Z=R2+X2 |

在这些方程中：

- *Vmin* 是最小电源电压（相间 RMS）参数的值。
- *Pactual* 是 Dynamic Load (Three-Phase) 模块消耗的有功功率。
- *Pin* 是 Dynamic Load (Three-Phase) 模块的输入有功功率，由外部输入端口 **P** 决定。
- *Qactual* 是 Dynamic Load (Three-Phase) 模块消耗的无功功率。
- *Qin* 是 Dynamic Load (Three-Phase) 模块的输入无功功率，由外部输入端口 **Q** 决定。

Dynamic Load (Three-Phase) 模块根据输入有功功率 *Pin* 的极性消耗或生成有功功率。如果 *Pin* > 0，则该模块消耗有功功率。如果 *Pin* < 0，则该模块生成有功功率。

### 故障

要在 Dynamic Load (Three-Phase) 模块中建模故障，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅《故障行为建模》和《故障触发》。

Dynamic Load (Three-Phase) 模块允许您将电气故障建模为开路。该模块可以在特定时间触发故障事件。

### 潮流分析

如果该模块位于与频率-时间仿真模式兼容的网络中，您可以对该网络执行潮流分析。潮流分析提供可用于初始化电机的稳态值。

有关详细信息，请参阅《使用 Simscape Electrical 执行潮流分析》和《频率和时间仿真模式》。
