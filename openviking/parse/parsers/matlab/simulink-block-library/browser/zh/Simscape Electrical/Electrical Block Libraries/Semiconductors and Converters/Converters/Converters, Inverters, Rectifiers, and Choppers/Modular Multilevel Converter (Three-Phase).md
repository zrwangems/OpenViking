---
type: simulink-block
title: 'Modular Multilevel Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'modularmultilevelconverterthreephase'
documentation_source_path: 'ref/modularmultilevelconverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Modular Multilevel Converter (Three-Phase)

## 端口

### 输入

### **G** — 物理信号的子模块门极控制矩阵

与 modular multilevel converter 所有子模块的门极信号相关联的物理信号端口，指定为 matrix。

如果将 **换流器拓扑** 参数设置为 `Half-bridge`，则该信号是长度为 *12 \* Nsm* 的 vector，其中 *Nsm* 是 **功率子模块数量**。

如果将 **换流器拓扑** 参数设置为 `Full-bridge`，则该信号是长度为 *24 \* Nsm* 的 vector。

#### 依赖项

要启用此端口，请将 **保真度级别** 设置为 `Detailed model - switching devices` 或 `Equivalent model - PWM-controlled`。

### **ref** — 物理信号的子模块参考波形 vector

与子模块参考波形相关联的物理信号端口，指定为长度为 *6* 的 vector。

#### 依赖项

要启用此端口，请将 **保真度级别** 设置为 `Equivalent model - waveform-controlled`。

### 输出

### **vc** — 物理信号的电容器电压 vector

与 modular multilevel converter 中每个子模块的电容器电压相关联的物理信号端口，以 vector 形式返回。

#### 依赖项

要启用此端口，请将 **电容器电压** 设置为 `Instrumented`。

### 守恒

### **+** — 正极端子电气

与 modular multilevel converter 的正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与 modular multilevel converter 的负极端子相关联的电气守恒端口。

### **~** — 三相端口电气

与 modular multilevel converter 的三相端子相关联的可扩展三相电气端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

### 主要

### **电气连接** — 电气连接 `Composite three-phase ports` (default) | `Expanded three-phase ports`

是否使用复合三相端口或扩展三相端口。

### **换流器拓扑** — 换流器拓扑 `Half-bridge` (default) | `Full-bridge`

modular multilevel converter 的拓扑。

### **保真度级别** — 模型保真度 `Detailed model - switching devices` (default) | `Equivalent model - PWM-controlled` | `Equivalent model - waveform-controlled`

模型的保真度级别。

### **电容器电压** — 电容器电压测量 `Instrumented` (default) | `Uninstrumented`

是否测量电容器电压。

### **功率子模块数量** — 子模块数量 `1` (default) | positive scalar

modular multilevel converter 的功率子模块数量。

### **电容** — 子模块电容 `1e-7` `F` (default) | scalar | vector

子模块的电容。如果输入 vector，则该 vector 的长度必须为 *6 \* Nsm*，其中 *Nsm* 是 **功率子模块数量**。

### **电容器等效串联电阻** — 电容器等效串联电阻 `1e-6` `Ohm` (default) | scalar | vector

电容器等效串联电阻。如果输入 vector，则该 vector 的长度必须为 *6 \* Nsm*，其中 *Nsm* 是 **功率子模块数量**。

#### 依赖项

要启用此参数，请将 **保真度级别** 设置为 `Detailed model - switching devices`。

### **桥臂电感** — 桥臂电感 `1e-6` `H` (default) | scalar

桥臂的电感。

### **桥臂电感串联电阻** — 桥臂电感串联电阻 `0` `Ohm` (default) | scalar

桥臂电感串联电阻。

### **电容器初始电压** — 电容器初始电压 `500` `V` (default) | scalar | vector

电容器的初始电压。如果输入 vector，则该 vector 的长度必须为 *6 \* Nsm*，其中 *Nsm* 是 **功率子模块数量**。

### 开关器件

此表显示 **开关器件** 设置中启用的参数如何取决于您选择的 **开关器件**。要了解如何阅读该表，请参阅参数依赖关系。要启用这些设置，请将 **保真度级别** 设置为 `Detailed model - switching devices`。

**开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **开关器件** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| **通态电阻** | **正向电压** | **正向电压** | **漏源通态电阻** | **正向电压** | **通态电阻** |
| **断态电导** | **通态电阻** | **通态电阻** | **断态电导** | **通态电阻** |
| **阈值电压** | **断态电导** | **断态电导** | **阈值电压** | **断态电导** |
| **栅极触发电压, Vgt** | **阈值电压** | **栅极触发电压, Vgt** | **用于门极输入分段常数近似的整数 (0 for disabled)** |
| **栅极关断电压, Vgt\_off** | **保持电流** |
| **保持电流** |

### **开关器件** — 开关类型 `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

换流器的开关器件类型。

#### 依赖项

请参阅开关器件参数依赖关系表。

### **正向电压** — 电压 `0.8` `V` (default) | scalar

对于不同的开关器件类型，**正向电压** 是：

- GTO — 使器件 I-V 特性的斜率为 1/*Ron* 所需的阳极和阴极模块端口两端的最小电压，其中 *Ron* 是 **通态电阻** 的值
- IGBT — 使二极管 I-V 特性的斜率为 1/*Ron* 所需的集电极和发射极模块端口两端的最小电压，其中 *Ron* 是 **通态电阻** 的值
- Thyristor — 使器件导通所需的最小电压

#### 依赖项

请参阅开关器件参数依赖关系表。

### **通态电阻** — 电阻 `0.001` `Ohm` (default) | scalar

对于不同的开关器件类型，**通态电阻** 是：

- GTO — 高于正向电压时电压相对于电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖项

请参阅开关器件参数依赖关系表。

### **漏源通态电阻** — 电阻 `0.001` `Ohm` (default) | scalar

漏极与源极之间的电阻。栅源电压也会影响 **漏源通态电阻** 参数。

#### 依赖项

请参阅开关器件参数依赖关系表。

### **断态电导** — 器件关断时的电导 `1e-5` `1/Ohm` (default) | scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **通态电阻** 的值。

对于不同的开关器件类型，**通态电阻** 是：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏源电导
- Thyristor — 阳极-阴极电导

#### 依赖项

请参阅开关器件参数依赖关系表。

### **阈值电压** — 电压阈值 `6` `V` (default) | scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。根据所使用的开关器件，电压阈值适用于不同器件：

- Ideal semiconductor switch — 门阴极电压
- IGBT — 栅射极电压
- MOSFET — 栅源极电压

#### 依赖项

请参阅开关器件参数依赖关系表。

### **栅极触发电压, Vgt** — 门阴极激活电压阈值 `1` `V` (default) | scalar

门阴极电压阈值。当门阴极电压高于此值时，器件导通。

#### 依赖项

请参阅开关器件参数依赖关系表。

### **栅极关断电压, Vgt\_off** — 门阴极去激活电压阈值 `-1` `V` (default) | scalar

门阴极电压阈值。当门阴极电压低于此值时，器件关断。

#### 依赖项

请参阅开关器件参数依赖关系表。

### **保持电流** — 电流阈值 `1` `A` (default) | scalar

门极电流阈值。当电流高于此值时，即使门阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖项

请参阅开关器件参数依赖关系表。

### **用于门极输入分段常数近似的整数 (0 for disabled)** — FPGA 部署的整数模式 `0` (default) | nonnegative scalar

用于对门极输入执行分段常数近似以进行 FPGA 部署的整数。

#### 依赖项

要启用此参数，请将 **开关器件** 设置为 `Averaged Switch`。

### 保护二极管

有关这些参数的详细信息，请参阅 Diode。

### **模型动态** — 二极管模型 `Diode with no dynamics` (default) | `Diode with charge dynamics` | `None`

二极管类型。选项包括：

- `None` — 该模块不对二极管动态进行建模。
- `Diode with no dynamics` — 选择此选项以使用 Diode 模块优先考虑仿真速度。
- `Diode with charge dynamics` — 选择此选项以使用 Diode 模块的换向二极管模型，优先考虑反向模式电荷动态方面的模型保真度。

**注意**

如果在 **开关器件** 设置中将 **开关器件** 设置为 `Averaged Switch`，则会自动选择 `Diode with no dynamics` 设置。

#### 依赖项

要启用此参数，请将 **开关器件** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **正向电压** — 正向电压 `0.8` `V` (default) | scalar

使二极管 I-V 特性的斜率为 1/*Ron* 所需的 `+` 和 `-` 模块端口两端的最小电压，其中 *Ron* 是 **导通电阻** 的值。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **导通电阻** — 导通电阻 `0.001` `Ohm` (default) | scalar

高于 **正向电压** 时电压相对于电流的变化率。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **关断电导** — 关断电导 `1e-5` `1/Ohm` (default) | scalar

反向偏置二极管的电导。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **结电容** — 结电容 `50` `nF` (default) | scalar

二极管结电容。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`。

### **峰值反向电流, iRM** — 峰值反向电流 `-235` `A` (default) | negative scalar

由外部测试电路测得的峰值反向电流。该值必须小于零。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `300` `A` (default) | positive scalar

测量峰值反向电流时的初始正向电流。该值必须大于零。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`。

### **测量 iRM 时的电流变化率** — 测量 iRM 时的电流变化率 `-50` `A/μs` (default) | negative scalar

测量峰值反向电流时的电流变化率。该值必须小于零。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`。

### **反向恢复时间参数化** — 反向恢复时间选项 `Specify stretch factor` (default) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

确定您如何指定反向恢复时间。

如果您选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则您指定一个值，该模块使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`。

### **反向恢复时间, trr** — 反向恢复时间 `15` `μs` (default) | scalar

从电流最初变为零（二极管关断时）到电流降至峰值反向电流的 10% 以下的时间间隔。**反向恢复时间, trr** 参数的值必须大于 **峰值反向电流, iRM** 参数的值除以 **测量 iRM 时的电流变化率** 参数的值。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`，并将 **反向恢复时间参数化** 设置为 `Specify reverse recovery time directly`。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3` (default) | scalar

该模块用于计算 **反向恢复时间, trr** 的值。该值必须大于 `1`。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单方法。拉伸因子的值越大，反向恢复电流消散所需时间越长。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`，并将 **反向恢复时间参数化** 设置为 `Specify stretch factor`。

### **反向恢复电荷, Qrr** — 反向恢复电荷 `1500` `s*μA` (default) | scalar

该模块用于计算 **反向恢复时间, trr** 的值。如果您的二极管数据表指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **峰值反向电流, iRM** 指定的值。
- *a* 是为 **测量 iRM 时的电流变化率** 指定的值。

#### 依赖项

要启用此参数，请将 **模型动态** 设置为 `Diode with charge dynamics`，并将 **反向恢复时间参数化** 设置为 `Specify reverse recovery charge`。

### 缓冲器

要启用 **缓冲器** 设置，请将 **保真度级别** 设置为 `Detailed model - switching devices`，并将 **开关器件** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **缓冲器** — 缓冲器 `None` (default) | `RC snubber`

每个开关器件的缓冲器：

- `None`
- `RC snubber`

### **缓冲电阻** — 缓冲电阻 `0.1` `Ohm` (default) | scalar

缓冲电阻。

#### 依赖项

要启用此参数，请将 **缓冲器** 设置为 `RC snubber`。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F` (default) | scalar

缓冲电容。

#### 依赖项

要启用此参数，请将 **Snubber** 设置为
`RC snubber`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：Electrical connection 端口更新

自 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有串联功率子模块的三相模块化多电平换流器

Modular Multilevel Converter (Three-Phase) 模块对三相模块化多电平换流器进行建模。每相由两个桥臂组成，这些桥臂使用多个串联连接的功率子模块实现。

每个子模块由半桥或全桥换流器和一个电容器组成。

**半桥拓扑**

**全桥拓扑**

此模块允许您通过选择带有开关器件的详细模型或等效模型来选择模型保真度级别。您可以从以下开关器件中选择：

- GTO — 门极可关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 中的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制 (PWM) 信号取平均。然后可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### 用于 FPGA 部署的 Averaged Switch 中的分段常数近似

如果将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则此模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 函数的模式 *Gsat*。为使这些方程与硬件描述语言 (HDL) 代码生成（并因此与 FPGA 部署）兼容，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后此模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前的非线性分区变为线性时变分区。

现在，范围 `[0,K]` 中的整数值与范围 `[0,1]` 中的每个实数值模式相关联，其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值。此模块通过将原始模式除以 K 将其重新归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真稳健性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
