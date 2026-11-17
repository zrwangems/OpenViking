---
type: simulink-block
title: 'Modular Multilevel Converter Leg'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'modularmultilevelconverterleg'
documentation_source_path: 'ref/modularmultilevelconverterleg.html'
language: zh-CN
chinese_source: worker-translation
---

# Modular Multilevel Converter Leg

## 端口
```yaml
ports:
- name: G
  summary: 物理信号子模块门极控制向量
  direction: input
- name: ref
  summary: 物理信号子模块参考波形向量
  direction: input
- name: vc
  summary: 物理信号电容电压向量
  direction: output
- name: +
  summary: 正极端子电气
  direction: output
- name: '-'
  summary: 负极端子电气
  direction: output
- name: a
  summary: 相 *a* 端子电气
  direction: output
```

### 输入

### **G** — 物理信号子模块门极控制向量

与模块化多电平换流器桥臂所有子模块的门极信号相关联的物理信号端口，指定为物理信号向量。

如果将 **Converter topology** 参数设置为 `Half-bridge`，则输出为长度为 *4 \* Nsm* 的向量，其中 *Nsm* 为 **Number of power submodules**。

如果将 **Converter topology** 参数设置为 `Full-bridge`，则输出为长度为 *8 \* Nsm* 的向量。

#### 依赖

要启用此端口，请将 **Fidelity level** 设置为 `Detailed model - switching devices` 或 `Equivalent model - PWM-controlled`。

### **ref** — 物理信号子模块参考波形向量

与参考波形相关联的物理信号端口，指定为长度为 *2* 的物理信号向量。

#### 依赖

要启用此端口，请将 **Fidelity level** 设置为 `Equivalent model - waveform-controlled`。
### 输出

### **vc** — 物理信号电容电压向量

与模块化多电平换流器桥臂中每个子模块的电容电压相关联的物理信号端口，指定为物理信号向量。

#### 依赖

要启用此端口，请将 **Capacitor voltages** 设置为 `Instrumented`。
### 守恒

### **+** — 正极端子电气

与模块化多电平换流器桥臂正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与模块化多电平换流器桥臂负极端子相关联的电气守恒端口。

### **a** — 相 *a* 端子电气

与模块化多电平换流器桥臂单相端子相关联的电气守恒端口。
## 参数
```yaml
parameters:
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
  group: 开关器件
- name: Forward voltage
  summary: 电压 0.8 V（默认）| 标量
  group: 开关器件
- name: On-state resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: 开关器件
- name: Drain-source on resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: 开关器件
- name: Off-state conductance
  summary: 器件关断时的电导 1e-5 1/Ohm（默认）| 标量
  group: 开关器件
- name: Threshold voltage
  summary: 电压阈值 6 V（默认）| 标量
  group: 开关器件
- name: Gate trigger voltage, Vgt
  summary: 栅极-阴极激活电压阈值 1 V（默认）| 标量
  group: 开关器件
- name: Gate turn-off voltage, Vgt_off
  summary: 门极关断电压，Vgt_off -1 V（默认）| 标量
  group: 开关器件
- name: Holding current
  summary: 维持电流 1 A（默认）| 标量
  group: 开关器件
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: 用于门极输入分段常数近似的整数（0 表示禁用） 0（默认）| 非负标量
  group: 开关器件
- name: Model dynamics
  summary: 二极管模型 Diode with no dynamics（默认）| Diode with charge dynamics | None
  group: Protection Diodes — 保护二极管
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Junction capacitance
  summary: 结电容 50 nF（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Peak reverse current, iRM
  summary: 峰值反向电流，iRM -235 A（默认）| 负标量
  group: Protection Diodes — 保护二极管
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: Protection Diodes — 保护二极管
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50 A/μs（默认）| 负标量
  group: Protection Diodes — 保护二极管
- name: Reverse recovery time parameterization
  summary: 反向恢复时间参数化选项 Specify stretch factor（默认）| Specify reverse recovery time directly | Specify reverse recovery charge
  group: Protection Diodes — 保护二极管
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 s*μA（默认）| 标量
  group: Protection Diodes — 保护二极管
- name: Snubber
  summary: 缓冲电路 None（默认）| RC snubber
  group: Snubbers — 缓冲电路
- name: Snubber resistance
  summary: 缓冲电阻 0.1 Ohm（默认）| 标量
  group: Snubbers — 缓冲电路
- name: Snubber capacitance
  summary: 缓冲电容 1e-7 F（默认）| 标量
  group: Snubbers — 缓冲电路
```

### 主

### **Converter topology** — 换流器拓扑 `Half-bridge`（默认）| `Full-bridge`

模块化多电平换流器的拓扑。

### **Fidelity level** — 模型保真度 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled` | `Equivalent model - waveform-controlled`

模型的保真度级别。

### **Capacitor voltages** — 电容电压测量 `Instrumented`（默认）| `Uninstrumented`

是否测量电容电压。

### **Number of power submodules** — 子模块数量 `1`（默认）| 正标量

模块化多电平换流器的功率子模块数量。

### **Capacitance** — 子模块电容 `1e-7` `F`（默认）| 标量 | 向量

子模块的电容。如果输入向量，则该向量的长度必须为 *2 \* Nsm*，其中 *Nsm* 为 **Number of power submodules**。

### **Capacitor effective series resistance** — 电容等效串联电阻 `1e-6` `Ohm`（默认）| 标量 | 向量

电容等效串联电阻。如果输入向量，则该向量的长度必须为 *2 \* Nsm*，其中 *Nsm* 为 **Number of power submodules**。

#### 依赖

要启用此参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Arm inductance** — 桥臂电感 `1e-6` `H`（默认）| 标量

桥臂的电感。

### **Arm inductance series resistance** — 桥臂电感串联电阻 `0` `Ohm`（默认）| 标量

桥臂电感串联电阻。

### **Capacitor initial voltage** — 电容初始电压 `500` `V`（默认）| 标量 | 向量

电容的初始电压。如果输入向量，则该向量的长度必须为 *2 \* Nsm*，其中 *Nsm* 为 **Number of power submodules**。

### 开关器件

此表显示了 **Switching Devices** 设置中启用的参数如何取决于您选择的 **Switching device**。要了解如何阅读该表，请参阅参数依赖关系。要启用这些设置，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

**Switching Devices 参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| **On-state resistance** | **Forward voltage** | **Forward voltage** | **Drain-source on resistance** | **Forward voltage** | **On-state resistance** |
| **Off-state conductance** | **On-state resistance** | **On-state resistance** | **Off-state conductance** | **On-state resistance** |
| **Threshold voltage** | **Off-state conductance** | **Off-state conductance** | **Threshold voltage** | **Off-state conductance** |
| **门极触发电压，Vgt** | **阈值电压** | **门极触发电压，Vgt** | **用于门极输入分段常数近似的整数（0 表示禁用）** |
| **Gate turn-off voltage, Vgt\_off** | **Holding current** |
| **Holding current** |

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

换流器的开关器件类型。

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

对于不同的开关器件类型，**Forward voltage** 分别为：

- GTO — 使器件 I-V 特性梯度为 1/*Ron* 所需的阳极和阴极模块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性梯度为 1/*Ron* 所需的集电极和发射极模块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 使器件导通所需的最小电压

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

对于不同的开关器件类型，**On-state resistance** 分别为：

- GTO — 高于正向电压时电压随电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

漏极和源极之间的电阻。栅极-源极电压也会影响 **Drain-source on resistance** 参数。

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Off-state conductance** — 器件关断时的电导 `1e-5` `1/Ohm`（默认）| 标量

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 分别为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V`（默认）| 标量

栅极电压阈值。当栅极电压高于此值时，器件导通。电压阈值适用于不同的器件，具体取决于所使用的开关器件：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Gate trigger voltage, Vgt** — 栅极-阴极激活电压阈值 `1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖

请参阅 Switching Devices 参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 门极关断电压，Vgt\_off `-1` `V`（默认）| 标量

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Holding current** — 维持电流 `1` `A`（默认）| 标量

门极电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — 用于门极输入分段常数近似的整数（0 表示禁用） `0`（默认）| 非负标量

用于对门极输入执行分段常数近似以进行 FPGA 部署的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### Protection Diodes — 保护二极管

有关这些参数的详细信息，请参阅 Diode。

### **Model dynamics** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics` | `None`

二极管类型。选项包括：

- `None` — 该模块不对二极管动态特性进行建模。
- `Diode with no dynamics` — 选择此选项可使用 Diode 模块优先提高仿真速度。
- `Diode with charge dynamics` — 选择此选项可使用 Diode 模块的换流二极管模型，在反向模式电荷动态特性方面优先提高模型保真度。

**注意**

如果在 **Switching Device** 设置中将 **Switching device** 设置为 `Averaged Switch`，则会自动选择 `Diode with no dynamics` 设置。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性梯度为 1/*Ron* 时，`+` 和 `-` 模块端口两端所需的最小电压，其中 *Ron* 是 **On resistance** 的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）| 标量

高于 **Forward voltage** 时电压相对于电流的变化率。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Junction capacitance** — 结电容 `50` `nF`（默认）| 标量

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流，iRM `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50` `A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间参数化选项 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

确定指定反向恢复时间的方式。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块将使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）| 标量

电流最初降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。此值必须大于 `1`。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单方法。拉伸因子的值越大，反向恢复电流消散所需的时间就越长。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*μA`（默认）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。如果二极管的数据手册指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

### Snubbers — 缓冲电路

要启用 **Snubbers** 设置，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **Snubber** — 缓冲电路 `None`（默认）| `RC snubber`

每个开关器件的缓冲电路：

- `None`
- `RC snubber`

### **Snubber resistance** — 缓冲电阻 `0.1` `Ohm`（默认）| 标量

缓冲电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F`（默认）| 标量

缓冲电容。

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

## 描述

模块化多电平换流器桥臂，包含串联功率子模块

模块化多电平换流器桥臂模块将模块化多电平换流器桥臂建模为由多个串联功率子模块实现的两个桥臂。

**半桥拓扑**

**全桥拓扑**

该模块允许您通过在详细模型（含开关器件）和等效模型之间进行选择，来选取模型保真度级别。您可以从以下开关器件中进行选择：

- GTO — 门极关断晶闸管。有关该器件 I-V 特性的信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件 I-V 特性的信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件 I-V 特性的信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件 I-V 特性的信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件 I-V 特性的信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制（PWM）信号取平均。然后您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### 平均开关中用于 FPGA 部署的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 函数的模式 *Gsat*。为了使这些方程与硬件描述语言（HDL）代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。该模块随后将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性的分区转变为线性时变分区。

范围 `[0,K]` 内的一个整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
