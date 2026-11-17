---
type: simulink-block
title: 'OFDM Demodulator'
family: 'wireless-hdl'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'ofdmdemodulator'
documentation_source_path: '../wireless-hdl/ref/ofdmdemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# OFDM Demodulator

## 端口
```yaml
ports:
- name: data
  summary: 输入数据 标量 | 列向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: 指示有效输入数据 标量
  direction: input
  data_types: Boolean
- name: FFTLen
  summary: FFT 长度 标量
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: CPLen
  summary: 循环前缀长度 标量
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: numLgSc
  summary: OFDM 符号左侧保护载波数 标量
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: numRgSc
  summary: OFDM 符号右侧保护载波数 标量
  direction: input
  data_types: single | double | uint8 | uint16 | uint32 | unsigned fixed point
- name: CPFraction
  summary: CP 比例 实数正标量
  direction: input
  data_types: single | double | unsigned fixed point
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 解调输出数据 标量 | 列向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | signed fixed point
- name: valid
  summary: 指示有效输出数据 标量
  direction: output
  data_types: Boolean
- name: ready
  summary: 指示模块已就绪 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入数据 标量 | 列向量

输入数据，指定为实数或复数值的标量或列向量。向量大小必须是 2 的幂，范围从 1 到 64，并且小于或等于 FFT 长度。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输入数据 标量

指示有效输入数据，指定为标量。

此端口是一个控制信号，用于指示 **data** 输入端口上的采样何时有效。当此值为 `1` 时，模块捕获 **data** 输入端口上的值。当此值为 `0` 时，模块忽略 **data** 输入端口上的值。

**数据类型：** `Boolean`

### **FFTLen** — FFT 长度 标量

FFT 的长度，指定为标量。FFT 长度必须是 2 的幂，范围从 8 到 65,536。此值必须小于或等于 **Maximum FFT length** 参数值。

为支持最小 FFT 长度 8，**FFTLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPLen** — 循环前缀长度 标量

循环前缀的长度，指定为范围从 0 到 **FFTLen** 的标量。

为支持最小 FFT 长度 8，**CPLen** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 4。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numLgSc** — OFDM 符号左侧保护载波数 标量

OFDM 符号左侧保护载波数，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为支持最小 FFT 长度 8，**numLgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **numRgSc** — OFDM 符号右侧保护载波数 标量

OFDM 符号右侧保护载波数，指定为范围从 0 到 (**FFTLen**/2) – 1 的标量。

为支持最小 FFT 长度 8，**numRgSc** 数据类型必须为 `fixdt(0,k,0)`，其中 *k* 大于或等于 2。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `uint32` | `unsigned fixed point`

### **CPFraction** — CP 比例 实数正标量

CP 比例，指定为范围 [0, 1] 内的实数正标量。

为支持最大精度，**CPFraction** 数据类型必须为 `fixdt(0,k,p)`，其中 *k* 小于或等于 16，*p* 等于 *k* - 1。

#### 依赖关系

要启用此端口，请选择 **Enable CP fraction** 参数，并将 **CP fraction source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `unsigned fixed point`

### **reset** — 清除内部状态 标量

清除内部状态，指定为标量。当此值为 `1`（true）时，模块停止当前计算并清除所有内部状态。

#### 依赖关系

要启用此端口，请选择 **Enable reset input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 解调输出数据 标量 | 列向量

解调输出数据，以复数值标量或列向量形式返回。输出数据类型取决于输入 **data** 端口的数据类型。

- 当您将 **OFDM parameters source** 参数设置为 `Property` 并清除 **Divide butterfly outputs by two** 参数时，输出字长增加 log2(*FFTLength*) 位。
- 当您将 **OFDM parameters source** 参数设置为 `Input port` 并清除 **Divide butterfly outputs by two** 参数时，输出字长增加 log2(*MaxFFTLength*) 位。

为避免溢出，请选择 **Divide butterfly outputs by two** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 指示有效输出数据 标量

指示有效输入数据，以标量形式返回。

此端口是一个控制信号，用于指示 **data** 输出端口何时有效。当 **data** 输出端口上有数据采样可用时，模块将此值设置为 `1`。当您选择 **Remove DC subcarrier** 参数时，此值在输出采样的中心处设置为 `0`，以排除 DC 载波。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

控制信号，用于指示模块何时准备好接收新的输入数据。当此值为 `1` 时，模块在下一个时间步接受输入数据。当此值为 `0` 时，模块在下一个时间步忽略输入数据。

#### 依赖关系

要启用此端口，请将 **OFDM parameters source** 参数设置为 `Input port`。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: OFDM parameters source
  summary: OFDM 参数来源 Property（默认）| Input port
  group: 主
- name: Maximum FFT length
  summary: FFT 最大长度 长度 64（默认）| 范围从 8 到 65,536 的 2 的幂
  group: 主
- name: FFT length
  summary: FFT 长度 64（默认）| 范围从 8 到 65,536 的 2 的幂
  group: 主
- name: Cyclic prefix length
  summary: 循环前缀长度 16（默认）| 范围从 0 到 *FFTLength* 的整数
  group: 主
- name: Number of left guard subcarriers
  summary: OFDM 符号最左侧的保护频带子载波数 6（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数
  group: 主
- name: Number of right guard subcarriers
  summary: OFDM 符号最右侧的保护频带子载波数 5（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数
  group: 主
- name: Enable CP fraction
  summary: CP 比例使能 off（默认）| on
  group: 主
- name: CP fraction source
  summary: CP 比例来源类型 Property（默认）| Input port
  group: 主
- name: CP fraction
  summary: 要移除的循环前缀百分比 0.55（默认）| 范围从 0 到 1
  group: 主
- name: Remove DC subcarrier
  summary: 排除或包含 DC 子载波 on（默认）| off
  group: 主
- name: Enable reset input port
  summary: 复位信号 off（默认）| on
  group: 主
- name: Divide butterfly outputs by two
  summary: 将 FFT 蝶形输出除以二 off（默认）| on
  group: FFT 参数
- name: Rounding Method
  summary: 内部定点计算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Zero
  group: FFT 参数
```

### 主

### **OFDM parameters source** — OFDM 参数来源 `Property`（默认）| `Input port`

您可以通过输入端口或为参数选择值来设置 OFDM 参数。

选择 `Property` 以启用 **FFT length**、**Cyclic prefix length**、**Number of left guard subcarriers** 和 **Number of right guard subcarriers** 参数。

选择 `Input port` 以启用 **FFTLen**、**CPLen**、**numLgSc**、**numRgSc** 输入端口和 **Maximum FFT length** 参数。**Maximum FFT length** 参数设置 **FFTLen** 输入端口有效值范围的上限。

### **Maximum FFT length** — FFT 最大长度 长度 `64`（默认）| 范围从 8 到 65,536 的 2 的幂

指定 FFT 的最大长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Input port`。

### **FFT length** — FFT 长度 `64`（默认）| 范围从 8 到 65,536 的 2 的幂

指定 FFT 长度。当您将 **OFDM parameters source** 参数设置为 `Property` 时，模块将此 FFT 长度值用作最大 FFT 长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Cyclic prefix length** — 循环前缀长度 `16`（默认）| 范围从 0 到 *FFTLength* 的整数

指定循环前缀的长度。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Number of left guard subcarriers** — OFDM 符号最左侧的保护频带子载波数 `6`（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数

指定左侧保护子载波的数量。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Number of right guard subcarriers** — OFDM 符号最右侧的保护频带子载波数 `5`（默认）| 范围从 0 到 (*FFTLength*/2) – 1 的整数

指定右侧保护子载波的数量。

#### 依赖关系

要启用此参数，请将 **OFDM parameters source** 参数设置为 `Property`。

### **Enable CP fraction** — CP 比例使能 `off`（默认）| `on`

选择此参数以通过 `Property` 或 `Input port` 启用 CP 比例。

### **CP fraction source** — CP 比例来源类型 `Property`（默认）| `Input port`

您可以通过输入端口或为参数选择值来设置 CP 比例。

选择 `Property` 以启用 **CP fraction** 参数。

选择 `Input port` 以启用 **CPFraction** 输入端口。

#### 依赖关系

要启用此参数，请选择 **Enable CP fraction** 参数。

### **CP fraction** — 要移除的循环前缀百分比 `0.55`（默认）| 范围从 0 到 1

循环前缀比例，指定为从 0 到 1（含）的值。此参数指定模块从 OFDM 符号起始处移除的 CP 采样百分比。模块将剩余的 CP 采样移位到 OFDM 符号的末尾。

当此参数为 `0.55` 时，模块从符号起始处移除 55% 的 CP，并将 45% 移位到符号末尾。当您将此参数设置为 `1` 时，模块从 OFDM 符号起始处移除 100% 的 CP，并且不移位任何采样到末尾。

#### 依赖关系

要启用此参数，请选择 **Enable CP fraction** 参数，并将 **CP fraction source** 参数设置为 `Property`。

### **Remove DC subcarrier** — 排除或包含 DC 子载波 `on`（默认）| `off`

当您选择此参数时，模块通过在输出子载波的中心处将输出有效信号设置为 `0`，从而在输出中排除 DC 子载波。

### **Enable reset input port** — 复位信号 `off`（默认）| `on`

选择此参数以启用 **reset** 输入端口。

### FFT 参数

### **Divide butterfly outputs by two** — 将 FFT 蝶形输出除以二 `off`（默认）| `on`

此参数控制 OFDM Demodulator 模块内部 FFT 模块的缩放选项。

当您选择此参数时，FFT 通过将每个蝶形乘法的输出除以二来实现总体 1/*N* 缩放因子。此调整使 FFT 的输出保持与其输入相同的幅度范围。如果您清除此参数，模块通过在每次蝶形乘法后将字长增加一位来避免溢出。

### **Rounding Method** — 内部定点计算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

此参数指定内部定点计算的舍入模式类型。有关舍入模式的详细信息，请参阅舍入模式。当输入为任何整数数据类型或定点数据类型时，FFT 算法使用定点算术进行内部计算。当输入为 `single` 或 `double` 数据类型时，此参数不适用。舍入适用于旋转因子乘法和缩放操作。
## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

此模块没有任何 HDL 模块属性。

## 版本历史

**在 R2019b 中引入**

### R2023a：CP 比例作为输入端口

您现在可以通过端口指定 CP 比例。要启用此端口，请选择 **Enable CP fraction** 参数，并将 **CP fraction source** 参数设置为 `Input port`。

## 描述

解调时域 OFDM 采样并返回用于自定义通信协议的子载波

OFDM Demodulator 模块解调时域正交频分复用（OFDM）采样，并根据 OFDM 参数输出子载波。该模块支持 5G 新空口（NR）标准、长期演进（LTE）[1]、无线局域网（WLAN 802.11a/g/n/ac）[2]、WiMAX、数字视频广播（DVB）和数字音频广播（DAB）标准。

该模块接受输入数据以及有效控制信号和以下 OFDM 参数：FFT 长度、CP 长度以及左右保护子载波数。该模块输出解调数据以及 valid 和 ready 控制信号。仅当这些 OFDM 参数通过输入端口提供给模块时，模块才启用 **ready** 输出端口。模块仅在 **ready** 端口为 `1`（高）且每个 OFDM 符号的第一个 **valid** 端口为 `1`（高）时采样相应的 OFDM 参数。

该模块支持标量和向量输入。您可以使用向量输入来提高数据吞吐量并实现千兆采样每秒（GSPS）的吞吐量。该模块提供适合 HDL 代码生成和硬件部署的接口和架构。
