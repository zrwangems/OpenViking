---
type: simulink-block
title: 'M-PAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Amplitude Modulation'
documentation_page: 'mpamdemodulatorbaseband'
documentation_source_path: 'ref/mpamdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PAM Demodulator Baseband

## 端口

### 输入

### **In** — *M*-PAM 调制信号 标量 | 列向量

*M*-PAM 调制信号，指定为标量或列向量。此端口在模块上未命名。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes
### 输出

### **Out** — 解调信号 标量 | 向量

解调信号，以标量或向量形式返回。解调信号的维度取决于您为 **Output data type** 参数指定的值。此端口在模块上未命名。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **M-ary number** — 调制阶数 `4`（默认）| 正偶数整数

调制阶数，指定为正偶数整数。调制阶数 *M* 指定信号星座中的点数。该模块根据 **Normalization method** 参数的设置方式来缩放信号星座。

### **Output type** — 输出类型 `Integer`（默认）| `Bit`

输出类型，指定为 `Integer` 或 `Bit`。当您将此参数设置为 `Bit` 时，**M-ary number** 参数必须为 2*K*，其中 *K* 为某个正整数。

### **Constellation ordering** — 符号映射顺序 `Binary`（默认）| `Gray`

符号的映射顺序，指定为 `Gray` 或 `Binary`。此参数决定模块如何将每个符号映射到输出位组或整数。

**Constellation ordering** 参数指示模块如何将二进制字分配给信号星座的点。有关详细信息，请参阅 Integer-Valued Signals and Binary-Valued Signals。

### **Normalization method** — 星座的缩放方法 `Min. distance between symbols`（默认）| `Average Power` | `Peak Power`

星座的缩放方法，指定为 `Min. distance between symbols`、`Average Power` 或 `Peak Power`。有关详细信息，请参阅 Integer-Valued Signals and Binary-Valued Signals。

### **Minimum distance** — 两个最近星座点之间的距离 `2`（默认）| 正标量

两个最近星座点之间的距离，指定为正标量。

#### 依赖项

当您将 **Normalization method** 设置为 `Min. distance between symbols` 时，此参数出现。

### **Average power, referenced to 1 ohm (watts)** — 平均功率 `1`（默认）| 正标量

星座中符号的平均功率，以 watts 为单位，指定为正标量。功率值假设标称阻抗为 1 ohm。

#### 依赖项

当您将 **Normalization method** 设置为 `Average Power` 时，此参数出现。

### **Peak power, referenced to 1 ohm (watts)** — 最大功率 `1`（默认）| 正标量

星座中符号的最大功率，以 watts 为单位，指定为正标量。功率值假设标称阻抗为 1 ohm。

#### 依赖项

当您将 **Normalization method** 设置为 `Peak Power` 时，此参数出现。

### 数据类型

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输出数据类型，指定为 `Inherit via internal rule`、`Smallest unsigned integer`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

- 当您选择 `Inherit via internal rule` 时，模块基于内部规则继承数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。如果输入的类型为 `single` 或 `double`，则输出数据类型与输入数据类型相同。否则，输出数据类型与 `'Smallest unsigned integer'` 相同。
- 当您选择 `'Smallest unsigned integer'` 时，模块根据 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中的设置来设置输出数据类型。如果在 **Hardware Implementation** 窗格中选择了 `ASIC/FPGA`，则输出数据类型为理想最小大小，即对于位输出为 `ufix(1)`，对于整数输出为 `ufix(ceil(log2(M)))`。对于所有其他选择，它是具有最小可用字长的无符号整数，该字长足够大以适合理想最小大小，通常对应于 char 的大小（例如 `uint8`）。
- 对于整数输出，您可以将此参数设置为 `Smallest unsigned integer`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`single` 和 `double`。对于位输出，选项为 `Smallest unsigned integer`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single` 或 `double`。

有关指定数据类型的信息，请参阅 Data Type Assistant。

### **Denormalization factor** — 去归一化因子数据类型 `Inherit: Same word length as input`（默认）| `fixdt(1,16)` | `<data type expression>`

将去归一化因子数据类型指定为 `Inherit: Same word length as input`、`fixdt(1,16)` 或 `<data type expression>`。此缩放因子派生自 **Normalization method** 和模块的其他参数。模块始终使用最佳精度小数长度。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖项

此参数仅当输入信号为定点且派生的去归一化因子为非单位值（不等于 1）时适用。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `fixdt(1,16)` | `<data type expression>`

将乘积数据类型指定为 `Inherit: Inherit via internal rule`、`fixdt(1,16)` 或 `<data type expression>`。

当您选择 `Inherit: Inherit via internal rule` 时，模块计算全精度乘积字长和小数长度。有关全精度 **Product output** 内部规则的信息，请参阅 Internal Rule for Product Data Types。

当定点计算的结果不能精确映射到由存储结果的数据类型和定标所表示的数字时，模块使用舍入模式。有关详细信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖项

此参数仅当输入为定点信号且派生的去归一化因子为非单位值（不等于 1）时适用。

### **Rounding mode** — 定点运算的舍入模式 `Wrap`（默认）| `Saturate`

将 **Product output** 定点运算的舍入模式指定为 `Wrap` 或 `Saturate`。当定点计算的结果不能精确映射到可由该数据类型表示的数字时，模块使用舍入模式。有关详细信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

#### 依赖项

此参数仅适用于 **Product output**。

### **Saturate on integer overflow** — 在整数溢出时饱和的选项 `off`（默认）| `on`

选中此复选框可在整数溢出时饱和。

#### 依赖项

此参数仅适用于 **Product output**。

### **Sum** — 和数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as product output` | `fixdt(1,16)` | `<data type expression>`

将和数据类型指定为 `Inherit: Inherit via internal rule`、`Inherit: Same as product output`、`fixdt(1,16)` 或 `<data type expression>`。

- 当您选择 `Inherit: Inherit via internal rule` 时，模块基于定点硬判决算法信号流程图中求和的两个输入，计算全精度和字长和小数长度。该规则与 Sum (Simulink) 模块中内部 **Accumulator data type** 参数的定点继承规则相同。
- 当您选择 `Inherit: Same as product output` 且 **Product output** 适用时，模块将 **Sum** 参数的数据类型配置为与 **Product output** 数据类型相同。
- 当您选择 `Inherit: Same as product output` 且 **Product output** 不适用时，模块忽略此设置并使用 `Inherit: Inherit via internal rule` 和计算得到的和。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖项

此参数仅当输入为定点信号时适用。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 定点输入必须为有符号。  b 当在 Hardware Implementation Pane 中选择 ASIC/FPGA 时，对于位输出，输出为 ufix(1)；对于整数输出，输出为 ufix(ceil(log2(M)))。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调 M-PAM 调制数据

M-PAM Demodulator Baseband 模块解调使用 *M* 进制脉冲幅度调制进行调制的信号。

**注意**

所有功率值均假设标称阻抗为 1 ohm。
