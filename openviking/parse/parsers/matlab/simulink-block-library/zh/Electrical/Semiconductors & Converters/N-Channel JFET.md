---
type: simulink-block
title: 'N-Channel JFET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'nchanneljfet'
documentation_source_path: 'ref/nchanneljfet.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Channel JFET

## 端口

### 守恒端口

### **G** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对生成的热量和器件温度的影响进行建模。

### 主

### **Parameterization** — 模块参数化 `Specify from a datasheet`（默认）| `Specify using equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify from a datasheet`
  — 提供模块将其转换为描述晶体管的方程的参数。这是默认
  方法。
- `Specify using equation parameters
  directly` — 直接提供方程
  参数 *β*、*IS*、
  *V*t0 和
  *λ*。

### **Gate reverse current, I\_gss** — 栅极反向电流 `-1` `nA`（默认）

当漏极和源极短路并施加较大负栅源电压时，流过二极管的反向电流。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Saturated drain current, I\_dss** — 饱和漏极电流 `3` `mA`（默认）

在指定的栅源电压下施加较大正漏源电压时流过的电流。对于耗尽型
器件，此栅源电压可能为零，此时
*I\_dss* 可称为零栅压
漏极电流。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **I\_dss measurement point, [V\_gs V\_ds]** — I\_dss 测量点 `[0, 15]` `V`（默认）

测量 *I\_dss* 时的
*V*GS 和
*V*DS 值组成的向量。通常
*V*GS 为零。
*V*DS 应大于
零。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Small-signal parameters, [g\_fs g\_os]** — 小信号参数 `[3000, 10]` `uS``uS`（默认）

*g\_fs* 和
*g\_os* 值组成的向量。*g\_fs* 是正向
转移电导，即在固定漏源电压下的电导。*g\_os* 是输出电导，即在
固定栅源电压下的电导。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Small-signal measurement point, [V\_gs V\_ds]** — 小信号测量点 `[0, 15]` `V`（默认）

测量 *g\_fs* 和 *g\_os* 时的
*V*GS 和
*V*DS 值组成的向量。
*V*DS 应大于
零。对于耗尽型器件，
*V*GS 通常为
零。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Transconductance parameter** — 跨导参数 `6.2e-4` `AV2`（默认）

漏极电流对栅极电压的导数。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Saturation current** — 饱和电流 `5e-10` `A`（默认）

在非常大的反向偏置水平下，理想二极管方程渐近趋近的电流
幅值。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Threshold voltage** — 阈值电压 `-2.3` `V`（默认）

晶体管产生非零漏极电流时的栅源电压。对于增强型器件，Vt0 应为正值。对于
耗尽型器件，Vt0 应为负值。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Channel-length modulation** — 沟道长度调制 `0.003` `1/V`（默认）

沟道长度调制。

#### 依赖关系

仅当为 **Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

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

- `Specify from a datasheet`
  — 提供模块将其转换为
  结电容值的参数。这是默认
  方法。
- `Specify using equation parameters
  directly` — 直接提供结
  电容参数。

### **Input capacitance, Ciss** — 输入电容 `4.5` `pF`（默认）

漏极短接到源极时的栅源电容。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为
**Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Reverse transfer capacitance, Crss** — 反向传输电容 `1.5` `pF`（默认）

源极接地时的漏栅电容。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为
**Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Gate-source junction capacitance** — 栅源结电容 `3` `pF`（默认）

放置在栅极和源极之间的电容值。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为
**Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Gate-drain junction capacitance** — 栅漏结电容 `1.5` `pF`（默认）

放置在栅极和漏极之间的电容值。

#### 依赖关系

仅当在 **Junction Capacitance** 选项卡中为
**Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

选择以下方法之一进行温度依赖性参数化：

- `None — Simulate at parameter
  measurement temperature` —
  不对温度依赖性建模。这是默认
  方法。
- `Model temperature dependence`
  — 对温度相关效应建模。根据
  模块参数化方法，您还必须提供一组附加参数。如果从
  数据手册对模块进行参数化，则必须提供
  第二测量温度下的
  *I\_gss* 和 *I\_dss* 值。如果通过
  直接指定方程参数进行参数化，则必须提供
  *EG*、
  *XTI* 和栅极阈值电压
  温度系数
  *d**Vt0*/*d**T* 的值。
  无论采用何种模块参数化方法，您还必须
  提供 *BEX* 和
  仿真温度
  *T*s 的值。

### **Gate reverse current, I\_gss, at second measurement temperature** — 第二测量温度下的栅极反向电流 `-200` `nA`（默认）

第二测量温度下的栅极反向电流 *I\_gss* 值。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Saturated drain current, I\_dss, at second measurement temperature** — 第二测量温度下的饱和漏极电流 `2.5` `mA`（默认）

第二测量温度下的饱和漏极电流 *I\_dss* 值，且
*I\_dss* 测量点与 **Main** 选项卡中
**I\_dss measurement point, [V\_gs V\_ds]** 参数
所定义的相同。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `degC`（默认）

测量 **Gate reverse current, I\_gss, at second measurement
temperature** 和 **Saturated drain current, I\_dss,
at second measurement temperature** 时的第二温度
*Tm2*。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify from a datasheet` 时，此参数才可见。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

能隙值。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

饱和电流温度系数值。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Gate threshold voltage temperature coefficient, dVt0/dT** — 栅极阈值电压温度系数 `-2` `mV/K`（默认）

栅极阈值电压随温度的变化率。

#### 依赖关系

仅当在 **Main** 选项卡中为
**Parameterization** 参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **Mobility temperature exponent, BEX** — 迁移率温度指数 `-1.5`（默认）

迁移率温度系数值。对于大多数 JFET，可以使用默认值。
有关其他注意事项，请参阅假设和限制
部分。

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

从 R2019b 起，可以在内部或外部对此模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。
如果您有以编程方式访问 simlog 的脚本，则必须手动
更新它以反映这些更改。

## 描述

N 沟道结型场效应晶体管

N-Channel JFET 模块使用 Shichman 和 Hodges
方程来表示 N 沟道 JFET，其模型结构如下：

G 是晶体管栅极，D 是晶体管漏极，S 是晶体管源极。
漏极电流 *I*D 取决于工作区域
以及晶体管工作在正常模式还是反向模式。

- 在正常模式下（*V*DS ≥
  0），模块提供以下漏极电流 *I*D 与
  漏源电压
  *V*DS 之间的关系。

  | 区域 | *V*GS 和 *V*DS 值的适用范围 | 对应的 *I*D 方程 |
  | --- | --- | --- |
  | 截止 | *V*GS – *V*t0 ≤ 0 | *I*D = 0 |
  | 线性 | 0 < *V*DS < *V*GS – *V*t0 | *I*D = *β**V*DS(2(*V*GS – *V*t0) – *V*DS)(1 + *λ**V*DS) |
  | 饱和 | 0 < *V*GS – *V*t0 ≤ *V*DS | *I*D = *β*(*V*GS – *V*t0)2 (1 + *λ**V*DS) |
- 在反向模式下（*V*DS <
  0），模块提供以下漏极电流 *I*D 与
  漏源电压
  *V*DS 之间的关系。

  | 区域 | *V*GS 和 *V*DS 值的适用范围 | 对应的 *I*D 方程 |
  | --- | --- | --- |
  | 截止 | *V*GD – *V*t0 ≤ 0 | *I*D = 0 |
  | 线性 | 0 < –*V*DS < *V*GD – *V*t0 | *I*D = *β**V*DS(2(*V*GD – *V*t0) + *V*DS)(1 – *λ**V*DS) |
  | 饱和 | 0 < *V*GD – *V*t0 ≤ –*V*DS | *I*D = *β*(*V*GD – *V*t0)2 (1 – *λ**V*DS) |

在上述方程中：

- *VGS* 是栅源
  电压。
- *VGD* 是栅漏
  电压。
- *Vt0* 是阈值电压。如果
  为 **Parameterization** 参数选择 `Specify using equation parameters
  directly`，则 *V*t0 为
  **Threshold voltage** 参数值。否则，
  模块根据您指定的数据手册参数计算 *Vt0*。
- *β* 是跨导参数。如果为 **Parameterization** 参数选择
  `Specify using equation parameters directly`，
  则 *β* 为 **Transconductance
  parameter** 参数值。否则，模块根据您指定的数据手册参数计算
  *β*。
- *λ* 是沟道长度调制参数。如果为
  **Parameterization** 参数选择 `Specify using equation parameters directly`，
  则 *λ* 为 **Channel-length
  modulation** 参数值。否则，模块根据您指定的数据手册参数计算
  *λ*。

每个二极管中的电流满足指数二极管方程

IGD=IS⋅(eqVGDkTm1−1)

IGS=IS⋅(eqVGSkTm1−1)

其中：

- *IS* 是饱和电流。如果为
  **Parameterization** 参数选择
  `Specify using equation parameters directly`，
  则 **IS** 为 **Saturation
  current** 参数值。否则，模块根据您指定的数据手册参数
  计算 **IS**。
- *q* 是电子的基本电荷（1.602176e–19
  库仑）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *Tm1* 是测量温度。
  该值来自 **Measurement temperature**
  参数。

模块将栅极结电容建模为固定的栅漏电容
*CGD* 和固定的栅源
电容 *CGS*。如果为
**Parameterization** 参数选择
`Specify using equation parameters directly`，则直接使用
**Gate-drain junction capacitance** 和 **Gate-source
junction capacitance** 参数指定这些值。否则，模块从
**Input capacitance Ciss** 和 **Reverse transfer
capacitance Crss** 参数值推导它们。这两种参数化的关系
如下：

- *CGD* =
  *Crss*
- *CGS* = *Ciss* –
  *Crss*

### 温度依赖性建模

默认行为是不对温度依赖性进行建模，器件在您提供模块参数的温度下进行仿真。您可以选择在仿真期间包含晶体管静态行为对温度的依赖性建模。不建模结电容的温度依赖性，因为其影响要小得多。

当包含温度依赖性时，晶体管定义方程保持不变。测量温度值 *Tm1* 被替换为仿真温度 *Ts*。跨导 *β* 和阈值电压 *Vt0* 根据以下方程变为温度的函数：

βTs=βTm1(TsTm1)BEX

*Vt0s* = *Vt01* + *α* ( *Ts* – *Tm1*)

其中：

- *Tm1* 是晶体管参数被指定时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *βTm1* 是测量温度下的 JFET 跨导。
- *βTs* 是仿真温度下的 JFET 跨导。这是当温度依赖性被建模时在 JFET 方程中使用的跨导值。
- *Vt01* 是测量温度下的阈值电压。
- *Vt0s* 是仿真温度下的阈值电压。这是当温度依赖性被建模时在 JFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**Vth*/*d**T*。

对于大多数 JFET，您可以使用 *BEX* 的默认值 `-1.5`。一些数据手册给出了 *α* 的值，但最常见的是它们提供饱和漏极电流 *I\_dss* 的温度依赖性。根据模块参数化方法，您有两种指定 *α* 的方式：

- 如果您从数据手册参数化模块，您必须提供第二个测量温度下的 *I\_dss*。模块然后基于此数据计算 *α* 的值。
- 如果您通过指定方程参数进行参数化，您必须直接提供 *α* 的值。

如果您有更多数据，包括在多个温度下绘制的固定漏源电压下漏极电流作为栅源电压的函数，那么您还可以使用 Simulink® Design Optimization™ 软件来帮助调整 *α* 和 *BEX* 的值。

此外，栅漏和栅源电流方程中的饱和电流项 *IS* 取决于温度

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

其中：

- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是当温度依赖性被建模时在栅极二极管方程中使用的饱和电流值。
- *EG* 是能隙。
- *k* 是玻尔兹曼常数 (1.3806503e–23 J/K)。
- *XTI* 是饱和电流温度指数。

与 *α* 类似，您有两种指定 *EG* 和 *XTI* 的方式：

- 如果您从数据手册参数化模块，您必须指定第二个测量温度下的栅极反向电流 *I\_gss*。模块然后基于此数据并假设 p-n 结标称值为 `3` 的 *XTI* 来计算 *EG* 的值。
- 如果您通过指定方程参数进行参数化，您必须直接提供 *EG* 和 *XTI* 的值。此选项为您提供最大的灵活性来匹配器件行为，例如，如果您有 *I\_gss* 作为温度函数的图表。有了这些数据，您可以使用 Simulink Design Optimization 软件来帮助调整 *EG* 和 *XTI* 的值。

### 热端口

您可以暴露热端口来建模生成的热量和器件温度的影响。要暴露热端口，将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口，也不仿真器件中的热量生成。
- `Show thermal port` — 模块包含一个热端口，允许您对传导损耗生成的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口和 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 N-Channel JFET 模块的基本 I-V 特性。使用这些图来探索您的参数选择对器件特性的影响。如果您从数据手册参数化模块，您可以将您的图与数据手册进行比较，以检查您是否正确参数化了模块。如果您有一个完整的工作模型但不知道使用哪个制造部件，您可以将您的图与数据手册进行比较以帮助您做出决定。

要启用此选项，将 N-Channel JFET 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，右键单击模块并从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
