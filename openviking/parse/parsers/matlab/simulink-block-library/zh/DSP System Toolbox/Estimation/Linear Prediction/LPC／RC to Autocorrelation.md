---
type: simulink-block
title: 'LPC/RC to Autocorrelation'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lpcrctoautocorrelation'
documentation_source_path: 'ref/lpcrctoautocorrelation.html'
language: zh-CN
chinese_source: worker-translation
---

# LPC/RC to Autocorrelation

## 端口

### 输入

### **A** — LPC 系数向量 | 矩阵

将 LPC 系数指定为向量或矩阵。模块将矩阵的每一列视为一个单独通道。当您指定未定向向量时，模块将输入视为一个通道。

#### 依赖关系

要启用此端口，请将 **转换类型** 设置为 `LPC to autocorrelation`。

**数据类型：** `single` | `double`

### **K** — RC 系数向量 | 矩阵

将 RC 系数指定为向量或矩阵。模块将矩阵的每一列视为一个单独通道。当您指定未定向向量时，模块将输入视为一个通道。

#### 依赖关系

要启用此端口，请将 **转换类型** 设置为 `RC to autocorrelation`。

**数据类型：** `single` | `double`

### **P** — 预测误差功率标量 | 向量

通过此端口将每个通道的非单位预测误差功率 *P* 指定为向量。该向量的长度必须等于输入中的通道数。

#### 依赖关系

要启用此端口，请将 **指定 P** 设置为 `Via input port`。

**数据类型：** `single` | `double`

### 输出

### **AC** — 自相关系数向量 | 矩阵

自相关系数，以向量或矩阵形式返回。

**数据类型：** `single` | `double`

## 参数

### **转换类型** — 转换类型 `LPC to autocorrelation`（默认） | `RC to autocorrelation`

将系数的转换域指定为以下之一：

- `LPC to autocorrelation`
- `RC to autocorrelation`

### **指定 P** — 指定预测误差功率 *P* 的方法 `Assume P = 1`（默认） | `Via input port`

使用以下选项之一指定预测误差功率 *P*：

- `Assume P=1` –– 将 *P* 的值指定为 1。
- `Via input port` –– 使用 **P** 端口输入每个通道的实际非单位预测误差功率值。该向量的长度必须等于输入中的通道数。

### **如果第一个输入值不为 1** — 当第一个输入值不为 1 时要执行的操作 `Replace it with 1`（默认） | `Normalize` | `Normalize and warn` | `Error`

指定当 LPC 系数向量的第一个系数不为 1 时要执行的操作。您可以将此参数设置为以下选项之一：

- `Replace it with 1` — 模块将系数向量的第一个值更改为 1。其余系数值保持不变。
- `Normalize` — 模块将整个系数向量除以第一个系数，以使 LPC 系数向量的第一个系数为 1。
- `Normalize and Warn` — 模块将整个系数向量除以第一个系数，以使 LPC 系数向量的第一个系数为 1。模块会显示一条警告消息，说明系数向量已归一化。
- `Error` — 模块会显示错误，告知您 LPC 系数向量的第一个系数不为 1。

#### 依赖关系

要启用此参数，请将 **转换类型** 设置为 `LPC to autocorrelation`。

## 所属库

DSP System Toolbox / Estimation / Linear Prediction

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将线性预测系数或反射系数转换为自相关系数

LPC/RC to Autocorrelation 模块可以将线性预测系数 (LPC) 转换为自相关系数 (AC)，或将反射系数 (RC) 转换为自相关系数 (AC)。将 **转换类型** 参数设置为 `LPC to autocorrelation` 或 `RC to autocorrelation`，以选择系数的转换域。
