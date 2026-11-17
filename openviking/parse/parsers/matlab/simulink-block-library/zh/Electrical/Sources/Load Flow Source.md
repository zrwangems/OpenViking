---
type: simulink-block
title: 'Load Flow Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'loadflowsource'
documentation_source_path: 'ref/loadflowsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Load Flow Source

## 端口

### 守恒端口

### **~** — 三相电压电气端口

与电压相 *a*、*b* 和 *c* 关联的三相端口。

### **n** — 星形中性点电气端口

与星形中性点关联的电气守恒端口。

## 参数

### 主设置

### **Source type** — 电压源模型 `Swing bus`（默认）| `Voltage source with series impedance` | `PV bus` | `PQ bus`

模块所建模的电压源类型。

#### 依赖关系

**Source voltage (pu)**、**Terminal voltage (pu)**、**Active power generated**、**Active power consumed**、**Reactive power consumed**、**Source phase**、**Minimum voltage (pu)** 和 **Internal source phase search range** 的可见性取决于您为此参数选择的值。

### **Source voltage (pu)** — 源电压 `1`（默认）| 标量

源产生的标幺电压。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `Voltage source with series impedance` 时，此参数才可见。

### **Terminal voltage (pu)** — 端子电压 `1`（默认）| 标量

源产生的标幺端子电压。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `Swing bus` 或 `PV bus` 时，此参数才可见。

### **Active power generated** — 产生的有功功率 `0` `W`（默认）| 标量

源产生的有功功率。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `PV bus` 时，此参数才可见。

### **Active power consumed** — 消耗的有功功率 `0` `W`（默认）

源消耗的有功功率。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `PQ bus` 时，此参数才可见。

### **Reactive power consumed** — 消耗的无功功率 `0` `V*A`（默认）

源消耗的无功功率。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `PQ bus` 时，此参数才可见。

### **Rated voltage (phase-to-phase RMS)** — 额定相间 RMS 电压 `sqrt(3) * 100 / sqrt(2)` `V`（默认）| 标量

额定相间均方根（RMS）电压。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）| 标量

额定频率，单位为 Hz。

### **Source phase** — 源相位 `0` `deg`（默认）| 标量

源的相移。

#### 依赖关系

仅当您将 **Source type** 参数设置为 `Voltage source with series impedance` 时，此参数才可见。

### 阻抗

### **Source impedance** — 源阻抗方法 `None`（默认）| `X/R Ratio` | `Series R` | `Series L` | `Series RL`

源阻抗的类型。选择任何其他选项将启用其他参数。选项包括：

- `None`
- `X/R Ratio`
- `Series R`
- `Series L`
- `Series RL`

#### 依赖关系

**Short-circuit power level**、**Source X/R ratio**、**Source impedance parasitic parallel conductance**、**Source resistance** 和 **Source inductance** 的可见性取决于您为此参数选择的值。

### **Short-circuit power level** — 短路功率水平 `1e6` `V*A`（默认）| 标量

短路功率水平。

#### 依赖关系

仅当您将 **Source impedance** 参数设置为 `X/R ratio` 时，此参数才可见。

### **Source X/R ratio** — 电抗与电阻之比 `15`（默认）| 标量

电抗与电阻之比。

#### 依赖关系

仅当您将 **Source impedance** 参数设置为 `X/R ratio` 时，此参数才可见。

### **Source impedance parasitic parallel conductance** — 源阻抗寄生并联电导 `0` `1/Ohm`（默认）| 标量

源阻抗寄生并联电导。

#### 依赖关系

仅当您将 **Source impedance** 参数设置为 `X/R ratio` 或 `Series L` 或 `Series RL` 时，此参数才可见。

### **Source resistance** — 源电阻 `0.01` `Ohm`（默认）| 标量

源电阻。

#### 依赖关系

仅当您将 **Source impedance** 参数设置为 `Series R` 或 `Series RL` 时，此参数才可见。

### **Source inductance** — 源电感 `3.97e-4` `H`（默认）| 标量

源电感。

#### 依赖关系

仅当您将 **Source impedance** 参数设置为 `Series L` 或 `Series RL` 时，此参数才可见。

### 预期范围

### **Minimum voltage (pu)** — 最小电压 `0.95`（默认）| 标量

标幺最小电压。此参数有助于在具有非物理极低电压的模型中进行初始求解。

#### 依赖关系

仅当您在 **Main** 设置中将 **Source type** 参数设置为 `Swing bus`、`PV bus` 或 `PQ bus` 时，此参数才可见。

### **Internal source phase search range** — 相位搜索范围 `[-inf, inf]` `deg`（默认）| 向量

内部源相位搜索的下边界和上边界向量。使用此范围可帮助初始求解收敛到所需的潮流解。

#### 依赖关系

仅当您在 **Main** 设置中将 **Source type** 参数设置为 `PV bus` 或 `PQ bus` 时，此参数才可见。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

用于执行潮流分析的三相电压源

Load Flow Source 模块是一个三相电压源，用于潮流分析。此模块仅适用于与频率-时间仿真模式兼容的三相 Simscape™ 网络。

此模块可与 Busbar 模块配合使用，以实现平衡节点、PV 节点或 PQ 节点。节点类型从 **Source type** 下拉菜单参数中选择。有关 Simscape Electrical™ 中潮流的更多信息，请参阅 Perform a Load-Flow Analysis Using Simscape Electrical。

当您为 **Source impedance** 参数选择 `None` 时，Load Flow Source 模块建模一个理想三相电压源，无论流过源的电流如何，它都能在其端子上维持指定幅值的正弦电压。

该源采用星形配置，端口 **n** 提供与星形中性点的连接。端口 **~** 是表示相 *a*、*b* 和 *c* 的三相端口。如果电流从正极流向星形中性点，则电流为正，每相电压等于正极端子电压与星形中性点电压之差，*V*(+) – *V*n。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
