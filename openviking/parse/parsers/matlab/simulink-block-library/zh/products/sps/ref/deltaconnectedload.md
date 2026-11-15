---
type: simulink-block
title: 'Delta-Connected Load'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'deltaconnectedload'
documentation_source_path: 'ref/deltaconnectedload.html'
language: zh-CN
chinese_source: worker-translation
---

# Delta-Connected Load

## 端口

### 守恒

### **~** — 三相端口电气

复合三相端口。

有关复合和扩展三相端口的详细信息，请参阅 Three-Phase Ports。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

### 主

### **电气连接** — 对复合还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

*自 R2024b 起*

对复合还是扩展三相端口进行建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图相对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **参数化** — 参数化 `Specify by rated power and voltage`（默认）| `Specify component values directly`

选择如何指定 R、L 和 C 组件的值：

- `Specify by rated power and voltage` — 按额定电压和频率下的额定功率指定 R、L 和 C 组件的值。此选项为默认值。
- `Specify component values directly` — 直接按电阻、电感和电容指定 R、L 和 C 组件的值。

切换 **参数化** 值会重置 **组件结构** 值。请先选择组件参数化选项，然后选择组件结构。如果您稍后切换 **参数化** 值，请检查 **组件结构** 值，并在必要时重新选择它。

### **组件结构** — 所需的组件组合 `R`（默认）| `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

选择电阻 (R)、电容 (C) 和电感 (L) 以串联或并联方式连接的所需组合。

### **额定电压** — 额定电压 `24e3` `V`（默认）| 非负标量

指定负载功率时所用的电压。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify by rated power and voltage`。

### **有功功率** — 总耗散有功功率 `1e3` `W`（默认）| 正标量

在三相负载以额定电压供电时，三相负载耗散的总有功功率。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify by rated power and voltage`，并将 **组件结构** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **额定电气频率** — 额定电气频率 `60` `Hz`（默认）| 正标量

指定负载无功功率时所用的频率。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify by rated power and voltage`。

### **感性无功功率** — 感性无功功率 `1e2` `A*V`（默认）| 正标量

在三相负载以额定电压供电时，三相负载吸收的总感性无功功率。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify by rated power and voltage`，并将 **组件结构** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **容性无功功率** — 总容性无功功率 `-1e2` `A*V`（默认）| 负标量

在三相负载以额定电压供电时，三相负载吸收的总容性无功功率。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify by rated power and voltage`，并将 **组件结构** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### **电阻** — 电阻 `1` `Ohm`（默认）| 正标量

每个负载支路的电阻。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify component values`，并将 **组件结构** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **电感** — 电感 `0.001` `H`（默认）| 正标量

每个负载支路的电感。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify component values`，并将 **组件结构** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **电容** — 电容 `1e-6` `F`（默认）| 正标量

每个负载支路中的电容。

#### 依赖项

要启用此参数，请将 **参数化** 设置为 `Specify component values`，并将 **组件结构** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### 寄生

### **寄生串联电阻** — 寄生串联电阻 `0` `Ohm`（默认）| 非负标量

添加到负载中所有电容器实例的串联电阻值。

#### 依赖项

要启用此参数，请将 **组件结构** 设置为 `C`、`Parallel RC` 或 `Parallel LC`。

### **寄生并联电导** — 寄生并联电导 `0` `1/Ohm`（默认）| 非负标量

在负载中所有电感器实例两端添加的并联电导值。此参数表示小的寄生效应。

如果将 **组件结构** 设置为 `Series RL`、`Series LC` 或 `Series RLC`，则寄生并联电导连接在模块的完整支路两端。

#### 依赖项

要启用此参数，请将 **组件结构** 设置为 `L`、`Series RL`、`Series LC` 或 `Series RLC`。

### 初始条件

### **端子电压幅值** — 端子电压幅值 `24e3` `V`（默认）| 非负标量

端子电压的幅值。

#### 依赖项

要启用此参数，请将 **组件结构** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### **端子电压角度** — 端子电压角度 `0` `deg`（默认）| 标量

端子电压的角度。

#### 依赖项

要启用此参数，请将 **组件结构** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### **频率** — 频率 `60` `Hz`（默认）| 正标量

频率。

#### 依赖项

要启用此参数，请将 **组件结构** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### 故障

要修改故障，请创建故障，然后在模块对话框中单击 **打开故障属性**。要打开故障，请在属性检查器中单击 **故障行为** 链接。

### **连接故障** — 将故障添加到连接端口的选项 `Add fault`

*自 R2024b 起*

将故障添加到负载的三相连接端口的选项。

要添加故障，请单击 **添加故障** 超链接。

#### 依赖项

要启用此参数，请将 **对两个线路段建模** 设置为 `Yes`。

### **故障类型** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2024b 起*

要建模的故障类型。相关参数的可见性取决于故障模型。

#### 依赖项

要启用此参数，请通过单击 **连接故障** 参数旁边的 **添加故障** 超链接向模块添加故障。

### **故障相-中性点电阻** — 相连接与中性点之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2024b 起*

故障激活时，相连接与中性点之间的电阻。

#### 依赖项

要启用此参数，请通过单击 **连接故障** 参数旁边的 **添加故障** 超链接向模块添加故障，并将 **故障类型** 参数设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **故障中性点-地电阻** — 中性点与电气参考之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2024b 起*

故障激活时，中性点与电气参考之间的电阻。

#### 依赖项

要启用此参数，请通过单击 **连接故障** 参数旁边的 **添加故障** 超链接向模块添加故障，并将 **故障类型** 参数设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **无故障相-中性点电导** — 相连接与中性点之间的无故障电导 `1e-6` `1/Ohm`（默认）| 正标量

*自 R2024b 起*

故障未激活时，相连接与中性点之间的电导。

#### 依赖项

要启用此参数，请通过单击 **连接故障** 参数旁边的 **添加故障** 超链接向模块添加故障，并将 **故障类型** 参数设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：在三相连接端口处对故障建模

现在，您可以在负载的三相连接端口处对相接地或相间故障进行建模。要指定故障电阻和无故障电导的值，请使用 **故障相-中性点电阻**、**故障中性点-地电阻** 和 **无故障相-中性点电导** 参数。

### R2024b：**建模选项** 参数已更改

**建模选项** 参数已替换为模块对话框或属性检查器的 **主** 部分中的 **电气连接** 参数。

如果您在较早版本中创建的模型包含此模块，软件会自动将 **电气连接** 参数的值设置为您为 **建模选项** 参数指定的值。

## 描述

采用三角形配置接线的三相负载

Delta-Connected Load 模块对采用三角形配置接线的三相负载进行建模。负载的每个支路都可以包含以串联或并联方式连接的电阻 (R)、电容 (C) 和电感 (L) 的任意组合。

您可以直接按电阻、电感和电容来指定 R、L 和 C 组件的值，也可以按额定电压和频率下的额定功率来指定。

- 如果直接按 R、L 和 C 值对该模块进行参数化，则为了初始化，请提供电容初始电压的三元素行向量和电感初始电流的三元素行向量。
- 如果按额定功率对该模块进行参数化，则按初始电压、初始电压相位和初始频率指定初始条件。例如，如果负载直接连接到三相电压源，则初始条件与源的 RMS 线电压、频率和相移值相同。要指定零初始电压幅值，请将初始电压设置为 0。

对于 R、L 和 C 的某些组合，对于某些电路拓扑，您应指定有助于仿真在数值上收敛的寄生电阻或电导值。这些寄生项有助于为电感器创建小的并联电阻路径，并为电容器创建小的串联电阻。当按额定功率对该模块进行参数化时，额定功率值不考虑这些小的寄生项。额定功率仅表示负载本身的 R、L 和 C 值。

### 模块参数化

这些表列出了针对 **组件结构** 参数的每个值对应的模块参数，具体取决于您选择的 **参数化** 选项：

- `Specify by rated power and voltage`
- `Specify component values directly`

**按额定功率和电压指定**

| 组件结构 | 主要参数 | 寄生参数 | 初始条件参数 |
| --- | --- | --- | --- |
| `R` | 额定电压  有功功率 | 无 | 无 |
| `L` | 额定电压  额定电气频率  感性无功功率 | 寄生并联电导 | 端子电压幅值  端子电压角度  频率 |
| `C` | 额定电压  额定电气频率  容性无功功率 | 寄生串联电阻 | 端子电压幅值  端子电压角度  频率 |
| `Series RL` | 额定电压  额定电气频率  有功功率  感性无功功率 | 寄生并联电导 | 端子电压幅值  端子电压角度  频率 |
| `Series RC` | 额定电压  额定电气频率  有功功率  容性无功功率 | 无 | 端子电压幅值  端子电压角度  频率 |
| `Series LC` | 额定电压  额定电气频率  感性无功功率  容性无功功率 | 寄生并联电导 | 端子电压幅值  端子电压角度  频率 |
| `Series RLC` | 额定电压  额定电气频率  有功功率  感性无功功率  容性无功功率 | 寄生并联电导 | 端子电压幅值  端子电压角度  频率 |
| `Parallel RL` | 额定电压  额定电气频率  有功功率  感性无功功率 | 无 | 端子电压幅值  端子电压角度  频率 |
| `Parallel RC` | 额定电压  额定电气频率  有功功率  容性无功功率 | 寄生串联电阻 | 端子电压幅值  端子电压角度  频率 |
| `Parallel LC` | 额定电压  额定电气频率  感性无功功率  容性无功功率 | 寄生串联电阻 | 端子电压幅值  端子电压角度  频率 |
| `Parallel RLC` | 额定电压  额定电气频率  有功功率  感性无功功率  容性无功功率 | 寄生串联电阻 | 端子电压幅值  端子电压角度  频率 |

**直接指定组件值**

| 组件结构 | 主要参数 | 寄生参数 | 初始条件参数 |
| --- | --- | --- | --- |
| `R` | 电阻 | 无 | 无 |
| `L` | 电感 | 寄生并联电导 | 初始电感电流 [ Ia Ib Ic ] |
| `C` | 电容 | 寄生串联电阻 | 初始电容电压 [ Va Vb Vc ] |
| `Series RL` | 电阻  电感 | 寄生并联电导 | 初始电感电流 [ Ia Ib Ic ] |
| `Series RC` | 电阻  电容 | 无 | 初始电容电压 [ Va Vb Vc ] |
| `Series LC` | 电感  电容 | 寄生并联电导 | 初始电感电流 [ Ia Ib Ic ]  初始电容电压 [ Va Vb Vc ] |
| `Series RLC` | 电阻  电感  电容 | 寄生并联电导 | 初始电感电流 [ Ia Ib Ic ]  初始电容电压 [ Va Vb Vc ] |
| `Parallel RL` | 电阻  电感 | 无 | 初始电感电流 [ Ia Ib Ic ] |
| `Parallel RC` | 电阻  电容 | 寄生串联电阻 | 初始电容电压 [ Va Vb Vc ] |
| `Parallel LC` | 电感  电容 | 寄生串联电阻 | 初始电感电流 [ Ia Ib Ic ]  初始电容电压 [ Va Vb Vc ] |
| `Parallel RLC` | 电阻  电感  电容 | 寄生串联电阻 | 初始电感电流 [ Ia Ib Ic ]  初始电容电压 [ Va Vb Vc ] |

### 故障

*自 R2024b 起*

要在 Delta-Connected Load 模块中对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅故障行为建模和故障触发。

Delta-Connected Load 模块允许您在以下三相连接端口处对这些类型的故障建模：

- 单相接地故障（a-g、b-g 或 c-g）
- 两相故障（a-b、b-c 或 c-a）
- 两相接地故障（a-b-g、b-c-g 或 c-a-g）
- 三相故障（a-b-c）
- 三相接地故障（a-b-c-g）

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可以提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅按标称值进行系统缩放。

对于此模块，仅当在 **主要** 部分中，将 **参数化** 参数设置为 `Specify component values directly`，并且未将 **组件结构** 参数设置为 `R` 时，**初始目标** 和 **标称值** 设置才可见。
