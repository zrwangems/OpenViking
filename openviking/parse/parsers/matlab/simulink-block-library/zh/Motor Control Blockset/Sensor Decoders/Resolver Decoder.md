---
type: simulink-block
title: 'Resolver Decoder'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensor Decoders'
documentation_page: 'resolverdecoder'
documentation_source_path: 'ref/resolverdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Resolver Decoder

## 端口
```yaml
ports:
- name: V Sin
  summary: 采样的次级正弦信号向量
  direction: input
  data_types: single | double | fixed point
- name: V Cos
  summary: 采样的次级余弦信号向量
  direction: input
  data_types: single | double | fixed point
- name: Reset
  summary: 复位 PLL 标量
  direction: input
  data_types: single | double | fixed point
- name: θm
  summary: 电机机械位置标量
  direction: output
  data_types: single | double | fixed point
- name: sinθe
  summary: 电机电角度位置的正弦标量
  direction: output
  data_types: single | double | fixed point
- name: cosθe
  summary: 电机电角度位置的余弦标量
  direction: output
  data_types: single | double | fixed point
- name: ωm
  summary: 电机机械速度标量
  direction: output
  data_types: single | double | fixed point
- name: PLLEn
  summary: PLL 状态标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **V Sin** — 采样的次级正弦信号向量

从旋转变压器输出的采样的次级正弦波形。当使用正弦激励时，将此信号归一化，使其位于 [-1, 1] 范围内并以 0 为中心。

**数据类型：** `single` | `double` | `fixed point`

### **V Cos** — 采样的次级余弦信号向量

从旋转变压器输出的采样的次级余弦波形。当使用正弦激励时，将此信号归一化，使其位于 [-1, 1] 范围内并以 0 为中心。

**数据类型：** `single` | `double` | `fixed point`

### **Reset** — 复位 PLL 标量

复位模块内部使用的锁相环。

#### 依赖

要启用此端口，请将 **Computation method** 参数设置为 `PLL`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **θm** — 电机机械位置标量

旋转变压器（及电机）的机械角位置，单位为度、弧度或标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **sinθe** — 电机电角度位置的正弦标量

电机电角度位置的正弦。

**数据类型：** `single` | `double` | `fixed point`

### **cosθe** — 电机电角度位置的余弦标量

电机电角度位置的余弦。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 电机机械速度标量

电机的机械速度，单位为度/秒、弧度/秒、RPM 或标幺值。

**数据类型：** `single` | `double` | `fixed point`

### **PLLEn** — PLL 状态标量

此端口指示模块内部使用的 PLL 的就绪状态。该端口可提供以下值：

- `1` — 表示 PLL（以及其他模块输出）已就绪可供使用。
- `0` — 表示 PLL（以及其他模块输出）尚未就绪。

#### 依赖

要启用此端口，请将 **Computation method** 参数设置为 `PLL`。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Computation method
  summary: 模块使用的计算方法 Arithmetic（默认）| PLL
  group: ''
- name: Block Output
  summary: 模块输出 Mechanical position（默认）| Sine and Cosine electrical position | Mechanical speed
  group: ''
- name: Number of pole-pairs for resolver
  summary: 旋转变压器极对数 1（默认）| 标量
  group: 输入参数
- name: Type of excitation method
  summary: 旋转变压器激励方法 Sinusoidal Excitation（默认）| Square Pulse Excitation
  group: 输入参数
- name: Enable input normalization
  summary: 启用模块对输入进行归一化 off（默认）| on
  group: 输入参数
- name: Discrete step size (s)
  summary: 模块再次执行前的采样时间 50e-6（默认）| 标量
  group: 输入参数
- name: Number of pole-pairs for motor
  summary: 电机极对数 3（默认）| 标量
  group: 正弦和余弦电角位置的输入
- name: Position offset (mechanical radians)
  summary: 旋转变压器机械位置偏移（以弧度为单位） 0（默认）| 标量
  group: 正弦和余弦电角位置的输入
- name: Integer rounding mode
  summary: 定点运算的舍入模式 Zero（默认）| Simplest
  group: 正弦和余弦电角位置的输入
- name: Phase delay (electrical radians)
  summary: 输入信号的相位延迟 0.1746（默认）| 标量
  group: Inputs for sinusoidal excitation method
- name: Number of samples per excitation cycle
  summary: 输入信号每周期采样数 16（默认）| 大于零的偶数标量
  group: Inputs for sinusoidal excitation method
- name: Maximum application frequency (Hz)
  summary: 最大可应用输入频率 7500（默认）| 标量
  group: PLL Parameters
- name: Speed filter cutoff frequency (Hz)
  summary: 低通滤波器的截止频率 10（默认）| 标量
  group: PLL Parameters
- name: Number of data points for lookup table
  summary: 查找表数组的大小 1024（默认）| 标量
  group: PLL Parameters
- name: Proportional (P)
  summary: 比例控制器增益 942.4778（默认）| 标量
  group: PLL Parameters
- name: Integral (I)
  summary: 积分控制器增益 222066.099（默认）| 标量
  group: PLL Parameters
- name: Error threshold (Hz)
  summary: PLL 误差阈值 2e-2（默认）| 标量
  group: PLL Parameters
- name: Position unit
  summary: 位置输出的单位 Radians（默认）| Degrees | Per-unit
  group: 输出参数
- name: Position data type
  summary: 角位置输出的数据类型 single（默认）| double | fixed point
  group: 输出参数
- name: Table data type
  summary: 正弦-余弦查找表的数据类型 single（默认）| double | fixed point
  group: 输出参数
- name: Speed unit
  summary: 速度输出的单位 Degrees/Sec（默认）| Radians/Sec | RPM | Per-unit
  group: 输出参数
- name: Speed data type
  summary: 角速度输出的数据类型 single（默认）| double | fixed point
  group: 输出参数
- name: Base speed (RPM)
  summary: 电机基准速度（RPM） 2000（默认）| 标量
  group: 输出参数
```

### **Computation method** — 模块使用的计算方法 `Arithmetic`（默认）| `PLL`

将 Resolver Decoder 模块设置为使用以下计算技术之一：

- `Arithmetic` — 使用基于算术方程和 atan2 运算的算法来计算模块输出。有关此技术的更多信息，请参阅本页中关于该技术的章节。
- `PLL` — 使用基于 PLL 的算法来计算模块输出。有关此技术的更多信息，请参阅 PLL with Feed Forward。

### **Block Output** — 模块输出 `Mechanical position`（默认）| `Sine and Cosine electrical position` | `Mechanical speed`

将 Resolver Decoder 模块设置为输出以下一项或多项：

- `Mechanical position` — 使模块能够计算电机机械位置。
- `Sine and Cosine electrical position` — 使模块能够计算电机电角度位置的正弦和余弦值。如果选择此值，模块将在 **Input Parameters** 选项卡中启用 **Inputs for Sine and Cosine electrical position** 部分。
- `Mechanical speed` — 使模块能够计算电机的机械速度。

**注意**

当使用 PLL 计算技术时，如果启用全部三个模块输出，则模块使用 PLL 计算正弦和余弦电角度位置及机械速度，但使用 `atan2` 函数计算机械位置。

### 输入参数

### **Number of pole-pairs for resolver** — 旋转变压器极对数 `1`（默认）| 标量

旋转变压器中可用的极对数。

### **Type of excitation method** — 旋转变压器激励方法 `Sinusoidal Excitation`（默认）| `Square Pulse Excitation`

用于获取次级正弦和余弦波形的旋转变压器激励方法。

### **Enable input normalization** — 启用模块对输入进行归一化 `off`（默认）| `on`

使用方波激励方法时，仅当您选择此参数，模块才会对次级正弦和余弦输入进行归一化。

#### 依赖关系

要启用此参数，请将 **Type of excitation method** 设置为 `Square Pulse Excitation`。

### **Discrete step size (s)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

每两次连续模块执行之间的固定时间间隔（以秒为单位）。

#### 依赖关系

- 如果将模块配置为使用算术计算方法，您可以通过选择 **Block Output** 部分中提供的 **Mechanical speed** 参数来启用此参数。
- 如果将模块配置为使用 PLL 计算方法，模块会始终启用此参数。

### 正弦和余弦电角位置的输入

### **Number of pole-pairs for motor** — 电机极对数 `3`（默认）| 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数，请将 **Block Output** 设置为 `Sine and Cosine electrical position`。

### **Position offset (mechanical radians)** — 旋转变压器机械位置偏移（以弧度为单位） `0`（默认）| 标量

旋转变压器机械位置与电机机械位置之间的偏移（以弧度为单位）。

#### 依赖关系

要启用此参数，请将 **Block Output** 设置为 `Sine and Cosine electrical position`。

### **Integer rounding mode** — 定点运算的舍入模式 `Zero`（默认）| `Simplest`

选择计算电机电角度正弦和余弦时所用定点运算的舍入模式。

- `Simplest` — 模块生成紧凑的舍入代码，计算速度更快。但是，随着时间推移，此模式可能会在正弦和余弦电角度输出中引入偏置。
- `Zero` — 模块确保舍入代码不会在正弦和余弦电角度输出中引入任何偏置。但是，这会导致计算速度较慢。

#### 依赖关系

要启用此参数，请将 **Block Output** 设置为 `Sine and Cosine electrical position`。

### Inputs for sinusoidal excitation method

### **Phase delay (electrical radians)** — 输入信号的相位延迟 `0.1746`（默认）| 标量

模块添加到 `Sin` 和 `Cos` 输入端口信号的相位延迟。

#### 依赖关系

要启用此参数，请将 **Type of excitation method** 设置为 `Sinusoidal Excitation`。

### **Number of samples per excitation cycle** — 输入信号每周期采样数 `16`（默认）| 大于零的偶数标量

`Sin` 和 `Cos` 输入端口信号一个周期内可用的采样数。

#### 依赖关系

要启用此参数，请将 **Type of excitation method** 设置为 `Sinusoidal Excitation`。

### PLL Parameters

### **Maximum application frequency (Hz)** — 最大可应用输入频率 `7500`（默认）| 标量

输入信号可能的最大频率（以赫兹为单位）。

#### 依赖关系

要启用此参数，请将 **Computation method** 参数设置为 `PLL`

### **Speed filter cutoff frequency (Hz)** — 低通滤波器的截止频率 `10`（默认）| 标量

模块用于对估计角频率进行滤波的低通滤波器的截止频率（以赫兹为单位）。

#### 依赖关系

要启用此参数，请将 **Computation method** 参数设置为 `PLL`

### **Number of data points for lookup table** — 查找表数组的大小 `1024`（默认）| 标量

模块提供给内部使用的 SinCos Embedded Optimized 模块的查找表数组大小。此参数接受 125 到 4095 之间的值。

#### 依赖关系

要启用此参数：

- 将 **Computation method** 参数设置为
  `PLL`。
- 选中 **Block Output** 部分中可用的 **Mechanical position** 参数。
- 清除 **Block Output** 部分中可用的 **Sine and Cosine electrical position**
  参数。

### **Proportional (P)** — 比例控制器增益 `942.4778`（默认）| 标量

该模块用于计算角频率的 PI 控制器的比例增益（*Kp*）。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`

### **Integral (I)** — 积分控制器增益 `222066.099`（默认）| 标量

该模块用于计算角频率的 PI 控制器的积分增益（*Ki*）。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`

点击 **Compute default parameters** 以计算近似比例增益（*Kp*）和积分增益
（*Ki*）并更新这些字段。

### **Error threshold (Hz)** — PLL 误差阈值 `2e-2`（默认）| 标量

由于闭环锁相环（PLL）中的动态特性，PLL 的输出需要时间才能达到稳态。此参数定义了一个阈值，模块使用该阈值来判断 PLL 是否已达到稳态。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`

### 输出参数

### **Position unit** — 位置输出的单位 `Radians`（默认）| `Degrees` | `Per-unit`

模块机械位置输出的单位。

#### 依赖关系

对于算术和 PLL 两种计算方法，仅当您选中 **Block Output** 部分中可用的 **Mechanical position** 参数时，模块才会启用此参数。

### **Position data type** — 角位置输出的数据类型 `single`（默认）| `double` | `fixed point`

角位置输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`，并选中 **Block Output**
部分中可用的 **Mechanical position** 参数。

### **Table data type** — 正弦-余弦查找表的数据类型 `single`（默认）| `double` | `fixed point`

模块使用的正弦-余弦查找表的数据类型。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`，并选中 **Block Output**
部分中可用的 **Mechanical position** 参数。

### **Speed unit** — 速度输出的单位 `Degrees/Sec`（默认）| `Radians/Sec` | `RPM` | `Per-unit`

模块机械速度输出的单位。

#### 依赖关系

对于算术和 PLL 两种计算方法，仅当您选中 **Block Output** 部分中可用的 **Mechanical speed** 参数时，模块才会启用此参数。

### **Speed data type** — 角速度输出的数据类型 `single`（默认）| `double` | `fixed point`

角速度输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Computation method**
参数设置为 `PLL`，并选中 **Block Output**
部分中可用的 **Mechanical speed** 参数。

### **Base speed (RPM)** — 电机基准速度（RPM） `2000`（默认）| 标量

电机的额定速度（以 RPM 为单位）。

#### 依赖关系

对于算术和 PLL 两种计算方法，仅当您选中 **Block Output** 部分中可用的 **Mechanical speed** 参数，然后将 **Speed unit** 设置为 `Per-Unit` 时，模块才会启用此参数。
## 所属库

Motor Control Blockset / Sensor Decoders

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

计算电机机械位置和速度以及电机电位置的 sine 和 cosine 值

Resolver Decoder 模块为连接到电机轴的旋转变压器计算以下内容：

- 电机的机械角位置
- 电机电角位置的 sine 和 cosine 值
- 电机的机械速度

旋转变压器使用一次励磁输入信号生成调制后的二次 sine 和 cosine 波形，然后由 ADC 采样。旋转变压器利用一绕组到两绕组的变换。由于这些二次绕组的设计和构造，sine 和 cosine 调制发生在二次绕组中，这些绕组的位置彼此相隔 90 度。

有关该模块所用算法的更多详细信息，请参见 。
