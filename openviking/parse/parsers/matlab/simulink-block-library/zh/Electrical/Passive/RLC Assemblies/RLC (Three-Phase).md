---
type: simulink-block
title: 'RLC (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'rlcthreephase'
documentation_source_path: 'ref/rlcthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# RLC (Three-Phase)

## 端口

### 守恒端口

### **~1** — 三相端口电气

复合三相端口。

有关复合和展开三相端口的详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **~2** — 三相端口电气

复合三相端口。

有关复合和展开三相端口的详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a1** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b1** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c1** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **a2** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b2** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c2** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

## 参数

### 主要

### **Electrical connection** — 建模为复合还是展开三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

*自 R2024b 起*

建模为复合还是展开三相端口。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建与三相电气系统单线图对应的模型。

展开三相端口使用三个独立的电气守恒端口来表示三相系统的各相。

### **Component structure** — 所需的元件组合 `R`（默认）| `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

选择电阻 (R)、电容 (C) 和电感 (L) 以串联或并联方式连接的所需组合。

### **Resistance** — 电阻 `1` `Ohm`（默认）| 正标量

各线路阻抗的电阻。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **Inductance** — 电感 `1e-3` `H`（默认）| 正标量

各线路阻抗的电感。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **Capacitance** — 电容 `1e-6` `F`（默认）| 正标量

各线路阻抗的电容。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### 寄生效应

### **Parasitic series resistance** — 寄生串联电阻 `0` `Ohm`（默认）| 非负标量

添加到负载中所有电容实例的串联电阻值。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `C`、`Parallel RC` 或 `Parallel LC`。

### **Parasitic parallel conductance** — 寄生并联电导 `0` `1/Ohm`（默认）| 非负标量

跨负载中所有电感实例添加的并联电导值。此参数表示小的寄生效应。

如果将 **Component structure** 设置为 `Series RL`、`Series LC` 或 `Series RLC`，则寄生并联电导连接在模块的整个支路两端。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`Series RL`、`Series LC` 或 `Series RLC`。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。要打开故障，请在 Property Inspector 中点击 **Fault behavior** 链接。

### **Branch fault** — 添加支路故障的选项 `Add fault`

*自 R2024b 起*

在 RLC (Three-Phase) 模块中添加支路故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Faulted phase** — 指定故障相的选项 `Phase a`（默认）| `Phase b` | `Phase c` | `Phase a and b` | `Phase b and c` | `Phase c and a` | `Phase a, b and c`

*自 R2024b 起*

指定 RLC (Three-Phase) 模块故障相的选项。您可以指定一个或多个故障相。

#### 依赖关系

要启用此参数，请通过点击 **Branch fault** 参数中的 **Add fault** 超链接向 RLC (Three-Phase) 模块添加故障。

### **Faulted resistance** — 故障阻抗元件的电阻 `0.01` `Ohm`（默认）| 正标量

*自 R2024b 起*

故障阻抗元件的电阻。

#### 依赖关系

要启用此参数，请通过点击 **Branch fault** 参数中的 **Add fault** 超链接向 RLC (Three-Phase) 模块添加故障。

## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：对支路故障建模

您现在可以对一个或多个故障相建模。该模块将故障相建模为电阻。要指定故障电阻的值，请使用 **Faulted resistance** 参数。

### R2024b：**Modeling Option** 参数已更改

**Modeling option** 参数已替换为模块对话框或 Property Inspector 中 **Main** 部分内的 **Electrical connection** 参数。

如果您在较早版本中创建的模型包含此模块，软件会自动将 **Electrical connection** 参数的值设置为您为 **Modeling option** 参数指定的值。

## 描述

三相阻抗

RLC (Three-Phase) 模块对具有两个三相连接的三相阻抗进行建模。三个相同的阻抗元件中的每一个都可以包含电阻 (R)、电容 (C) 和电感 (L) 以串联或并联方式的任意组合。

通过指定相应的模块参数来定义 R、L 和 C 元件的值。不要将参数值设置为零或无穷大来移除项。而应为 **Component structure** 参数选择正确的选项。

对于 R、L 和 C 的某些组合以及某些电路拓扑，您应指定寄生电阻或电导值，以帮助仿真在数值上收敛。这些寄生项有助于为电感创建小的并联电阻路径，为电容创建小的串联电阻。

### 故障

*自 R2024b 起*

要对 RLC (Three-Phase) 模块中的故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

RLC (Three-Phase) 模块允许您表示一个或多个故障相。该模块将故障相建模为电阻。要指定故障电阻的值，请使用 **Faulted resistance** 参数。

例如，此图显示了三相电感支路的等效电路。

三相电感支路的等效电路。顶部电感标记为 La，中间电感标记为 Lb，底部电感标记为 Lc。

当您添加支路故障并将 **Faulted phase** 参数设置为 `Phase a` 时，此图显示了故障三相电感支路的等效电路。

故障三相电感支路的等效电路。顶部电阻标记为 Rfa，中间电感标记为 Lb，底部电感标记为 Lc。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅基于标称值的系统缩放。

对于此模块，仅当在 **Main** 部分中未将 **Component structure** 参数设置为 `R` 时，**Initial Targets** 和 **Nominal Values** 设置才可见。
