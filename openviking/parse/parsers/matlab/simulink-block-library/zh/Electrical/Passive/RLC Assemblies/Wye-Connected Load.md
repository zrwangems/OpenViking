---
type: simulink-block
title: 'Wye-Connected Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'wyeconnectedload'
documentation_source_path: 'ref/wyeconnectedload.html'
language: zh-CN
chinese_source: worker-translation
---

# Wye-Connected Load

## 端口
```yaml
ports:
- name: '~'
  summary: 三相复合电气端口
  direction: conserving
- name: a
  summary: '*a* 相电气端口'
  direction: conserving
- name: b
  summary: '*b* 相电气端口'
  direction: conserving
- name: c
  summary: '*c* 相电气端口'
  direction: conserving
- name: n
  summary: 中性相电气端口
  direction: conserving
```

### 守恒端口

### **~** — 三相复合电气端口

复合三相端口。

有关复合和展开三相端口的详细信息，请参阅三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气端口

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气端口

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气端口

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **n** — 中性相电气端口

与中性相相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 建模为复合还是展开三相端口 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主要
- name: Parameterization
  summary: 参数化方式 Specify by rated power and voltage（默认）| Specify component values directly
  group: 主要
- name: Component structure
  summary: 所需的组件组合 R（默认）| L | C | Series RL | Series RC | Series LC | Series RLC | Parallel RL | Parallel RC | Parallel LC
    | Parallel RLC
  group: 主要
- name: Rated voltage
  summary: 额定电压 24e3 V（默认）| 非负标量
  group: 主要
- name: Real power
  summary: 总有功耗散功率 1e3 W（默认）| 正标量
  group: 主要
- name: Rated electrical frequency
  summary: 额定电气频率 60 Hz（默认）| 正标量
  group: 主要
- name: Inductive reactive power
  summary: 感性无功功率 1e2 A*V（默认）| 正标量
  group: 主要
- name: Capacitive reactive power
  summary: 总容性无功功率 -1e2 A*V（默认）| 负标量
  group: 主要
- name: Resistance
  summary: 电阻 1 Ohm（默认）| 正标量
  group: 主要
- name: Inductance
  summary: 电感 0.001 H（默认）| 正标量
  group: 主要
- name: Capacitance
  summary: 电容 1e-6 F（默认）| 正标量
  group: 主要
- name: Parasitic series resistance
  summary: 寄生串联电阻 0 Ohm（默认）| 非负标量
  group: 寄生参数
- name: Parasitic parallel conductance
  summary: 寄生并联电导 0 1/Ohm（默认）| 非负标量
  group: 寄生参数
- name: Terminal voltage magnitude
  summary: 端电压幅值 24e3 V（默认）| 非负标量
  group: 初始条件
- name: Terminal voltage angle
  summary: 端电压角度 0 deg（默认）| 标量
  group: 初始条件
- name: Frequency
  summary: 频率 60 Hz（默认）| 正标量
  group: 初始条件
- name: Connection fault
  summary: 向连接端口添加故障的选项 Add fault
  group: 故障
- name: Fault type
  summary: 故障类型 Single-phase to ground (a-g)（默认）| Single-phase to ground (b-g) | Single-phase to ground (c-g) | Two-phase
    (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase to ground
    (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: 故障
- name: Faulted phase-neutral resistance
  summary: 故障时相连接与中性点之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: Faulted neutral-ground resistance
  summary: 故障时中性点与电气参考之间的电阻 1e-3 Ohm（默认）| 正标量
  group: 故障
- name: Unfaulted phase-neutral conductance
  summary: 未故障时相连接与中性点之间的电导 1e-6 1/Ohm（默认）| 正标量
  group: 故障
```

### 主要

### **Electrical connection** — 建模为复合还是展开三相端口 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

*自 R2024b 起*

选择建模为复合还是展开三相端口。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建与三相电气系统单线图对应的模型。

展开三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。

### **Parameterization** — 参数化方式 `Specify by rated power and voltage`（默认）| `Specify component values directly`

选择如何为 R、L 和 C 组件指定值：

- `Specify by rated power and voltage` — 通过额定电压和频率下的额定功率为 R、L 和 C 组件指定值。此选项为默认值。
- `Specify component values directly` — 直接以电阻、电感和电容的形式为 R、L 和 C 组件指定值。

切换 **Parameterization** 值会重置 **Component structure** 值。请先选择组件参数化选项，然后选择组件结构。如果之后切换了 **Parameterization** 值，请检查 **Component structure** 值，必要时重新选择。

### **Component structure** — 所需的组件组合 `R`（默认）| `L` | `C` | `Series RL` | `Series RC` | `Series LC` | `Series RLC` | `Parallel RL` | `Parallel RC` | `Parallel LC` | `Parallel RLC`

选择电阻（R）、电容（C）和电感（L）以串联或并联方式连接的所需组合。

### **Rated voltage** — 额定电压 `24e3` `V`（默认）| 非负标量

指定负载功率所对应的电压。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify by rated power and voltage`。

### **Real power** — 总有功耗散功率 `1e3` `W`（默认）| 正标量

三相负载在额定电压供电时耗散的总有功功率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify by rated power and voltage`，并将 **Component structure** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

指定无功负载功率所对应的频率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify by rated power and voltage`。

### **Inductive reactive power** — 感性无功功率 `1e2` `A*V`（默认）| 正标量

三相负载在额定电压供电时吸收的总感性无功功率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify by rated power and voltage`，并将 **Component structure** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **Capacitive reactive power** — 总容性无功功率 `-1e2` `A*V`（默认）| 负标量

三相负载在额定电压供电时吸收的总容性无功功率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify by rated power and voltage`，并将 **Component structure** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### **Resistance** — 电阻 `1` `Ohm`（默认）| 正标量

每个负载支路的电阻。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify component values`，并将 **Component structure** 设置为 `R`、`Series RL`、`Series RC`、`Series RLC`、`Parallel RL` 或 `Parallel RC`。

### **Inductance** — 电感 `0.001` `H`（默认）| 正标量

每个负载支路的电感。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify component values`，并将 **Component structure** 设置为 `L`、`Series RL`、`Series LC`、`Series RLC`、`Parallel RL` 或 `Parallel LC`。

### **Capacitance** — 电容 `1e-6` `F`（默认）| 正标量

每个负载支路的电容。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Specify component values`，并将 **Component structure** 设置为 `C`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RC` 或 `Parallel LC`。

### 寄生参数

### **Parasitic series resistance** — 寄生串联电阻 `0` `Ohm`（默认）| 非负标量

添加到负载中所有电容实例的串联电阻值。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `C`、`Parallel RC` 或 `Parallel LC`。

### **Parasitic parallel conductance** — 寄生并联电导 `0` `1/Ohm`（默认）| 非负标量

添加到负载中所有电感实例两端的并联电导值。此参数表示小的寄生效应。

如果将 **Component structure** 设置为 `Series RL`、`Series LC` 或 `Series RLC`，则寄生并联电导连接在模块的整个支路两端。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`Series RL`、`Series LC` 或 `Series RLC`。

### 初始条件

### **Terminal voltage magnitude** — 端电压幅值 `24e3` `V`（默认）| 非负标量

端电压的幅值。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### **Terminal voltage angle** — 端电压角度 `0` `deg`（默认）| 标量

端电压的角度。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### **Frequency** — 频率 `60` `Hz`（默认）| 正标量

频率。

#### 依赖关系

要启用此参数，请将 **Component structure** 设置为 `L`、`C`、`Series RL`、`Series RC`、`Series LC`、`Series RLC`、`Parallel RL`、`Parallel RC` 或 `Parallel LC`。

### 故障

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。要打开故障，请在 Property Inspector 中点击 **Fault behavior** 链接。

### **Connection fault** — 向连接端口添加故障的选项 `Add fault`

*自 R2024b 起*

向负载的三相连接端口添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **Fault type** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2024b 起*

要建模的故障类型。相关参数的可见性取决于故障模型。

#### 依赖关系

要启用此参数，请通过点击 **Connection fault** 参数旁边的 **Add fault** 超链接向模块添加故障。

### **Faulted phase-neutral resistance** — 故障时相连接与中性点之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2024b 起*

故障激活时相连接与中性点之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **Connection fault** 参数旁边的 **Add fault** 超链接向模块添加故障，并将 **Fault type** 参数设置为以下选项之一：

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

### **Faulted neutral-ground resistance** — 故障时中性点与电气参考之间的电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2024b 起*

故障激活时中性点与电气参考之间的电阻。

#### 依赖关系

要启用此参数，请通过点击 **Connection fault** 参数旁边的 **Add fault** 超链接向模块添加故障，并将 **Fault type** 参数设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **Unfaulted phase-neutral conductance** — 未故障时相连接与中性点之间的电导 `1e-6` `1/Ohm`（默认）| 正标量

*自 R2024b 起*

故障未激活时相连接与中性点之间的电导。

#### 依赖关系

要启用此参数，请通过点击 **Connection fault** 参数旁边的 **Add fault** 超链接向模块添加故障，并将 **Fault type** 参数设置为以下选项之一：

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

您现在可以在负载的三相连接端口处对相接地故障或相间故障进行建模。要指定故障电阻和未故障电导的值，请使用 **Faulted phase-neutral resistance**、**Faulted neutral-ground resistance** 和 **Unfaulted phase-neutral conductance** 参数。

### R2024b：**Modeling Option** 参数已更改

**Modeling option** 参数已被模块对话框或 Property Inspector 中 **Main** 部分内的 **Electrical connection** 参数取代。

如果您在早期版本中创建的模型包含此模块，软件会自动将 **Electrical connection** 参数的值设置为您为 **Modeling option** 参数指定的值。

## 描述

以星形配置接线的三相负载

Wye-Connected Load 模块对以星形配置接线的三相负载进行建模。负载的每个支路可以包含电阻（R）、电容（C）和电感（L）以串联或并联方式连接的任意组合。

您可以直接以电阻、电感和电容的形式为 R、L 和 C 组件指定值，也可以通过额定电压和频率下的额定功率来指定。

- 如果直接以 R、L 和 C 值的形式对模块进行参数化，则为了初始化，请提供电容初始电压的三元素行向量和电感初始电流的三元素行向量。
- 如果以额定功率的形式对模块进行参数化，则以初始电压、初始电压相位和初始频率的形式指定初始条件。例如，如果负载直接连接到三相电压源，则初始条件与源的 RMS 线电压、频率和相移值相同。要指定零初始电压幅值，请将初始电压设置为 `0`。

对于 R、L 和 C 的某些组合以及某些电路拓扑，您应指定寄生电阻或电导值，以帮助仿真在数值上收敛。这些寄生项有助于为电感创建小的并联电阻路径，为电容创建小的串联电阻。当您以额定功率的形式对模块进行参数化时，额定功率值不考虑这些小的寄生项。额定功率仅表示负载本身的 R、L 和 C 值。

### 模块参数化

这些表列出了基于您选择的**参数化**选项，**组件结构**参数每个值对应的模块参数：

- `Specify by rated power and voltage`
- `Specify component values directly`

**按额定功率和电压指定**

| 组件结构 | 主参数 | 寄生参数 | 初始条件参数 |
| --- | --- | --- | --- |
| `R` | 额定电压  有功功率 | 无 | 无 |
| `L` | 额定电压  额定电气频率  感性无功功率 | 寄生并联电导 | 端电压幅值  端电压相角  频率 |
| `C` | 额定电压  额定电气频率  容性无功功率 | 寄生串联电阻 | 端电压幅值  端电压相角  频率 |
| `Series RL` | 额定电压  额定电气频率  有功功率  感性无功功率 | 寄生并联电导 | 端电压幅值  端电压相角  频率 |
| `Series RC` | 额定电压  额定电气频率  有功功率  容性无功功率 | 无 | 端电压幅值  端电压相角  频率 |
| `Series LC` | 额定电压  额定电气频率  感性无功功率  容性无功功率 | 寄生并联电导 | 端电压幅值  端电压相角  频率 |
| `Series RLC` | 额定电压  额定电气频率  有功功率  感性无功功率  容性无功功率 | 寄生并联电导 | 端电压幅值  端电压相角  频率 |
| `Parallel RL` | 额定电压  额定电气频率  有功功率  感性无功功率 | 无 | 端电压幅值  端电压相角  频率 |
| `Parallel RC` | 额定电压  额定电气频率  有功功率  容性无功功率 | 寄生串联电阻 | 端电压幅值  端电压相角  频率 |
| `Parallel LC` | 额定电压  额定电气频率  感性无功功率  容性无功功率 | 寄生串联电阻 | 端电压幅值  端电压相角  频率 |
| `Parallel RLC` | 额定电压  额定电气频率  有功功率  感性无功功率  容性无功功率 | 寄生串联电阻 | 端电压幅值  端电压相角  频率 |

**直接指定组件值**

| 组件结构 | 主参数 | 寄生参数 | 初始目标变量 |
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

要在 Wye-Connected Load 模块中建模故障，请在**故障**部分中，单击要建模的故障旁边的**添加故障**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

Wye-Connected Load 模块允许您在三相连接端口处建模以下类型的故障：

- 单相接地故障（a-g、b-g 或 c-g）
- 两相故障（a-b、b-c 或 c-a）
- 两相接地故障（a-b-g、b-c-g 或 c-a-g）
- 三相故障（a-b-c）
- 三相接地故障（a-b-c-g）

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅 System Scaling by Nominal Values。

对于此模块，仅当您在**主**部分中将**参数化**参数设置为 `Specify component values directly`，且未将**组件结构**参数设置为 `R` 时，**初始目标**和**标称值**设置才可见。
