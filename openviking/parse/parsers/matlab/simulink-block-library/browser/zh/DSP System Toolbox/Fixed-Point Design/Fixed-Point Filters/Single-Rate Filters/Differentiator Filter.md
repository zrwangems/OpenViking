---
type: simulink-block
title: 'Differentiator Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filter Design and Analysis / Filter Design / Singlerate'
documentation_page: 'differentiatorfilter'
documentation_source_path: 'ref/differentiatorfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Differentiator Filter

## 端口

### 输入

### **Input** — 数据输入 向量 | 矩阵

指定数据输入为向量或矩阵。如果输入信号是矩阵，则矩阵的每一列被视为一个独立通道。

此模块支持可变大小输入，使您能够在仿真期间更改通道长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** Yes
### 输出

### **Output** — 微分器滤波器输出 向量 | 矩阵

微分器滤波器输出，以向量或矩阵形式返回。

输出端口属性（如数据类型、复/实性和维度）与输入端口属性相同。

**数据类型：** `single` | `double` | `fixed point`
**复数支持：** Yes

## 参数

### 主选项卡

### **Design minimum order filter** — 设计最小阶数滤波器 `on`（默认）| `off`

当您选中此复选框时，模块会设计一个具有最小阶数且使用您在 **Maximum passband ripple (dB)** 中指定的通带纹波的滤波器。当您清除此复选框时，请在 **Filter order** 中指定滤波器的阶数。

### **Filter order** — 微分器滤波器的阶数 `31`（默认）| 正奇数

将微分器滤波器的阶数指定为正奇数。

#### 依赖关系

要启用此参数，请清除 **Design minimum order filter** 参数。

### **Maximum passband ripple (dB)** — 最大通带纹波 `0.1`（默认）| 正标量

将通带中滤波器响应的最大纹波指定为以 dB 为单位的实正标量。

### **Scale filter coefficients** — 缩放滤波器系数 `off`（默认）| `on`

当您选中此复选框时，模块会缩放滤波器系数以保留输入动态范围。默认情况下，此复选框未选中。

### **View Filter Response** — 查看滤波器响应按钮（默认）

单击此按钮以打开 Filter Visualization Tool（`fvtool`）并显示 Differentiator Filter 模块的幅值和相位响应。该响应基于模块对话框参数。对这些参数所做的更改会更新 FVTool。

要在 FVTool 运行时更新幅值响应，请修改对话框参数，然后单击 **Apply**。

### **Simulate using** — 仿真方式 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution`
  （默认）

  使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，并且仿真速度比 `Code generation` 更快。
- `Code generation`

  使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但可提供更快的后续仿真。

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定输出定点运算的舍入方法。舍入方法有 `Ceiling`、`Convergent`、`Floor`、`Nearest`、`Round`、`Simplest` 和 `Zero`。默认值为 `Floor`。

### **Coefficients** — 系数 `fixdt(1,16)`（默认）| `fixdt(1,16,0)` | `<data type expression>`

将系数的定点数据类型指定为以下项之一：

- `fixdt(1,16)` — 字长为 `16` 且使用二进制小数点定标的带符号定点数据类型。模块根据系数值自动确定小数长度，使系数在不溢出的情况下占据最大可表示范围。
- `fixdt(1,16,0)` — 字长为 `16`、小数长度为 `0` 的带符号定点数据类型。您可以将小数长度更改为任何其他整数值。
- `<data type expression>` — 使用可求值为数据类型对象的表达式指定数据类型，例如数值类型 (`fixdt`(`[ ]`,`16`,`15`))。将此数据类型的符号模式指定为 `[ ]` 或 `true`。
- `Refresh Data Type` — 刷新为默认数据类型。

单击 **Show data type assistant** 按钮 以显示数据类型助手，它可帮助您设置阶段输入参数。

有关详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

输出的字长与输入的字长相同。输出的小数长度经过计算，使得输出的整个动态范围都能在不溢出的情况下表示。有关模块如何计算小数长度的详细信息，请参阅 Fixed-Point Precision Rules for Avoiding Overflow in FIR Filters。

## 所属库

DSP System Toolbox / Filtering / Filter Designs

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

当输入信号的数据类型为 `single` 或 `double` 时，Differentiator Filter 模块支持使用 Intel AVX2 代码替换库进行 SIMD 代码生成。

SIMD 技术可显著提高生成代码的性能。有关详细信息，请参阅 SIMD Code Generation。要从此模块生成 SIMD 代码，请参阅 Use Intel AVX2 Code Replacement Library to Generate SIMD Code from Simulink Blocks。

## 版本历史

**在 R2015b 中引入**

## 描述

直接型 FIR 全频带微分器滤波器

Differentiator Filter 模块对输入信号应用全频带微分器滤波器，以对其所有频率分量进行微分。该模块使用 FIR 等波纹滤波器设计来设计微分器滤波器。微分器的理想频率响应为 D(ω)=jω，其中 −π≤ω≤π。

您可以按最小阶数或指定阶数设计滤波器。

此模块还支持 SIMD 代码生成。有关详细信息，请参阅 Code Generation。
