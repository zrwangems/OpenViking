---
type: simulink-block
title: 'Varying Delay'
family: 'linear-parameter-varying'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Linear Parameter Varying'
documentation_page: 'varyingdelay'
documentation_source_path: 'ref/varyingdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Varying Delay

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

当您使用 **Fixed delays (indices)** 参数将信号延迟指定为固定，并为 **Nominal delay** 参数指定值 `0` 时，此端口具有直接馈通。

**数据类型：** `double`

### **Port\_2** — 瞬时时间延迟输入 标量 | 向量

瞬时时间延迟输入，指定为标量或向量。此值用于指定可变延迟。该模块将任何负输入值视为零。

#### 依赖关系

要启用此端口，请将至少一个索引指定为可变，也就是说，**Fixed delays (indices)** 参数不能将所有通道都指定为固定。

**数据类型：** `double`
### 输出

### **Port\_1** — 延迟信号 标量 | 向量

输出信号，指定为标量或向量。

**数据类型：** `double`

## 参数

要交互式编辑模块参数，请使用 **属性检查器**。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **Nominal delay** — 延迟的标称值 1（默认）| 正标量 | 正数值向量

指定每个输入通道中延迟的标称值。

### **Maximum delay** — 时间延迟输入的最大值 `10`（默认）| 非负标量 | 非负数值向量

设置时间延迟输入的最大值。此值定义此模块允许的最大时间延迟输入。该模块会对超过此值的任何延迟进行限幅。

### **Minimum delay** — 时间延迟输入的最小值 `0`（默认）| 非负标量 | 非负数值向量

设置时间延迟输入的最小值。此值定义此模块允许的最小时间延迟输入。对于任何小于此值的延迟，该模块都会保持此值。

### **Fixed delays (indices)** — 具有固定延迟的信号索引 `[]`（默认）| 正标量 | 正数值向量

指定输入信号通道中延迟为固定的索引。例如，如果您有一个 4×1 输入信号，并且要在第一个和第四个通道中指定固定延迟，请为此参数使用值 `[1 4]`。该模块使用 **Nominal delay** 参数对应索引处指定的值。

当您将所有通道都列为固定时，该模块会禁用第二个输入端口 **Port\_2**。

### **Initial output** — 初始输出 `0`（默认）| 标量 | 向量

对于每个输入通道，指定输出值，直到仿真时间首次超过该通道的时间延迟。

### **Initial buffer size** — 初始内存分配 `1024`（默认）| 标量

定义要存储的输入点数的初始内存分配。输入点定义截至当前仿真时间的输入信号历史记录。

- 如果输入点数超过初始缓冲区大小，该模块会分配额外的内存。
- 仿真结束后，如果缓冲区不足且必须分配更多内存，则会显示一条消息。

#### 提示

- 由于分配内存会减慢仿真速度，因此如果仿真速度是个问题，请谨慎选择此值。
- 对于长时间延迟，此模块可能会使用大量内存，特别是对于多维输入。

### **Use fixed buffer size** — 使用固定大小的缓冲区 `off`（默认）| `on`

选中此复选框将使用固定大小的缓冲区保存先前时间步的输入数据。清除此复选框时，该模块不使用固定大小的缓冲区。

**Initial buffer size** 参数指定缓冲区大小。如果缓冲区已满，新数据将替换缓冲区中已有的数据。软件使用线性外推来估计不在缓冲区中的输出值。

**注意**

即使您未选中此复选框，ERT 或 GRT 代码生成也会使用固定大小的缓冲区。

#### 提示

- 如果输入数据是线性的，选中此复选框可以节省内存。
- 如果输入数据是非线性的，请不要选中此复选框。否则可能会产生不准确的结果。

### **Pade order (for linearization)** — Pade 近似的阶数 `0`（默认）| 正整数 | 向量

设置用于线性化例程的 Pade 近似阶数。

- 默认值为 `0`，这将产生单位增益且无动态状态。
- 将阶数设置为正整数 `n` 会向模型添加 `n` 个状态，但会得到更准确的延迟线性模型。

使用正整数向量为每个输入通道指定不同的阶数。

## 所属库

Control System Toolbox / Linear Parameter Varying

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

支持固定延迟和零延迟（直接馈通）的 Varying Delay

Varying Delay 模块扩展了 `Simulink` / `Continuous` 库中 Variable Transport Delay (Simulink) 模块的功能，额外支持指定固定延迟和零延迟。当您希望对零延迟、固定延迟和可变延迟的混合进行建模时，此模块很有用，这种情况可能出现在 LPV 模型中。
