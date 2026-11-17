---
type: simulink-block
title: 'M-APSK Modulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / APSK'
documentation_page: 'mapskmodulatorbaseband'
documentation_source_path: 'ref/mapskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-APSK Modulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。输入信号必须由二进制值或范围 [0, (*M* – 1)] 内的整数组成，其中 *M* 是 M-APSK 的 Modulation Order。此端口在模块上未命名。

**注意**

要将输入信号作为二进制元素处理，请将输入类型参数值设置为 `Bit`。对于二进制输入，行数必须是 log2(*M*) 的整数倍。一列中每 log2(*M*) 个比特组成一组映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Out** — APSK 调制信号 标量 | 向量 | 矩阵

APSK 调制信号，返回为复标量、向量或矩阵。输出信号维度取决于指定的输入类型值。此端口在模块上未命名。

| **输入类型** | 输出信号维度 |
| --- | --- |
| `Integer` | 输出信号具有与输入信号相同的维度。 |
| `Bit` | 输出信号的行数等于输入信号的行数除以 log2(*M*)，其中 *M* 是 M-APSK 的 Modulation Order。 |

使用输出数据类型指定输出数据类型。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。从 Simulink® 工具条，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **每个圆的星座点数量** — 每个 PSK 环的星座点数量 `[4,12]`（默认） | 向量

每个 PSK 环的星座点数量，指定为包含多个元素的向量。每个向量元素表示其对应 PSK 环中的星座点数量。第一个元素对应最内层圆，以此类推直到最后一个元素，它对应最外层圆。**每个圆的星座点数量** 中元素的总和确定调制阶数。元素值必须是四的倍数，并且调制阶数必须是二的幂。

**示例：** `[4,12,16]` 指定一个具有 32 调制阶数的三 PSK 环星座。

### **每个圆的半径** — 每个 PSK 环的半径 `[0.5,1]`（默认） | 向量

每个 PSK 环的半径，指定为长度与“每个圆的星座点数量”相同的向量。每个向量元素表示其对应 PSK 环的半径。第一个元素对应最内层圆，以此类推直到最后一个元素，它对应最外层圆。这些元素值必须为正，并按递增顺序排列。

**示例：** `[0.5,1,2]` 定义三个星座 PSK 环的半径。内环半径为 0.5，第二个环半径为 1.0，外环半径为 2.0。

### **每个圆的相位偏移 (rad)** — 每个 PSK 环的相位偏移 `[pi/4,pi/12]`（默认） | 标量 | 向量

每个 PSK 环的相位偏移，以弧度为单位，指定为标量或长度与“每个圆的星座点数量”相同的向量。每个向量元素表示其对应 PSK 环的相位偏移。第一个元素对应最内层圆，以此类推直到最后一个元素，它对应最外层圆。仅当 **每个圆的星座点数量** 的所有元素都相同时，**每个圆的相位偏移 (rad)** 才能为标量。

**示例：** `[pi/4,pi/12,pi/16]` 定义三个星座 PSK 环的相位偏移。内环的相位偏移为 π/4，第二个环的相位偏移为 π/12，外环的相位偏移为 π/16。

### **符号映射** — 符号映射 `Auto`（默认） | `Contourwise-gray` | `Gray` | `User-defined`

符号映射，指定为以下之一：

- `Contourwise-gray` — 对每个 PSK 环在相位维度上沿轮廓使用 Gray 映射。
- `Gray` — 在幅度和相位两个维度上沿轮廓使用 Gray 映射。对于 Gray 符号映射，“每个圆的星座点数量”的所有值必须相等，并且“每个圆的相位偏移 (rad)”的所有值必须相等。有关所用 Gray 映射的说明，请参阅 [2]。
- `User-defined` — 请参阅自定义符号映射。

默认符号映射取决于 **每个圆的星座点数量** 和 **每个圆的相位偏移 (rad)**。当 **每个圆的星座点数量** 的所有元素都相等且 **每个圆的相位偏移 (rad)** 的所有元素都相等时，默认值为 `Gray`。对于所有其他情况，默认值为 `Contourwise-gray`。

### **自定义符号映射** — 自定义符号映射 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]`（默认） | 整数向量

自定义符号映射，指定为整数向量。此向量必须由 *M* 个唯一元素组成，值在范围 [0, (*M* – 1)] 内，其中 *M* 是 M-APSK 的 Modulation Order。**自定义符号映射** 中的第一个元素对应最内层圆第一象限中的星座点，后续元素沿 PSK 环逆时针排列。

**示例：** 默认值 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]` 指定 contourwise-gray 符号映射。星座点的分布在所有轮廓上都是非均匀的。

#### 依赖关系

要启用此参数，请将符号映射设置为 `User-defined`。

### **输入类型** — 输入类型 `Integer`（默认） | `Bit`

输入类型，指定为以下选项之一。

- `Integer` –– 输入信号必须由范围 [0, (*M* – 1)] 内的整数组成。
- `Bit` –– 输入信号必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 M-APSK 的 Modulation Order。二进制输入信号假定为左 MSB 对齐并按列指定。一列中每 log2(sum(*M*)) 个比特组成一组映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

### **输出数据类型** — 输出数据类型 `double`（默认） | `single`

输出数据类型，指定为 `double` 或 `single`。

### **View Constellation** — 绘制参考星座 `button`

要绘制参考星座，请点击 **View Constellation** 按钮。

**提示**

在点击 **View Constellation** 之前，请先点击 **Apply**，以查看最新参数值。

### **仿真使用** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / APM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

M 进制幅相键控 (APSK) 调制

M-APSK Modulator Baseband 模块使用 *M* 进制幅相键控 (APSK) 调制对输入信号进行调制。输出是调制信号的基带表示。*M*（M-APSK 的 Modulation Order）等于 **每个圆的星座点数量** 中元素的总和。有关 *M*-APSK 调制的说明，请参阅算法。

**注意**

M-APSK Modulator Baseband 专门适用于多环 PSK 星座。对于单环 PSK 星座，请使用 M-PSK Modulator Baseband。
