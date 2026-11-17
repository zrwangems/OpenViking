---
type: simulink-block
title: 'Variable Fractional Delay'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'variablefractionaldelay'
documentation_source_path: 'ref/variablefractionaldelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Fractional Delay

## 端口

### 输入

### **In** — 数据输入 向量 | 矩阵

将数据输入指定为向量或矩阵。数据输入必须与延迟输入具有相同的数据类型。

此模块支持可变大小输入信号。也就是说，您可以在仿真期间更改输入行数。但是，通道数必须保持不变。

**示例：** [1 2 3 4;5 1 4 2;2 6 2 3;1 2 3 2;3 4 5 6;1 2 3
1]

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Delay** — 延迟输入 标量 | 向量 | 矩阵 | *N* 维数组

以采样为单位将延迟输入指定为标量、向量、矩阵或 *N* 维数组。延迟可以是整数值或小数值。该模块对信号进行插值，以在非整数采样间隔处获得新采样。延迟输入必须与数据输入具有相同的数据类型。

模块对话框显示以采样为单位的有效延迟范围。该模块根据模块对话框中的设置确定此范围。如果您指定的延迟值小于最小可接受值，该模块将执行您在 **For small input delay values** 参数中选择的操作。如果您将 **Interpolation mode** 设置为 `Linear`，则最小可接受值为 0。

如果您指定的延迟值大于最大可接受值，该模块会将延迟值裁剪到最大值。

此模块支持可变大小延迟信号。也就是说，您可以在仿真期间更改延迟信号的一个或两个维度。但是，该模块必须确保生成的输出通道数在整个仿真过程中保持不变。

当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，下表显示了延迟输入的维度对数据输入的影响。有关示例，请参阅 Delay Signal Using Multitap Fractional Delay。

| 数据输入 | 延迟输入 | 输出 | 延迟输入对数据输入的影响 |
| --- | --- | --- | --- |
| *N*（无方向，一个通道） | 标量 | 无方向 (N) | 一个延迟值应用于输入通道 |
| *N*（无方向，一个通道） | 无方向 (N) | 无方向 (N) | 延迟值在帧内逐采样变化 |
| *N*（无方向，一个通道） | 1×*P* | *N*×*P* | *P* 个抽头。输出中的每一列是输入的延迟版本。延迟值由延迟输入向量中的对应元素指定。 |
| *N*（无方向，一个通道） | *N*×*P* | *N*×*P* | *P* 个抽头。此外，延迟在每个帧内逐采样变化。 |
| *N*×1（一个通道，帧大小等于 *N*） | 标量 | *N*×1 | 一个延迟值应用于输入通道 |
| *N*×1（一个通道，帧大小等于 *N*） | 无方向 (N) | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×1 | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | 1×*P* | *N*×*P* | *P* 个抽头。输出中的每一列是输入的延迟版本。延迟值由延迟输入向量中的对应元素指定。 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×*P* | *N*×*P* | *P* 个抽头。此外，延迟在每个帧内逐采样变化。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 标量 | *N*×*L* | 一个延迟值应用于所有输入通道 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×*L* | *N*×*L* | 每个输入通道有唯一的延迟值 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×1 | *N*×*L* | 延迟值在帧内逐采样变化。所有通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×*L* | *N*×*L* | 延迟值在帧内逐采样变化。每个输入通道有不同的延迟值。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×1×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。所有通道使用相同的延迟。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×*L*×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。抽头因通道而异。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×1×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。延迟在帧内逐采样变化。每个通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×*L*×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。延迟在帧内逐采样变化。每个通道使用不同的延迟值集合。 |

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，下表显示了延迟输入的维度对数据输入的影响。

| 数据输入 | 延迟输入 | 输出 | 延迟输入对数据输入的影响 |
| --- | --- | --- | --- |
| *N*（无方向，一个通道） | 标量 | 无方向 (N) | 一个延迟值应用于输入通道 |
| *N*（无方向，一个通道） | 无方向 (N) | 无方向 (N) | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | 标量 | *N*×1 | 一个延迟值应用于输入通道 |
| *N*×1（一个通道，帧大小等于 *N*） | 无方向 (N) | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×1 | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | 标量 | *N*×*L* | 一个延迟值应用于所有输入通道 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | 1×*L* | *N*×*L* | 每个输入通道有唯一的延迟值 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | *N*×1 | *N*×*L* | 延迟值在帧内逐采样变化。所有通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | *N*×*L* | *N*×*L* | 延迟值在帧内逐采样变化。每个输入通道有不同的延迟值。 |

**示例：** [2 3 4 5]

**示例：** [2.5]

**示例：** [5.6]

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 延迟输出 向量 | 矩阵

延迟输出，以向量或矩阵形式返回。输出的数据类型和复数性与数据输入的数据类型和复数性匹配。

当 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，下表显示了延迟输入的维度对数据输入的影响。

| 数据输入 | 延迟输入 | 输出 | 延迟输入对数据输入的影响 |
| --- | --- | --- | --- |
| *N*（无方向，一个通道） | 标量 | 无方向 (N) | 一个延迟值应用于输入通道 |
| *N*（无方向，一个通道） | 无方向 (N) | 无方向 (N) | 延迟值在帧内逐采样变化 |
| *N*（无方向，一个通道） | 1×*P* | *N*×*P* | *P* 个抽头。输出中的每一列是输入的延迟版本。延迟值由延迟输入向量中的对应元素指定。 |
| *N*（无方向，一个通道） | *N*×*P* | *N*×*P* | *P* 个抽头。此外，延迟在每个帧内逐采样变化。 |
| *N*×1（一个通道，帧大小等于 *N*） | 标量 | *N*×1 | 一个延迟值应用于输入通道 |
| *N*×1（一个通道，帧大小等于 *N*） | 无方向 (N) | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×1 | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | 1×*P* | *N*×*P* | *P* 个抽头。输出中的每一列是输入的延迟版本。延迟值由延迟输入向量中的对应元素指定。 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×*P* | *N*×*P* | *P* 个抽头。此外，延迟在每个帧内逐采样变化。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 标量 | *N*×*L* | 一个延迟值应用于所有输入通道 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×*L* | *N*×*L* | 每个输入通道有唯一的延迟值 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×1 | *N*×*L* | 延迟值在帧内逐采样变化。所有通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×*L* | *N*×*L* | 延迟值在帧内逐采样变化。每个输入通道有不同的延迟值。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×1×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。所有通道使用相同的延迟。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | 1×*L*×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。抽头因通道而异。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×1×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。延迟在帧内逐采样变化。每个通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，帧大小等于 *N*） | *N*×*L*×*P* | *N*×*L*×*P* | *L* 个通道。每个通道 *P* 个抽头。延迟在帧内逐采样变化。每个通道使用不同的延迟值集合。 |

当 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，下表显示了延迟输入的维度对数据输入的影响。

| 数据输入 | 延迟输入 | 输出 | 延迟输入对数据输入的影响 |
| --- | --- | --- | --- |
| *N*（无方向，一个通道） | 标量 | 无方向 (N) | 一个延迟值应用于输入通道 |
| *N*（无方向，一个通道） | 无方向 (N) | 无方向 (N) | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | 标量 | *N*×1 | 一个延迟值应用于输入通道 |
| *N*×1（一个通道，帧大小等于 *N*） | 无方向 (N) | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×1（一个通道，帧大小等于 *N*） | *N*×1 | *N*×1 | 延迟值在帧内逐采样变化 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | 标量 | *N*×*L* | 一个延迟值应用于所有输入通道 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | 1×*L* | *N*×*L* | 每个输入通道有唯一的延迟值 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | *N*×1 | *N*×*L* | 延迟值在帧内逐采样变化。所有通道使用相同的延迟值集合。 |
| *N*×*L*（*L* 个通道，每个通道 *N* 个采样） | *N*×*L* | *N*×*L* | 延迟值在帧内逐采样变化。每个输入通道有不同的延迟值。 |

**示例：** [0 0 0 0;0 0 0 0;1 0 0 0;5 2 0 0;2 1 3 0;1 6 4
4]

**示例：** [0 0 0 0;0 0 0 0;0.5 1.0 1.5 2.0;3 1.5 3.5 3.0;3.5 3.5 3.0
2.5;1.5 4.0 2.5 2.5]

**示例：** [0 0 0 0;0 0 0 0;0 0 0 0;0 0 0 0;0 0 0 0;0.4 0.8 1.2
1.6]

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

## 参数

### **Interpolation mode** — 插值方法 `Linear`（默认）| `FIR` | `Farrow`

指定插值方法。使用此方法，该模块对信号进行插值，以在非整数采样间隔处获得新采样。

- `Linear` —— 线性插值。在此模式下，该模块为每个通道存储 **In** 端口接收到的最近 **Dmax**+1 个采样。**Dmax** 是您在 **Maximum delay (Dmax) in samples** 参数中指定的值。
- `FIR` —— 多相 FIR 插值。在此模式下，该模块为每个通道存储 **In** 端口接收到的最近 **Dmax**+**P**+1 个采样。**P** 是您在 **Interpolation filter half-length (P)** 参数中指定的值。
- `Farrow` —— LaGrange 方法。在此模式下，该模块为每个通道存储 **In** 端口接收到的最近 **Dmax**+N2+1 个采样。**N** 是您在 **Farrow filter length (N)** 参数中指定的值。

有关这些方法的更多详细信息，请参阅算法。

### **Interpolation filter half-length (P)** — 插值滤波器半长度 `4`（默认）| 范围 [1 65535] 内的正整数

FIR 插值滤波器的半长度。对于周期信号，此属性的较大值（表示更高阶的滤波器）可以更好地估计延迟输出采样。属性值为 4 到 6（对应于 7 阶到 11 阶滤波器）通常就足够了。

**示例：** `6`

**示例：** `10`

#### 依赖关系

此参数仅在将 **Interpolation mode** 设置为 `FIR` 时适用。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Interpolation points per input sample** — 每个输入采样的插值点数 `10`（默认）| 范围 [2, 65,535] 内的正整数

每个输入采样中计算唯一 FIR 插值滤波器的插值点数。

**示例：** `20`

**示例：** `5`

#### 依赖关系

此参数仅在将 **Interpolation mode** 设置为 `FIR` 时适用。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Normalized input bandwidth (0 to 1)** — 归一化输入带宽 `1`（默认）| 范围 (0, 1] 内的实标量

用于约束插值输出采样的归一化输入带宽。值 `1` 等于奈奎斯特频率，即采样频率 *Fs* 的一半。使用此属性可以利用输入的带限频率内容。例如，如果输入信号没有高于 *Fs*/4 的频率内容，您可以指定值 `0.5`。

**示例：** `0.5`

**示例：** `0.8`

#### 依赖关系

此参数仅在将 **Interpolation mode** 设置为 `FIR` 时适用。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Farrow filter length (N)** — Farrow 滤波器长度 `4`（默认）| 大于或等于 2 的整数

使用 Farrow 结构实现的 FIR 滤波器长度。如果长度等于 2，则滤波器执行线性插值。

**示例：** `4`

**示例：** `10`

#### 依赖关系

此参数仅在将 **Interpolation mode** 设置为 `Farrow` 时适用。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Maximum delay (Dmax) in samples** — 最大延迟 `100`（默认）| 范围 [0 65535] 内的整数

该模块可以产生的最大延迟 **Dmax**。超过此最大值的输入延迟值将被裁剪到 **Dmax**。

**示例：** 200

**示例：** 500

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **输入处理** — 处理输入的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

指定模块应如何处理输入。您可以将此参数设置为以下选项之一：

- `Columns as channels (frame based)`
  （默认）— 当您选择此选项时，模块将输入的每一列视为单独的通道。模块将 *R* 个输入列中的每一列视为包含 *Mi* 个顺序时间样本的独立通道。

  **Delay** 端口的输入 *v* 包含浮点值，用于指定延迟当前输入的采样间隔数。

  **Delay** 端口的输入可以是标量值，以均匀延迟每个通道中的每个样本。它也可以是长度为 *M* 的列向量，包含输入帧中每个样本的一个延迟值。模块将向量中包含的延迟集合相同地应用于多通道输入的每个通道。**Delay** 端口输入也可以是长度为 *R* 的行向量，包含每个通道的一个延迟值。最后，**Delay** 端口输入可以是 *M*×*R* 矩阵，包含输入中每个对应元素的不同延迟值。

  例如，如果 *v* 是 *Mi*×1 矩阵
  `[v(1) v(2) ... v(Mi)]'`，则当前帧中最早的样本被延迟 `v(1)` 个分数采样间隔，帧中的下一个样本被延迟 `v(2)` 个分数采样间隔，依此类推。模块将 *v* 中包含的分数延迟集合相同地应用于多通道输入的每个通道。
- `Elements as channels (sample based)` ——
  当您选择此选项时，模块将输入的每个元素视为单独的通道。模块将 N 维输入数组 *u* 的每个元素视为独立通道。**Delay** 端口的输入 *v* 必须是大小和维度与输入 *u* 相同的 N 维数组，或者是标量值，使得 *Dmin* ≤ *v* ≤ *Dmax*。

  例如，考虑一个 *M*×*R* 输入矩阵。模块将 *M*\**R* 个矩阵元素中的每一个视为独立通道。**Delay** 端口的输入可以是 *M*×*R* 的浮点值矩阵，范围在 *Dmin* ≤ *v* ≤ *Dmax* 内，用于指定延迟输入每个通道的采样间隔数，也可以是标量浮点值 *Dmin* ≤ *v* ≤ *Dmax*，用于均匀延迟所有通道。

  在基于样本的处理模式下，模块将无方向向量输入视为 *M*×1 矩阵。在此模式下，输出也是无方向向量。

### **InitialConditions** — 存储器中的初始值 `0`（默认）| 标量 | 1×*R*×*D* 数组 | 1×*R*×(*D*+*L*) 数组

指定仿真开始时模块存储器中的值。此参数的维度可以根据您需要固定初始条件还是时变初始条件而变化。模块将 *R* 个输入列中的每一列视为包含来自独立通道的 *M* 个顺序时间样本的帧。

对于 *M*×*R* 输入矩阵 *u*，您可以按如下方式设置此参数：

- 要指定固定初始条件，请将此参数设置为标量值。模块使用您指定的值初始化存储器中每个通道的每个样本。
- 您为时变初始条件指定的维度取决于插值方法。要为每个通道指定不同的时变初始条件，请按如下方式设置此参数：

  - 如果您将 **Interpolation mode** 设置为 `Linear`，请将 **Initial conditions** 设置为大小为 `1`×*R*×*D* 的数组，其中 *D* 是 **Maximum delay (Dmax) in samples** 参数中的值。
  - 如果您将 **Interpolation mode** 设置为 `FIR` 或 `Farrow`，请将 **Initial conditions** 设置为大小为 1×*R*×(*D*+*L*) 的数组，其中 *D* 是最大延迟的值。对于 FIR 插值，`L` 是插值滤波器半长度的值。对于 Farrow 插值，`L` 等于 farrow 滤波器长度值的一半的 `floor`（`floor( farrow filter length/2)`）。

**示例：** `1`

**示例：** randn(1,3,104)

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Disable direct feedthrough by increasing minimum possible delay by one** — 禁用直接馈通 `off`（默认）| `on`

选中此框可通过将最小可能延迟值增加一来禁用直接馈通。当您将 **Input processing** 参数设置为 `Columns as channels (frame based)` 时，模块将最小可能延迟值增加 *`frame size`* – 1。类似地，当您将 **Input processing** 参数设置为 `Elements as channels (sample based)` 时，模块将最小可能延迟值增加一个样本。

选中此框允许您在反馈回路中使用 Variable Fractional Delay 模块。

### **For small input delay values** — 对较小输入延迟值采取的操作 `Clip to the minimum value necessary for centered kernel`（默认）| `Use off-centered kernel` | `Switch to linear interpolation if kernel cannot be centered`

指定当输入延迟值太小而无法将核居中时模块的行为。

您可以使用以下选项之一来指定模块如何处理太小而无法将核居中的输入延迟值：

- 在 `FIR` 和 `Farrow` 插值模式下，您可以选择 `Clip to the minimum value necessary for centered kernel`。此选项强制模块将 *Dmin* 增加到保持核居中所需的最小值。
- 在 `FIR` 插值模式下，您可以选择 `Switch to linear interpolation if kernel cannot be centered`。此选项强制模块保留 *Dmin* 的值，并使用 `Linear` 插值计算所有插值。
- 在 `Farrow` 插值模式下，您可以选择 `Use off-centered kernel`。此选项强制模块保留 *Dmin* 的值，并使用具有偏心核的 farrow 滤波器计算插值。

#### 依赖关系

此参数仅在 **Interpolation mode** 设置为 `FIR` 或 `Farrow` 时适用。

### **Valid delay range (in samples)** — 有效延迟值范围 只读：[0 100]（默认）| [*Dmin* *Dmax*]

此参数为只读。

延迟范围值 [*Dmin* *Dmax*] 由模块根据当前参数设置计算得出（以样本为单位）。*Dmin* 是最小可能有效延迟值（以样本为单位）。模块将所有小于 *Dmin* 的输入延迟值裁剪为 *Dmin*。*Dmax* 是最大有效延迟值（以样本为单位）。模块将所有大于 *Dmax* 的输入延迟值裁剪为 *Dmax*。

当 **Interpolation mode** 设置为以下之一时：

- `Linear` —— *Dmin* 等于 0。*Dmax* 等于您在 **Maximum delay (Dmax) in samples** 参数中指定的值。
- `FIR` —— *Dmin* 等于 *P* – 1，其中 *P* 是您在 **Interpolation filter half-length (P)** 中指定的值。*Dmax* 等于您在 **Maximum delay (Dmax) in samples** 参数中指定的值。
- `Farrow` —— *Dmin* 等于 *N/2* – 1，其中 *N* 是您在 **Farrow filter length (N)** 中指定的值。*Dmax* 等于您在 **Maximum delay (Dmax) in samples** 参数中指定的值。

**示例：** [1 100]

**示例：** [2 100]

**示例：** [3 100]

### 定点属性

#### 定点属性

### **Rounding mode** — 定点运算的舍入方法 `Zero`（默认）| `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Simplest`

将定点运算的舍入模式指定为以下之一：

- `Zero`
- `Ceiling`
- `Convergent`
- `Floor`
- `Nearest`
- `Round`
- `Simplest`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作方法 off（默认）| on

当您选中此参数时，模块将饱和其定点运算的结果。当您清除此参数时，模块将环绕其定点运算的结果。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Coefficients** — 系数的数据类型 `Same word length as input`（默认）| `Specify word length`

将滤波器系数的数据类型指定为以下之一：

- `Same word length as input` —— 滤波器系数的字长与模块输入的字长匹配。系数的分数长度自动设置为仅二进制点缩放，在给定系数的值和字长的情况下为您提供最佳精度。
- `Specify word length` —— 以位为单位指定系数的字长。在此模式下，系数的分数长度自动设置为仅二进制点缩放，在给定系数的值和字长的情况下为您提供最佳精度。

有关此模块使用的系数数据类型的更多信息，请参阅定点数据类型部分。

### **Product output** — 乘积输出的数据类型 `Same as first input`（默认）| `Binary point scaling`

将乘积输出的数据类型指定为以下之一：

- `Same as first input` —— 模块将乘积输出数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定乘积输出的字长和分数长度。

有关乘积输出数据类型的更多信息，请参阅乘法数据类型和定点数据类型部分。

### **Accumulator** — 累加运算的数据类型 `Same as product output`（默认）| `Same as first input` | `Binary point scaling`

将累加运算的数据类型指定为以下之一：

- `Same as product output` —— 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `Same as first input` —— 模块将累加器数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定累加器输出的字长和分数长度。

有关此模块使用的累加器数据类型的更多信息，请参阅定点数据类型部分。

### **Product output polyval** — 乘积多项式值的数据类型 `Same as first input`（默认）| `Binary point scaling`

将乘积多项式值的数据类型指定为以下之一：

- `Same as first input` —— 模块将乘积多项式值数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定乘积输出多项式的字长和分数长度。

有关此模块使用的乘积多项式值数据类型的更多信息，请参阅定点数据类型部分。

#### 依赖关系

此属性在您将 **Interpolation mode** 设置为 `Farrow` 时适用。

### **Accumulator polyval** — 累加器多项式值的数据类型 `Same as first input`（默认）| `Binary point scaling`

将累加器多项式值的数据类型指定为以下之一：

- `Same as first input` —— 模块将累加器多项式值数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定累加器多项式值的字长和分数长度。

有关此模块使用的累加器多项式值数据类型的更多信息，请参阅定点数据类型部分。

#### 依赖关系

此属性在您将 **Interpolation mode** 设置为 `Farrow` 时适用。

### **Multiplicand polyval** — 被乘数多项式值的数据类型 `Same as first input`（默认）| `Binary point scaling`

将被乘数多项式值的数据类型指定为以下之一：

- `Same as first input` —— 模块将被乘数多项式值数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定被乘数多项式值的字长和分数长度。

有关此模块使用的被乘数多项式值数据类型的更多信息，请参阅定点数据类型部分。

#### 依赖关系

此属性在您将 **Interpolation mode** 设置为 `Farrow` 时适用。

### **Output** — 模块输出的数据类型 `Same as accumulator`（默认）| `Same as first input` | `Binary point scaling`

将模块输出的数据类型指定为以下之一：

- `Same as accumulator` —— 模块将输出数据类型指定为与累加器输出数据类型相同。
- `Same as first input` —— 模块将输出数据类型指定为与数据输入相同。
- `Binary point scaling` —— 以位为单位指定模块输出的字长和分数长度。

有关此模块使用的输出数据类型的更多信息，请参阅定点数据类型部分。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Signal Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入延迟时变分数个采样周期

Variable Fractional Delay 模块沿输入的每个通道将输入信号延迟指定的分数样本数。该模块还可以同时计算同一信号的多个延迟版本（抽头）。有关示例，请参阅使用多抽头分数延迟对信号进行延迟。

当延迟具有分数值时，模块对输入信号进行插值，以在非整数采样间隔处获得新样本。您可以将 **Interpolation mode** 参数设置为 `Linear`、`FIR` 或 `Farrow` 之一。模块支持时变延迟值。也就是说，延迟值可以在帧内逐样本变化。

模块假设 **Delay** 端口处的输入值在 *Dmin* 和 *Dmax* 之间，其中 *Dmin* 出现在模块对话框 **Main** 选项卡的 `Valid delay range` 部分中，*Dmax* 是 **Maximum delay (Dmax) in samples** 参数的值。模块将小于 *Dmin* 的延迟值裁剪为 *Dmin*，将大于 *Dmax* 的延迟值裁剪为 *Dmax*。

在为 `FIR` 和 `Farrow` 插值模式选择有效的 `Delay` 值时，您必须考虑其他因素。有关详细信息，请参阅算法。
