---
type: simulink-block
title: 'DVBS-APSK Modulator Baseband'
family: 'satcom'
product_id: 'satcom'
product_name: 'Satellite Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation'
documentation_page: 'dvbsapskmodulatorbaseband'
documentation_source_path: 'ref/dvbsapskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DVBS-APSK Modulator Baseband

## 端口
```yaml
ports:
- name: In
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: DVB-S2/S2X/SH 标准特定 APSK 调制信号 标量 | 向量 | 矩阵
  direction: output
```

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。输入信号必须是二进制值或范围在 [0, (*M* – 1)] 内的整数，其中 *M* 是**调制阶数**。该端口在模块上未命名。

**注意**

要将输入信号作为二进制元素处理，请将**输入类型**参数值设置为 `Bit`。对于二进制输入，行数必须是 log2(*M*) 的整数倍。每列中 log2(*M*) 个比特为一组映射到一个符号，第一个比特表示 MSB，最后一个比特表示 LSB。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — DVB-S2/S2X/SH 标准特定 APSK 调制信号 标量 | 向量 | 矩阵

DVB-S2/S2X/SH 标准特定 APSK 调制信号，返回为复标量、向量或矩阵。输出信号维度取决于指定的**输入类型**值。该端口在模块上未命名。

| **输入类型** | 输出信号维度 |
| --- | --- |
| `Integer` | 输出信号与输入信号具有相同的维度。 |
| `Bit` | 输出信号的行数等于输入信号的行数除以 log2(*M*)，其中 *M* 是**调制阶数**。 |

使用**输出数据类型**指定输出数据类型。
## 参数
```yaml
parameters:
- name: DVB standard suffix
  summary: 标准后缀 S2（默认）| S2X | SH
  group: ''
- name: Frame length
  summary: 帧长度 Normal（默认）| Short
  group: ''
- name: Modulation order
  summary: 调制阶数 16（默认）| 8 | 32 | 64 | 256
  group: ''
- name: Code identifier
  summary: 码标识符 2/3 | 字符向量
  group: ''
- name: Constellation scaling
  summary: 星座缩放 Outer radius as 1（默认）| Unit average power
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

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **DVB standard suffix** — 标准后缀 `S2`（默认）| `S2X` | `SH`

DVB 调制变体的标准后缀，指定为 `S2`、`S2X` 或 `SH`。

### **Frame length** — 帧长度 `Normal`（默认）| `Short`

帧长度，指定为 `Normal` 或 `Short`。

#### 依赖关系

此参数仅在**DVB standard suffix**设置为 `S2` 或 `S2X` 时适用。

### **Modulation order** — 调制阶数 `16`（默认）| `8` | `32` | `64` | `256`

调制阶数 *M*，指定为 2 的幂。调制阶数指定输出信号星座图中的总点数。有效调制阶数列表因**DVB standard suffix**和**Frame length**的值而异。

| **DVB standard suffix** | **Frame length** | **Modulation order** 选项 |
| --- | --- | --- |
| `S2` | `Normal` 或 `Short` | `16` 或 `32` |
| `S2X` | `Normal` | `8`、`16`、`32`、`64` 或 `256` |
| `Short` | `16` 或 `32` |
| `SH` | 不适用 | `16` |

### **Code identifier** — 码标识符 `2/3` | 字符向量

码标识符，指定为字符向量。有效码标识符值的列表根据 **DVB standard suffix**、**Frame length** 和 **Modulation order** 的指定值而变化。下表列出了 **Code identifier** 值的选项。

| **Modulation order** | **DVB standard suffix** | **Frame length** | **Code identifier** 选项 |
| --- | --- | --- | --- |
| `8` | `S2X` | `Normal` | `100/180` 或 `104/180` |
| `16` | `S2` 或 `S2X` | `Normal` | `2/3`、`3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `2/3`、`3/4`、`4/5`、`5/6` 或 `8/9` |
| `16` | `S2X` | `Normal` | `26/45`、`3/5`、`28/45`、`23/36`、`25/36`、`13/18`、`140/180`、`154/180`、`100/180`、`96/180`、`90/180`、`18/30` 或 `20/30` |
| `Short` | `7/15`、`8/16`、`26/45`、`3/5` 或 `32/45` |
| `32` | `S2` 或 `S2X` | `Normal` | `3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `3/4`、`4/5`、`5/6` 或 `8/9` |
| `32` | `S2X` | `Normal` | `128/180`、`132/180`、`140/180` 或 `2/3` |
| `Short` | `2/3` 或 `32/45` |
| `64` | `S2X` | `Normal` | `128/180`、`132/180`、`7/9`、`4/5` 或 `5/6` |
| `128` | `S2X` | `Normal` | `135/180` 或 `140/180` |
| 256 | `S2X` | `Normal` | `116/180`、`124/180`、`128/180`、`20/30` 或 `135/180` |

有关更多信息，请参阅 DVB-S2 标准 [1] 中的表 9 和表 10，以及 DVB-S2X 标准 [2] 中的表 17a。

#### 依赖关系

此参数仅在 **DVB standard suffix** 设置为 `S2` 或 `S2X` 时适用。

### **Constellation scaling** — 星座缩放 `Outer radius as 1`（默认）| `Unit average power`

星座缩放，指定为 `Outer radius as 1` 或 `Unit average power`。

#### 依赖关系

此参数仅在 **DVB standard suffix** 设置为 `S2` 或 `S2X` 时适用。

### **Input type** — 输入类型 `Integer`（默认）| `Bit`

输入类型，指定为 `Integer` 或 `Bit`。要使用 `Integer`，输入信号必须由范围 [0, (*M* – 1)] 内的整数组成。要使用 `Bit`，输入数据必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 **Modulation order**。

### **Output data type** — 输出数据类型 `double`（默认）| `single`

输出数据类型，指定为 `double` 或 `single`。

### **View Constellation** — 绘制参考星座 `button`

要绘制参考星座，请点击 **View Constellation** 按钮。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为：

- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间。
- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，您可以调试模块的源代码。
## 所属库

Satellite Communications Toolbox / Modulation / Digital Baseband Modulation

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

### R2024b：从 Communications Toolbox 移至 Satellite Communications Toolbox

此前，`DVBS-APSK Modulator Baseband` 需要 Communications Toolbox™。

## 描述

DVB-S2/S2X/SH 标准特定的 APSK 调制

DVBS-APSK Modulator Baseband 模块使用数字视频广播（DVB-S2/S2X/SH）标准特定的幅相键控（APSK）调制对输入信号进行调制。
