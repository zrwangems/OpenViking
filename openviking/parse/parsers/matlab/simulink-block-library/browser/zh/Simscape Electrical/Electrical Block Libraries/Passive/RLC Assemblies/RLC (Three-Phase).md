---
type: simulink-block
title: 'RLC (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'rlcthreephase'
documentation_source_path: 'ref/rlcthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# RLC (Three-Phase)

## 端口

### 守恒

### **~1** — 三相端口电气

复合三相端口。

有关复合和扩展三相端口的详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **~2** — 三相端口电气

复合三相端口。

有关复合和扩展三相端口的详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a1** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b1** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c1** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **a2** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b2** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c2** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

### 主

### **电气连接** — 是对复合三相端口还是扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

*自 R2024b 起*

是对复合三相端口还是扩展三相端口建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图相对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各个相。

### **元件结构** — 所需元件组合 `R`（默认）| `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

选择电阻器 (R)、电容器 (C) 和电感器 (L) 以串联或并联方式连接所需的组合。

### **电阻** — 电阻 `1` `Ohm`（默认）| positive scalar

每个线路阻抗的电阻。

#### 依赖关系

要启用此参数，请将 **元件结构** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **电感** — 电感 `1e-3` `H`（默认）| positive scalar

每个线路阻抗的电感。

#### 依赖关系

要启用此参数，请将 **元件结构** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **电容** — 电容 `1e-6` `F`（默认）| positive scalar

每个线路阻抗中的电容。

#### 依赖关系

要启用此参数，请将 **元件结构** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### 寄生

### **寄生串联电阻** — 寄生串联电阻 `0` `Ohm`（默认）| nonnegative scalar

添加到负载中所有电容器实例的串联电阻值。

#### 依赖关系

要启用此参数，请将 **元件结构** 设置为 `C`、`Parallel RC` 或 `Parallel LC`。

### **寄生并联电导** — 寄生并联电导 `0` `1/Ohm`（默认）| nonnegative scalar

添加到负载中所有电感器实例两端的并联电导值。此参数表示较小的寄生效应。

如果将 **元件结构** 设置为 `Series RL`、`Series LC` 或 `Series RLC`，则寄生并联电导连接在模块的完整支路两端。

#### 依赖关系

要启用此参数，请将 **元件结构** 设置为 `L`、`Series RL`、`Series LC` 或 `Series RLC`。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **打开故障属性**。要打开故障，请在属性检查器中点击 **故障行为** 链接。

### **支路故障** — 添加支路故障的选项 `Add fault`

*自 R2024b 起*

在 RLC (Three-Phase) 模块中添加支路故障的选项。

要添加故障，请点击 **添加故障** 超链接。

### **故障相** — 指定故障相的选项 `Phase a`（默认）| `Phase b` | `Phase c` | `Phase a and b` | `Phase b and c` | `Phase c and a` | `Phase a, b and c`

*自 R2024b 起*

指定 RLC (Three-Phase) 模块故障相的选项。您可以指定一个或多个故障相。

#### 依赖关系

要启用此参数，请点击 **支路故障** 参数中的 **添加故障** 超链接，向 RLC (Three-Phase) 模块添加故障。

### **故障电阻** — 故障阻抗元件的电阻 `0.01` `Ohm`（默认）| positive scalar

*自 R2024b 起*

故障阻抗元件的电阻。

#### 依赖关系

要启用此参数，请点击 **支路故障** 参数中的 **添加故障** 超链接，向 RLC (Three-Phase) 模块添加故障。

## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：对支路故障建模

现在可以对一个或多个故障相建模。该模块将故障相建模为电阻器。要指定故障电阻的值，请使用 **故障电阻** 参数。

### R2024b：**建模选项** 参数已更改

**建模选项** 参数已替换为模块对话框或属性检查器中 **主** 部分内的 **电气连接** 参数。

如果您在较早版本中创建的模型包含此模块，软件会自动将 **电气连接** 参数的值设置为您为 **建模选项** 参数指定的值。

## 描述

三相阻抗

RLC (Three-Phase) 模块对具有两个三相连接的三相阻抗建模。三个相同的阻抗元件中的每一个都可以包含电阻器 (R)、电容器 (C) 和电感器 (L) 以串联或并联方式连接的任意组合。

通过指定相应的模块参数来定义 R、L 和 C 元件的值。不要为了移除项而将参数值设置为零或无穷大。而应为 **元件结构** 参数选择正确的选项。

对于 R、L 和 C 的某些组合以及某些电路拓扑，您应指定有助于仿真在数值上收敛的寄生电阻或电导值。这些寄生项有助于为电感器创建小的并联电阻路径，并为电容器创建小的串联电阻。

### 故障

*自 R2024b 起*

要对 RLC (Three-Phase) 模块中的故障建模，请在 **故障** 部分中，点击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

RLC (Three-Phase) 模块允许您表示一个或多个故障相。该模块将故障相建模为电阻器。要指定故障电阻的值，请使用 **故障电阻** 参数。

例如，此图显示了三相电感支路的等效电路。

三相电感支路的等效电路。顶部电感器标记为 La，中间电感器标记为 Lb，底部电感器标记为 Lc。

当您添加支路故障并将 **故障相** 参数设置为 `Phase a` 时，此图显示了故障三相电感支路的等效电路。

故障三相电感支路的等效电路。顶部电阻器标记为 Rfa，中间电感器标记为 Lb，底部电感器标记为 Lc。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。

对于此模块，仅当您在 **主** 部分中未将 **元件结构** 参数设置为 `R` 时，**初始目标** 和 **标称值** 设置才可见。
