---
type: simulink-block
title: 'LPC to/from RC'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lpctofromrc'
documentation_source_path: 'ref/lpctofromrc.html'
language: zh-CN
chinese_source: worker-translation
---

# LPC to/from RC

## 端口
```yaml
ports:
- name: K
  summary: RC 系数向量 | 矩阵
  direction: input
  data_types: single | double
- name: A
  summary: LPC 系数向量 | 矩阵
  direction: input
  data_types: single | double
- name: K
  summary: RC 系数向量 | 矩阵
  direction: output
  data_types: single | double
- name: A
  summary: LPC 系数向量 | 矩阵
  direction: output
  data_types: single | double
- name: P
  summary: 归一化预测误差功率向量
  direction: output
  data_types: single | double
- name: S
  summary: 滤波器稳定性输出向量
  direction: output
  data_types: Boolean
```

### 输入

### **K** — RC 系数向量 | 矩阵

将 RC 系数指定为向量或矩阵。该模块将矩阵的每一列视为一个通道。当您指定无方向向量时，该模块将输入视为一个通道。

#### 依赖关系

要启用此输入端口，请将 **Type of conversion** 设置为 `RC to LPC`。

**数据类型：** `single` | `double`

### **A** — LPC 系数向量 | 矩阵

将 LPC 系数指定为向量或矩阵。该模块将矩阵的每一列视为一个通道。当您指定无方向向量时，该模块将输入视为一个通道。

#### 依赖关系

要启用此输入端口，请将 **Type of conversion** 设置为 `LPC to RC`。

**数据类型：** `single` | `double`
### 输出

### **K** — RC 系数向量 | 矩阵

RC 系数，以向量或矩阵形式返回。

#### 依赖关系

要启用此输出端口，请将 **Type of conversion** 设置为 `LPC to RC`。

**数据类型：** `single` | `double`

### **A** — LPC 系数向量 | 矩阵

LPC 系数，以向量或矩阵形式返回。输入的每个通道必须至少有两个采样点。

#### 依赖关系

要启用此输出端口，请将 **Type of conversion** 设置为 `RC to LPC`。

**数据类型：** `single` | `double`

### **P** — 归一化预测误差功率向量

归一化预测误差功率，以向量形式返回，每个输入通道对应一个元素。每个元素的值在 0 到 1 之间变化。

#### 依赖关系

要启用此端口，请选中 **Output normalized prediction error power** 复选框。

**数据类型：** `single` | `double`

### **S** — 滤波器稳定性输出向量

滤波器稳定性输出，以向量形式返回，每个输入通道对应一个元素。滤波器由 LPC 或 RC 表示。

当 LPC 多项式的每个根的绝对值小于 1 时，由 LPC 表示的综合滤波器是稳定的。当每个反射系数的绝对值小于 1 时，由 RC 表示的格型滤波器是稳定的。当滤波器稳定时，该模块为每个输入通道输出布尔值 `1`。当滤波器不稳定时，该模块为每个输入通道输出布尔值 `0`。

#### 依赖关系

要启用此端口，请选中 **Output LPC filter stability** 复选框。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Type of conversion
  summary: 转换类型 RC to LPC（默认）| LPC to RC
  group: ''
- name: Output normalized prediction error power
  summary: 输出归一化预测误差功率 on（默认）| off
  group: ''
- name: Output LPC filter stability
  summary: 输出 LPC 滤波器稳定性 off（默认）| on
  group: ''
- name: If first input value is not 1
  summary: 当第一个输入值不为 1 时采取的操作 Replace it with 1（默认）| Normalize | Normalize and warn | Error
  group: ''
```

### **Type of conversion** — 转换类型 `RC to LPC`（默认）| `LPC to RC`

选择 `LPC to RC` 或 `RC to LPC` 以选择系数的转换域。

### **Output normalized prediction error power** — 输出归一化预测误差功率 `on`（默认）| `off`

选中此复选框以在端口 **P** 上输出归一化预测误差功率。

### **Output LPC filter stability** — 输出 LPC 滤波器稳定性 `off`（默认）| `on`

选中此复选框以输出滤波器的稳定性。

当 LPC 多项式的每个根的绝对值小于 1 时，由 LPC 表示的综合滤波器是稳定的。当每个反射系数的绝对值小于 1 时，由 RC 表示的格型滤波器是稳定的。当滤波器稳定时，该模块在 **S** 端口为每个输入通道输出布尔值 `1`。当滤波器不稳定时，该模块在 **S** 端口为每个输入通道输出布尔值 `0`。

### **If first input value is not 1** — 当第一个输入值不为 1 时采取的操作 `Replace it with 1`（默认）| `Normalize` | `Normalize and warn` | `Error`

指定当任何通道中 LPC 系数向量的第一个系数不为 1 时采取的操作。您可以将此参数设置为以下之一：

- `Replace it with 1` — 将系数通道的第一个值更改为 1。其他系数值保持不变。
- `Normalize` — 将整个系数通道除以第一个系数，使 LPC 系数向量的第一个系数为 1。
- `Normalize and Warn` — 将整个系数通道除以第一个系数，使 LPC 系数向量的第一个系数为 1。该模块会显示一条警告消息，告知您系数向量已被归一化。
- `Error` — 显示错误，告知您 LPC 系数通道的第一个系数不为 1。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `LPC to RC`。
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

将线性预测系数转换为反射系数，或将反射系数转换为线性预测系数

LPC to/from RC 模块可以将线性预测系数（LPC）转换为反射系数（RC），或将反射系数转换为线性预测系数。将 **Type of conversion** 参数设置为 `LPC to RC` 或 `RC to LPC` 以选择系数的转换域。有关详细信息，请参阅算法。

考虑一个信号 *x* (*n*)，作为由 LPC 系数表示的 FIR 分析滤波器的输入。分析滤波器的输出 *e* (*n*) 称为预测误差信号。该误差信号的功率记为 *P*。当 *x* (*n*) 的零延迟自相关系数为 1 时，自相关序列和预测误差功率被称为归一化的。
