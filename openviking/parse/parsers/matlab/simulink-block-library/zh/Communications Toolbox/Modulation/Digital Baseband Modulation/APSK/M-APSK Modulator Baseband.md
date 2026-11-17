---
type: simulink-block
title: 'M-APSK Modulator Baseband'
family: 'comm'
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
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: APSK 调制信号 标量 | 向量 | 矩阵
  direction: output
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。输入信号必须由二进制值或范围在 [0, (*M* – 1)] 内的整数组成，其中 *M* 是 M-APSK 的调制阶数。此端口在模块上未命名。

**注意**

要将输入信号作为二进制元素处理，请将输入类型参数值设置为 `Bit`。对于二进制输入，行数必须是 log2(*M*) 的整数倍。列中每 log2(*M*) 个比特为一组映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — APSK 调制信号 标量 | 向量 | 矩阵

APSK 调制信号，返回为复标量、向量或矩阵。输出信号维度取决于指定的输入类型值。此端口在模块上未命名。

| **输入类型** | 输出信号维度 |
| --- | --- |
| `Integer` | 输出信号与输入信号具有相同的维度。 |
| `Bit` | 输出信号的行数等于输入信号的行数除以 log2(*M*)，其中 *M* 是 M-APSK 的调制阶数。 |

使用输出数据类型指定输出数据类型。
## 参数
```yaml
parameters:
- name: Constellation points per circle
  summary: 每个 PSK 环的星座点 [4,12]（默认）| 向量
  group: ''
- name: Radius of each circle
  summary: 每个 PSK 环的半径 [0.5,1]（默认）| 向量
  group: ''
- name: Phase offset of each circle (rad)
  summary: 每个 PSK 环的相位偏移 [pi/4,pi/12]（默认）| 标量 | 向量
  group: ''
- name: Symbol mapping
  summary: 符号映射 Auto（默认）| Contourwise-gray | Gray | User-defined
  group: ''
- name: Custom symbol mapping
  summary: 自定义符号映射 [0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]（默认）| 整数向量
  group: ''
- name: Input type
  summary: 输入类型 Integer（默认）| Bit
  group: ''
- name: Output data type
  summary: 输出数据类型 double（默认）| single
  group: ''
- name: View Constellation
  summary: 绘制参考星座 button
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡上，在**准备**库中，选择**属性检查器**。

### **Constellation points per circle** — 每个 PSK 环的星座点 `[4,12]`（默认）| 向量

每个 PSK 环的星座点，指定为具有多个元素的向量。每个向量元素表示其对应 PSK 环中的星座点数。第一个元素对应最内层圆，依此类推，直到最后一个元素对应最外层圆。**Constellation points per circle** 中元素的总和决定了调制阶数。元素值必须是四的倍数，且调制阶数必须是二的幂。

**示例：** `[4,12,16]` 指定一个三 PSK 环星座，调制阶数为 32。

### **Radius of each circle** — 每个 PSK 环的半径 `[0.5,1]`（默认）| 向量

每个 PSK 环的半径，指定为与 Constellation points per circle 长度相同的向量。每个向量元素表示其对应 PSK 环的半径。第一个元素对应最内层圆，依此类推，直到最后一个元素对应最外层圆。这些元素值必须为正数并按递增顺序排列。

**示例：** `[0.5,1,2]` 定义三个星座 PSK 环的半径。内环半径为 0.5，第二环半径为 1.0，外环半径为 2.0。

### **Phase offset of each circle (rad)** — 每个 PSK 环的相位偏移 `[pi/4,pi/12]`（默认）| 标量 | 向量

每个 PSK 环的相位偏移，以弧度为单位，指定为标量或与 Constellation points per circle 长度相同的向量。每个向量元素表示其对应 PSK 环的相位偏移。第一个元素对应最内层圆，依此类推，直到最后一个元素对应最外层圆。仅当 **Constellation points per circle** 的所有元素值相同时，**Phase offset of each circle (rad)** 才可以是标量。

**示例：** `[pi/4,pi/12,pi/16]` 定义三个星座 PSK 环的相位偏移。内环相位偏移为 π/4，第二环相位偏移为 π/12，外环相位偏移为 π/16。

### **Symbol mapping** — 符号映射 `Auto`（默认）| `Contourwise-gray` | `Gray` | `User-defined`

符号映射，指定为以下之一：

- `Contourwise-gray` — 对每个 PSK 环在相位维度上沿轮廓使用格雷映射。
- `Gray` — 在幅度和相位两个维度上沿轮廓使用格雷映射。对于格雷符号映射，Constellation points per circle 的所有值必须相等，且 Phase offset of each circle (rad) 的所有值必须相等。有关所用格雷映射的描述，请参见 [2]。
- `User-defined` — 参见自定义符号映射。

默认符号映射取决于 **Constellation points per circle** 和 **Phase offset of each circle (rad)**。当 **Constellation points per circle** 的所有元素相等且 **Phase offset of each circle (rad)** 的所有元素相等时，默认为 `Gray`。对于所有其他情况，默认为 `Contourwise-gray`。

### **Custom symbol mapping** — 自定义符号映射 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]`（默认）| 整数向量

自定义符号映射，指定为整数向量。此向量必须由 *M* 个唯一元素组成，值在 [0, (*M* – 1)] 范围内，其中 *M* 是 M-APSK 的调制阶数。**Custom symbol mapping** 中的第一个元素对应最内层圆第一象限的星座点，后续元素沿 PSK 环逆时针排列。

**示例：** 默认值 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]` 指定轮廓格雷符号映射。星座点在所有轮廓上呈非均匀分布。

#### 依赖关系

要启用此参数，请将 Symbol mapping 设置为 `User-defined`。

### **Input type** — 输入类型 `Integer`（默认）| `Bit`

输入类型，指定为以下选项之一。

- `Integer` –– 输入信号必须由范围在 [0, (*M* – 1)] 内的整数组成。
- `Bit` –– 输入信号必须包含二进制值，且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 M-APSK 的调制阶数。二进制输入信号假定为左 MSB 对齐并按列指定。列中每 log2(sum(*M*)) 个比特为一组映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

### **Output data type** — 输出数据类型 `double`（默认）| `single`

输出数据类型，指定为 `double` 或 `single`。

### **View Constellation** — 绘制参考星座 `button`

要绘制参考星座，请点击 **View Constellation** 按钮。

**提示**

在点击 **View Constellation** 之前先点击 **Apply** 以查看最新参数值。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型发生变化，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参见 Interpreted Execution vs. Code Generation (Simulink)。
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

M-APSK Modulator Baseband 模块使用 *M* 进制幅相键控 (APSK) 调制对输入信号进行调制。输出是调制信号的基带表示。*M*，即 M-APSK 的调制阶数，等于 Constellation points per circle 中元素的总和。有关 *M*-APSK 调制的描述，请参见算法。

**注意**

M-APSK Modulator Baseband 专门适用于多环 PSK 星座。对于单环 PSK 星座，请使用 M-PSK Modulator Baseband。
