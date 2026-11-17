---
type: simulink-block
title: 'P-Channel JFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'pchanneljfet'
documentation_source_path: 'ref/pchanneljfet.html'
language: zh-CN
chinese_source: worker-translation
---

# P-Channel JFET

## 端口
```yaml
ports:
- name: G
  summary: 栅极端子电气端口
  direction: conserving
- name: D
  summary: 漏极端子电气端口
  direction: conserving
- name: S
  summary: 源极端子电气端口
  direction: conserving
- name: H
  summary: 热端口热端口
  direction: conserving
```

### 守恒端口

### **G** — 栅极端子电气端口

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气端口

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气端口

与晶体管源极端子关联的电气守恒端口。

### **H** — 热端口热端口

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Parameterization
  summary: 模块参数化 Specify from a datasheet（默认）| Specify using equation parameters directly
  group: 主
- name: Gate reverse current, I_gss
  summary: 栅极反向电流 5 nA（默认）
  group: 主
- name: Saturated drain current, I_dss
  summary: 饱和漏极电流 -3 mA（默认）
  group: 主
- name: I_dss measurement point, [V_gs V_ds]
  summary: I_dss 测量点 [ 0 -15 ] V（默认）
  group: 主
- name: Small-signal parameters, [g_fs g_os]
  summary: 小信号参数 [ 2.5e+3 75 ] uS（默认）
  group: 主
- name: Small-signal measurement point [V_gs V_ds]
  summary: 小信号测量点 [ 0 -15 ] V（默认）
  group: 主
- name: Transconductance parameter
  summary: 跨导参数 1e-04 A/V2（默认）
  group: 主
- name: Saturation current
  summary: 饱和电流 1e-14 A（默认）
  group: 主
- name: Threshold voltage
  summary: 阈值电压 2 V（默认）
  group: 主
- name: Channel-length modulation
  summary: 沟道长度调制 0 1/V（默认）
  group: 主
- name: Measurement temperature
  summary: 测量温度 25 degC（默认）
  group: 主
- name: Source ohmic resistance
  summary: 源极欧姆电阻 0.0001 Ohm（默认）| 非负标量
  group: 欧姆电阻
- name: Drain ohmic resistance
  summary: 漏极欧姆电阻 0.01 Ohm（默认）| 非负标量
  group: 欧姆电阻
- name: Parameterization
  summary: 结电容参数化 Specify from a datasheet（默认）| Specify using equation parameters directly
  group: 结电容
- name: Input capacitance, Ciss
  summary: 输入电容 5 pF（默认）
  group: 结电容
- name: Reverse transfer capacitance, Crss
  summary: 反向传输电容 1 pF（默认）
  group: 结电容
- name: Gate-source junction capacitance
  summary: 栅源结电容 4 pF（默认）
  group: 结电容
- name: Gate-drain junction capacitance
  summary: 栅漏结电容 1 pF（默认）
  group: 结电容
- name: Parameterization
  summary: 温度依赖性参数化 None — Simulate at parameter measurement temperature（默认）| Model temperature dependence
  group: 温度依赖性
- name: Gate reverse current, I_gss, at second measurement temperature
  summary: 第二测量温度下的栅极反向电流 I_gss 950 nA（默认）
  group: 温度依赖性
- name: Saturated drain current, I_dss, at second measurement temperature
  summary: 第二测量温度下的饱和漏极电流 I_dss -2.3 mA（默认）
  group: 温度依赖性
- name: Second measurement temperature
  summary: 第二测量温度 125 degC（默认）
  group: 温度依赖性
- name: Energy gap, EG
  summary: 能隙 1.11 eV（默认）
  group: 温度依赖性
- name: Saturation current temperature exponent, XTI
  summary: 饱和电流温度指数 3（默认）
  group: 温度依赖性
- name: Gate threshold voltage temperature coefficient, dVt0/dT
  summary: 栅极阈值电压温度系数 1 mV/K（默认）
  group: 温度依赖性
- name: Mobility temperature exponent, BEX
  summary: 迁移率温度指数 -1.5（默认）
  group: 温度依赖性
- name: Device simulation temperature
  summary: 器件仿真温度 25 degC（默认）
  group: 温度依赖性
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对产生的热量和器件温度效应进行建模。

### 主

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify from a datasheet` — 提供模块将其转换为描述晶体管的方程的参数。这是默认方法。
- `Specify using equation parameters directly` —
  直接提供方程参数 *β*、*IS*、
  *Vt0* 和 *λ*。

### **Gate reverse current, I\_gss** — 栅极反向电流 `5` `nA`（默认）

当漏极和源极短路并施加大正向栅源电压时，二极管中流过的反向电流。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Saturated drain current, I\_dss** — 饱和漏极电流 `-3` `mA`（默认）

在指定的栅源电压下施加大负漏源电压时流过的电流。对于耗尽型器件，此栅源电压可以为零，此时 *I\_dss* 可称为零栅压漏极电流。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **I\_dss measurement point, [V\_gs V\_ds]** — I\_dss 测量点 `[ 0 -15 ]` `V`（默认）

测量 *I\_dss* 时的 *VGS* 和
*VDS* 值向量。通常 *VGS* 为零。
*VDS* 应小于零。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Small-signal parameters, [g\_fs g\_os]** — 小信号参数 `[ 2.5e+3 75 ]` `uS`（默认）

*g\_fs* 和 *g\_os* 的值向量。
*g\_fs* 是正向转移电导，即在固定漏源电压下的电导。*g\_os* 是输出电导，即在固定栅源电压下的电导。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Small-signal measurement point [V\_gs V\_ds]** — 小信号测量点 `[ 0 -15 ]` `V`（默认）

测量 *g\_fs* 和
*g\_os* 时的 *VGS* 和
*VDS* 值向量。*VDS* 应小于零。对于耗尽型器件，*VGS*
通常为零。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Transconductance parameter** — 跨导参数 `1e-04` `A/V2`（默认）

漏极电流对栅极电压的导数。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Saturation current** — 饱和电流 `1e-14` `A`（默认）

理想二极管方程在非常大的反向偏置水平下渐近逼近的电流幅值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Threshold voltage** — 阈值电压 `2` `V`（默认）

晶体管产生非零漏极电流时的栅源电压。对于增强型器件，Vt0 应为负值。对于耗尽型器件，Vt0 应为正值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Channel-length modulation** — 沟道长度调制 `0` `1/V`（默认）

沟道长度调制。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

数据手册参数所对应的温度。

### 欧姆电阻

### **Source ohmic resistance** — 源极欧姆电阻 `0.0001` `Ohm`（默认）| 非负标量

晶体管源极电阻。

### **Drain ohmic resistance** — 漏极欧姆电阻 `0.01` `Ohm`（默认）| 非负标量

晶体管漏极电阻。

### 结电容

### **Parameterization** — 结电容参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify from a datasheet` — 提供模块将其转换为结电容值的参数。这是默认方法。
- `Specify using equation parameters directly` —
  直接提供结电容参数。

### **Input capacitance, Ciss** — 输入电容 `5` `pF`（默认）

漏极短接到源极时的栅源电容。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Reverse transfer capacitance, Crss** — 反向传输电容 `1` `pF`（默认）

源极接地时的漏栅电容。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Gate-source junction capacitance** — 栅源结电容 `4` `pF`（默认）

放置在栅极和源极之间的电容值。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Gate-drain junction capacitance** — 栅漏结电容 `1` `pF`（默认）

放置在栅极和漏极之间的电容值。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

选择以下方法之一进行温度依赖性参数化：

- `None — Simulate at parameter measurement
  temperature` — 不对温度依赖性建模。这是默认方法。
- `Model temperature dependence` — 对温度相关效应建模。根据模块参数化方法，您还需要提供一组附加参数。如果从数据手册对模块进行参数化，则必须提供第二测量温度下的 *I\_gss* 和
  *I\_dss* 值。如果通过直接指定方程参数进行参数化，则必须提供
  *EG*、*XTI* 以及栅极阈值电压温度系数
  *d**Vt0*/*d**T* 的值。
  无论采用何种模块参数化方法，您还必须提供
  *BEX* 和仿真温度
  *Ts* 的值。

### **Gate reverse current, I\_gss, at second measurement temperature** — 第二测量温度下的栅极反向电流 I\_gss `950` `nA`（默认）

在第二测量温度下且 *I\_gss* 测量点与 **Main** 选项卡上 **Gate reverse current, I\_gss** 参数所定义相同时，栅极反向电流 *I\_gss* 的值。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Saturated drain current, I\_dss, at second measurement temperature** — 第二测量温度下的饱和漏极电流 I\_dss `-2.3` `mA`（默认）

在第二测量温度下且 *I\_dss* 测量点与 **Main** 选项卡上 **I\_dss measurement point, [V\_gs V\_ds]** 参数所定义相同时，饱和漏极电流 *I\_dss* 的值。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

测量 **Gate reverse current, I\_gss, at second measurement temperature** 和 **Saturated
drain current, I\_dss, at second measurement temperature** 时的第二温度 *Tm2*。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify from a
datasheet` 时，此参数才可见。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

能隙值。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

饱和电流温度系数值。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Gate threshold voltage temperature coefficient, dVt0/dT** — 栅极阈值电压温度系数 `1` `mV/K`（默认）

栅极阈值电压随温度的变化率。

#### 依赖关系

仅当在 **Main** 选项卡上为 **Parameterization** 参数选择 `Specify using equation
parameters directly` 时，此参数才可见。

### **Mobility temperature exponent, BEX** — 迁移率温度指数 `-1.5`（默认）

迁移率温度系数值。对于大多数 JFET，可以使用默认值。有关其他注意事项，请参阅假设和限制部分。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

仿真器件时的温度 *Ts*。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2019b：热网络 simlog 路径

从 R2019b 开始，可以在内部或外部对此模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您有以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

P 沟道结型场效应晶体管

P-Channel JFET 模块使用 Shichman 和 Hodges 方程来表示 P 沟道 JFET，其模型结构如下：

G 是晶体管栅极，D 是晶体管漏极，S 是晶体管源极。漏极电流 *ID* 取决于工作区域以及晶体管是工作在正常模式还是反向模式。

- 在正常模式下（–*VDS* ≥ 0），模块提供漏极电流
  *ID* 与漏源电压
  *VDS* 之间的以下关系。

  | 区域 | *VGS* 和 *VDS* 值的适用范围 | 对应的 *ID* 方程 |
  | --- | --- | --- |
  | 截止 | –*VGS* ≤ –*Vt0* | *ID* = 0 |
  | 线性 | 0 < –*VDS* < –*VGS* + *Vt0* | *ID* = *β**VDS*(2(–*VGS* + *Vt0*) + *VDS*)(1 – *λ**VDS*) |
  | 饱和 | 0 < –*VGS* + *Vt0* ≤ –*VDS* | *ID* = –*β*(–*VGS* + *Vt0*)2 (1 – *λ**VDS*) |
- 在反向模式下（–*VDS* < 0），模块提供漏极电流
  *ID* 与漏源电压
  *VDS* 之间的以下关系。

  | 区域 | *VGS* 和 *VDS* 值的适用范围 | 对应的 *ID* 方程 |
  | --- | --- | --- |
  | 截止 | –*VGD* ≤ –*Vt0* | *ID* = 0 |
  | 线性 | 0 < *VDS* < – *VGD* + *Vt0* | *ID* = *β**VDS*(2(–*VGD* + *Vt0*) – *VDS*)(1 + *λ**VDS*) |
  | 饱和 | 0 < –*VGD* + t0*V* ≤*VDS* | *ID* = *β*(–*VGD* + *Vt0*)2 (1 + *λ**VDS*) |

在上述方程中：

- *VGS* 是栅源电压。
- *VGD* 是栅漏电压。
- *Vt0* 是阈值电压。如果您为
  **Parameterization** 参数选择
  `Specify using equation parameters directly`，
  则 *Vt0* 为 **Threshold voltage**
  参数值。否则，模块根据您指定的数据手册参数计算 *Vt0*。
- *β* 是跨导参数。如果您为
  **Parameterization** 参数选择
  `Specify using equation parameters directly`，则 *β* 为
  **Transconductance parameter** 参数值。否则，模块
  根据您指定的数据手册参数计算 *β*。
- *λ* 是沟道长度调制参数。如果您为
  **Parameterization** 参数选择
  `Specify using equation parameters directly`，则 *λ* 为
  **Channel-length modulation** 参数值。否则，模块
  根据您指定的数据手册参数计算 *λ*。

每个二极管中的电流满足指数二极管方程

IGD=−IS⋅(e−qVGD/kTm1−1)

IGS=−IS⋅(e−qVGS/kTm1−1)

其中：

- *IS* 是饱和电流。如果您为 **Parameterization**
  参数选择 `Specify using
  equation parameters directly`，则 **IS** 为 **Saturation
  current** 参数值。否则，模块根据您指定的数据手册参数计算
  **IS**。
- *q* 是电子的基本电荷（1.602176e–19
  库仑）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *Tm1* 是测量温度。该值
  来自 **Measurement temperature** 参数。

模块将栅极结电容建模为固定的栅漏电容
*CGD* 和固定的栅源电容
*CGS*。如果您为 **Parameterization**
参数选择 `Specify using
equation parameters directly`，则使用 **Gate-drain junction
capacitance** 和 **Gate-source junction capacitance** 参数直接指定这些值。
否则，模块从 **Input capacitance Ciss** 和
**Reverse transfer capacitance Crss** 参数值推导它们。这两种
参数化的关系如下：

- *CGD* = *Crss*
- *CGS* = *Ciss* –
  *Crss*

### 温度依赖建模

默认行为是不对温度依赖进行建模，器件在您提供模块参数时所对应的温度下进行仿真。您可以选择在仿真期间包含晶体管静态行为对温度依赖的建模。结电容的温度依赖不被建模，因为其影响要小得多。

当包含温度依赖时，晶体管定义方程保持不变。测量温度值 *Tm1* 被替换为仿真温度 *Ts*。跨导 *β* 和阈值电压 *Vt0* 根据以下方程成为温度的函数：

βTs=βTm1(TsTm1)BEX

*Vt0s* =
*Vt01* + *α* (
*Ts* – *Tm1*)

其中：

- *Tm1* 是晶体管参数被指定时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *βTm1* 是测量温度下的 JFET 跨导。
- *βTs* 是仿真温度下的 JFET 跨导。这是当温度依赖被建模时在 JFET 方程中使用的跨导值。
- *Vt01* 是测量温度下的阈值电压。
- *Vt0s* 是仿真温度下的阈值电压。这是当温度依赖被建模时在 JFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**V*th/*d**T*。

对于大多数 JFET，您可以使用 `-1.5` 作为 *BEX* 的默认值。一些数据手册给出了 *α* 的值，但最常见的是它们提供饱和漏极电流 *I\_dss* 的温度依赖关系。根据模块参数化方法，您有两种方式指定 *α*：

- 如果您从数据手册对模块进行参数化，您必须提供第二个测量温度下的 *I\_dss*。模块随后基于此数据计算 *α* 的值。
- 如果您通过指定方程参数进行参数化，您必须直接提供 *α* 的值。

如果您有更多数据，包括在多个温度下绘制的固定漏源电压下漏极电流作为栅源电压的函数，那么您还可以使用 Simulink® Design Optimization™ 软件来帮助调整 *α* 和 *BEX* 的值。

此外，栅漏和栅源电流方程中的饱和电流项 *IS* 取决于温度

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

其中：

- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是当温度依赖被建模时在栅极二极管方程中使用的饱和电流值。。
- *EG* 是能隙。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *XTI* 是饱和电流温度指数。

与 *α* 类似，您有两种方式指定 *EG* 和 *XTI*：

- 如果您从数据手册对模块进行参数化，您必须指定第二个测量温度下的栅极反向电流 *I\_gss*。模块随后基于此数据计算 *EG* 的值，并假设 *XTI* 的 p-n 结标称值为 `3`。
- 如果您通过指定方程参数进行参数化，您必须直接提供 *EG* 和 *XTI* 的值。此选项为您提供最大的灵活性来匹配器件行为，例如，如果您有 *I\_gss* 作为温度函数的图表。有了这些数据，您可以使用 Simulink Design Optimization 软件来帮助调整 *EG* 和 *XTI* 的值。

### 热端口

您可以暴露热端口来对生成的热量和器件温度的影响进行建模。要暴露热端口，将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口，也不对器件中的热量生成进行仿真。
- `Show thermal port` — 模块包含一个热端口，允许您对传导损耗生成的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 P-Channel JFET 模块的基本 I-V 特性。使用这些图来探索您的参数选择对器件特性的影响。如果您从数据手册对模块进行参数化，您可以将您的图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造部件，您可以将您的图与数据手册进行比较以帮助您做出决定。

要启用此选项，将 P-Channel JFET 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，右键单击模块并从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
