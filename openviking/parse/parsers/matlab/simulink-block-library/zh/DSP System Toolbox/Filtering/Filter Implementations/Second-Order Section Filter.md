---
type: simulink-block
title: 'Second-Order Section Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'secondordersectionfilter'
documentation_source_path: 'ref/secondordersectionfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Second-Order Section Filter

## 端口

### 输入

### **In** — 输入信号 向量 | 矩阵

将输入信号指定为向量或矩阵。输入可以是可变大小信号，即信号的帧大小可以在仿真期间变化，但通道数不能变化。

在将 **Coefficient source** 参数设置为 `Input ports` 之前，此端口没有名称。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Num** — 分子系数 *P*×3 矩阵

将 SOS 滤波器的分子系数指定为 *P*×3 矩阵，其中 *P* 是滤波器节数。有关此输入端的更多详细信息，请参阅 **Numerator**。

在仿真期间，您不能更改系数矩阵的大小，但可以更改系数值。

**Num** 和 **Den** 输入的大小和复数性质必须相同。

#### 依赖关系

要启用此端口，请将 **Coefficient source** 参数设置为 `Input ports`。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Den** — 分母系数 *P*×3 矩阵 | *P*×2 矩阵

将 SOS 滤波器的分母系数指定为 *P*×3 矩阵或 *P*×2 矩阵，其中 *P* 是滤波器节数。有关此输入端的更多详细信息，请参阅 **Denominator**。

当您指定 *P*×3 矩阵时，模块始终假定前导分母系数为 1。如果您在第一列中指定任何其他值，模块将忽略此值并将其视为 1。如果您指定 *P*×2 矩阵，模块将在矩阵的每一行前面添加一个值为 1 的列。

在仿真期间，您不能更改系数矩阵的大小，但可以更改系数值。

**Num** 和 **Den** 输入的大小和复数性质必须相同。

#### 依赖关系

要启用此端口，请将 **Coefficient source** 参数设置为 `Input ports`。

**数据类型：** `single` | `double`
**复数支持：** 是

### **g** — 每个二阶节的缩放值 标量 | 向量

将模块在 SOS 滤波器每个节之前和之后应用的缩放值指定为标量或具有 *P* + 1 个元素的向量，其中 *P* 是滤波器节数。

如果您输入标量，模块将在第一个滤波器节之前应用此增益值，并将所有其他节之前的增益值设置为 `1`。如果您指定 *P* + 1 个值的向量，模块将每个值应用于滤波器的单独节。

**可调：** 是

#### 依赖关系

要启用此端口，请将 **Coefficient source** 设置为 `Input ports` 并选中 **Specify scale values** 参数。

**数据类型：** `single` | `double`
### 输出

### **Out** — 滤波后的输出 向量 | 矩阵

滤波后的输出，以向量或矩阵形式返回。输出的大小和数据类型与输入相同。如果输入信号、分子系数或分母系数为复数，则输出信号为复数。

在将 **Coefficient source** 参数设置为 `Input ports` 之前，此端口没有名称。

**数据类型：** `single` | `double`
**复数支持：** 是

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Filter structure** — 滤波器结构 `Direct form II transposed`（默认）| `Direct form I` | `Direct form I transposed` | `Direct form II`

将滤波器结构指定为以下之一：

- `Direct form I`
- `Direct form I transposed`
- `Direct form II`
- `Direct form II transposed`

### **Coefficient source** — 滤波器系数来源 `Dialog parameters`（默认）| `Input ports`

将滤波器系数来源指定为以下之一：

- `Dialog parameters` —— 通过模块对话框中的 **Numerator**、**Denominator** 和 **Scale Values** 参数设置滤波器系数和缩放值。
- `Input ports` —— 通过 **Num**、**Den** 和 **g** 输入端口设置滤波器系数和缩放值。

### **Numerator** — 滤波器的分子系数 [`0.0975 0.195 0.0975`]（默认）| *P*×3 矩阵

将 SOS 滤波器的分子系数 **b** 指定为 *P*×3 矩阵，其中 *P* 是滤波器节数。

b=[b01b11b21b02b12b22⋮⋮⋮b0Pb1Pb2P]

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **a** 是分母系数矩阵。有关如何指定此矩阵的更多详细信息，请参阅 **Denominator**。
- *k* 是行索引。

在仿真期间不能更改此参数的大小，但可以更改其值。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 `Dialog parameters`。

**可调：** 是

**数据类型：** `single` | `double`
**复数支持：** 是

### **Denominator** — 滤波器的分母系数 [`1 -0.9428 0.3333`]（默认）| *P*×3 矩阵 | *P*×2 矩阵

将 SOS 滤波器的分母系数 **a** 指定为 *P*×3 矩阵或 *P*×2 矩阵，其中 *P* 是滤波器节数。

a=[a01a11a21a02a12a22⋮⋮⋮a0Pa1Pa2P]

模块算法假定前导系数的值始终为 1。如果分母的大小为 *P*×2，模块算法将在分母前面添加一列 1，将其大小更改为 *P*×3。如果分母的大小为 *P*×3 且第一列中的元素不等于 1，算法将忽略第一列中的值并将其设置为 1。

此方程以传递函数形式表示 SOS 滤波器。

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

其中

- **b** 是分子系数矩阵。有关如何指定此矩阵的更多详细信息，请参阅 **Numerator**。
- *k* 是行索引。

在仿真期间不能更改此参数的大小，但可以更改其值。

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 `Dialog parameters`。

**可调：** 是

**数据类型：** `single` | `double`
**复数支持：** 是

### **Specify scale values** — 指定滤波器是否为每个节具有缩放值 `off`（默认）| `on`

指定滤波器是否为每个节具有缩放值。当您选中此参数时，可以使用模块对话框中的 **Scale Values** 参数或通过 **g** 输入端口指定缩放值。

### **Scale Values** — 每个二阶节的缩放值 [`1 1`]（默认）| 标量 | 向量

将模块在 SOS 滤波器每个节之前和之后应用的缩放值指定为标量或具有 *P* + 1 个元素的向量，其中 *P* 是滤波器节数。

如果将此属性设置为标量，模块将在第一个滤波器节之前应用此增益值，并将所有其他节之前的增益值设置为 `1`。如果将此属性设置为 *P* + 1 个值的向量，模块将每个值应用于滤波器的单独节。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Coefficient source** 设置为 `Dialog parameters` 并选中 **Specify scale values** 参数。

**数据类型：** `single` | `double`

### **Input processing** — 处理输入的方法 `Columns as channels (frame based)`（默认）| `Elements as channels (sample based)`

将输入处理方法指定为以下之一：

- `Columns as channels (frame based)` —— 模块将输入的每一列视为单独的通道。

  有关更多信息，请参阅 What Is Frame-Based Processing?
- `Elements as channels (sample based)` —— 模块将输入的每个元素视为单独的通道。

  有关更多信息，请参阅 What Is Sample-Based Processing?

### **View Filter Response** — 查看滤波器响应 按钮

打开 Filter Visualization 工具并显示 SOS 滤波器的幅值响应。响应基于您在模块对话框中选择的参数。要更新幅值响应，请修改对话框中的参数并点击 **Apply**。

## 所属库

DSP System Toolbox / Filtering / Filter Implementations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

**符号维度支持**

此模块支持为仿真和代码生成设置符号维度。您可以在模块中将维度信息指定为符号（变量）。这些符号在仿真期间传播到整个模型，然后进入生成的代码。这样，您就不需要在每次更新此信息时更改模块中的维度。

- 支持符号维度的端口如下：

  - `Num` —— 维度必须为 `[P 3]`，其中 `P` 是节数。
  - `Den` —— 维度必须为 `[P M]`，其中 `M` 可以是 `2` 或 `3`。
  - `g` —— 维度必须为 `P+1`，其中 `P` 是节数。
- 模块仅在正常仿真模式下支持符号维度。

您必须具有 Simulink Coder™ 和 Embedded Coder® 才能使用此功能。

有关更多信息，请参阅 Implement Symbolic Dimensions for Array Sizes in Generated Code (Embedded Coder)。

## 版本历史

**在 R2023b 中引入**

### R2025a：使用符号维度进行仿真和代码生成

Second-Order Section Filter 模块支持为仿真和代码生成设置符号维度。

## 描述

实现二阶节滤波器级联

Second-Order Section Filter 模块在 Simulink® 中实现二阶节 (SOS) 滤波器的级联。您可以在模块参数对话框中或通过输入端口指定滤波器的分子和分母系数。
