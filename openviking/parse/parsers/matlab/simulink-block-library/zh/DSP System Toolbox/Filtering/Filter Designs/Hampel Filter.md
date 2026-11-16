---
type: simulink-block
title: 'Hampel Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Designs'
documentation_page: 'hampelfilter'
documentation_source_path: 'ref/hampelfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Hampel Filter

## 端口

### 输入

### **x** — 数据输入向量 | 矩阵

模块接受多通道输入，即 *m*×*n* 大小的输入，其中 *m* ≥ 1，*n* ≥ 1。*m* 是每帧（通道）中的样本数，*n* 是通道数。模块还接受可变大小输入。也就是说，可以在仿真期间更改每个输入通道的大小。但是，通道数不能更改。

在选择 **Specify threshold from input port** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **T** — 阈值 大于或等于 0 的实数标量

用于离群值检测的阈值，指定为大于或等于 0 的实数标量。有关如何使用此参数检测离群值的信息，请参阅算法。

#### 依赖关系

此端口在您选择 **Specify threshold from input port** 参数时出现。

**数据类型：** `single` | `double`

### 输出

### **y** — 滤波后的输出向量 | 矩阵

此输出的大小和数据类型与输入的大小和数据类型匹配。

在选择 **Output outlier status** 复选框之前，此端口未命名。

**数据类型：** `single` | `double`

### **outlier** — 输出离群值状态向量 | 矩阵

此输出中的 `1` 值表示输入中的对应元素是离群值。此输出的大小与输入相同。

#### 依赖关系

要启用此端口，请选中 **Output outlier status** 复选框。

**数据类型：** `Boolean`

## 参数

如果参数被列为可调，则可以在仿真期间更改其值。

### **Window length** — 滑动窗口的长度 `11`（默认） | 正奇标量整数

滑动窗口的长度，指定为正奇标量整数。有限长度窗口在数据上滑动，模块计算窗口中数据的中位数和中位数绝对偏差。

### **Specify threshold from input port** — 指定阈值的标志 off（默认） | on

选中此复选框时，阈值通过 **T** 端口输入。清除此复选框时，阈值通过 **Threshold for outlier detection (standard deviations)** 参数在模块对话框中指定。

### **Threshold for outlier detection (standard deviations)** — 阈值 3（默认） | 大于或等于 0 的实数标量

用于离群值检测的阈值，指定为大于或等于 0 的实数标量。有关如何使用此参数检测离群值的信息，请参阅算法。

**可调：** Yes

#### 依赖关系

当您清除 **Specify threshold from input port** 复选框时，此参数出现。

### **Output outlier status** — 用于输出离群值状态的标志 off（默认） | on

选中此参数以输出与输入大小相同的 `boolean` 值矩阵。此矩阵中的每个元素指示输入中的对应元素是否为离群值。`1` 值表示离群值。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认） | `Code generation`

指定要运行的仿真类型。可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真更快。

## 所属库

DSP System Toolbox / Filtering / Filter Designs

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

## 版本历史

**在 R2017a 中引入**

## 描述

使用 Hampel identifier 过滤离群值

Hampel Filter 模块使用 Hampel identifier 检测并去除输入信号中的离群值。Hampel identifier 是统计学三西格玛规则的一种变体，对离群值具有鲁棒性。对于输入信号的每个样本，模块计算一个窗口的中位数，该窗口由当前样本以及当前样本每一侧的 (*Len*−1)/2 个相邻样本组成。*Len* 是您通过 **Window length** 参数指定的窗口长度。模块还通过中位数绝对偏差估计每个样本相对于其窗口中位数的标准差。如果样本与中位数的差异大于阈值乘以标准差，则滤波器用中位数替换该样本。有关详细信息，请参阅算法。
