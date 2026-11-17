---
type: simulink-block
title: 'Kasami Sequence Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'kasamisequencegenerator'
documentation_source_path: 'ref/kasamisequencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Kasami Sequence Generator

## 端口
```yaml
ports:
- name: oSiz
  summary: 当前输出大小 标量 | 向量
  direction: input
  data_types: double
- name: Ref
  summary: 参考输入信号 标量 | 列向量
  direction: input
  data_types: double
- name: Rst
  summary: 复位信号 标量 | 向量
  direction: input
  data_types: double
- name: Out
  summary: 输出信号 向量
  direction: output
  data_types: double
```

### 输入

### **oSiz** — 当前输出大小 标量 | 向量

当前输出大小，指定为标量或形式为 [*n*,1] 的向量，其中 *n* 是输出序列中的元素数量。

**示例：** `[10 1]` 指定当前输出列向量的大小为 10×1。

#### 依赖关系

要启用此端口，请将 **Maximum output size source** 参数设置为 `Dialog parameter`。

**数据类型：** `double`

### **Ref** — 参考输入信号 标量 | 列向量

参考输入信号，指定为标量或列向量。

#### 依赖关系

要启用此端口，请将 **Maximum output size source** 参数设置为 `Inherit from reference input`。

**数据类型：** `double`

### **Rst** — 复位信号 标量 | 向量

复位信号，根据输出大小指定为标量或向量。

- 当输出大小可变时，将此端口指定为标量。
- 否则，将此端口指定为标量或长度等于 **Samples per frame** 参数值的列向量。

对于非零的 **Rst** 输入值，输出信号复位。有关详细信息，请参阅复位行为。

#### 依赖关系

要启用此端口，请选择 **Reset on nonzero input** 参数。

**数据类型：** `double`
### 输出

### **Out** — 输出信号 向量

输出信号，以二值列向量形式返回。**Initial states** 参数向量中至少有一个元素必须非零，模块才能生成非零序列。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Generator polynomial
  summary: 生成多项式 'z^6 + z + 1'（默认）| 多项式字符向量 | 字符串标量 | 二值行向量 | 整数值行向量
  group: ''
- name: Initial states
  summary: 初始状态 [0 0 0 0 0 1]（默认）| 二值标量 | 二值行向量
  group: ''
- name: Sequence index(es)
  summary: 序列索引 0（默认）| 整数 | 形式为 [*k* *m*] 的向量
  group: ''
- name: Shift
  summary: 序列相对于起始点的偏移 0（默认）| 整数
  group: ''
- name: Output variable-size signals
  summary: 输出可变长度信号的选项 off（默认）| on
  group: ''
- name: Maximum output size source
  summary: 最大输出大小来源 Dialog parameter（默认）| Inherit from reference port
  group: ''
- name: Maximum output size
  summary: 最大输出大小 [10 1]（默认）| 形式为 [*n* 1] 的向量
  group: ''
- name: Sample time
  summary: 输出采样时间 1（默认）| -1 | 正标量
  group: ''
- name: Samples per frame
  summary: 每帧采样数 1（默认）| 正整数
  group: ''
- name: Reset on nonzero input
  summary: 复位输出信号的选项 off（默认）| on
  group: ''
- name: Output data type
  summary: 输出数据类型 double（默认）| boolean
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Generator polynomial** — 生成多项式 `'z^6 + z + 1'`（默认）| 多项式字符向量 | 字符串标量 | 二值行向量 | 整数值行向量

指定生成多项式，它决定了生成序列的移位寄存器中的连接，可以是以下选项之一。

- 包含数字 `1` 的多项式字符向量或字符串标量（例如 `'z^4 + z + 1'`）。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 按降幂顺序列出多项式系数的二值行向量。第一个和最后一个元素必须为 `1`。此向量的长度必须比生成多项式的阶数大一。
- 按降幂顺序包含多项式非零项指数的整数值行向量。最后一个元素必须为 `0`。

例如，`'z^8 + z^2 + 1'`、`[1 0 0 0 0 0 1 0 1]` 和 `[8 2 0]` 表示相同的多项式 *p*(*z*) = *z*8 + *z*2 + 1。

### **Initial states** — 初始状态 `[0 0 0 0 0 1]`（默认）| 二值标量 | 二值行向量

移位寄存器的初始状态用于生成序列。如果指定二值行向量，其长度必须等于 **Generator polynomial** 参数指定的生成多项式的阶数。如果指定二值标量，模块会将标量扩展为长度等于生成多项式阶数的行向量。所得向量的所有元素都等于该标量。

### **Sequence index(es)** — 序列索引 `0`（默认）| 整数 | 形式为 [*k* *m*] 的向量

指定一个整数或形式为 [*k* *m*] 的向量，以从可能的序列集合中选择感兴趣的 Kasami 序列。存在两类 Kasami 序列：从小集合获得的序列和从大集合获得的序列。您可以通过将此参数设置为范围 [0, 2*n*/2–2] 内的整数来从小集合中选择 Kasami 序列。您可以通过将此参数设置为形式为 [*k* *m*] 的向量来从大集合中选择序列。*k* 必须是范围 [–2, 2*n*–2] 内的整数，*m* 必须是范围 [–1, 2*n*/2–2] 内的整数。有关详细信息，请参阅序列索引。

### **Shift** — 序列相对于起始点的偏移 `0`（默认）| 整数

指定 Kasami 序列相对于初始时间的偏移。

您可以通过选择 **Reset on nonzero input** 参数，使用外部信号将内部移位寄存器的值复位到初始状态。此选择会在此模块中为外部信号创建一个输入端口。模块复位内部移位寄存器的方式取决于其输出信号和复位信号是基于采样的还是基于帧的。有关示例，请参阅复位行为。

### **Output variable-size signals** — 输出可变长度信号的选项 `off`（默认）| `on`

选择此参数以在仿真期间启用可变长度输出序列。清除此参数时，模块输出固定长度序列。选择此参数时，模块可以输出可变长度序列。有关可变大小信号的信息，请参阅可变大小信号基础（Simulink）。

### **Maximum output size source** — 最大输出大小来源 `Dialog parameter`（默认）| `Inherit from reference port`

选择如何指定最大序列输出大小。

- `Dialog parameter` — 选择此值可将模块配置为使用 **Maximum output size** 参数设置作为允许的最大输出序列长度。**oSiz** 输入端口指定输出信号的当前大小，模块输出从输入信号继承采样时间。**oSiz** 的输入值必须小于或等于 **Maximum output size** 参数。
- `Inherit from reference port` — 选择此值可启用 **Ref** 输入端口，并将模块配置为从 **Ref** 输入端口处的可变大小信号继承采样时间、最大大小和当前输出大小。这些设置了允许的最大输出序列长度。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals**。

### **Maximum output size** — 最大输出大小 `[10 1]`（默认）| 形式为 [*n* 1] 的向量

指定模块的最大输出大小。*n* 是正标量。

**示例：** `[10 1]` 指定输出信号的最大大小为 10×1。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals** 并将 **Maximum output size source** 设置为 `Dialog parameter`。

### **Sample time** — 输出采样时间 `1`（默认）| `-1` | 正标量

正标量指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，输出信号将从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅采样时序。

#### 依赖关系

要启用此参数，请清除 **Output variable-size signals**。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

指定输出数据一个通道中每帧的采样数。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅采样时序。

### **Reset on nonzero input** — 复位输出信号的选项 `off`（默认）| `on`

选择此参数以启用 **Rst** 输入端口。使用该端口指定一个输入信号，将内部移位寄存器复位为 **Initial states** 参数值的原始值。

### **Output data type** — 输出数据类型 `double`（默认）| `boolean`

指定模块的输出数据类型。
## 所属库

Communications Toolbox / Comm Sources / Sequence Generators

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a: 现有模型自动将此模块更新为当前版本

从 R2020a 开始，Simulink 不再允许使用 R2015b 之前可用的 Kasami Sequence Generator 模块版本。

现有模型会自动更新，以加载在“源模块输出连续时间样本的帧但不使用帧属性”中公布的 Kasami Sequence Generator 模块版本。有关模块转发的详细信息，请参阅 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

从 Kasami 序列集合生成 Kasami 序列

Kasami Sequence Generator 模块从一组 Kasami 序列中生成序列。Kasami 序列是一组具有良好互相关特性的序列。有关详细信息，请参阅 Kasami Sequences。

此模块可以输出在仿真期间长度变化的序列。有关可变大小信号的详细信息，请参阅 Variable-Size Signal Basics (Simulink)。

这些图标显示了启用 `oSiz`、`Ref` 和 `Rst` 端口的模块。

Kasami Sequence Generator 模块显示用于输出大小和复位的可选输入端口Kasami Sequence Generator 模块显示用于参考信号和复位的可选输入端口
