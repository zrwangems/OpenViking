---
type: simulink-block
title: 'Diode'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'diode'
documentation_source_path: 'ref/diode.html'
language: zh-CN
chinese_source: worker-translation
---

# Diode

## 端口

### 守恒

### **+** — 正极端子（电气）

与阳极相关联的电气守恒端口。

### **-** — 负极端子（电气）

与阴极相关联的电气守恒端口。

### **H** — 热端口（热）

热守恒端口。

#### 依赖关系

要启用此端口，请将 **建模选项** 设置为 `Show
thermal port`。

## 参数

### **建模选项** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口并对生成的热量和设备温度的影响进行建模。

### **选定部件** — 预定义参数化选项 `<click to select>`（默认）

用于将模块参数化以表示特定供应商的组件的选项。单击
**<click to select>** 超链接以打开 Block
Parameterization Manager 窗口。有关 Block Parameterization
Manager 的详细信息，请参阅 Load Predefined Parameterizations。

### 主要

### **保真度级别** — 保真度级别 `Include capacitance and charge dynamics`（默认） | `Ideal switching`

二极管动态模型的详细程度。如果选择 `Ideal
switching`，模块仅对反向恢复损耗进行建模。如果选择
`Include capacitance and charge dynamics`，模块会对结电容和电荷动态进行建模。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Show
thermal port`。

### **二极管模型** — 二极管模型 `Piecewise Linear`（默认） | `Exponential` | `Tabulated I-V curve`

选择以下二极管模型之一：

- `Piecewise Linear` — 对二极管使用分段线性模型，如 Piecewise Linear Diode 中所述。这是默认方法。
- `Exponential` — 对二极管使用标准指数模型，如 Exponential Diode 中所述。
- `Tabulated I-V curve` — 使用表格化的正向偏置 I-V 数据以及固定的反向偏置断态电导，如 Tabulated Diode 中所述。

### **表类型** — 表格化函数 `Table in If(Tj,Vf) form`（默认） | `Table in Vf(Tj,If) form`

是将电流表示为温度和电压的函数，还是将电压
表示为温度和电流的函数。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Tabulated I-V curve`。

### **正向电压** — 正向电压 `0.6` `V`（默认）

使二极管变为正向偏置所需施加的最小电压。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Piecewise linear`。

### **导通电阻** — 导通电阻 `0.3` `Ohm`（默认）

二极管正向偏置时的电阻。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Piecewise linear`。

### **断态电导** — 断态电导 `1e-8` `1/Ohm`（默认）

二极管反向偏置时的电导。当清除 **齐纳二极管建模**
参数时，模块使用此值确定反向 I-V 特性。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Piecewise linear` 或 `Tabulated I-V
curve`。

### **参数化** — 模型参数化 `Use two I-V curve data points`（默认） | `Use parameters IS and N` | `Use an I-V data point and IS` | `Use an I-V data point and N`

选择以下模型参数化方法之一：

- `Use two I-V curve data points` — 指定二极管 I-V 曲线上两个点的测量数据。这是默认方法。
- `Use parameters IS and N` — 指定饱和电流和发射系数。
- `Use an I-V data point and IS` — 指定二极管 I-V 曲线上单个点的测量数据并结合饱和电流。
- `Use an I-V data point and N` — 指定二极管 I-V 曲线上单个点的测量数据并结合发射系数。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`。

### **电流 [I1 I2]** — 两个点处的电流值向量 `[.0137, .545]` `A`（默认）

二极管 I-V 曲线上两个点处的电流值向量，模块使用这些值计算 *IS* 和 *N*。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use two I-V curve data points`。

### **电压 [V1 V2]** — 两个点处的电压值向量 `[.6, .7]` `V`（默认）

二极管 I-V 曲线上两个点处的电压值向量，模块使用这些值计算 *IS* 和 *N*。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use two I-V curve data points`。

### **饱和电流 IS** — 饱和电流 `1e-12` `A`（默认）

对于非常大的反向偏置水平，理想二极管方程渐近逼近的电流大小。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use parameters IS and N` 或 `Use an I-V data point
and IS`。

### **发射系数 N** — 二极管发射系数 `1`（默认）

二极管发射系数或理想因子。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use parameters IS and N` 或 `Use an I-V data point
and N`。

### **电流 I1** — 电流值 `0.0137` `A`（默认）

二极管 I-V 曲线上模块用于计算的点的电流值。
根据 **参数化** 的值，模块使用此参数
计算 *N* 或 *IS*。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use an I-V data point and IS` 或 `Use an I-V data
point and N`。

### **电压 V1** — 电压值 `0.6` `V`（默认）

二极管 I-V 曲线上模块用于计算的点的电压值。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`，并将 **参数化** 设置为
`Use an I-V data point and IS` 或 `Use an I-V data
point and N`。

### **欧姆电阻 RS** — 欧姆电阻 `0` `Ohm`（默认）

串联二极管连接电阻。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Exponential`。

### **测量温度** — 测量温度 `298.15` `K`（默认）

测量 IS 或 I-V 曲线时的温度 *Tm1*。

### **正向电流 If(Tj,Vf)** — 正向电流向量 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认） | 非负向量

正向电流。此参数必须为至少包含三个非负元素
且按升序排列的向量。零点可选（*If(Tj,Vf)* = 0A）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
If(Tj,Vf) form`。

### **正向电压 Vf(Tj,If)** — 正向电压向量 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认） | 非负向量

正向电压。此参数必须为至少包含三个非负元素
且按升序排列的向量。零点可选（*Vf(Tj,If)* = 0V）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
Vf(Tj,If) form`。

### **结温 Tj** — 结温向量 `[25, 125]` `degC`（默认）

结温向量。

如果向量的大小等于 `1`，则二极管特性
不依赖于温度。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Tabulated I-V curve`。

### **正向电压 Vf** — 正向电压向量 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认）

正向电压向量。此参数必须为至少包含三个
非负元素且按升序排列的向量。零点可选（*Vf* =
0V）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
If(Tj,Vf) form`。

### **正向电流 If** — 正向电流向量 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）

正向电流向量。此参数必须为至少包含三个
非负元素且按升序排列的向量。零点可选（*If* =
0A）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
Vf(Tj,If) form`。

### **反向电流 Ir(Tj,Vr)** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认） | 非负向量

*自 R2024a 起*

反向电流。此参数必须为至少包含三个非负元素
且按升序排列的向量。零点可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
If(Tj,Vf) form` 并选中 **齐纳二极管建模**
参数。

### **反向电压 Vr** — 反向电压向量 `[10, 20, 40, 50, 70, 80, 100]` `V`（默认）

*自 R2024a 起*

反向电压向量。此参数必须为至少包含三个
非负元素且按升序排列的向量。零点可选（*Vr* =
0V）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
If(Tj,Vf) form` 并选中 **齐纳二极管建模**
参数。

### **反向电压 Vr(Tj,Ir)** — 反向电压向量 `[10, 100, 200, 250, 300, 325, 350; 10, 70, 160, 220, 270, 300, 320]` `V`（默认） | 非负向量

*自 R2024a 起*

反向电压。此参数必须为至少包含三个非负元素
且按升序排列的向量。零点可选（*Vr(Tj,Ir)* = 0V）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
Vf(Tj,If) form` 并选中 **齐纳二极管建模**
参数。

### **反向电流 Ir** — 反向电流向量 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）

*自 R2024a 起*

反向电流向量。此参数必须为至少包含三个
非负元素且按升序排列的向量。零点可选（*Ir* =
0A）。

#### 依赖关系

要启用此参数，请将 **表类型** 设置为 `Table in
Vf(Tj,If) form` 并选中 **齐纳二极管建模**
参数。

### **串联二极管数** — 串联连接的二极管数 `1`（默认）

在 **+** 和
**–** 模块端口之间串联连接的二极管数。不会对多个二极管进行建模。相反，每个二极管的所有电压相关量都按您指定的因子进行缩放。

### **并联二极管数** — 并联二极管数 `1`（默认）

在 **+** 和 **–** 模块端口之间的并联二极管数，或由串联连接的二极管形成的并联路径数。不会
对多个二极管进行建模。相反，每个二极管的所有电流相关量都按您指定的因子进行缩放。

### **齐纳二极管建模** — 为齐纳二极管建模的选项 `Off`（默认） | `On`

*自 R2023b 起*

为齐纳二极管建模的选项。

选择此参数以对在正向和反向偏置方向上导通的齐纳二极管进行建模。模块图标显示齐纳二极管的电子符号，并且您可以在 **击穿** 选项卡中启用这些参数。必须为 **反向击穿电压** 参数指定有限值。

选择此选项后，您可以通过指定新的 **反向电压 Vr(Tj,Ir)**、**反向电流 Ir(Tj,Vr)**、**反向电压 Vr** 和 **反向电流 Ir**
参数来为 Diode 模块的反向 I-V 特性建模。*（自 R2024a 起）*

清除此参数以对仅在单个方向上导通的标准二极管进行建模。
模块假定反向击穿电压为无穷大，从而有效地从模型中省略反向击穿。模块图标显示标准二极管的电子符号。

### 击穿

要启用这些参数，请选中 **齐纳二极管建模**
参数。

### **齐纳电阻** — 齐纳电阻 `0.3` `Ohm`（默认） | 正标量

当电压小于 **反向击穿电压** 值时二极管的电阻。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Piecewise linear`。

### **反向击穿电压** — 反向击穿电压 `inf` `V`（默认） | 正标量

低于该反向电压时，对二极管击穿时发生的电导快速增加进行建模。

#### 依赖关系

要启用此参数，请将 **二极管模型** 设置为
`Piecewise linear` 或
`Exponential`。

### 电容

要启用这些参数，请将 **建模选项** 设置为 `No
thermal port`，或将 **保真度级别** 设置为 `Include
capacitance and charge dynamics`。

### **参数化** — 为结电容建模 `Fixed or zero junction capacitance`（默认） | `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

为结电容建模的方法：

- `Fixed or zero junction capacitance` — 将结电容建模为固定值。
- `Use C-V curve data points` — 指定二极管 C-V 曲线上三个点的测量数据。
- `Use parameters CJ0, VJ, M & FC` — 指定零偏结电容、结电位、梯度系数和正向偏置耗尽电容系数。

### **结电容** — 结电容 `0` `pF`（默认）

固定结电容值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为
`Fixed or zero junction capacitance`。

### **反向偏置电压 [VR1 VR2 VR3]** — 反向偏置电压值向量 `[.1, 10, 100]` `V`（默认）

二极管 C-V 曲线上三个点处的反向偏置电压值向量，模块使用这些值计算 *CJ0*、*VJ* 和 *M*。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
C-V curve data points`。

### **对应电容 [C1 C2 C3]** — 电容值向量 `[3.5, 1, .4]` `pF`（默认）

二极管 C-V 曲线上三个点处的电容值向量，模块使用这些值计算 *CJ0*、*VJ* 和 *M*。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
C-V curve data points`。

### **零偏结电容 CJ0** — 零偏结电容 `5` `pF`（默认）

与传导电流项并联的电容值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **结电位 VJ** — 结电位 `1` `V`（默认）

结电位。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **梯度系数 M** — 梯度系数 `0.5`（默认）

梯度系数。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **电容系数 FC** — 电容系数 `0.5`（默认）

拟合系数，用于量化耗尽电容随施加电压的增加而减小的程度。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
parameters CJ0, VJ, M & FC`。

### **电荷动态** — 电荷动态参数化 `Do not model charge dynamics`（默认） | `Use peak reverse current and stretch factor` | `Use peak reverse current and reverse recovery time` | `Use peak reverse current and reverse recovery charge` | `Use peak reverse current and reverse recovery energy` | `Use transit time and carrier lifetime`

选择以下电荷动态参数化方法之一：

- `Do not model charge dynamics` — 不包括电荷动态建模。这是默认方法。
- `Use peak reverse current and stretch factor` — 通过提供峰值反向电流 *iRM* 和拉伸因子 *λ* 的值，以及在测试电路中测量 *iRM* 和 *trr* 时所用的初始正向电流和电流变化率信息，来对电荷动态建模。
- `Use peak reverse current and reverse recovery time` — 通过提供峰值反向电流 *iRM* 和反向恢复时间 *trr* 的值，以及在测试电路中测量 *iRM* 和 *trr* 时所用的初始正向电流和电流变化率信息，来对电荷动态建模。如果制造商数据表未提供渡越时间 *TT* 和载流子寿命 *τ* 的值，请使用此选项。
- `Use peak reverse current and reverse recovery charge` — 通过提供峰值反向电流 *iRM* 和反向恢复电荷 *Qrr* 的值，以及在测试电路中测量 *iRM* 和 *trr* 时所用的初始正向电流和电流变化率信息，来对电荷动态建模。
- `Use peak reverse current and reverse recovery energy` — 通过提供峰值反向电流 *iRM* 和反向恢复能量 *Erec* 的值，以及在测试电路中测量 *iRM* 时所用的初始正向电流和电流变化率信息，来对电荷动态建模。
- `Use transit time and carrier lifetime` — 通过提供渡越时间 *TT* 和载流子寿命 *τ* 的值，来对电荷动态建模。

### **峰值反向电流，iRM** — 峰值反向电流 `-7.15` `A`（默认） | negative scalar

由外部测试电路测得的峰值反向电流。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `4` `A`（默认） | positive scalar

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **测量 iRM 时的电流变化率** — 测量 iRM 时的电流变化率 `-750` `A/μs`（默认） | negative scalar

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and stretch factor`、`Use peak reverse current and reverse recovery time`、`Use peak reverse current and reverse recovery charge` 或 `Use peak reverse current and reverse recovery energy`。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3`（默认）

模块用于计算 **反向恢复时间，trr** 的值。此值必须大于 `1`。默认值为 `3`。

与指定反向恢复电荷相比，指定拉伸因子是一种更简便的反向恢复时间参数化方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and stretch factor`。

### **反向恢复时间，trr** — 反向恢复时间 `115`（默认）

从二极管关断时电流初始降至零的时刻，到电流降至小于峰值反向电流百分之十的时刻之间的时间。默认值为 `115` `ns`。

**反向恢复时间，trr** 参数的值必须大于 **峰值反向电流，iRM** 参数的值除以 **测量 iRM 时的电流变化率** 参数的值。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and reverse recovery time`。

### **反向恢复电荷，Qrr** — 反向恢复电荷 `1500` `s*μA`（默认）

模块用于计算 **反向恢复时间，trr** 的值。如果您的二极管器件数据表指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −iRM²/(2a)，

其中：

- *iRM* 是为 **峰值反向电流，iRM** 指定的值。
- *a* 是为 **测量 iRM 时的电流变化率** 指定的值。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and reverse recovery charge`。

### **测量 Erec 时的二极管关断电压** — 测量 Erec 时的二极管关断电压 `-600` `V`（默认）

稳态时二极管两端的电压。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and reverse recovery energy`。

### **测量 Erec 时的杂散电感** — 测量 Erec 时的杂散电感 `150` `nH`（默认）

测量电路中的总非预期电感。模块使用此值计算 **反向恢复能量，Erec**。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and reverse recovery energy`。

### **反向恢复能量，Erec** — 反向恢复能量 `0.03` `J`（默认）

由于二极管反向恢复引起的总开关损耗。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use peak reverse current and reverse recovery energy`。

### **渡越时间，TT** — 渡越时间 `50` `ns`（默认）

载流子穿过二极管结所需时间的度量。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use transit time and carrier lifetime`。

### **载流子寿命，tau** — 载流子寿命 `100` `ns`（默认）

二极管不再导通后载流子消散所需时间的度量。默认值为 `100` `ns`。

#### 依赖关系

要启用此参数，请将 **电荷动态** 设置为 `Use transit time and carrier lifetime`。

### 反向恢复损耗

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`，并将 **保真度级别** 设置为 `Ideal switching`。

### **反向恢复损耗模型** — 反向恢复损耗的模型 `Fixed loss`（默认） | `Tabulated loss`

是建立固定反向恢复损耗模型还是表格化反向恢复损耗模型。

### **反向恢复损耗** — 反向恢复损耗 `0` `J`（默认） | nonnegative scalar

每次关断事件中耗散的能量，与开关事件前后二极管的状态无关。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Fixed loss`。

### **根据电流和电压缩放反向恢复损耗** — 缩放反向恢复损耗的选项 `On`（默认） | `Off`

*自 R2023b 起*

根据电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Fixed loss`。

### **测量恢复损耗时的正向电流，Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认） | positive scalar

*自 R2023b 起*

在反向恢复事件之前流过二极管的正向电流，模块使用该电流来测量恢复损耗。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **根据电流和电压缩放反向恢复损耗** 参数。

### **测量恢复损耗时的关断电压，Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认） | positive scalar

用于测量恢复损耗的反向恢复事件之后二极管两端的电压。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **根据电流和电压缩放反向恢复损耗** 参数。
- 将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **电压和电流值的滤波器时间常数** — 电压和电流值的滤波器时间常数 `1 / 1000 / 100` `s`（默认） | positive scalar

模块用于计算反向恢复损耗的电压和电流值的滤波器时间常数。将此参数设置为小于最快开关周期的值。

#### 依赖关系

要启用此参数，请从以下选项中选择一项：

- 将 **反向恢复损耗模型** 设置为 `Fixed loss`，并选择 **根据电流和电压缩放反向恢复损耗** 参数。
- 将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`。

### **反向恢复损耗表，Erec(Tj, If)** — 反向恢复损耗 `zeros(2, 3)` `J`（默认） | vector of nonnegative scalars

耗散能量，是开关事件之前紧邻时刻的正向电流 *If* 以及二极管进入关断状态后的最终关断态电压的函数。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Tabulated loss`。

### **恢复损耗表的温度向量，Tj** — 恢复损耗表的温度向量 `[298.15, 398.15]` `K`（默认） | vector

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Tabulated loss`。

### **恢复损耗表的正向电流向量，If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `A`（默认） | vector of nonnegative scalars

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数，请将 **反向恢复损耗模型** 设置为 `Tabulated loss`。

### 温度依赖性

本节仅适用于 `Exponential` 和 `Tabulated I-V curve` 二极管模型。

此表显示了 **温度依赖性** 设置的可见性如何取决于您在 **Main** 设置中配置 **二极管模型** 参数的方式以及是否暴露热端口。要了解如何阅读此表，请参阅参数依赖关系。

**温度依赖性设置的可见性**

| 参数、选项和设置的可见性 | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **二极管模型** | | | | | | | |
| *`Piecewise linear`* | | | | *`Exponential`* | | *`Tabulated I-V curve`* | |
| **热端口** | | | | **热端口** | | **热端口** | |
| *`Not exposed`* | *`Exposed`* | | | *`Not exposed`* | *`Exposed`* | *`Not exposed`* | *`Exposed`* |
| 隐藏 | 隐藏 | | | 可见 | 可见 | 可见 | 隐藏 |

### **参数化** — 温度依赖性参数化 `None - Use characteristics at parameter measurement temperature`（默认） | `Use an I-V data point at second measurement temperature` | `Specify saturation current at second measurement temperature` | `Specify the energy gap EG`

选择以下温度依赖性参数化方法之一：

- `None - Use characteristics at parameter measurement temperature` — 不对温度依赖性建模，或者模型在测量温度 *T*m1 下仿真（如 **Main** 选项卡上的 **测量温度** 参数所指定）。这是默认方法。
- `Use an I-V data point at second measurement temperature T2` — 如果选择此选项，您需要指定第二测量温度 *T*m2，以及该温度下的电流和电压值。模型使用这些值以及第一测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify saturation current at second measurement temperature T2` — 如果选择此选项，您需要指定第二测量温度 *T*m2，以及该温度下的饱和电流值。模型使用这些值以及第一测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify the energy gap EG` — 直接指定能隙值。

### **第二测量温度下的电流 I1** — 第二测量温度下的电流 I1 `0.0245` `A`（默认）

指定在第二测量温度下电压为 *V1* 时的二极管电流 *I1* 值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use an I-V data point at second measurement temperature`。

### **第二测量温度下的电压 V1** — 第二测量温度下的电压 V1 `0.5` `V`（默认）

指定在第二测量温度下电流为 *I1* 时的二极管电压 *V1* 值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use an I-V data point at second measurement temperature`。

### **第二测量温度下的饱和电流，IS** — 第二测量温度下的饱和电流，IS `1.25e-7` `A`（默认）

指定第二测量温度下的饱和电流 *IS* 值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify saturation current at second measurement temperature`。

### **第二测量温度** — 第二测量温度 `125` `°C`（默认）

指定第二测量温度的值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use an I-V data point at second measurement temperature` 或 `Specify saturation current at second measurement temperature`。

### **能隙参数化** — 能隙参数化 `Use nominal value for silicon (EG=1.11eV)`（默认） | `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

从预定义选项列表中选择能隙值，或指定自定义值：

- `Use nominal value for silicon (EG=1.11eV)` — 这是默认值。
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — 如果选择此选项，对话框中会出现 **能隙，EG** 参数，以便您为 *EG* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Specify the energy gap EG`。

### **能隙，EG** — 能隙 `1.11` `eV`（默认）

为能隙 *EG* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **能隙参数化** 设置为 `Specify a custom value`。

### **饱和电流温度指数参数化** — 饱和电流温度指数参数化 `Use nominal value for pn-junction diode (XTI=3)`（默认） | `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

选择以下选项之一来指定饱和电流温度指数值：

- `Use nominal value for pn-junction diode (XTI=3)` —
  这是默认值。
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — 如果选择此选项，
  则 **饱和电流温度指数, XTI** 参数会出现在
  对话框中，以便为 *XTI* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`。

### **饱和电流温度指数, XTI** — 饱和电流温度指数 `3`（默认）

为饱和电流温度指数 *XTI* 指定自定义值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`，并将 **饱和电流温度指数
参数化** 设置为 `Specify a custom value`。

### **反向击穿电压温度系数, dBV/dT** — 反向击穿电压温度系数 `0` `V/K`（默认）

调制反向击穿电压 *BV*。如果将反向击穿电压 *BV* 定义为正值，则
*TCV* 为正值意味着反向击穿电压的幅度随温度降低。

#### 依赖关系

要启用此参数，请选择 **对 Zener 二极管建模** 参数，
并将 **参数化** 设置为 `Use an I-V data point at
second measurement temperature`、`Specify saturation current at
second measurement temperature` 或 `Specify the energy gap,
EG`。

### **器件仿真温度** — 器件仿真温度 `25` `°C`（默认）

指定用于仿真器件的温度 *Ts* 的值。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Use
an I-V data point at second measurement temperature`、`Specify
saturation current at second measurement temperature` 或 `Specify
the energy gap, EG`。

### 故障

### **Diode 故障** — 用于在 Diode 中对故障建模的选项 `Add fault`（默认）

用于在 Diode 模块中对故障建模的选项。

要添加故障，请点击 **添加故障**
超链接。

### **故障模式** — 故障类别 `Open`（默认） | `Short` | `Parameter shift`

指定 Diode 模块的故障模式：

- `Open` — 一旦触发故障，串联
  电阻会瞬时增大。可以使用此类型的故障来对因金属化烧毁而失效的二极管建模。
- `Short` — 一旦触发故障，并联
  电导会瞬时增大。可以使用此选项来对因穿通而失效的二极管建模。
- `Parameter shift` — 从触发故障的那一刻起，
  模块参数随时间变化。可以使用此选项来
  对因老化而失效的二极管建模。

#### 依赖关系

要启用此参数，请通过点击 **Diode 故障**
参数中的 **添加故障** 超链接，向 Diode 模块添加故障。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障过渡时间常数** — 故障过渡时间常数 `1e-3` `s`（默认） | 正标量

过渡到故障状态的时间常数。

#### 依赖关系

要启用此参数，请通过点击 **Diode 故障**
参数中的 **添加故障** 超链接，向 Diode 模块添加故障。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障串联电阻** — 故障串联电阻 `1000` `Ohm`（默认） | 有限非负标量

故障状态下的串联电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **故障模式** 设置为 `Open`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障并联电导** — 故障并联电导 `1000` `1/Ohm`（默认） | 有限非负标量

故障状态下的并联电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **故障模式** 设置为 `Short`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障正向电压** — 故障正向电压 `0.6` `V`（默认） | 正标量

故障状态下的正向电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Piecewise
  linear`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障导通电阻** — 故障导通电阻 `0.3` `Ohm`（默认） | 正标量

故障状态下的导通电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Piecewise
  linear`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障关断电导** — 故障关断电导 `1e-8` `S`（默认） | 正标量

故障状态下的关断电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Piecewise
  linear`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障 Zener 电阻** — 故障 Zener 电阻 `0.3` `Ohm`（默认） | 正标量

故障状态下的关断电导。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Piecewise
  linear`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障反向击穿电压** — 故障反向击穿电压 `inf` `V`（默认） | 正标量

故障状态下的反向击穿电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Piecewise
  linear`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障电流, [I1 I2]** — 故障电流 `[.0137, .545]` `A`（默认） | 正标量的二维向量

故障状态下的 *I1* 和 *I2* 电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use two I-V curve data
  points`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障电压, [V1 V2]** — 故障电压 `[.6, .7]` `V`（默认） | 正标量的二维向量

故障状态下的 *V1* 和 *V2* 电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use two I-V curve data
  points`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障欧姆电阻, RS** — 故障电压 `0` `Ohm`（默认） | 非负标量

故障状态下的欧姆电阻。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障饱和电流, IS** — 故障饱和电流 `1e-12` `A`（默认） | 正标量

故障状态下的饱和电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use parameters IS and
  N` 或 `Use an I-V data point and IS`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障发射系数, N** — 故障发射系数 `1`（默认） | 正标量

故障状态下的发射系数。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use parameters IS and
  N` 或 `Use an I-V data point and N`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障电流, I1** — 故障电流 `0.0137` `A`（默认） | 正标量

故障状态下的电流。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use an I-V data point and
  IS` 或 `Use an I-V data point and N`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障电压, V1** — 故障电压 `0.6` `V`（默认） | 正标量

故障状态下的电压。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为
  `Exponential`。
- 将 **参数化** 设置为 `Use an I-V data point and
  IS` 或 `Use an I-V data point and N`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障正向电流, If(Tj,Vf)** — 故障正向电流 `[.07, .12, .19, 1.75, 4.24, 7.32, 11.2; .16, .3, .72, 2.14, 4.02, 6.35, 9.12]` `A`（默认） | 非负标量的矩阵

故障状态下的正向电流 *If(Tj,Vf)*。此参数必须
是一个至少包含三个非负元素且按升序排列的向量。零点
是可选的（*Ir(Tj,Vr)* = 0A）。

#### 依赖关系

要启用此参数：

- 通过点击 **Diode 故障**
  参数中的 **添加故障** 超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in If(Tj,Vf)
  form`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，将显示
**打开故障检查器** 超链接，而不是 **添加
故障** 超链接。有关展示如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障正向电压, Vf** — 故障正向电压 `[.5, .7, .9, 1.3, 1.7, 2.1, 2.5]` `V`（默认） | 非负标量的向量

故障状态下的正向电压 *Vf*。此参数必须是一个
至少包含三个非负元素且按升序排列的向量。零点
是可选的（*Vf* = 0V）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in If(Tj,Vf)
  form`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障反向电流, Ir(Tj,Vr)** — 故障反向电流 `[1e-06, 2e-06, 5e-06, 1e-05, 2.5e-05, 5e-05, .0001; 2e-06, 5e-06, 1e-05, 4e-05, 8e-05, .0002, .0005]` `A`（默认）| 非负标量矩阵

*自 R2024a 起*

故障状态下的反向电流 *Ir(Tj,Vr)*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*Ir(Tj,Vr)* = 0A）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in If(Tj,Vf)
  form`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障反向电压, Vr** — 故障反向电压 `[1, 2, 4, 5, 7, 8, 10]` `V`（默认）| 非负标量向量

*自 R2024a 起*

故障状态下的反向电压 *Vr*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*Vr* = 0V）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in If(Tj,Vf)
  form`。
- 选择 **对 Zener 二极管建模** 参数。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障正向电压, Vf(Tj,If)** — 故障正向电压 `[.9, 1.15, 1.25, 1.5, 1.75, 2.17, 2.6, 2.85; .58, .68, .75, 1.1, 1.38, 1.77, 2.27, 2.7]` `V`（默认）| 非负标量矩阵

故障状态下的正向电压 *Vf(Tj,If)*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*Vf(Tj,If)* = 0V）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in Vf(Tj,If)
  form`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障正向电流, If** — 故障正向电流 `[.1, .2, .5, 1, 2, 4, 7, 10]` `A`（默认）| 非负标量向量

故障状态下的正向电流 *If*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*If* = 0A）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in Vf(Tj,If)
  form`。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障反向电压, Vr(Tj,Ir)** — 故障反向电压 `[1, 10, 20, 25, 30, 32.5, 35; 1, 5, 10, 20, 25, 30, 32]` `V`（默认）| 非负标量矩阵

*自 R2024a 起*

故障状态下的反向电压 *Vr(Tj,Ir)*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*Vr(Tj,ir)* = 0V）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in Vf(Tj,If)
  form`。
- 选择 **对 Zener 二极管建模** 参数。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障反向电流, Ir** — 故障反向电流 `[1e-06, 2e-06, 5e-06, 1e-05, 2e-05, 5e-05, .0001]` `A`（默认）| 非负标量向量

*自 R2024a 起*

故障状态下的反向电流 *Vr*。此参数必须为至少包含三个非负元素且按升序排列的向量。零点可选（*Ir* = 0A）。

#### 依赖项

要启用此参数：

- 通过点击 **Diode 故障** 参数中的 **添加故障**
  超链接，向 Diode 模块添加故障。
- 将 **Diode 模型** 设置为 `Tabulated I-V
  curve`。
- 将 **表类型** 设置为 `Table in Vf(Tj,If)
  form`。
- 选择 **对 Zener 二极管建模** 参数。
- 将 **故障模式** 设置为 `Parameter
  shift`。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **故障电容与电荷占未故障状态的百分比** — 故障电容与电荷占未故障状态的百分比 `100`（默认）| 有限正标量

故障状态下的电容与电荷占未故障状态的百分比。

#### 依赖项

要启用此参数，请点击 **Diode 故障** 参数中的 **添加故障** 超链接，向 Diode 模块添加故障。

创建故障后，可以在 **故障检查器** 窗口中更改属性。当打开具有故障的模块时，会出现 **打开故障检查器** 超链接，而不是 **添加故障** 超链接。有关如何包含故障的示例，请参阅分析直流电枢绕组故障。

### **在指定时间触发故障** — 进入故障状态前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态时的仿真时间。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Timed`。

### **最大允许反向电压** — 最大允许反向电压 `inf` `V`（默认）| 正标量

超过该值可能触发故障的最大反向电压。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **超过电压时失效的事件数** — 超过电压时失效的事件数 `1`（默认）| 正整数标量

在触发故障之前，二极管必须超过反向电压阈值的次数。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **最大允许电流** — 发生故障转换的电流阈值 `inf` `A`（默认）| 正标量

发生故障转换的电流阈值。如果电流超过此值的时间长于 **超过电流时失效的时间** 参数值，则模块进入故障状态。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **超过电流时失效的时间** — 电流超过阈值的最长持续时间 `1` `s`（默认）| 非负标量

电流可以在不触发故障的情况下超过最大允许值的最长时间。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **最大二极管恢复, dV/dt** — 二极管恢复阈值 `inf` `V/s`（默认）| 正标量

最大二极管恢复。

#### 依赖项

要启用此参数，请将 **触发类型** 设置为 `Behavioral`。

### **最大允许温度** — 发生故障转换的温度阈值 `inf` `K`（默认）| 正标量

最大允许温度值。如果温度超过此值的时间长于 **超过温度时失效的时间** 参数的值，则模块进入故障状态。

#### 依赖项

要启用此参数：

- 在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Behavioral`。
- 将 **Diode 模型** 设置为 `Piecewise Linear`。

此参数出现在 **故障检查器** 窗口的 **触发** 部分。

### **超过温度时失效的时间** — 超过电流时失效的时间 `1` `s`（默认）| 正标量

在触发行为故障之前，温度必须持续超过最大允许温度的时间量。

#### 依赖项

要启用此参数：

- 在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Behavioral`。
- 将 **Diode 模型** 设置为 `Piecewise Linear`。

此参数出现在 **故障检查器** 窗口的 **触发** 部分。

### 热端口

要启用这些参数，请将 **建模选项** 设置为 `Show thermal port`。

有关使用热端口和 **热端口** 参数的详细信息，请参阅半导体热效应仿真。

### **热网络** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

模块热网络的建模选项。

### **热质量参数化** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

热质量参数化选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **结-壳与壳-环境（或壳-散热器）热阻, [R\_JC R\_CA]** — 结-壳与壳-环境（或壳-散热器）热阻 `[0, 10]` `K/W`（默认）| 非负值向量

行向量 [ *R\_JC*
*R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **结与壳热时间常数, [t\_J t\_C]** — 结与壳热时间常数 `[0, 10]` `s`（默认）| 非负值向量

行向量 [ *t\_J*
*t\_C* ]，包含两个热时间常数值。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal time constants`。

### **结与壳热质量, [M\_J M\_C]** — 结与壳热质量 `[0, 1]` `J/K`（默认）| 正值向量

行向量 [ *M\_J*
*M\_C* ]，包含两个热质量值。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **结与壳初始温度, [T\_J T\_C]** — 结与壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

行向量 [ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Specify junction and case thermal parameters`。

### **热阻, [R1 R2 … Rn]** — 热阻 `[1, 3, 10]` `K/W` | `[4, 6]` `K/W` | 正值向量

由 *n* 个热阻值组成的行向量，由热网络中使用的 Cauer 元件表示。

如果将 **热网络** 设置为 `Cauer
model`，默认值为 `[1, 3, 10]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[4, 6]`。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **热质量, [M1 M2 … Mn]** — 热质量 `[.1, .3, 1]` `J/K` | `[1.5, 3]` `J/K` | 正值向量

由 *n* 个热质量值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **热网络** 设置为 `Cauer
model`，默认值为 `[.1, .3, 1]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[1.5, 3]`。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **热质量参数化** 设置为 `By thermal mass`。

### **热质量初始温度, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

由温度值组成的行向量，这些温度值对应于模型中每个热容上的温度降。

#### 依赖项

要启用此参数，请将 **热网络** 设置为 `Cauer model`。

### **热时间常数, [t1 t2 … tn]** — 热时间常数 `[1, 3, 10]` `s` | `[6, 18]` `s` | 正值向量

由 *n* 个热时间常数值组成的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **热阻, [R1 R2 … Rn]** 的长度匹配。
使用此参数化时，模块按 `Mi =
ti/Ri` 计算热质量，其中 `Mi`、`ti`
和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **热网络** 设置为 `Cauer model`）或 Foster 元件（如果将 **热网络** 设置为 `Cauer model
parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **热网络** 设置为 `Cauer
model`，默认值为 `[1, 3, 10]`。如果将 **热网络** 设置为 `Cauer model parameterized with Foster
coefficients`，默认值为 `[6, 18]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Initial node temperatures, [T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

从结开始的每个节点的温度值的行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **Junction thermal mass** — 结的热质量 `0.01` `J/K`（默认）| 正标量

结的热质量。

#### 依赖关系

要启用此参数，请将 **Fidelity level** 设置为 `Ideal switching`，并将 **Thermal network** 设置为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

### R2024a：对表格化的反向 I-V 特性建模

现在，您可以为 Diode 模块对表格化的反向 I-V 特性建模。

要对反向 I-V 特性建模，请选择 **Model Zener diode** 参数，然后指定新的 **Reverse voltages, Vr(Tj,Ir)**、**Reverse currents, Ir(Tj,Vr)**、**Reverse voltages, Vr** 和 **Reverse currents, Ir** 参数。

在 R2024a 之前，只能通过指定反向偏置二极管的关断电导来对反向 I-V 特性建模。

### R2024a：**Junction capacitance voltage** 变量替换为 **Charge of junction capacitance** 变量

如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，则现在使用 **Charge of junction capacitance** 变量为电容和电荷建模指定 **Initial Targets** 和 **Nominal Values**。**Junction capacitance voltage** 变量不再启用。

如果您在较早版本中创建的模型为 **Parameterization** 使用这些值，并为 **Junction capacitance voltage** 变量指定 **Initial Targets** 或 **Nominal Values**，则必须更新该模型。有关如何计算结电容电荷的详细信息，请参阅结电容。

### R2023b：在模块图标中显示齐纳二极管的电子符号

Diode 模块图标现在会根据您建模的是标准二极管还是齐纳二极管显示不同的电子符号。要对齐纳二极管建模，请选择 **Model a Zener diode** 参数，并为 **Reverse breakdown voltage** 参数指定有限值。

在 R2023b 之前，可以通过为 **Reverse breakdown voltage** 参数指定有限值来对齐纳二极管建模，但模块图标显示的是标准二极管的电子符号。要启用 **Reverse breakdown voltage** 参数，请将 **Diode model** 设置为 `Piecewise linear` 或 `Exponential`。

如果您在 R2023b 之前创建模型，并为 **Reverse breakdown voltage** 参数指定有限值，则为了实现向后兼容，模块现在默认启用 **Model a Zener diode** 参数。

### R2023b：随电流和电压缩放反向恢复损耗

现在，您可以随电流和电压缩放固定的反向恢复损耗值。要启用此选项，请选择 **Scale reverse recovery loss with current and voltage** 参数。

对于在 R2023a 或更早版本中创建的模型，为了实现向后兼容，默认不缩放。

### R2023b：使用内置参数化对特定二极管建模

现在，您可以使用表示特定供应商组件的内置参数化来参数化 Diode 模块。这些二极管的参数化与制造商数据表一致。使用这些参数化设置此模块，以复现特定供应商数据表中的正向电压 V-I 曲线。要加载预定义的参数化，请双击 Diode 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

### R2023a：使用单个参数为故障实现时序或行为触发器

**Enable temporal trigger** 和 **Enable behavioral trigger** 参数已移除，并替换为 **Fault trigger** 参数。您可以将 **Fault trigger** 参数设置为 `Temporal` 或 `Behavioral`。只能启用一个触发器。

如果您在较早版本中创建模型并同时启用了时序和行为触发器，则现在仅启用时序触发器。因此，如果行为触发器在您的模型中导致故障，仿真结果将不同。

如果要在特定时间触发故障，请将 **Fault trigger** 参数设置为 `Temporal`。如果要确定系统是否发生故障以及何时发生故障，请将 **Fault Trigger** 参数设置为 `Behavioral`。

## 描述

分段线性、指数或表格化二极管

Diode 模块可表示分段线性二极管、指数二极管或具有表格化 I-V 曲线的二极管。使用 **Fidelity level** 参数选择动态模型中的详细程度。

### 分段线性二极管

分段线性二极管模型与 **Simscape™** > **Foundation Library** > **Electrical** > **Electrical Elements** > **Diode** 模块的模型相同，但额外包含固定结电容和可选的电荷动态。如果二极管正向电压超过 **Forward voltage** 参数中指定的值，则二极管表现为线性电阻，其阻值为 **On resistance** 参数中指定的值。否则，二极管表现为线性电阻，其电导为 **Off conductance** 参数中指定的小电导。二极管两端电压为零时，流过的电流为零。

有关 Simscape Foundation library 中 Diode 模块的详细信息，请参阅 Diode。

### 指数二极管

指数二极管模型表示二极管电流 *I* 与二极管电压 *V* 之间的以下关系：

I=IS⋅(eqVNkTm1−1)   V>−BVI=−IS⋅(e−q(V+Vz)kTm1−eqVNkTm1)  V≤−BV

其中：

- *q* 是电子的基本电荷（1.602176e–19 coulombs）。
- *k* 是玻尔兹曼常数（1.3806503e–23 J/K）。
- *BV* 是 **Reverse breakdown voltage** 参数值。
- *N* 是发射系数。
- *IS* 是饱和电流。
- *Tm1* 是指定二极管参数时的温度，由 **Measurement temperature** 参数值定义。

当 (*q**V* / *N**k**Tm1*) > 80 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* – 79)e80，这与 (*q**V* / *N**k**Tm1*) = 80 处二极管电流的梯度匹配，并进行线性外推。当 (*q**V* / *N**k**Tm1*) < –79 时，模块将 eqVNkTm1 替换为 (*q**V* / *N**k**Tm1* + 80)e–79，这同样匹配梯度并进行线性外推。典型电路不会达到这些极端值。模块提供此线性外推，以帮助在仿真期间求解约束时收敛。

当为 **Parameterization** 参数选择 `Use parameters IS and N` 时，您通过 **Saturation current IS** 和 **Emission coefficient N** 参数指定二极管。当为 **Parameterization** 参数选择 `Use two I-V curve data points` 时，您指定二极管 I-V 曲线上的两个电压和电流测量点，模块推导出 *IS* 和 *N* 值。然后模块按如下方式计算 *IS* 和 *N*：

- N=((V1−V2)/Vt)/(log(I1)−log(I2))
- IS=(I1/(exp(V1/(NVt))−1)+I2/(exp(V2/(NVt))−1))/2

其中：

- *Vt* = *k**Tm1* / *q*。
- *V1* 和 *V2* 是 **Voltages [V1 V2]** 向量中的值。
- *I1* 和 *I2* 是 **Currents [I1 I2]** 向量中的值。

当为 **Parameterization** 参数选择 `Use an I-V data point and IS` 时，模块按如下方式计算 *N*：

N=V1/(Vtlog(I1IS+1))

当为 **Parameterization** 参数选择 `Use an I-V data point and N` 时，模块按如下方式计算 *IS*：

IS=I1/(exp(V1/(NVt)−1))

### 表格化二极管

要对表格化二极管建模，请将 **Diode model** 参数设置为 `Tabulated I-V curve`。下图显示了表格化二极管选项的实现：

如果选择 **Model Zener Diode** 参数，还可以对表格化的反向 I-V 特性建模。*（自 R2024a 起）*

如果未选择 **Model Zener Diode** 参数，则模块使用 **Off conductance** 参数对反向特性建模：

- 如果电压小于 -1 V，则模块使用等于 **Off conductance** 参数值的恒定关断电导对 I-V 关系建模。您指定的值必须小于小正电压下正向 I-V 曲线的梯度。
- 如果电压介于 -1 V 和 0 V 之间，则模块使用 makima 插值，使正向和反向偏置的 I-V 曲线平滑重叠。

模块使用 `makima` 插值查找中间值。如果电压或电流超出表格数据范围，则模块在最后一个电压-电流数据点之后使用线性外推。

### 结电容

Diode 模块仅在将 **Modeling option** 参数设置为 `No thermal port` 或将 **Fidelity level** 参数设置为 `Include capacitance and charge dynamics` 时，才对结电容建模。要包含结电容：

- 为 **Parameterization** 参数选择 `Include fixed or zero junction capacitance`。电容是固定的。
- 为 **Parameterization** 参数选择 `Use parameters CJO, VJ, M & FC`。模块使用系数 *CJO*、*VJ*、*M* 和 *FC* 计算取决于结电压的结电容。
- 为 **Parameterization** 参数选择 `Use C-V curve data points`。模块使用 C-V 电容曲线上的三个电容值来估计 *CJO*、*VJ* 和 *M*，并将这些值与指定的 *FC* 值一起使用，以计算取决于结电压的结电容。模块按如下方式计算 *CJO*、*VJ* 和 *M*：

  - CJ0=C1((VR2−VR1)/(VR2−VR1(C2/C1)−1/M))M
  - VJ=−(−VR2(C1/C2)−1/M+VR1)/(1−(C1/C2)−1/M)
  - M=log(C3/C2)/log(VR2/VR3)

  其中：

  - *VR1*、*VR2* 和 *VR3* 是 **Reverse bias voltages [VR1 VR2 VR3]** 向量中的值。
  - *C1*、*C2* 和 *C3* 是 **Corresponding capacitances [C1 C2 C3]** 向量中的值。

  反向偏置电压（定义为正值）应满足 *VR3* > *VR2* > *VR1*。这意味着电容应满足 *C1* > *C2* > *C3*，因为反向偏置会加宽耗尽层，从而降低电容。违反这些不等式会导致错误。电压 *VR2* 和 *VR3* 应远离结电势 *VJ*。电压 *VR1* 应小于结电势 *VJ*，*VR1* 的典型值为 0.1 V。

电压相关的结电容通过结电容电荷 *Qj* 定义如下：

- 当 *V* < *FC*·*VJ* 时：

  Qj=CJ0⋅(VJ/(M−1))⋅((1−V/VJ)1−M−1)
- 当 *V* ≥ *FC*·*VJ* 时：

  Qj=CJ0⋅F1+(CJ0/F2)⋅(F3⋅(V−FC⋅VJ)+0.5(M/VJ)⋅(V2−(FC⋅VJ)2))

其中：

- F1=(VJ/(1−M))⋅(1−(1−FC)1−M))
- F2=(1−FC)1+M))
- F3=1−FC⋅(1+M)
- *V* 是结电容电压。

这些方程与 [2] 中使用的方程相同，不同之处在于未对 *VJ* 和 *FC* 的温度依赖性建模。

### 电荷动态

Diode 模块仅在将 **建模选项** 参数设置为 `No thermal port` 或将 **保真度级别** 参数设置为 `Include capacitance and charge dynamics` 时才会对电荷动态建模。对于换流二极管等应用，对二极管电荷动态进行建模可能很重要。当正向偏置的二极管两端施加反向电压时，电荷需要一段时间才能消散，因此二极管需要一段时间才能关断。二极管关断所需的时间主要由渡越时间参数体现。一旦二极管关断，任何剩余电荷随后会消散，消散速率由载流子寿命决定。

Diode 模块使用 Lauritzen 和 Ma [3] 的模型来体现这些效应。以下是定义方程。

|  |  |
| --- | --- |
| i=qE−qMTM | **(1)** |

|  |  |
| --- | --- |
| dqMdt+qMτ−qE−qMTM=0 | **(2)** |

|  |  |
| --- | --- |
| qE=(τ+TM)i | **(3)** |

其中：

- *i* 是二极管电流。
- *qE* 是结电荷。
- *qM* 是总存储电荷。
- *TM* 是渡越时间。
- *τ* 是载流子寿命。
- *vD* 是二极管两端电压。
- *vF* 是二极管正向电压。
- *R* 是二极管导通电阻。
- *G* 是二极管关断电导。

下图显示了二极管器件的典型反向模式电流特性。

其中：

- *iRM* 是峰值反向电流。
- *iF* 是测量 *iRM* 时的起始正向电流。
- *a* 是测量 *iRM* 时的电流变化率。
- *trr* 是反向恢复时间。

二极管数据手册会给出在初始正向电流和稳定电流变化率下的峰值反向电流值。数据手册还可能提供反向恢复时间和总恢复电荷的值。

**模块如何计算 *TM* 和 Tau**

模块根据你为 **电荷动态** 参数输入的值计算渡越时间 *TM* 和载流子寿命 *τ*。模块使用 *TM* 和 *τ* 求解电荷动态方程 1、2 和 3。

在反向模式下的初始电流下降期间，二极管仍处于导通状态，电流变化率由外部测试电路决定。

首先，模块使用方程 1 执行此计算。

|  |  |
| --- | --- |
| iF+at=qE−qMTM | **(4)** |

然后，它将方程 4 代入方程 2。

|  |  |
| --- | --- |
| dqMdt+qMτ=iF+at | **(5)** |

然后，它求解方程 5 得到 *qM*，

|  |  |
| --- | --- |
| qM=iFτ−aτ2+kexp(tτ)+aτt, | **(6)** |

其中 *k* 是常数。

当 *t* 为零时，*i* = *iF* 且 *qM* = *τiF*，因为系统处于稳态。

将这些关系代入方程 6 并求解该方程，得到 *k* = *aτ2*。

因此，

|  |  |
| --- | --- |
| qM=iFτ+aτ2(1exp(tτ)−1)+aτt. | **(7)** |

在时间 *t* = *ts* 时，电流为 *iRM*，结电荷 *qE* 为零。

模块将这些值代入方程 1。

|  |  |
| --- | --- |
| iRM=−qMTM | **(8)** |

模块重新整理方程 8 以求解 *qM*，并将结果代入方程 7。

|  |  |
| --- | --- |
| −TMiRM=iFτ+aτ2(1exp(tsτ)−1)+aτts | **(9)** |

然后，模块用 *iRM*、*iF* 和 *a* 表示时间 *ts*。

|  |  |
| --- | --- |
| ts=iRM−iFa | **(10)** |

考虑二极管恢复，即当 *t* > *ts* 时。二极管反向偏置，电流和结电荷实际上为零。

电流由以下方程定义。

|  |  |
| --- | --- |
| i=iRMexp[−(t−ts)τrr], | **(11)** |

其中：

|  |  |
| --- | --- |
| 1τrr=1τ+1TM. | **(12)** |

模块现在将方程 12 中的表达式与反向恢复时间 *trr* 关联起来。

当 t=iFa+trr 时，电流为 iRM10。

因此，

|  |  |
| --- | --- |
| exp(−t−tsτrr)=0.1 | **(13)** |

并且

|  |  |
| --- | --- |
| trr=τrrlog(10)+iRMa. | **(14)** |

模块使用方程 9 和 14 计算 *TM* 和 *τ* 的值。由于方程 9 中存在指数项，该计算使用迭代方案。

**直接指定 *trr* 的替代方法**

除了允许你直接指定反向恢复时间 *trr* 外，模块还支持三种替代参数化方式。模块可以从以下任一参数推导 *trr*：

- 反向恢复时间拉伸因子 *λ*
- 反向恢复电荷 *Qrr*，当数据手册指定此值而不是反向恢复时间时。
- 反向恢复能量 *Erec*，当数据手册指定此值而不是反向恢复时间时。

反向恢复时间拉伸因子 *λ* 与 *trr* 之间的关系由以下方程表示

λ=trraiRM.

反向恢复时间必须大于 iRMa，典型值为 3(iRMa)。

因此，*λ* 的典型值为 3。*λ* 必须大于 1。

反向恢复电荷 *Qrr* 是反向电流从变为负值到衰减回零期间对时间的积分。

初始电荷，到时间 ts 为止（如图所示），由以下方程表示：

|  |  |
| --- | --- |
| Qs=12(−iRM)iRMa. | **(15)** |

对方程 11 积分得到时间 ts 与 inf 之间的电荷。该电荷等于

τrriRM.

因此，总反向恢复电荷由以下方程给出：

|  |  |
| --- | --- |
| Qrr=−iRM22a−τrriRM. | **(16)** |

重新整理方程 16 以求解 *τrr*，并将结果代入方程 14，得到用 *Qrr* 表示 *trr* 的方程：

trr=(QrriRM+iRM2a)log(10)+iRMa.

或者，模块使用反向恢复能量 *Erec* 计算 *τrr*。以下方程定义二极管电压曲线：

|  |  |
| --- | --- |
| vd=vR−(vR−vRM)exp(−(t−t1)/τrr), | **(17)** |

其中 vRM=vR−iRM(R−Lτrr) 是最大二极管反向电压。

如果 Lτrr≫R（这是反向恢复测试电路的常见条件），模块按如下方式计算最大二极管反向电压：

vRM=vR+iRMLτrr.

由于下降时间值很小，模块假设二极管电流下降是线性的：

|  |  |
| --- | --- |
| iF+didt · t = qE−qMTM. | **(18)** |

然后，它将方程 18 代入方程 5：

|  |  |
| --- | --- |
| dqMd+qMτ=iF+didt · t. | **(19)** |

为获得总存储电荷，它求解方程 19：

|  |  |
| --- | --- |
| qM=iFτ+didt · τ2(1exp(tτ)−1)+didt · τt, | **(20)** |

其中 *didt* 是电流的梯度。

当 t=t1=iRM−iFdidt 时，峰值反向电流为：

|  |  |
| --- | --- |
| iRM=−qMTM. | **(21)** |

模块现在将方程 21 代入方程 20：

|  |  |
| --- | --- |
| −iRMTM=iFτ+ didt · τ2(exp(−iRM−iFdidt · τ)−1)+τ(iRM−iF)−(TM+τ)iRM=didt · τ2(exp(−iRM−iFdidt · τ)−1)iRM=F(didt,iF,TM,τ). | **(22)** |

最后，模块求解方程 22 以获得反向恢复能量：

|  |  |
| --- | --- |
| Erec=∫t1t2idvddtErec=τrriRM(vR+vRM)2Erec=iRM(2vRτrr+iRML)2. | **(23)** |

**带故障的电荷动态**

当器件发生故障时，Diode 模块按如下方式计算结电荷

qE=(τ+TM)idiode,

其中：

- *idiode* 是不含电荷模型的二极管电流。
- *qE* 是结电荷。
- *TM* 是渡越时间。
- *τ* 是载流子寿命。

然后，以下方程定义二极管电流的值：

dqMdt+qMτ−qE−qMTM=0i=qE−qMTMQscale−(Qscale−1)idiode

其中：

- *i* 是二极管电流。
- *qM* 是总存储电荷。
- *Qscale* 是电荷比的当前值。

### 温度依赖性

Diode 模块的默认行为是不对温度依赖性建模，器件在为其提供模块参数的温度下进行仿真。指数二极管模型包含若干选项，用于在仿真期间对二极管电流-电压关系的温度依赖性建模。结电容的温度依赖性不建模，因为其影响小得多。

当包含温度依赖性时，二极管定义方程保持不变。测量温度值 *Tm1* 替换为仿真温度 *Ts*。饱和电流 *IS* 根据以下方程变为温度的函数：

ISTs=ISTm1⋅(Ts/Tm1)XTI/N⋅exp(−EGNkTs(1−Ts/Tm1))

其中：

- *Tm1* 是指定二极管参数时的温度，由 **测量温度** 参数值定义。
- *Ts* 是仿真温度。
- *ISTm1* 是测量温度下的饱和电流。
- *ISTs* 是仿真温度下的饱和电流。这是对温度依赖性建模时标准二极管方程中使用的饱和电流值。
- *EG* 是半导体类型的能隙，单位为焦耳(J)。硅的值通常取为 1.11 eV，其中 1 eV 为 1.602e-19。
- *XTI* 是饱和电流温度指数。对于 pn 结二极管通常设为 3.0，对于肖特基势垒二极管设为 2.0。
- *N* 是发射系数。
- *k* 是玻尔兹曼常数 (1.3806503e–23 J/K)。

*XTI* 和 *EG* 的合适值取决于二极管类型和所使用的半导体材料。特定材料类型和二极管类型的默认值可近似体现随温度变化的行为。模块为常见二极管类型提供默认值。

在实践中，需要调整 *XTI* 和 *EG* 的值，以对特定二极管的精确行为建模。一些制造商会在 SPICE Netlist 中给出这些调整后的值，你可以从中读取合适的值。否则，你可以使用数据手册定义的较高温度下的电流-电压数据点来确定 *EG* 的改进估计值。模块为此提供参数化选项。它还提供直接指定较高温度下饱和电流 *ISTm2* 的选项。

你也可以自行调整 *XTI* 和 *EG* 的值，以匹配特定器件的实验室数据。你可以使用 Simulink® Design Optimization™ 软件来帮助调整 *XTI* 和 *EG* 的值。

**小心**

器件温度行为还取决于发射系数。不合适的发射系数值可能导致错误的温度依赖性，因为饱和电流是 *EG* 与 *N* 之比的函数。

如果定义有限反向击穿电压 (*BV*)，则反向 *BV* 的值由反向击穿温度系数 *TCV* 调制（使用 **反向击穿电压温度系数, dBV/dT** 参数指定）：

|  |  |
| --- | --- |
| *BVTs* = *BVTm1* – *TCV*· (*Ts* – *Tm1*) | **(24)** |

### 理想开关

你可以将理想开关选项用于以下理想开关半导体模块：

- GTO
- Half-Bridge (Ideal, Switching)
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

你可以在这些模块内部对二极管建模，也可以使用单独的 Diode 模块在外部对二极管建模。

要启用理想开关选项，请将 **保真度级别** 参数设置为 `Ideal Switching`。

下图显示了半桥内开关状态下二极管的电压和电流。

反向恢复损耗是二极管热损耗的主要来源之一。二极管每次从导通状态关断到开路状态时都会耗散能量。

使用理想开关时，模块不使用基于物理的电荷模型。模块将电荷在反向恢复期间产生的损耗表示为瞬时损耗。

模块通过将结温升高一个等于反向恢复损耗除以结处总热质量的值来施加反向恢复损耗。

如果将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`，则 **反向恢复损耗表, Erec(Tj, If)** 参数的值指定耗散能量，它是结温和开关事件之前正向电流的函数。关断状态电压相对于 **测量恢复损耗时的关断电压, Vrec** 参数值对损耗进行线性缩放。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **电压和电流值的滤波时间常数** 参数设置为低于最快开关周期的值。

如果将 **反向恢复损耗模型** 参数设置为 `Fixed loss`，则 **反向恢复损耗** 参数的值指定每次关断事件期间耗散的能量。如果选择 **按电流和电压缩放反向恢复损耗** 参数，则模块按导通状态电流和关断状态电压对该损耗值进行线性缩放。要使用接近瞬时值的缩放值，请将 **电压和电流值的滤波时间常数** 设置为低于最快开关周期的值。

**注意**

记录的仿真数据中的 `lastReverseRecoveryLoss` 变量将反向恢复损耗包含为一个脉冲，其幅度等于能量损耗。如果你使用脚本对定义仿真周期内的总损耗求和，则必须在每个脉冲上升沿对脉冲值求和。或者，你可以使用 `ee_getPowerLossSummary` 和 `ee_getPowerLossTimeSeries` 函数从记录数据中提取导通损耗和开关损耗。要了解如何记录和绘制仿真数据，请参阅 Log and Plot Simulation Data 示例。

记录的仿真数据中的 `power_dissipated` 变量不包括开关损耗，因为模块将这些损耗建模为瞬时事件。`power_dissipated` 变量报告欧姆导通状态损耗。

### 故障

要在 Diode 模块中对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling 和 Fault Triggering。

Diode 模块允许你对三种类型的故障建模：

- `Open` — 一旦触发故障，串联电阻会瞬时增加。你可以使用此类故障对因金属化烧毁而失效的二极管建模。
- `Short` — 一旦触发故障，并联电导会瞬时增加。你可以使用此选项对因穿通而失效的二极管建模。
- `Parameter shift` — 从触发故障的时刻开始，模块参数随时间偏移。你可以使用此选项对因老化而失效的二极管建模。

模块可以触发故障事件：

- 在特定时间。
- 当电流限值、电压限值或温度限值超过特定时间间隔时。

如果要在特定时间触发故障，请在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Timed`。如果要确定系统是否失效以及何时失效，请在 **故障检查器** 窗口中，将 **触发类型** 设置为 `Behavioral`。

如果选择行为触发，则只要其中一个触发条件为 true，组件就会失效。

**参数偏移故障**

如果在 **故障** 设置中，将 **失效模式** 参数设置为 `Parameter shift`，则二极管因其组件老化而失效。以下方程定义偏移参数的值：

Parameter(t)=Parameterfaulted−(Parameterfaulted−Parameterunfaulted)sech(t−tthτ),

其中 *tth* 是触发故障时的时间阈值，*τ* 是 **故障过渡时间常数** 参数的值。

### 热效应建模

您可以公开热端口，以对生成的热和设备温度的影响建模。要公开热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口，也不模拟设备中的热生成。
- `Show thermal port` — 该模块包含热端口，允许您对导通损耗生成的热进行建模。出于数值效率考虑，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参见《半导体中的热效应仿真》。

### Zener 二极管建模

*自 R2023b 起*

要建模在正向和反向偏置方向均导通的 Zener 二极管，请选择 **Model Zener diode** 参数，并为 **Reverse breakdown voltage** 参数指定有限值。

选择此选项后，您可以通过指定新的 **Reverse voltages, Vr(Tj,Ir)**、**Reverse currents, Ir(Tj,Vr)**、**Reverse voltages, Vr** 和 **Reverse currents, Ir** 参数，来为 Diode 模块建模反向 I-V 特性。*(自 R2024a 起)*

Diode 模块图标取决于您是否建模 Zener 二极管以及是否公开热端口。有关公开热端口的详细信息，请参见热效应建模。

| **Modeling option** 参数值 | **Model a Zener diode** 参数值 | 模块图标 |
| --- | --- | --- |
| `No thermal port` | `Off` |  |
| `On` |  |
| `Show thermal port` | `Off` |  |
| `On` |  |

### 参数化

*自 R2023b 起*

Diode 模块支持多个预定义参数化。

使用此参数化数据来复现来自特定供应商数据手册的正向电压 V-I 曲线。要加载预定义参数化，请双击 Diode 模块，单击 **Selected part** 参数的 **<click to select>** 超链接，然后在 Block Parameterization Manager 窗口中，从可用组件列表中选择要使用的部件。

**注意**

Simscape 组件的预定义参数化使用可用的数据源来获取参数值。使用工程判断和简化假设来填补缺失数据。因此，预计仿真行为与实际物理行为之间会存在偏差。为确保准确性，请根据实验数据验证仿真行为，并按需细化组件模型。

有关预定义参数化以及可用组件列表的详细信息，请参见《预参数化组件列表》。

您还可以使用 `ee_importDeviceParameters` 函数从 XML 文件中提取设备参数并将其导入模块。XML 文件必须位于 MATLAB® 路径上，并且必须使用 Hitachi 或 Infineon® 支持的参数化格式。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见《设置模块变量的优先级和初始目标》。

**注意**

为满足所有初始目标，请不要将超过模块方程中微分变量总数的初始目标优先级设置为 `High`。

- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 设置为 `0`，则模块方程中微分变量的总数为零。不要将 **Initial Targets** 部分中任何变量的优先级设置为 `High`。
- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Fixed or zero junction capacitance`，并将 **Junction capacitance** 参数设置为非零值，则模块方程中微分变量的总数为一。在 **Initial Targets** 部分中，将优先级设置为 `High` 的变量不得超过一个。
- 如果在 **Capacitance** 部分中，将 **Parameterization** 设置为 `Use C-V curve data points` 或 `Use parameters Cj0, VJ, M & FC`，则模块方程中微分变量的总数为一。在 **Initial Targets** 部分中，将优先级设置为 `High` 的变量不得超过一个。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见《基于标称值的系统缩放》。

### 绘制基本 I-V 特性

您无需构建完整模型即可绘制 Diode 模块的基本 I-V 特性。使用这些图来探究参数选择对设备特性的影响。如果您根据数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查是否正确地对模块进行了参数化。如果您有一个完整可工作的模型，但不知道使用哪个制造部件，可以将图与数据手册进行比较，以帮助做出决定。

要启用此选项，请将 Diode 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参见《绘制半导体模块的基本 I-V 特性》。
