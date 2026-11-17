---
type: simulink-block
title: 'Modular Multilevel Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'modularmultilevelconverterthreephase'
documentation_source_path: 'ref/modularmultilevelconverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Modular Multilevel Converter (Three-Phase)

## 端口
```yaml
ports:
- name: G
  summary: 物理信号子模块门极控制矩阵
  direction: input
- name: ref
  summary: 物理信号子模块参考波形向量
  direction: input
- name: vc
  summary: 物理信号电容电压向量
  direction: output
- name: +
  summary: 正极端子电气端口
  direction: conserving
- name: '-'
  summary: 负极端子电气端口
  direction: conserving
- name: '~'
  summary: 三相端口电气端口
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
```

### 输入

### **G** — 物理信号子模块门极控制矩阵

与模块化多电平换流器所有子模块的门极信号相关联的物理信号端口，指定为矩阵。

如果将 **Converter topology** 参数设置为 `Half-bridge`，则该信号为长度为 *12 \* Nsm* 的向量，其中 *Nsm* 为 **Number of power submodules**。

如果将 **Converter topology** 参数设置为 `Full-bridge`，则该信号为长度为 *24 \* Nsm* 的向量。

#### 依赖关系

要启用此端口，请将 **Fidelity level** 设置为 `Detailed model - switching devices` 或 `Equivalent model - PWM-controlled`。

### **ref** — 物理信号子模块参考波形向量

与子模块参考波形相关联的物理信号端口，指定为长度为 *6* 的向量。

#### 依赖关系

要启用此端口，请将 **Fidelity level** 设置为 `Equivalent model - waveform-controlled`。
### 输出

### **vc** — 物理信号电容电压向量

与模块化多电平换流器中每个子模块的电容电压相关联的物理信号端口，以向量形式返回。

#### 依赖关系

要启用此端口，请将 **Capacitor voltages** 设置为 `Instrumented`。
### 守恒端口

### **+** — 正极端子电气端口

与模块化多电平换流器正极端子相关联的电气守恒端口。

### **-** — 负极端子电气端口

与模块化多电平换流器负极端子相关联的电气守恒端口。

### **~** — 三相端口电气端口

与模块化多电平换流器三相端子相关联的可扩展三相电气端口。

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
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主
- name: Converter topology
  summary: 换流器拓扑 Half-bridge（默认）| Full-bridge
  group: 主
- name: Fidelity level
  summary: 模型保真度 Detailed model - switching devices（默认）| Equivalent model - PWM-controlled | Equivalent model - waveform-controlled
  group: 主
- name: Capacitor voltages
  summary: 电容电压测量 Instrumented（默认）| Uninstrumented
  group: 主
- name: Number of power submodules
  summary: 子模块数量 1（默认）| 正标量
  group: 主
- name: Capacitance
  summary: 子模块电容 1e-7 F（默认）| 标量 | 向量
  group: 主
- name: Capacitor effective series resistance
  summary: 电容等效串联电阻 1e-6 Ohm（默认）| 标量 | 向量
  group: 主
- name: Arm inductance
  summary: 桥臂电感 1e-6 H（默认）| 标量
  group: 主
- name: Arm inductance series resistance
  summary: 桥臂电感串联电阻 0 Ohm（默认）| 标量
  group: 主
- name: Capacitor initial voltage
  summary: 电容初始电压 500 V（默认）| 标量 | 向量
  group: 主
- name: Switching device
  summary: 开关类型 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: Switching Devices
- name: Forward voltage
  summary: 电压 0.8 V（默认）| 标量
  group: Switching Devices
- name: On-state resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: Switching Devices
- name: Drain-source on resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: Switching Devices
- name: 断态电导
  summary: 器件关断时的电导 1e-5 1/Ohm（默认）| 标量
  group: Switching Devices
- name: 阈值电压
  summary: 电压阈值 6 V（默认）| 标量
  group: Switching Devices
- name: 栅极触发电压，Vgt
  summary: 栅极-阴极激活电压阈值 1 V（默认）| 标量
  group: Switching Devices
- name: 栅极关断电压，Vgt_off
  summary: 栅极-阴极去激活电压阈值 -1 V（默认）| 标量
  group: Switching Devices
- name: 维持电流
  summary: 电流阈值 1 A（默认）| 标量
  group: Switching Devices
- name: 栅极输入分段常数逼近的整数（0 表示禁用）
  summary: 用于 FPGA 部署的整数模式 0（默认）| 非负标量
  group: Switching Devices
- name: 模型动态特性
  summary: 二极管模型 Diode with no dynamics（默认）| Diode with charge dynamics | None
  group: 保护二极管
- name: 正向电压
  summary: 正向电压 0.8 V（默认）| 标量
  group: 保护二极管
- name: 导通电阻
  summary: 导通电阻 0.001 Ohm（默认）| 标量
  group: 保护二极管
- name: 断态电导
  summary: 断态电导 1e-5 1/Ohm（默认）| 标量
  group: 保护二极管
- name: Junction capacitance
  summary: 结电容 50 nF（默认值）| 标量
  group: 保护二极管
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认值）| 负标量
  group: 保护二极管
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认值）| 正标量
  group: 保护二极管
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50 A/μs（默认值）| 负标量
  group: 保护二极管
- name: Reverse recovery time parameterization
  summary: 反向恢复时间选项 Specify stretch factor（默认值）| Specify reverse recovery time directly | Specify reverse recovery charge
  group: 保护二极管
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认值）| 标量
  group: 保护二极管
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认值）| 标量
  group: 保护二极管
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 s*μA（默认值）| 标量
  group: 保护二极管
- name: Snubber
  summary: 缓冲器 None（默认）| RC snubber
  group: 缓冲器
- name: Snubber resistance
  summary: 缓冲器电阻 0.1 Ohm（默认）| 标量
  group: 缓冲器
- name: Snubber capacitance
  summary: 缓冲器电容 1e-7 F（默认）| 标量
  group: 缓冲器
```

### 主

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Converter topology** — 换流器拓扑 `Half-bridge`（默认）| `Full-bridge`

模块化多电平换流器的拓扑。

### **Fidelity level** — 模型保真度 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled` | `Equivalent model - waveform-controlled`

模型的保真度级别。

### **Capacitor voltages** — 电容电压测量 `Instrumented`（默认）| `Uninstrumented`

是否对电容电压进行测量。

### **Number of power submodules** — 子模块数量 `1`（默认）| 正标量

模块化多电平换流器的功率子模块数量。

### **Capacitance** — 子模块电容 `1e-7` `F`（默认）| 标量 | 向量

子模块的电容。如果输入向量，则该向量的长度必须为 *6 \* Nsm*，其中 *Nsm* 为 **Number of power submodules**。

### **Capacitor effective series resistance** — 电容等效串联电阻 `1e-6` `Ohm`（默认）| 标量 | 向量

电容等效串联电阻。如果输入向量，则该向量的长度必须为 *6 \* Nsm*，其中 *Nsm* 为 **Number of power submodules**。

#### 依赖关系

要启用此参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Arm inductance** — 桥臂电感 `1e-6` `H`（默认）| 标量

桥臂的电感。

### **Arm inductance series resistance** — 桥臂电感串联电阻 `0` `Ohm`（默认）| 标量

桥臂电感串联电阻。

### **Capacitor initial voltage** — 电容初始电压 `500` `V`（默认）| 标量 | 向量

电容的初始电压。如果输入向量，则该向量的长度必须为
*6 \* Nsm*，其中 *Nsm* 是
**Number of power submodules**。

### Switching Devices

此表显示了 **Switching Devices**
设置中启用的参数如何取决于您选择的 **Switching device**。要
了解如何阅读该表，请参阅 Parameter Dependencies。要启用这些设置，请将
**Fidelity level** 设置为 `Detailed model - switching
devices`。

**Switching Devices Parameter Dependencies**

| Parameters and Options | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| **On-state resistance** | **Forward voltage** | **Forward voltage** | **Drain-source on resistance** | **Forward voltage** | **On-state resistance** |
| **Off-state conductance** | **On-state resistance** | **On-state resistance** | **Off-state conductance** | **On-state resistance** |
| **Threshold voltage** | **Off-state conductance** | **Off-state conductance** | **Threshold voltage** | **Off-state conductance** |
| **栅极触发电压，Vgt** | **阈值电压** | **栅极触发电压，Vgt** | **用于栅极输入分段常数近似的整数（0 表示禁用）** |
| **Gate turn-off voltage, Vgt\_off** | **Holding current** |
| **Holding current** |

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器的开关器件类型。

#### 依赖关系

请参阅 Switching Devices Parameter Dependencies 表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

对于不同的开关器件类型，**Forward voltage** 是：

- GTO — 使器件 I-V
  特性的梯度为
  1/*Ron* 所需的阳极和
  阴极模块端口之间的最小电压，其中
  *Ron* 是
  **On-state resistance** 的值
- IGBT — 使二极管 I-V
  特性的梯度为
  1/*Ron* 所需的集电极和
  发射极模块端口之间的最小电压，其中
  *Ron* 是
  **On-state resistance** 的值
- Thyristor — 使器件导通
  所需的最小电压

#### 依赖关系

请参阅 Switching Devices Parameter Dependencies 表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

对于不同的开关器件类型，**On-state resistance**
是：

- GTO — 高于正向电压时电压随电流的
  变化率
- Ideal semiconductor switch — 器件导通时的
  阳极-阴极电阻
- IGBT — 器件导通时的
  集电极-发射极电阻
- Thyristor — 器件导通时的
  阳极-阴极电阻
- Averaged switch — 器件导通时的
  阳极-阴极电阻

#### 依赖关系

请参阅 Switching Devices Parameter Dependencies 表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

漏极和源极之间的电阻。栅源电压也会影响
**Drain-source on resistance** 参数。

#### 依赖关系

请参阅 Switching Devices Parameter Dependencies 表。

### **断态电导** — 器件关断时的电导 `1e-5` `1/Ohm`（默认）| 标量

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是**通态电阻**的值。

对于不同的开关器件类型，**通态电阻**分别为：

- GTO — 阳极-阴极电导
- 理想半导体开关 — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- 晶闸管 — 阳极-阴极电导

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **阈值电压** — 电压阈值 `6` `V`（默认）| 标量

栅极电压阈值。当栅极电压高于此值时，器件导通。电压阈值适用于不同的器件，具体取决于所使用的开关器件：

- 理想半导体开关 — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **栅极触发电压，Vgt** — 栅极-阴极激活电压阈值 `1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **栅极关断电压，Vgt\_off** — 栅极-阴极去激活电压阈值 `-1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **维持电流** — 电流阈值 `1` `A`（默认）| 标量

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **栅极输入分段常数逼近的整数（0 表示禁用）** — 用于 FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对栅极输入执行分段常数逼近以进行 FPGA 部署的整数。

#### 依赖关系

要启用此参数，请将**开关器件**设置为 `Averaged Switch`。

### 保护二极管

有关这些参数的详细信息，请参阅 Diode。

### **模型动态特性** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics` | `None`

二极管类型。选项包括：

- `None` — 该模块不对二极管动态特性进行建模。
- `Diode with no dynamics` — 选择此选项可使用 Diode 模块优先提高仿真速度。
- `Diode with charge dynamics` — 选择此选项可使用 Diode 模块的换向二极管模型，在反向模式电荷动态特性方面优先提高模型保真度。

**注意**

如果在**开关器件**设置中将**开关器件**设置为 `Averaged Switch`，则会自动选择 `Diode with no dynamics` 设置。

#### 依赖关系

要启用此参数，请将**开关器件**设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **正向电压** — 正向电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性梯度为 1/*Ron* 所需的 `+` 和 `-` 模块端口之间的最小电压，其中 *Ron* 是**导通电阻**的值。

#### 依赖关系

要启用此参数，请将**模型动态特性**设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **导通电阻** — 导通电阻 `0.001` `Ohm`（默认）| 标量

在**正向电压**以上，电压相对于电流的变化率。

#### 依赖关系

要启用此参数，请将**模型动态特性**设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **断态电导** — 断态电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Junction capacitance** — 结电容 `50` `nF`（默认值）| 标量

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认值）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认值）| 正标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50` `A/μs`（默认值）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间选项 `Specify stretch factor`（默认值）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

确定您如何指定反向恢复时间。

如果您选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认值）| 标量

电流最初降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认值）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。此值必须大于 `1`。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间就越长。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*μA`（默认值）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管数据手册指定的是反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

### 缓冲器

要启用 **Snubbers** 设置，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **Snubber** — 缓冲器 `None`（默认）| `RC snubber`

每个开关器件的缓冲器：

- `None`
- `RC snubber`

### **Snubber resistance** — 缓冲器电阻 `0.1` `Ohm`（默认）| 标量

缓冲器电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

### **Snubber capacitance** — 缓冲器电容 `1e-7` `F`（默认）| 标量

缓冲器电容。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和展开端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

具有串联功率子模块的三相模块化多电平换流器

Modular Multilevel Converter (Three-Phase) 模块用于对三相模块化多电平换流器进行建模。每一相由两个桥臂组成，这些桥臂通过多个串联的功率子模块实现。

每个子模块由一个半桥或全桥换流器和一个电容器组成。

**半桥拓扑**

**全桥拓扑**

此模块允许您通过在详细模型（含开关器件）和等效模型之间进行选择，来选择模型保真度级别。您可以从以下开关器件中进行选择：

- GTO — 门极关断晶闸管。有关该器件 I-V 特性的信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件 I-V 特性的信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件 I-V 特性的信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件 I-V 特性的信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件 I-V 特性的信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制 (PWM) 信号进行平均。然后，您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### 用于 FPGA 部署的平均开关中的分段常数近似

如果将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 的函数的模式 *Gsat*。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，并因此适用于 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性的分区转变为线性时变分区。

范围 `[0,K]` 中的一个整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 中的每个实数值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
