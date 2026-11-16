---
type: simulink-block
title: 'CDSP'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'cdsp'
documentation_source_path: 'infineonaurix/ref/cdsp.html'
language: zh-CN
chinese_source: worker-translation
---

# CDSP

## 端口

### 输入

### **primary input** — 来自 DSADC 模块、EXMOD、TMADC 模块或 GP 寄存器的输入数据 scalar

该端口接收来自 DSADC 模块、EXMOD、TMADC 模块或 GP 寄存器的传入数据，并根据应用采用不同的信号处理技术。对于 DSADC 模块，必须将 Result type 参数设置为 `Counts`，因为 CDSP 模块接受以 counts 为单位的数据。对于 GP 寄存器，该模块接受来自 Simulink® 源模块（例如 Repeating Sequence Stair 模块）的数据。

**注意**

- 在代码生成工作流中，该端口接收来自 DSADC 模块、EXMOD、TMADC 模块或 GP 寄存器的数据。
- 在仿真工作流中，该端口接收来自任何具有离散输出的 Simulink 源模块的数据。

**数据类型：** `uint16` | `int16`

### **secondary input** — 用于在 Math filter block 中使用的输入数据 scalar

该端口接收来自 DSADC 模块、EXMOD、TMADC 模块或 GP 寄存器的传入数据，并将此 secondary input 数据用于在 Math filter block 中与 CDSP secondary input 进行加法或减法运算。对于 DSADC 模块，必须将 Result type 参数设置为 `Counts`，因为 CDSP 模块接受以 counts 为单位的数据。

#### 依赖关系

要启用此端口，请将 **DSP filter chain** 参数设置为 `Advanced average 1 (FC1)`、`Basic data accumulation (FC2)` 或 `Advanced average 2 (FC4)`。这些选项中的任何一个都会添加 **Math** 选项卡，您必须在其中将 **Math operation** 参数设置为 `Addition with CDSP secondary input` 或 `subtraction with CDSP secondary input`

**数据类型：** `uint16` | `int16`
### 输出

### **filtereddata** — 16 位滤波后数据向量

该模块以 N×1 数组的形式输出 16 位值的滤波后数据。N 根据 timestamp、输出样本数和 FIFO depth 配置而变化。

输出的大小取决于模块中其他参数的值。

| Enable FIFO | Enable timestamp output | Number of output samples | FIFO depth | filtereddata 的大小 |
| --- | --- | --- | --- | --- |
| Disable | Disable | NA | NA | 1-by-1 |
| Enable | NA | NA | 1-by-1 |
| Enable | Disable | 1 | 4 | 4-by-1 |
| 3 | 3-by-1 |
| 2 | 2-by-1 |
| 1 | 1-by-1 |
| 2 | 4 | 4-by-1 |
| 2 | 2-by-1 |
| Enable | 1 | 4 | 3-by-1 |
| 3 | 2-by-1 |
| 2 | 1-by-1 |
| 2 | 4 | 3-by-1 |

如果 FIR 系数不变，则当您在 Block Parameters 对话框中将 **DSP Filter chain** 参数设置为 `Demo FIR (FC0)` 时，CDSP 模块使用默认滤波器系数。

**注意**

为避免使用该模块时出现数据类型转换错误，请确保将输出和输入数据设置为同一类型。

下表显示了当您向 CDSP 模块提供常量输入，并将 DSP Filter chain 参数设置为使用默认系数的 `Demo FIR (FC0)` 时，accumulation filter 的结果。该模块将默认系数值填充到 Coefficients 参数中。

| CDSP 输入 | 输出 `Data Type` | 累加滤波器结果 | 结果描述 |
| --- | --- | --- | --- |
| int16(100) | int16 | 100 |  |
| int16(32767) | int16 | 32767 |
| int16(0) | int16 | 0 |
| int16(-32768) | int16 | -32768 |
| uint16(100) | uint16 | 32768 | 100 + 32768 = 32868，CDSP 模块报告结果的低 16 位 |
| uint16(65535) | uint16 | 32767 | 65535 + 32768 = 98303，CDSP 模块报告 98303 (32767) 的低 16 位 |
| uint16(0) | uint16 | 32768 | 0 + 32768 = 32768，CDSP 模块报告结果的低 16 位 |
| uint16(32767) | uint16 | 65535 | 32767 + 32768 = 65535，CDSP 模块报告结果的低 16 位 |
| uint16(32768) | uint16 | 0 | 326768 + 32768 = 65536，CDSP 模块报告结果的低 16 位 |

从表中可以观察到，当输出数据的数据类型为 `uint16` 时，CDSP 硬件会向输出结果加上 32768 (2^15)。例如，假设 CDSP 硬件输出 1000 0000 0000 0000（16 位值）。如果将输出数据类型设置为 `int16`，则累加滤波器的结果为 -32767（(-2^15 \* 1) + (2^14 \* 0) + (2^13 \* 0) + ….. + (2^0 \* 0)）。当将输出数据类型设置为 `uint16` 时，累加滤波器的结果为 32768（(2^15 \* 1) + (2^14 \* 0) + (2^13 \* 0) + ….. + (2^0 \* 0)）。

**数据类型：** `uint16` | `int16`

### **timestamp** — 16 位计数器值的 timestamp `scalar`

该端口输出 timestamp 计数器的 16 位计数器值的状态。

#### 依赖关系

要启用此端口，请选择 **Enable timestamp output** 参数。

**数据类型：** `uint16`

## 参数

### Filter Config

### **Enable timestamp output** — 用于启用 timestamp 输出的选项 `off`（默认） | `on`

选择此参数以配置 **timestamp** 输出端口。

选择此参数会启用 CDSP Peripheral Configuration 中 **Timestamp** 选项卡中的选项以及 Timestamp event（位于 **Events** 选项卡下）。

**注意**

由于 timestamp 始终与 trigger 关联，因此建议在启用 timestamp 时相应地配置并提供 trigger。否则，FIFO 功能无法工作，因为 timestamp 会先被刷新到 FIFO，然后再到结果寄存器。

### **DSP Filter chain** — 用于选择滤波器链的选项 `Demo FIR (FC0)`（默认） | `Advanced average 1 (FC1)` | `Basic data accumulation (FC2)` | `Advanced median (FC3)` | `Advanced average 2 (FC4)` | `Basic AURIX (FCM)`

选择 CDSP 模块要使用的滤波器链。

- `Demo FIR (FC0)` — 选择此选项以使用 finite impulse response (FIR) filter block。
- `Advanced average 1 (FC1)` — 选择此选项以按预定义顺序使用滤波器块：FIR > sixth-order infinite impulse response filter (IIR6) > Math filter (MAT) > Average filter (AVG)。
- `Basic data accumulation (FC2)` — 选择此选项以按预定义顺序使用滤波器块：FIR > IIR6 > MAT > Data accumulation filter (DA)。
- `Advanced median (FC3)` — 选择此选项以按预定义顺序使用滤波器块：FIR > IIR6 > Median filter (MDN)。
- `Advanced average 2 (FC4)` — 选择此选项以按预定义顺序使用滤波器块：IIR6 > FIR > MAT > AVG。
- `Basic AURIX (FCM)` — 选择此选项以按预定义顺序使用滤波器块：FIR > first-order infinite impulse response filter (IIR1) > DA。

根据 **DSP filter chain** 参数的选择，该模块会在模块参数对话框中添加 **FIR、IIR6、IIR1、MAT、AVG** 和 **DA** 选项卡。您可以在这些选项卡中设置滤波块参数。

### **Output datatype** — 滤波输出的数据类型 `int16`（默认） | `uint16`

选择滤波输出的数据类型。

### Filter Config > FIFO Configuration

### **Enable FIFO** — 用于启用 FIFO 寄存器的选项 `off`（默认） | `on`

选择此参数以启用 first-in first-out (FIFO) 寄存器。

### **Elements to retrieve from FIFO** — 要从 FIFO 读取的输出样本 `1`（默认） | `2`

配置是一次读取单个样本还是两个样本。

选择 `2` 有助于更快地从 FIFO 获取数据。

#### 依赖关系

要启用此参数，请选择 **Enable FIFO** 参数。

### **FIFO depth** — FIFO 寄存器深度 `4`（默认） | `3` | `2` | `1`（仅当未选择 Enable Timestamp 时）

指定模块在其后生成服务请求的 FIFO 级别。

#### 依赖关系

要查看此参数，请选择 **Enable FIFO** 参数。

### FIR

### **Bypass FIR block** — 用于在滤波器链中绕过 FIR block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 FIR block。

### **Coefficients** — FIR 滤波器的系数 `[8, 13, -39, -130, -170, -135, -68, 27, 220, 424, 400, 124, -268, -617, -763, -604, -74, 655, 1244, 1419, 971, -26, -1390, -2569, -2842, -1783, 736, 4316, 8296, 11711, 13682, 13682, 11711, 8296, 4316, 736, -1783, -2842, -2569, -1390, -26, 971, 1419, 1244, 655, -74, -604, -763, -617, -268, 124, 400, 424, 220, 27, -68, -135, -170, -130, -39, 13, 8]`（默认） | 范围 (-32767 to 32767) 内的标量 | 范围 (-32767 to 32768) 内的向量

指定大小范围为 1×1 到 1×128 的 FIR 滤波器系数。

#### 依赖关系

要启用此参数，请禁用 **Bypass FIR block** 参数。

### **Decimation rate** — FIR 滤波器中输入数据速率与输出数据速率的比率 `1`（默认） | `2` | `4` | `8` | `16`

指定 FIR 滤波器中输入数据速率与输出数据速率的比率。

**注意**

- 在代码生成工作流中，该模块支持 1 到 16 的 decimation rate。
- 在仿真工作流中，该模块支持 decimation rate 为 1。

#### 依赖关系

要启用此参数，请禁用 **Bypass FIR block** 参数。

### IIR6

### **Bypass IIR6 block** — 用于在滤波器链中绕过 IIR6 filter block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 IIR6 filter block。

### **Coefficients** — IIR6 滤波器的系数 `[16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0, 16384, 0, 0]`（默认） | 范围 (-32767 to 32768) 内的向量

按照 [a00, a01, a02, a10, a11, a12, a20, a21, a22, b00, b01, b02, b10, b11, b12, b20, b21, b22] 的顺序指定 1×18 滤波器系数，用于具有以下传递函数的 IIR6 滤波器：

b00+b01z−1+b02z−2a00+a01z−1+a02z−2×b10+b11z−1+b12z−2a10+a11z−1+a12z−2×b20+b21z−1+b22z−2a20+a21z−1+a22z−2

#### 依赖关系

要启用此参数，请禁用 **Bypass IIR6 block** 参数。

### **Decimation rate** — IIR6 滤波器中输入数据速率与输出数据速率的比率 `1`（默认） | `2` | `4` | `8` | `16`

指定 IIR6 滤波器中输入数据速率与输出数据速率的比率。

**注意**

- 在代码生成工作流中，该模块支持 1 到 16 的 decimation rate。
- 在仿真工作流中，该模块支持 decimation rate 为 1。

#### 依赖关系

要启用此参数，请禁用 **Bypass IIR6 block** 参数。

### **Bit extension** — 在 IIR6 filter block 的输入和输出数据中移位的位数 `0`（默认） | 范围 (0, 7) 内的标量

指定在 IIR6 filter block 中移位的位数以提高精度。

#### 依赖关系

要启用此参数，请禁用 **Bypass IIR6 block** 参数。

### Math

### **Bypass math block** — 用于在滤波器链中绕过 Math filter block 的选项 `off`（默认） | `on`

选择以在滤波器链中绕过 Math filter block。

### **Math operation** — 用于选择数学运算的选项 `Addition with constant`（默认） | `Addition with CDSP secondary input` | `Subtraction with constant` | `Subtraction with CDSP secondary input` | `Multiplication with constant`

指定 Math filter 的数学运算。

如果选择 `Addition with CDSP secondary input` 或 `Subtraction with CDSP secondary input`，则 CDSP 模块会为 secondary input 添加一个输入端口。

#### 依赖关系

要启用此参数，请禁用 **Bypass math block** 参数。

### **Constant value (-32768 to 32767)** — 用于为数学运算提供常量值的选项 `0`（默认） | 范围 (-32768 to 32767) 内的标量

指定要在 Math filter 中使用的常量值。

#### 依赖关系

要启用此参数，请禁用 **Bypass math block** 参数，并将 **Math operation** 参数设置为 `Addition with constant`、`Subtraction with constant` 或 `Multiplication with constant`。

### **Bit shift after math operation (-32 to 32)** — 对 Math 滤波输出进行算术右移的位数 `0`（默认） | 范围 (-32 to 32) 内的标量

指定对 Math 滤波输出进行算术右移操作的位数，以便在发生溢出时校正输出。

#### 依赖关系

要启用此参数，请禁用 **Bypass math block** 参数。

### Average

### **Bypass avegare block** — 用于在滤波器链中绕过 AVG filter block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 AVG filter block。

### **Number of samples** — 用于选择 averaging operation 样本数的选项 `1`（默认） | `2` | `4` | `8` | `16` | `32` | `64` | `128`

指定 averaging operation 要考虑的样本数。

#### 依赖关系

要启用此参数，请禁用 **Bypass average block** 参数。

### Median

### **Bypass median block** — 用于在滤波器链中绕过 MDN filter block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 MDN filter block。

### **Number of samples** — 用于选择 median operation 样本数的选项 `1`（默认） | `3` | `5` | `7` | `9`

指定 median filter 要考虑的样本数。

#### 依赖关系

要启用此参数，请禁用 **Bypass median block** 参数。

### IIR1

### **Bypass IIR1 block** — 用于在滤波器链中绕过 IIR1 filter block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 IIR1 filter block。

#### 依赖关系

要启用此参数，请禁用 **Bypass IIR1 block** 参数。

### **Coefficients** — IIR6 滤波器的系数 `[16384, -12288, 16384, -16384]`（默认） | 范围 (-32767 to 32768) 内的向量

按照 [a0, a1, b0, b1] 的顺序指定 1×4 滤波器系数，用于具有以下传递函数的 IIR1 滤波器：

b0+b1z−1a0+a1z−1

#### 依赖关系

要启用此参数，请禁用 **Bypass IIR1 block** 参数。

### DA

### **Bypass DA block** — 用于在滤波器链中绕过 DA filter block 的选项 `off`（默认） | `on`

选择此参数以在滤波器链中绕过 DA filter block。

禁用此参数以在 CDSP Peripheral Configuration 工具的 **Integrator Control** 选项卡中配置 data accumulation 参数。

### **Samples in accumulation cycle** — 用于选择每个 accumulation cycle 的数据样本数的选项 `1`（默认） | 范围 (1, 512) 内的标量

指定每个 accumulation cycle 的数据样本数。

#### 依赖关系

要启用此参数，请禁用 **Bypass DA block** 参数。

### **Samples to discard** — 用于选择 accumulation process 期间要丢弃的数据样本数的选项 `0`（默认） | 范围 (0, 63) 内的标量

指定 accumulation process 期间要丢弃的数据样本数。

#### 依赖关系

要启用此参数，请禁用 **Bypass DA block** 参数。

### **Adjust gain by right shift on DA result** — 用于选择对 data accumulation filter 结果进行右移操作的位数的选项 `0`（默认） | 范围 (0, 10) 内的标量

指定用于对 DA 结果进行右移操作以进行增益调整的位数。

#### 依赖关系

要启用此参数，请禁用 **Bypass DA block** 参数。

### **Disable filter chain restart** — 用于禁止重新启动 DA filter block 之前所有 filter block 的选项 `off`（默认） | `on`

选择此参数以禁止重新启动所选滤波器链中 DA filter block 之前的所有 filter block。

#### 依赖关系

要启用此参数，请禁用 **Bypass DA block** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

处理来自 Infineon AURIX TC4x 的 ADC 外设的输出

CDSP 模块对来自 DSADC 模块（使用片上调制器或外部调制器 (EXMOD)）、TMADC 模块或通用 (GP) 寄存器的数字数据应用信号处理技术。根据您在 Converter Digital Signal Processing (CDSP) 模块中指定的滤波器属性和滤波器链，该模块将滤波后的数据输出为 16 位有符号和无符号整数。

当您启用 timestamp 输出时，该模块会提供一个额外的输出端口，以 16 位无符号值读取 timestamp。
