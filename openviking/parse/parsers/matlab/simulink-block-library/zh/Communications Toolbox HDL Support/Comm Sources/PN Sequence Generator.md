---
type: simulink-block
title: 'PN Sequence Generator'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Sources'
documentation_page: 'pnsequencegenerator'
documentation_source_path: '../comm/ref/pnsequencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# PN Sequence Generator

## 端口
```yaml
ports:
- name: Mask
  summary: 输出掩码二进制向量
  direction: input
  data_types: double | uint8 | ufix1
- name: oSiz
  summary: 输出大小整数
  direction: input
  data_types: double
- name: Ref
  summary: 参考输入列向量
  direction: input
  data_types: double
- name: Rst
  summary: 复位序列生成器 0 | 1
  direction: input
  data_types: Boolean
- name: Out
  summary: 伪随机噪声序列二进制向量
  direction: output
```

### 输入

### **Mask** — 输出掩码二进制向量

用于从初始时刻延迟 PN 序列的输出掩码，指定为包含 *N* 个元素的二进制向量。*N* 是生成多项式的阶数。

#### 依赖关系

要启用此端口，请将 **Output mask source** 设置为 `Input port`。

**数据类型：** `double` | `uint8` | `ufix1`

### **oSiz** — 输出大小整数

可变大小输出信号的输出大小，指定为整数。有关可变大小信号的信息，请参阅 Variable-Size Signal Basics (Simulink)。

#### 依赖关系

要启用此端口，请选择 **Output variable-size signals** 并将 **Maximum output size source** 设置为 `Dialog parameter`。

**数据类型：** `double`

### **Ref** — 参考输入列向量

参考输入，指定为确定最大和当前输出序列长度的列向量。**Ref** 输入必须是可变大小信号。有关可变大小信号的信息，请参阅 Variable-Size Signal Basics (Simulink)。

#### 依赖关系

要启用此端口，请选择 **Output variable-size signals** 并将 **Maximum output size source** 设置为 `Inherit from reference input`。

**数据类型：** `double`

### **Rst** — 复位序列生成器 0 | 1

复位序列生成器，指定为 `0` 或 `1`。有关详细信息，请参阅 Reset Behavior。

#### 依赖关系

要启用此端口，请选择 **Reset on nonzero input**。

**数据类型：** `Boolean`
### 输出

### **Out** — 伪随机噪声序列二进制向量

PN 序列，以二进制向量形式返回。输出的数据类型由 **Output data type** 指定。
## 参数
```yaml
parameters:
- name: Generator polynomial
  summary: 生成多项式 'z^6 + z + 1'（默认）| 字符向量 | 字符串标量 | 二进制行向量 | 整数向量
  group: ''
- name: Initial states
  summary: 初始移位寄存器状态 [0 0 0 0 0 1]（默认）| 二进制行向量
  group: ''
- name: Output mask source
  summary: 输出掩码来源 Dialog parameter（默认）| Input port
  group: ''
- name: Output mask vector (or scalar shift value)
  summary: 输出掩码向量或标量移位值 0（默认）| 整数标量 | 二进制向量
  group: ''
- name: Output variable-size signals
  summary: 输出可变长度信号的选项 off（默认）| on
  group: ''
- name: Sample time
  summary: 输出采样时间 1（默认）| -1 | 正标量
  group: ''
- name: Samples per frame
  summary: 每帧采样数 1（默认）| 正整数
  group: ''
- name: Maximum output size source
  summary: 最大输出大小来源 Dialog parameter（默认）| Inherit from reference port
  group: ''
- name: Maximum output size
  summary: 最大输出大小 [10 1]（默认）| 形式为 [*n* 1] 的向量
  group: ''
- name: Reset on nonzero input
  summary: 非零输入时复位 off（默认）| on
  group: ''
- name: Enable bit-packed outputs
  summary: 启用位打包输出 off（默认）| on
  group: ''
- name: Number of packed bits
  summary: 打包位数 8（默认）| [1, 32] 范围内的整数
  group: ''
- name: Interpret bit-packed values as signed
  summary: 将位打包值解释为有符号 off（默认）| on
  group: ''
- name: Output data type
  summary: 输出数据类型 double（默认）| boolean | Smallest unsigned integer
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Generator polynomial** — 生成多项式 `'z^6 + z + 1'`（默认）| 字符向量 | 字符串标量 | 二进制行向量 | 整数向量

确定移位寄存器反馈连接的生成多项式，指定为以下选项之一：

- 常数项为 `1` 的多项式的字符向量或字符串标量。有关详细信息，请参阅 Representation of Polynomials in Communications Toolbox。
- 按降幂顺序表示多项式系数的二值行向量。此向量的长度必须为 *N* + 1，其中 *N* 是多项式的阶数。第一个和最后一个元素必须为 `1`，表示阶数为 *N* 的首项和常数项 1。
- 按降幂顺序表示多项式非零项指数的整数值行向量。最后一个元素必须为 `0`，表示常数项 1。

有关详细信息，请参阅 Simple Shift Register Generator 和 Polynomial Order and Shift Register Orientation。

**示例：** `'z^8 + z^2 + 1'`、`[1 0 0 0 0 0 1 0 1]` 和 `[8 2 0]` 表示相同的多项式，*p*(*z*) = *z*
8 + *z*
2 + 1。

### **Initial states** — 初始移位寄存器状态 `[0 0 0 0 0 1]`（默认）| 二进制行向量

仿真开始时 PN 序列生成器的初始移位寄存器状态，指定为二值行向量。向量的长度必须等于由 **Generator polynomial** 指定的生成多项式的阶数。有关详细信息，请参阅 Simple Shift Register Generator 和 Polynomial Order and Shift Register Orientation。

**注意**

为使模块生成非零序列，**Initial states** 向量必须包含至少一个非零元素。

### **Output mask source** — 输出掩码来源 `Dialog parameter`（默认）| `Input port`

指示如何将输出掩码信息提供给模块的输出掩码来源，指定为以下之一：

- `Dialog parameter`，使用 `Output mask vector (or scalar shift value)` 参数设置。
- `Input port`，添加并使用 `Mask` 输入端口。

### **Output mask vector (or scalar shift value)** — 输出掩码向量或标量移位值 0（默认）| 整数标量 | 二进制向量

输出掩码向量或标量移位值，指定为整数标量或长度为 *N* 的二进制行向量，其中 *N* 是生成多项式的阶数。此参数确定 PN 序列从初始时刻的延迟。有关详细信息，请参阅 Shifting PN Sequence Starting Point。

#### 依赖关系

要启用此参数，请将 **Output mask source** 设置为 `Dialog parameter`。

### **Output variable-size signals** — 输出可变长度信号的选项 `off`（默认）| `on`

选择此参数以在仿真期间启用可变长度输出序列。清除此参数时，模块输出固定长度序列。选择此参数时，模块可以输出可变长度序列。有关可变大小信号的信息，请参阅 Variable-Size Signal Basics (Simulink)。

### **Sample time** — 输出采样时间 `1`（默认）| -1 | 正标量

正标量指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，输出信号将从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅
Sample Timing。

**示例：** `1` 指定采样时间为 1 秒。

#### 依赖关系

要启用此参数，请清除 **Output variable-size signals**。

### **Samples per frame** — 每帧采样数 `1`（默认）| 正整数

输出信号一个通道中的每帧采样数，指定为正整数。有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅 Sample Timing。

#### 依赖关系

要启用此参数，请清除 **Output variable-size signals**。

### **Maximum output size source** — 最大输出大小来源 `Dialog parameter`（默认）| `Inherit from reference port`

选择如何指定最大序列输出大小。

- `Dialog parameter` — 选择此值可将模块配置为使用 **Maximum output size** 参数设置作为允许的最大输出序列长度。**oSiz** 输入端口指定输出信号的当前大小，模块输出从输入信号继承采样时间。**oSiz** 的输入值必须小于或等于 **Maximum output size** 参数。
- `Inherit from reference port` — 选择此值可启用 **Ref** 输入端口，并将模块配置为从 **Ref** 输入端口处的可变大小信号继承采样时间、最大大小和当前输出大小。这些设置确定允许的最大输出序列长度。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals**。

### **Maximum output size** — 最大输出大小 `[10 1]`（默认）| 形式为 [*n* 1] 的向量

指定模块的最大输出大小。*n* 是正标量。

**示例：** `[10 1]` 指定输出信号的最大大小为 10×1。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals** 并将 **Maximum output size source** 设置为 `Dialog parameter`。

### **Reset on nonzero input** — 非零输入时复位 off（默认）| on

选择此参数以添加 `Rst` 输入端口。有关详细信息，请参阅 Reset Behavior。

### **Enable bit-packed outputs** — 启用位打包输出 off（默认）| on

选择此参数以使 **Number of packed bits** 和 **Interpret bit-packed values as signed** 参数可用。

选择此参数时，模块生成 (*M*×*P*) 位。*M* 是 **Samples per frame** 参数中指定的每帧采样数。*P* 是 **Number of packed bits** 参数中指定的位打包字的大小。每组 *P* 位被打包为一个整数，从而产生包含 *M* 个元素的整数值输出向量。输出的数据类型由 **Output data type** 指定。

**注意**

对于整数表示，每组 *P* 位中的最高位被视为 MSB，而最低位被视为 LSB。

### **Number of packed bits** — 打包位数 8（默认）| [1, 32] 范围内的整数

打包位数，指定为 [1, 32] 范围内的整数。

#### 依赖关系

要启用此参数，请选择 **Enable bit-packed outputs**。

### **Interpret bit-packed values as signed** — 将位打包值解释为有符号 off（默认）| on

选择时将位打包值解释为有符号整数值，清除时解释为无符号整数值。选择时，最高位（符号位）中的 1 表示负值。

#### 依赖关系

要启用此参数，请选择 **Enable bit-packed outputs**。

### **Output data type** — 输出数据类型 `double`（默认）| `boolean` | `Smallest unsigned integer`

输出数据类型，指定为 `double`、`boolean` 或 `Smallest unsigned integer`。

- 清除 **Enable bit-packed outputs** 时，输出数据类型可以指定为 `double`、`boolean` 或 `Smallest unsigned integer`。当 **Output data type** 参数设置为 `Smallest unsigned integer` 时，输出数据类型根据模型 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中使用的设置进行选择。如果在 **Hardware Implementation** 窗格中选择 `ASIC/FPGA`，则输出数据类型为 `ufix(1)` = 理想最小一位大小。对于所有其他选择，它是具有足够容纳一位的最小可用字长的无符号整数，通常对应于 char 的大小（例如 `uint8`）。
- 选择 **Enable bit-packed outputs** 时，输出数据类型可以指定为 `double` 或 `Smallest unsigned integer`。当 **Output data type** 参数设置为 `Smallest unsigned integer` 时，输出数据类型根据 **Interpret bit-packed values as signed** 和 **Number of packed bits** 参数以及模型 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中使用的设置进行选择。如果在 **Hardware Implementation** 窗格中选择 `ASIC/FPGA`，则输出数据类型是基于 **Interpret bit-packed values as signed** 参数的理想最小 *n* 位大小，例如 `sfix(n)` 或 `ufix(n)`。对于所有其他选择，它是具有足够容纳 *n* 位的最小可用字长的有符号或无符号整数。
## 所属库

Communications Toolbox / Comm Sources / Sequence Generators Communications Toolbox HDL Support / Comm Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 您可以在模块上选择 `Input port` 作为 **Output mask source**。在这种情况下，`Mask` 输入信号必须是数据类型为 `ufix1` 的向量。
- 如果选择 **Reset on nonzero input**，则 `Rst` 端口的输入必须具有数据类型 `Boolean`。
- HDL 代码生成不支持 `double` 类型的输出。支持所有其他输出类型（包括位打包输出）。
- 不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。
- 如果选择了 **Use trigger signal as clock** 选项，则不能在 Triggered Subsystem 内为此模块生成 HDL。请参阅 Using Triggered Subsystems for HDL Code Generation (HDL Coder)。

## 版本历史

**在 R2006a 之前推出**

### R2020a：现有模型自动将此模块更新到当前版本

从 R2020a 开始，Simulink 不再允许您使用 R2015b 之前可用的 PN Sequence Generator 模块版本。

现有模型会自动更新以加载 Source blocks output frames of contiguous time samples but do not use frame attribute 中宣布的 PN Sequence Generator 模块版本。有关模块转发的更多信息，请参阅 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

生成伪噪声序列

PN Sequence Generator 模块使用线性反馈移位寄存器 (LFSR) 生成伪随机二进制数序列。伪噪声序列通常用于伪随机加扰以及直接序列扩频系统中。有关详细信息，请参阅 More About。

这些图标显示了启用所有端口的模块。
