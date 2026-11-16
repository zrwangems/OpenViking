---
type: simulink-block
title: 'Gold Sequence Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'goldsequencegenerator'
documentation_source_path: 'ref/goldsequencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Gold Sequence Generator

## 端口

### 输入

### **oSiz** — 当前输出大小 标量 | 二元素行向量

当前输出大小，指定为标量或二元素行向量。向量的第二个元素必须为 `1`。

**示例：** `[10 1]` 表示当前输出列向量的大小将为 10×1。

#### 依赖关系

要启用此端口，请选择 **Output variable-size signals** 参数，并将 **Maximum output size source** 设置为 `Dialog parameter`。

**数据类型：** `double`

### **Ref** — 参考输入信号 标量 | 列向量

参考输入信号，指定为标量、列向量。

#### 依赖关系

要启用此端口，请选择 **Output variable-size signals** 参数，并将 **Maximum output size source** 设置为 `Inherit from reference input`。

**数据类型：** `double`

### **Rst** — 复位信号 标量 | 列向量

复位信号，按以下形式之一指定。

- 当输出大小可变时，指定为标量。
- 否则，指定为标量或长度为 **Samples per frame** 的二维列向量。

对于非零 **Rst** 输入值，输出信号复位。有关详细信息，请参阅复位行为

#### 依赖关系

要启用此端口，请选择 **Reset on nonzero input** 参数。

**数据类型：** `double`

### 输出

### **Out** — 输出信号 二进制列向量

输出信号，返回为二进制列向量。为了使模块生成非零序列，**Initial states (1)** 或 **Initial states (2)** 向量中至少有一个元素必须为非零。

**数据类型：** `double`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Preferred polynomial (1)** — 第一序列多项式 `'z^6 + z + 1'`（默认） | 多项式字符向量 | 二进制行向量 | 整数行向量

第一序列多项式，按以下形式之一指定。

- 常数项为 `1` 的多项式字符向量或字符串标量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 按降幂顺序表示多项式系数的二进制值行向量。此向量的长度必须为 *N* + 1，其中 *N* 是多项式的阶数。第一个和最后一个条目必须为 `1`，表示阶数为 *N* 的最高次项和常数项 1。
- 按降幂顺序表示多项式非零项指数的整数值行向量。最后一个条目必须为 `0`，表示常数项 1。

此属性确定第一个首选 PN 序列生成器的移位寄存器的反馈连接。第一个生成器多项式的阶数必须等于由 **Preferred polynomial (2)** 参数指定的第二个生成器多项式的阶数。有关详细信息，请参阅首选序列对。

**示例：** `'z^8 + z^2 + 1'`、`[1 0 0 0 0 0 1 0 1]` 和 `[8 2 0]` 表示同一多项式，*p*(*z*) = *z*8 + *z*2 + 1。

### **Initial states (1)** — 第一序列多项式的初始状态 `[0 0 0 0 0 1]`（默认） | 二进制向量

首选对中第一个序列多项式的移位寄存器的初始状态，指定为长度等于 **Preferred polynomial (1)** 的阶数的二进制向量。

**注意**

为了使模块生成非零序列，第一个或第二个首选 PN 序列生成器的初始条件中至少有一个元素必须为非零。具体而言，至少一个移位寄存器的初始状态必须为非零。

### **Preferred polynomial (2)** — 第二序列多项式 `'z^6 + z^5 + z^2 + z + 1'`（默认） | 多项式字符向量 | 二进制行向量 | 整数行向量

第二序列多项式，按以下形式之一指定。

- 常数项为 `1` 的多项式字符向量或字符串标量。有关详细信息，请参阅 Communications Toolbox 中的多项式表示。
- 按降幂顺序表示多项式系数的二进制值行向量。此向量的长度必须为 *N* + 1，其中 *N* 是多项式的阶数。第一个和最后一个条目必须为 `1`，表示阶数为 *N* 的最高次项和常数项 1。
- 按降幂顺序表示多项式非零项指数的整数值行向量。最后一个条目必须为 `0`，表示常数项 1。

此属性确定第一个首选 PN 序列生成器的移位寄存器的反馈连接。第二个生成器多项式的阶数必须等于由 **Preferred polynomial (1)** 参数指定的第一个生成器多项式的阶数。有关详细信息，请参阅首选序列对。

**示例：** `'z^8 + z^2 + 1'`、`[1 0 0 0 0 0 1 0 1]` 和 `[8 2 0]` 表示同一多项式，*p*(*z*) = *z*8 + *z*2 + 1。

### **Initial states (2)** — 第二序列多项式的初始状态 `[0 0 0 0 0 1]`（默认） | 二进制向量

首选对中第二个序列多项式的移位寄存器的初始状态，指定为长度等于 **Preferred polynomial (2)** 的阶数的二进制向量。

**注意**

为了使模块生成非零序列，第一个或第二个首选 PN 序列生成器的初始条件中至少有一个元素必须为非零。具体而言，至少一个移位寄存器的初始状态必须为非零。

### **Sequence index** — 序列索引 `0`（默认） | 范围 [–2, 2*n*–2] 内的整数标量

输出序列在序列集合中的序列索引，指定为范围 [–2, 2*n*–2] 内的整数标量。*n* 是首选多项式的阶数。有关详细信息，请参阅 Gold 序列。

### **Shift** — Gold 序列的偏移 `0`（默认） | 整数标量

Gold 序列相对于初始时间的偏移，指定为整数标量。

### **Output variable-size signals** — 输出可变长度信号的选项 `off`（默认） | `on`

选择此参数以在仿真期间启用可变长度输出序列。清除此参数时，模块输出固定长度序列。选择此参数时，模块可以输出可变长度序列。有关可变大小信号的信息，请参阅可变大小信号基础 (Simulink)。

### **Maximum output size source** — 最大输出大小来源 `Dialog parameter`（默认） | `Inherit from reference port`

选择如何指定最大序列输出大小。

- `Dialog parameter` — 选择此值将模块配置为使用 **Maximum output size** 参数设置作为允许的最大输出序列长度。**oSiz** 输入端口指定输出信号的当前大小，模块输出从输入信号继承采样时间。**oSiz** 的输入值必须小于或等于 **Maximum output size** 参数。
- `Inherit from reference port` — 选择此值以启用 **Ref** 输入端口，并将模块配置为从 **Ref** 输入端口的可变大小信号继承采样时间、最大大小和当前输出大小。这些设置允许的最大输出序列长度。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals**。

### **Maximum output size** — 最大输出大小 `[10 1]`（默认） | 形式为 [*n* 1] 的向量

指定模块的最大输出大小。*n* 是正标量。

**示例：** `[10 1]` 指定输出信号的最大大小为 10×1。

#### 依赖关系

要启用此参数，请选择 **Output variable-size signals**，并将 **Maximum output size source** 设置为 `Dialog parameter`。

### **Sample time** — 输出采样时间 `1`（默认）

正标量指定输出信号每两个采样之间的时间，以 seconds 为单位。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅采样时序。

#### 依赖关系

要启用此参数，请不要选择 **Output variable-size signals**。

### **Samples per frame** — 每帧采样数 `1`（默认） | 正整数

每帧采样数，指定为正整数，表示输出数据的一个通道中每帧的采样数。有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅采样时序。

#### 依赖关系

要启用此参数，请不要选择 **Output variable-size signals**。

### **Reset on nonzero input** — 复位输出信号 `off`（默认） | `on`

选择此参数以启用 **Rst** 端口。当在 **Rst** 端口输入非零值时，内部移位寄存器将复位为 **Initial states (1)** 和 **Initial states (2)** 参数的原始值。

### **Output data type** — 输出数据类型 `double`（默认） | `boolean` | `Smallest unsigned integer`

输出数据类型，指定为 `boolean`、`double` 或 `Smallest unsigned integer`。

当设置为 `Smallest unsigned integer` 时，输出数据类型根据模型的 Configuration Parameters 对话框的 Hardware Implementation Pane (Simulink) 中所使用的设置来选择。如果在 Hardware Implementation Pane 中选择 ASIC/FPGA，则输出数据类型为理想的最小一位大小 (ufix(1))。对于所有其他选择，它是可用字长最小的无符号整数，其大小足以容纳一位，通常对应于 char 的大小 (uint8)。

## 所属库

Communications Toolbox / Comm Sources / Sequence Generators

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a：现有模型自动将此模块更新为当前版本

从 R2020a 开始，Simulink 不再允许使用 R2015b 之前可用的 Gold Sequence Generator 模块版本。

现有模型会自动更新以加载当前的 Gold Sequence Generator 模块版本。有关模块转发的详细信息，请参阅使用转发表维护库模块兼容性 (Simulink)。

## 描述

从序列集合生成 Gold 序列

Gold Sequence Generator 模块从有界序列集合生成具有小周期互相关特性的二进制序列。有关详细信息，请参阅 Gold 序列。

此模块可以在仿真期间输出长度变化的序列。有关可变大小信号的详细信息，请参阅可变大小信号基础 (Simulink)。

这些图标显示启用了所有端口的模块。

显示用于输出大小和复位的可选输入端口的 Gold Sequence Generator 模块。显示用于参考信号和复位的可选输入端口的 Gold Sequence Generator 模块。
