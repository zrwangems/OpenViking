---
type: simulink-block
title: 'N-Channel JFET'
family: 'semiconductors-converters'
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

### 守恒

### **G** — 栅极端子（电气）

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子（电气）

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子（电气）

与晶体管源极端子关联的电气守恒端口。

### **H** — 热端口（热）

热守恒端口。

#### 依赖项

要启用此端口，请将 **建模选项** 设置为 `Show thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口，并对产生的热量和设备温度的影响建模。

### 主

### **参数化** — 模块参数化 `Specify from a datasheet` (默认) | `Specify using equation parameters directly`

为模块参数化选择以下方法之一：

- `Specify from a datasheet`
  — 提供模块将其转换为描述晶体管的方程的参数。这是默认方法。
- `Specify using equation parameters
  directly` — 直接提供方程参数 *β*、*IS*、
  *V*t0 和
  *λ*。

### **栅极反向电流, I\_gss** — 栅极反向电流 `-1` `nA` (默认)

当漏极和源极短接且施加大的负栅源电压时，流过二极管的反向电流。

#### 依赖项

仅当为**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **饱和漏极电流, I\_dss** — 饱和漏极电流 `3` `mA` (默认)

当针对指定的栅源电压施加大的正漏源电压时，流过的电流。对于耗尽型器件，此栅源电压可以为零，在这种情况下，*I\_dss* 可称为零栅压漏极电流。

#### 依赖项

仅当为**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **I\_dss 测量点, [V\_gs V\_ds]** — I\_dss 测量点 `[0, 15]` `V` (默认)

由测量 *I\_dss* 时所使用的
*V*GS 和
*V*DS 值组成的向量。通常
*V*GS 为零。
*V*DS 应大于零。

#### 依赖项

仅当为**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **小信号参数, [g\_fs g\_os]** — 小信号参数 `[3000, 10]` `uS``uS` (默认)

由 *g\_fs* 和
*g\_os* 值组成的向量。*g\_fs* 是正向转移电导，即固定漏源电压下的电导。*g\_os* 是输出电导，即固定栅源电压下的电导。

#### 依赖项

仅当为**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **小信号测量点, [V\_gs V\_ds]** — 小信号测量点 `[0, 15]` `V` (默认)

由测量
*V*GS 和
*V*DS 时所使用的
*g\_fs* 和 *g\_os* 值组成的向量。
*V*DS 应大于零。对于耗尽型器件，
*V*GS 通常为零。

#### 依赖项

仅当为**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **跨导参数** — 跨导参数 `6.2e-4` `AV2` (默认)

漏极电流关于栅极电压的导数。

#### 依赖项

仅当为**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **饱和电流** — 饱和电流 `5e-10` `A` (默认)

对于非常大的反向偏置水平，理想二极管方程渐近趋近的电流幅值。

#### 依赖项

仅当为**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **阈值电压** — 阈值电压 `-2.3` `V` (默认)

高于该栅源电压时，晶体管产生非零漏极电流。对于增强型器件，Vt0 应为正。对于耗尽型器件，Vt0 应为负。

#### 依赖项

仅当为**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **沟道长度调制** — 沟道长度调制 `0.003` `1/V` (默认)

沟道长度调制。

#### 依赖项

仅当为**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **测量温度** — 测量温度 `25` `degC` (默认)

数据表参数所依据的温度。

### 欧姆电阻

### **源极欧姆电阻** — 源极欧姆电阻 `0.0001` `Ohm` (默认) | 非负标量

晶体管源极电阻。

### **漏极欧姆电阻** — 漏极欧姆电阻 `0.01` `Ohm` (默认) | 非负标量

晶体管漏极电阻。

### 结电容

### **参数化** — 结电容参数化 `Specify from a datasheet` (默认) | `Specify using equation parameters directly`

为模块参数化选择以下方法之一：

- `Specify from a datasheet`
  — 提供模块将其转换为结电容值的参数。这是默认方法。
- `Specify using equation parameters
  directly` — 直接提供结电容参数。

### **输入电容, Ciss** — 输入电容 `4.5` `pF` (默认)

漏极短接到源极时的栅源电容。

#### 依赖项

仅当在**结电容**选项卡中为
**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **反向传输电容, Crss** — 反向传输电容 `1.5` `pF` (默认)

源极连接到地时的漏栅电容。

#### 依赖项

仅当在**结电容**选项卡中为
**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **栅源结电容** — 栅源结电容 `3` `pF` (默认)

放置在栅极和源极之间的电容值。

#### 依赖项

仅当在**结电容**选项卡中为
**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **栅漏结电容** — 栅漏结电容 `1.5` `pF` (默认)

放置在栅极和漏极之间的电容值。

#### 依赖项

仅当在**结电容**选项卡中为
**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### 温度依赖性

### **参数化** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature` (默认) | `Model temperature dependence`

为温度依赖性参数化选择以下方法之一：

- `None — Simulate at parameter
  measurement temperature` —
  不对温度依赖性建模。这是默认方法。
- `Model temperature dependence`
  — 对温度相关效应建模。还必须根据模块参数化方法提供一组附加参数。如果从数据表参数化模块，则必须提供第二测量温度下的
  *I\_gss* 和 *I\_dss* 值。如果通过直接指定方程参数进行参数化，则必须提供
  *EG*、
  *XTI* 以及栅极阈值电压温度系数
  *d**Vt0*/*d**T* 的值。
  无论采用哪种模块参数化方法，还必须提供 *BEX* 以及仿真温度
  *T*s 的值。

### **第二测量温度下的栅极反向电流, I\_gss** — 第二测量温度下的栅极反向电流 `-200` `nA` (默认)

第二测量温度下的栅极反向电流 *I\_gss* 的值。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **第二测量温度下的饱和漏极电流, I\_dss** — 第二测量温度下的饱和漏极电流 `2.5` `mA` (默认)

第二测量温度下的饱和漏极电流 *I\_dss* 的值，且此时
*I\_dss* 测量点与
**主**选项卡上的 **I\_dss 测量点, [V\_gs V\_ds]** 参数所定义的相同。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **第二测量温度** — 第二测量温度 `125` `degC` (默认)

测量 **第二测量温度下的栅极反向电流, I\_gss** 和 **第二测量温度下的饱和漏极电流, I\_dss** 时的第二温度 *Tm2*。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify from a datasheet` 时，此参数才可见。

### **能隙, EG** — 能隙 `1.11` `eV` (默认)

能隙值。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **饱和电流温度指数, XTI** — 饱和电流温度指数 `3` (默认)

饱和电流温度系数值。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **栅极阈值电压温度系数, dVt0/dT** — 栅极阈值电压温度系数 `-2` `mV/K` (默认)

栅极阈值电压随温度的变化率。

#### 依赖项

仅当在**主**选项卡上为
**参数化**参数选择
`Specify using equation parameters
directly` 时，此参数才可见。

### **迁移率温度指数, BEX** — 迁移率温度指数 `-1.5` (默认)

迁移率温度系数值。对于大多数 JFET，可以使用默认值。有关其他注意事项，请参见假设和限制部分。

### **设备仿真温度** — 设备仿真温度 `25` `degC` (默认)

对设备进行仿真时的温度 *Ts*。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2019b: 热网络 simlog 路径

从 R2019b 开始，可以在内部或外部对本模块的热网络建模。

因此，对应于热网络的 simlog 路径已更改。
如果您有一个以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

N 沟道结型场效应晶体管

N-Channel JFET 模块使用 Shichman 和 Hodges 方程，通过具有以下结构的模型表示 N-Channel JFET：

G 是晶体管栅极，D 是晶体管漏极，S 是晶体管源极。
漏极电流 *I*D 取决于工作区域以及晶体管工作在正常模式还是反向模式。

- 在正常模式下（*V*DS ≥
  0），模块提供漏极电流 *I*D 与
  漏源电压
  *V*DS 之间的以下关系。

  | 区域 | *V*GS 和 *V*DS 值的适用范围 | 对应的 *I*D 方程 |
  | --- | --- | --- |
  | 截止 | *V*GS – *V*t0 ≤ 0 | *I*D = 0 |
  | 线性 | 0 < *V*DS < *V*GS – *V*t0 | *I*D = *β**V*DS(2(*V*GS – *V*t0) – *V*DS)(1 + *λ**V*DS) |
  | 饱和 | 0 < *V*GS – *V*t0 ≤ *V*DS | *I*D = *β*(*V*GS – *V*t0)2 (1 + *λ**V*DS) |
- 在反向模式下（*V*DS <
  0），模块提供漏极电流 *I*D 与
  漏源电压
  *V*DS 之间的以下关系。

  | 区域 | *V*GS 和 *V*DS 值的适用范围 | 对应的 *I*D 方程 |
  | --- | --- | --- |
  | 截止 | *V*GD – *V*t0 ≤ 0 | *I*D = 0 |
  | 线性 | 0 < –*V*DS < *V*GD – *V*t0 | *I*D = *β**V*DS(2(*V*GD – *V*t0) + *V*DS)(1 – *λ**V*DS) |
  | 饱和 | 0 < *V*GD – *V*t0 ≤ –*V*DS | *I*D = *β*(*V*GD – *V*t0)2 (1 – *λ**V*DS) |

在前述方程中：

- *VGS* 是栅源电压。
- *VGD* 是栅漏电压。
- *Vt0* 是阈值电压。如果为 **参数化** 参数选择 `Specify using equation parameters
  directly`，则 *V*t0 是
  **阈值电压** 参数值。否则，模块根据您指定的数据表参数计算 *Vt0*。
- *β* 是跨导参数。如果为 **参数化** 参数选择
  `Specify using equation parameters directly`，
  则 *β* 是 **跨导参数** 参数值。否则，模块根据您指定的数据表参数计算
  *β*。
- *λ* 是沟道长度调制参数。如果为 **参数化** 参数选择
  `Specify using equation parameters directly`，
  则 *λ* 是 **沟道长度调制** 参数值。否则，模块根据您指定的数据表参数计算
  *λ*。

每个二极管中的电流满足指数二极管方程

IGD=IS⋅(eqVGDkTm1−1)

IGS=IS⋅(eqVGSkTm1−1)

其中：

- *IS* 是饱和电流。如果为 **参数化** 参数选择
  `Specify using equation parameters directly`，
  则 **IS** 是 **饱和电流** 参数值。否则，模块根据您指定的数据表参数计算
  **IS**。
- *q* 是电子的基本电荷（1.602176e–19
  Coulombs）。
- *k* 是 Boltzmann 常数（1.3806503e–23 J/K）。
- *Tm1* 是测量温度。
  该值来自 **测量温度**
  参数。

模块将栅极结电容建模为固定的栅漏电容
*CGD* 和固定的栅源电容 *CGS*。如果为
**参数化**参数选择
`Specify using equation parameters directly`，则使用 **栅漏结电容** 和 **栅源结电容** 参数直接指定这些值。否则，模块根据
**输入电容 Ciss** 和 **反向传输电容 Crss** 参数值推导它们。这两种参数化的关系如下：

- *CGD* =
  *Crss*
- *CGS* = *Ciss* –
  *Crss*

### 温度依赖性建模

默认行为是不对温度依赖性建模，器件在您提供模块参数的温度下仿真。您可以选择在仿真期间包括对晶体管静态行为温度依赖性的建模。结电容的温度依赖性不建模，因为该效应小得多。

当包括温度依赖性时，晶体管定义方程保持不变。测量温度值 *Tm1* 替换为仿真温度 *Ts*。跨导 *β* 和阈值电压 *Vt0* 根据以下方程成为温度的函数：

βTs=βTm1(TsTm1)BEX

*Vt0s* =
*Vt01* + *α* (
*Ts* –
*Tm1*)

其中：

- *Tm1* 是规定晶体管参数时的温度，由 **Measurement temperature** 参数值定义。
- *Ts* 是仿真温度。
- *βTm1* 是测量温度下的 JFET 跨导。
- *βTs* 是仿真温度下的 JFET 跨导。这是在建模温度依赖性时 JFET 方程中使用的跨导值。
- *Vt01* 是测量温度下的阈值电压。
- *Vt0s* 是仿真温度下的阈值电压。这是在建模温度依赖性时 JFET 方程中使用的阈值电压值。
- *BEX* 是迁移率温度指数。*BEX* 的典型值为 -1.5。
- *α* 是栅极阈值电压温度系数，*d**Vth*/*d**T*。

对于大多数 JFETS，您可以使用 *BEX* 的默认值 `-1.5`。一些数据手册会给出 *α* 的值，但最常见的是提供饱和漏电流 *I\_dss* 的温度依赖性。根据模块参数化方法，您有两种指定 *α* 的方式：

- 如果您通过数据手册参数化模块，则必须在第二个测量温度下提供 *I\_dss*。然后模块基于此数据计算 *α* 的值。
- 如果您通过指定方程参数来参数化，则必须直接提供 *α* 的值。

如果您有更多数据，包括在多个温度下绘制的固定漏源电压下漏电流作为栅源电压函数的数据，则还可以使用 Simulink® Design Optimization™ 软件帮助调整 *α* 和 *BEX* 的值。

此外，栅漏和栅源电流方程中的饱和电流项 *IS* 取决于温度

ISTs=ISTm1⋅(Ts/Tm1)XTI⋅exp(−EGkTs(1−Ts/Tm1))

其中：

- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是在建模温度依赖性时栅极二极管方程中使用的饱和电流值。
- *EG* 是能隙。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *XTI* 是饱和电流温度指数。

与 *α* 类似，您有两种指定 *EG* 和 *XTI* 的方式：

- 如果您通过数据手册参数化模块，则必须在第二个测量温度下指定栅极反向电流 *I\_gss*。然后模块基于此数据并假设 p-n 结的 *XTI* 标称值为 `3` 来计算 *EG* 的值。
- 如果您通过指定方程参数来参数化，则必须直接提供 *EG* 和 *XTI* 的值。此选项为您提供最大的灵活性来匹配器件行为，例如，如果您有 *I\_gss* 随温度变化的图。利用这些数据，您可以使用 Simulink Design Optimization 软件帮助调整 *EG* 和 *XTI* 的值。

### 热端口

您可以暴露热端口来建模生成的热和器件温度的影响。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口，也不仿真器件中的热生成。
- `Show thermal port` — 该模块包含一个热端口，允许您对传导损耗生成的热进行建模。为了数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅半导体中的热效应仿真。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅按标称值进行系统缩放。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 N-Channel JFET 模块的基本 I-V 特性。使用这些绘图来探索参数选择对器件特性的影响。如果您通过数据手册参数化模块，则可以将绘图与数据手册进行比较，以检查模块参数化是否正确。如果您有一个完整可用的模型但不知道使用哪个制造部件，则可以将绘图与数据手册进行比较以帮助决定。

要启用此选项，请将 N-Channel JFET 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅绘制半导体模块的基本 I-V 特性。
