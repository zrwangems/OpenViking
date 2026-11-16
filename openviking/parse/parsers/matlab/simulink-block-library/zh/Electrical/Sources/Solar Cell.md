---
type: simulink-block
title: 'Solar Cell'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'solarcell'
documentation_source_path: 'ref/solarcell.html'
language: zh-CN
chinese_source: worker-translation
---

# Solar Cell

## 端口

### 输入

### **Ir** — 入射辐照度物理信号

与太阳能电池入射辐照度关联的物理信号。

### 守恒

### **+** — 正电压电气

与太阳能电池正电压关联的电气守恒端口。

### **-** — 负电压电气

与太阳能电池负电压关联的电气守恒端口。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Selected part** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商组件的选项。单击 **<click to select>** 超链接打开 Block Parameterization Manager 窗口。有关 Block Parameterization Manager 的更多信息，请参阅 Load Predefined Parameterizations。

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并对生成的热和设备温度的影响进行建模。

### 电池特性

此设置中的所有量均针对单个电池。

### **Parameterize by** — 模块参数化 `By s/c current and o/c voltage, 5 parameter`（默认） | `By equivalent circuit parameters, 5 parameter` | `By equivalent circuit parameters, 8 parameter`

选择以下模块参数化方法之一：

- `By s/c current and o/c voltage, 5
  parameter` — 提供短路电流和开路电压，模块将其转换为太阳能电池的等效电路模型。
- `By equivalent circuit parameters, 5
  parameter` — 使用 5-parameter 太阳能电池模型为太阳能电池的等效电路模型提供电气参数，该模型做出以下假设：

  - 第二个二极管的饱和电流为零。
  - 并联电阻具有无限阻抗。
- `By equivalent circuit parameters, 8
  parameter` — 使用 8-parameter 太阳能电池模型为太阳能电池的等效电路模型提供电气参数。

### **Short-circuit current, Isc** — 短路电流 `7.34` `A`（默认）

短路太阳能电池时流过的电流。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By s/c
current and o/c voltage, 5 parameter` 时，此参数才可见。

### **Open-circuit voltage, Voc** — 开路电压 `0.6` `V`（默认）

太阳能电池未连接时其两端的电压。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By s/c
current and o/c voltage, 5 parameter` 时，此参数才可见。

### **Diode saturation current, Is** — 第一个二极管饱和电流 `1e-6` `A`（默认）

在没有任何入射光的情况下，随着反向偏置增加，第一个二极管的渐近反向电流。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 5 parameter` 或
`By equivalent circuit parameters, 8
parameter` 时，此参数才可见。

### **Diode saturation current, Is2** — 第二个二极管饱和电流 `0` `A`（默认）

在没有任何入射光的情况下，随着反向偏置增加，第二个二极管的渐近反向电流。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 8 parameter` 时，此参数才可见。

### **Solar-generated current for measurements, Iph0** — 测量用太阳能产生电流 `7.34` `A`（默认）

当辐照度为 *Ir0* 时的太阳能感应电流。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 5 parameter` 或
`By equivalent circuit parameters, 8
parameter` 时，此参数才可见。

### **Irradiance used for measurements, Ir0** — 测量用辐照度 `1000` `W/m2`（默认）

在太阳能电池中产生 *Iph0* 电流的辐照度。

### **Quality factor, N** — 第一个二极管发射系数 `1.5`（默认）

第一个二极管的发射系数。

### **Quality factor, N2** — 第二个二极管发射系数 `2`（默认）

第二个二极管的发射系数。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 8 parameter` 时，此参数才可见。

### **Series resistance, Rs** — 串联电阻 `0` `Ohm`（默认）

内部串联电阻。

### **Parallel resistance, Rp** — 并联电阻 `inf` `Ohm`（默认）

内部并联电阻。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 8 parameter` 时，此参数才可见。

### 面板配置

### **Number of series-connected cells per string** — 每串串联太阳能电池数 `1`（默认） | 正标量

模块建模的每串串联太阳能电池数。该值必须大于 `0`。

### **Number of parallel-connected strings** — 并联串数 `1`（默认） | 正标量

并联连接的串数。该值必须大于 `0`。

### 温度依赖性

### **First order temperature coefficient for Iph, TIPH1** — Iph 的一阶温度系数 `0` `1/K`（默认） | 非负标量

随着温度升高，太阳能产生电流线性增加的阶数。该值必须大于或等于 `0`。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

太阳能电池激活能。该值必须大于或等于 0.1。

### **Temperature exponent for Is, TXIS1** — Is 的温度指数 `3`（默认） | 正标量

随着温度升高，第一个二极管电流指数增加的阶数。该值必须大于 `0`。

### **Temperature exponent for Is2, TXIS2** — Is2 的温度指数 `3`（默认） | 非负标量

随着温度升高，第二个二极管电流指数增加的阶数。该值必须大于或等于 `0`。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 8 parameter` 时，此参数才可见。

### **Temperature exponent for Rs, TRS1** — Rs 的温度指数 `0`（默认）

随着温度升高，串联电阻指数增加的阶数。该值必须大于或等于 `0`。

### **Temperature exponent for Rp, TRP1** — Rp 的温度指数 `0`（默认） | 非负标量

随着温度升高，并联电阻指数增加的阶数。该值必须大于或等于 `0`。

#### 依赖项

仅当您为 **Parameterize by** 参数选择 `By
equivalent circuit parameters, 8 parameter` 时，此参数才可见。

### **Measurement temperature** — 测量温度 `25` `degC`（默认） | 正标量

测量太阳能电池参数时的温度。该值必须大于 `0`。

### **Device simulation temperature** — 设备仿真温度 `25` `degC`（默认） | 正标量

仿真太阳能电池时的温度。该值必须大于 `0`。

### 热端口

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal mass per cell** — 每电池热质量 `100` `J/K`（默认）

将单个太阳能电池温度升高一度所需的热能。当对多个串联电池建模时，请指定单个电池的热质量。该值在内部乘以电池数量，以确定总热质量。

### **Initial temperature** — 初始温度 `25` `degC`（默认）

仿真开始时太阳能电池的温度。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024b: 生成数字数据表

现在，您可以使用 MATLAB live script 为 Solar Cell 模块生成数字数据表，其中包括电流-电压 (I-V) 和功率-电压 (P-V) 曲线。该脚本从您在模型中选择的 Solar Cell 模块导入参数。您可以使用这些特性曲线来评估最大功率点跟踪 (MPPT) 输出，因为这些曲线有助于识别不同辐照度和电池温度下的峰值功率。

## 描述

光伏太阳能电池

Solar Cell 模块表示太阳能电池电流源。

太阳能电池模型包括以下组件：

- 太阳能感应电流
- 温度依赖性
- 预定义参数化
- 热端口
- 生成数字数据表

### 太阳能感应电流

该模块将单个太阳能电池表示为电阻 *Rs*，其与以下元素的并联组合串联：

- 电流源
- 两个指数二极管
- 并联电阻 *Rp*

以下插图显示等效电路图：

输出电流 *I* 为

I=Iph−Is\*(e(V+I\*Rs)/(N\*Vt)−1)−Is2\*(e(V+I\*Rs)/(N2\*Vt)−1)−(V+I\*Rs)/Rp

其中：

- *Iph* 是太阳能感应电流：

  Iph=Iph0×IrIr0

  其中：

  - *Ir* 是辐照度（光强），单位为 W/m2，照射在电池上。
  - *Iph0* 是在辐照度 *Ir0* 下测得的太阳能产生电流。
- *Is* 是第一个二极管的饱和电流。
- *Is2* 是第二个二极管的饱和电流。
- *Vt* 是热电压，*kT/q*，其中：

  - *k* 是 Boltzmann 常数。
  - *T* 是 **Device simulation temperature** 参数值。
  - *q* 是电子上的基本电荷。
- *N* 是第一个二极管的品质因数（二极管发射系数）。
- *N2* 是第二个二极管的品质因数（二极管发射系数）。
- *V* 是太阳能电池电气端口两端的电压。

品质因数因非晶电池而异，对于多晶电池通常为 `2`。

该模块允许您在两种模型之间选择：

- 一个 8-parameter 模型，其中前述方程描述输出电流
- 一个 5-parameter 模型，其对前述方程应用以下简化假设：

  - 第二个二极管的饱和电流为零。
  - 并联电阻的阻抗为无限。

如果选择 5-parameter 模型，您可以按前述等效电路模型参数对该模块进行参数化，或者按模块用来推导这些参数的短路电流和开路电压进行参数化。

所有模型都根据温度调整模块的电阻和电流参数。

通过将参数 **Number of series-connected cells per string** 设置为大于 1 的值，您可以使用单个 Solar Cell 模块对任意数量的串联太阳能电池建模。在内部，模块仍然只模拟单个太阳能电池的方程，但会根据电池数量按比例放大输出电压。与单独模拟每个电池的方程相比，这会实现更高效的仿真。

### 温度依赖性

若干太阳能电池参数取决于温度。太阳能电池温度由 **Device simulation temperature** 参数值指定。

该模块提供太阳能感应电流 *Iph* 与太阳能电池温度 *T* 之间的以下关系：

Iph(T)=Iph\*(1+TIPH1\*(T−Tmeas))

其中：

- *TIPH1* 是 **First order temperature coefficient for Iph, TIPH1** 参数值。
- *Tmeas* 是 **Measurement temperature** 参数值。

该模块提供第一个二极管的饱和电流 *Is* 与太阳能电池温度 *T* 之间的以下关系：

Is(T)=Is\*(TTmeas)(TXIS1N)\*e(EG\*(TTmeas−1)/(N\*Vt))

其中 *TXIS1* 是 **Temperature exponent for Is, TXIS1** 参数值。

该模块提供第二个二极管的饱和电流 *Is2* 与太阳能电池温度 *T* 之间的以下关系：

Is2(T)=Is2\*(TTmeas)(TXIS2N2)\*e(EG\*(TTmeas−1)/(N2\*Vt))

其中 *TXIS2* 是 **Temperature exponent for Is2, TXIS2** 参数值。

该模块提供串联电阻 *Rs* 与太阳能电池温度 *T* 之间的以下关系：

Rs(T)=Rs\*(TTmeas)TRS1

其中 *TRS1* 是 **Temperature exponent for Rs, TRS1** 参数值。

该模块提供并联电阻 *Rp* 与太阳能电池温度 *T* 之间的以下关系：

Rp(T)=Rp\*(TTmeas)TRP1

其中 *TRP1* 是 **Temperature exponent for Rp, TRP1** 参数值。

### 预定义参数化

Solar Cell 模块有多个可用的内置参数化。

此预参数化数据允许您设置模块以表示特定供应商的组件。这些太阳能电池模块的参数化与制造商数据表匹配。要加载预定义参数化，请双击 Solar Cell 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape™ 组件的预定义参数化使用可用的数据源来获取参数值。工程判断和简化假设用于填补缺失数据。因此，预计仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

有关预参数化以及可用组件列表的更多信息，请参阅 List of Pre-Parameterized Components。

### 热端口

您可以公开热端口，以对生成的热和设备温度的影响进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 该模块不包含热端口，也不模拟设备中的热量生成。
- `Show thermal port` — 该模块包含一个热端口，允许您对传导损耗生成的热进行建模。为提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

以下插图所示的热端口模型仅表示设备的热质量。热质量直接连接到组件热端口 **H**。一个内部 Ideal Heat Flow Source 模块向端口和热质量提供热流。该热流表示内部生成的热。

太阳能电池内部生成的热根据参考页开头“太阳能感应电流”部分中所示的等效电路图计算。它是每个电阻的 *i*2 · *R* 损耗加上每个二极管中的损耗之和。

由电损耗引起的内部生成热是与太阳辐照不同的加热效应。要对太阳辐照引起的热加热建模，必须在模型中单独考虑它，并将热流添加到连接到太阳能电池热端口的物理节点。

### Generate Digital Datasheet

*自 R2024b 起*

为 Solar Cell 模块生成数字数据手册，包括电流-电压
(I-V) 和功率-电压 (P-V) 曲线，使用 MATLAB® 实时脚本。该脚本从您
在模型中选择的 Solar Cell 模块导入参数。您可以使用这些特性曲线来评估
最大功率点跟踪 (MPPT) 输出，因为这些曲线有助于识别
不同辐照度水平和电池温度下的峰值功率。要打开
MATLAB 实时脚本：

1. 双击该模块以打开 **模块参数** 窗口。
2. 打开 **描述** 选项卡。
3. 点击 `Generate datasheet` 超链接。

要生成数据手册，请在实时脚本中点击 `Generate
Datasheet` 按钮。
