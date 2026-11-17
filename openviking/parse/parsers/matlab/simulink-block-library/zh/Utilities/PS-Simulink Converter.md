---
type: simulink-block
title: 'PS-Simulink Converter'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'pssimulinkconverter'
documentation_source_path: '../simscape/ref/pssimulinkconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# PS-Simulink Converter

## 端口

### 输入

### **PS** — 输入物理信号 physical signal

该模块将其转换为输出 Simulink 信号的输入物理信号。
### 输出

### **Port\_1** — 输出 Simulink 信号 scalar | vector | matrix

该模块在转换输入物理信号后输出的 Simulink 信号。信号大小与输入物理信号的大小相匹配。**Output signal unit** 参数和 **Apply affine conversion** 复选框允许您对输入信号值应用缩放和线性偏移，以计算输出信号的正确值。

**Data Types:** `double`

## 参数

### **Vector format** — 指定如何输出向量物理信号 `inherit` (default) | `1-D array`

指定如何输出向量物理信号：

- `inherit` — 将 Simulink 输出信号格式化为与物理信号格式匹配：标量、行向量或列向量，或二维矩阵。
- `1-D array` — 如果物理信号是行向量或列向量，则将输出信号格式化为 Simulink 一维数组。使用此选项可简化此类信号的绘图。

### **Output signal unit** — 指定信号值转换的缩放因子 `inherit` (default) | `1` | `V` | `A` | `m^3/s` | `Pa` | `N` | `m` | `m/s` | `N*m` | `rad/s` | `rad` | `K` | `kg/s` | `J/s` | `kg` | `Wb` | `<unit expression>`

指定输出信号的所需单位。这些单位必须与进入模块的输入物理信号的单位一致。系统将您指定的单位与输入物理信号的实际单位进行比较，并在输出 Simulink 信号之前应用等于转换因子的增益。您可以从下拉列表中选择单位，或键入所需的单位名称（如 `rpm`）或有效表达式（如 `mm/s`）。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。默认值为 `inherit`，这意味着输出单位与模块输入端口处的单位匹配，且不应用增益。

### **Apply affine conversion** — 为仿射温度单位选择转换方法 off (default) | on

此复选框仅适用于可以使用或不使用仿射偏移进行转换的单位，例如 `degC` 或 `degF`。如果输出信号表示以摄氏度或华氏度为单位的绝对温度，请选中此复选框。有关更多信息，请参阅 Thermal Unit Conversions。

## 所属库

Simscape / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2022a：选择输出向量物理信号的格式

该模块包含一个附加参数 **Vector format**，它允许您指定如何输出向量物理信号：

- `inherit` — 将 Simulink 输出信号格式化为与物理信号格式匹配：标量、行向量或列向量，或二维矩阵。这是新模型的默认设置。
- `1-D array` — 如果物理信号是行向量或列向量，则将输出信号格式化为 Simulink 一维数组。此选项对应于以前版本中 PS-Simulink Converter 模块处理向量物理信号的方式。为保持向后兼容性，在 R2022a 之前创建的模型中，**Vector Format** 参数自动设置为 `1-D array`。

## 描述

将物理信号转换为 Simulink 输出信号

PS-Simulink Converter 模块将物理信号转换为 Simulink® 输出信号。使用此模块可将 Simscape™ 物理网络的输出连接到 Simulink 示波器或其他 Simulink 模块。

### 模块图标在模型画布上的显示

为了在传达信号转换的同时占用最少的画布空间，模块图标会根据是否连接到其他模块而动态变化。

| 当模块为... | 模块图标 |
| --- | --- |
| 未连接 |  |
| 连接到其他模块 |  |

### 单位转换与检查

**Output signal unit** 参数允许您指定输出信号的期望单位。这些单位必须与进入模块的输入物理信号单位一致。如果您指定了期望的输出单位，模块会在输出 Simulink 信号之前施加一个等于转换系数的增益。例如，如果进入模块的输入物理信号是位移，单位为米，而您将 **Output signal unit** 设置为 `mm`，则模块会在输出之前将输入信号的值乘以 1e3。如果输出信号单位与输入信号单位相同，则不施加增益。

**Output signal unit** 参数的默认值 `inherit` 会根据单位传播规则，自动将模块输出端口处的单位设置为与进入模块的输入物理信号单位匹配。这样，您可以轻松地将 PS-Simulink Converter 模块连接到任何信号，而无需担心设置一致的输出单位。

在下图中，PS-Simulink Converter 模块的输入信号是扭矩，单位为 N\*m，如果您不指定输出信号单位，Display 模块显示值为 10。如果您将 PS-Simulink Converter 模块中的 **Output signal unit** 参数值更改为 `N*cm`，则 Display 模块中的扭矩值变为 1000，如下图所示。

当输出信号与热力学变量相关且包含温度单位时，您必须决定是否需要应用仿射转换。有关详细信息，请参阅何时应用仿射转换。通常，如果输出信号表示相对温度，即温度变化，则需要应用线性转换，Δ*Tnew* = *L* \* Δ*Told*（默认方法）。但是，如果输出信号表示绝对温度，则需要应用仿射转换，*Tnew* = *L* \* *Told* + *O*。

在下图中，Display 模块显示室温。如果您想以摄氏度显示，请打开 PS-Simulink Converter 模块，在 **Output signal unit** 字段中键入 `degC`，并选中 **Apply affine conversion** 复选框。显示读数为 24.35。但是，如果您不清除 **Apply affine conversion** 复选框，Display 模块将显示 297.5。

**注意**

通过 **Output signal unit** 参数为输出信号指定的单位不会传播到物理网络之外。但是，如果您还指定了连接到模块输出端口的 Simulink 信号的物理单位属性，软件会检查这两个单位是否匹配。有关详细信息，请参阅使用 Simulink 单位。
