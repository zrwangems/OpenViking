---
type: simulink-block
title: 'Continuous Wave'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Circuit Envelope Fundamentals'
documentation_page: 'continuouswave'
documentation_source_path: 'ref/continuouswave.html'
language: zh-CN
chinese_source: worker-translation
---

# Continuous Wave

## 端口

R2025b 中未记录。

## 参数

### **Source type** — 波形类型 `Ideal voltage`（默认） | `Ideal current` | `Power`

- `Ideal Voltage` — 该模块在指定的 **Carrier frequencies** 处仿真恒定电压包络 *v*0。该包络的实部和虚部由 **Constant in-phase value** 和 **Constant quadrature value** 参数指定。
- `Ideal Current` — 该模块在指定的 **Carrier frequencies** 处仿真恒定电流包络 *i*0。该包络的实部和虚部由 **Constant in-phase value** 和 **Constant quadrature value** 参数确定。
- `Power` — 该模块仿真恒定电压包络

  v0=2P0Re(Zs)ejπ180ϕ

  其中：

  - *P*0 是 **Available power** 参数的值
  - *Zs* 是 **Source impedance (ohms)** 参数的值。
  - *ϕ* 是 **Angle (degrees)** 参数的值。

### **Constant in-phase value** — 载波频率的同相调制 `0 V`（默认） | 实数向量 | `V` | `mV` | `kV`

针对每个 **Carrier frequencies** 的同相调制，指定为实数向量。从对应的下拉列表中指定单位。

#### 依赖关系

要启用此参数，请在 **Source type** 选项卡上选择 `Ideal voltage` 或 `Ideal current`。

### **Constant quadrature value** — 载波频率的正交调制 `0 V`（默认） | 实数向量 | `V` | `mV` | `kV`

针对每个 RF 电路载波频率的正交调制，指定为实数向量。从对应的下拉列表中指定单位。

#### 依赖关系

要启用此参数，请在 **Source type** 选项卡上选择 `Ideal voltage` 或 `Ideal current`。

### **Source impedance(Ohm)** — 源的输入阻抗 `50`（默认） | 正实数 | 复数

源的输入阻抗，指定为正实数或复数。复数的实部和虚部必须大于或等于 `1e-18` ohms。

#### 依赖关系

要启用此参数，请在 **Source type** 选项卡上选择 `Power`。

### **Available power** — 载波频率的可用功率 `0 W`（默认） | 实数向量 | `W` | `mW` | `dBW` | `dBm`

在指定的 **Carrier frequencies** 处的可用功率，指定为实数向量。从下拉列表中指定单位。默认值为 `0` `W`。

#### 依赖关系

要启用此参数，请在 **Source type** 选项卡上选择 `Power`。默认值为 `0` `W`

### **Angle(degrees)** — 功率波的相位角 `0`（默认） | 实数向量

在指定的 **Carrier frequencies** 处的功率波相位角，指定为实数向量。默认值为 `0` degrees。

#### 依赖关系

要启用此参数，请在 **Source type** 选项卡上选择 `Power`。

### **Carrier frequencies** — 载波频率 `0`（默认） | 正实数向量 | `Hz` | `kHz` | `MHz` | `GHz`

载波频率，指定为正实数向量。载波频率中的元素是 Configuration 模块中基频音及其对应谐波的组合。默认值为 `0` `Hz`。

### **Add phase noise** — 添加相位噪声 `off`（默认） | `on`

选择此参数，以向具有连续波源的系统添加相位噪声。

### **Phase noise frequency offset (Hz)** — 相位噪声频率偏移 `0`（默认） | 标量 | 向量 | 矩阵

相位噪声频率偏移，指定为标量、向量或矩阵，每个元素的单位均为 hertz。

如果指定矩阵，则每一列应对应 CW 源的非直流载波频率。频率偏移值必须受仿真的包络带宽限制。有关详细信息，请参见 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Phase noise level (dBc/Hz)** — 相位噪声电平 `0`（默认） | 标量 | 向量 | 矩阵

相位噪声电平，指定为标量、向量或矩阵，元素单位为 decibel per hertz。

如果指定矩阵，则每一列应对应 CW 源的非直流载波频率。频率偏移值必须受仿真的包络带宽限制。有关详细信息，请参见 Configuration。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Automatically estimate impulse response duration** — 自动估计冲激响应持续时间 `on`（默认） | `off`

选择此参数可自动计算相位噪声的冲激响应。清除此参数可使用 **Impulse response duration** 手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Impulse response duration** — 冲激响应持续时间 `1e-10``s`（默认） | 标量

用于仿真相位噪声的冲激响应持续时间，指定为以 seconds 为单位的标量。如果放大器为非线性，则无法指定冲激响应。

**注意**

相位噪声分布在频率上的分辨率受用于仿真它的冲激响应持续时间的限制。增加此持续时间可提高相位噪声分布的精度。如果对于给定的冲激响应持续时间，相位噪声频率偏移分辨率过高，则会出现警告消息，并指定适合所需分辨率的最小持续时间

#### 依赖关系

要设置此参数，请先清除 **Automatically estimate impulse response duration**。

### **Plot phase noise characteristics** — 相位噪声幅度响应按钮

该模块基于 **Impairments** 选项卡中指定的参数，以及（如果可用）Configuration 模块中的 **Envelope bandwidth** 参数或 **Phase noise frequency offset (Hz)** 参数中指定的值，绘制相位噪声特性。

#### 依赖关系

要启用此参数，请选择 **Add phase noise**。

### **Ground and hide negative terminals** — 接地 RF 电路端子 `on`（默认） | `off`

选择此选项可在内部将负端子接地并隐藏它们。要暴露负端子，请清除此选项。通过暴露这些端子，您可以将其连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2022b：使用相位噪声偏移频率估计冲激响应持续时间

Continuous Wave 模块使用 **Phase noise frequency offset (Hz)** 参数估计冲激响应持续时间，并在您点击 **Plot phase noise characteristics** 按钮时可视化相位噪声特性。

### R2021b：Continuous Wave 模块图标已更新

从 R2021b 开始，Continuous Wave 模块图标现已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Continuous Wave 模块的模型时，软件会将该模块图标替换为 R2021b 版本。

## 描述

对恒定包络源建模

Continuous Wave 模块在 RF Blockset™ 电路包络仿真环境中对载波上的恒定调制进行建模。有关 RF 仿真的介绍，请参见示例 Simulate High Frequency Components。

该模块实现以下关系式

v(t)=v0ejωkt

或

i(t)=i0ejωkt

在载波 *ωk* 处，具体取决于源类型。

Continuous Wave 模块封装图标是动态的，并显示所应用噪声参数的当前状态。有关详细信息，请参见 Continuous Wave Block Icons。
