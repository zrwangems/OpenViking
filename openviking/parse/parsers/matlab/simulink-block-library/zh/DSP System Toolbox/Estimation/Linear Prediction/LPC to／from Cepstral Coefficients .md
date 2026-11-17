---
type: simulink-block
title: 'LPC to/from Cepstral Coefficients'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Estimation / Linear Prediction'
documentation_page: 'lpctofromcepstralcoefficients'
documentation_source_path: 'ref/lpctofromcepstralcoefficients.html'
language: zh-CN
chinese_source: worker-translation
---

# LPC to/from Cepstral Coefficients

## 端口
```yaml
ports:
- name: A
  summary: LPC 系数向量 | 矩阵
  direction: input
  data_types: single | double
- name: CC
  summary: 倒谱系数向量 | 矩阵
  direction: input
  data_types: single | double
- name: P
  summary: 预测误差功率标量 | 向量
  direction: input
  data_types: single | double
- name: CC
  summary: 倒谱系数向量 | 矩阵
  direction: output
  data_types: single | double
- name: P
  summary: 预测误差功率标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **A** — LPC 系数向量 | 矩阵

将 LPC 系数指定为向量或矩阵。该模块将矩阵的每一列视为一个通道。当您指定一个无方向向量时，该模块将输入视为一个通道。

在您将 **Specify P** 设置为 `via input port` 之前，此端口是未命名的。

#### 依赖关系

要启用此端口，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`。

**数据类型：** `single` | `double`

### **CC** — 倒谱系数向量 | 矩阵

将倒谱系数指定为向量或矩阵。该模块将矩阵的每一列视为一个通道。当您指定一个无方向向量时，该模块将输入视为一个通道。

#### 依赖关系

要启用此端口，请将 **Type of conversion** 设置为 `Cepstral coefficients to LPCs`。

**数据类型：** `single` | `double`

### **P** — 预测误差功率标量 | 向量

通过此端口将每个通道的预测误差功率 *P* 指定为向量。此向量的长度必须等于输入中的通道数。

#### 依赖关系

要启用此端口，请将 **Specify P** 设置为 `via input port`。

**数据类型：** `single` | `double`
### 输出

### **CC** — 倒谱系数向量 | 矩阵

倒谱系数，以向量或矩阵形式返回。

#### 依赖关系

要启用此端口，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`。

**数据类型：** `single` | `double`

### **P** — 预测误差功率标量 | 向量

每个通道的预测误差功率 *P*，通过此端口以标量或向量形式返回。此向量的长度必须等于输入中的通道数。

#### 依赖关系

要启用此端口，请选中 **Output P**。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Type of conversion
  summary: 转换类型 LPCs to cepstral coefficients（默认）| Cepstral coefficients to LPCs
  group: ''
- name: Specify P
  summary: 指定预测误差功率 *P* 的方法 assume P equals 1（默认）| via input port
  group: ''
- name: Output P
  summary: 输出预测误差功率 *P* off（默认）| on
  group: ''
- name: Output size same as input size
  summary: 输出大小与输入大小相同 off（默认）| on
  group: ''
- name: Length of output cepstral coefficients vector
  summary: 输出倒谱系数向量的长度 10（默认）| 正整数
  group: ''
- name: If first input value is not 1
  summary: 当第一个输入值不为 1 时采取的操作 Replace it with 1（默认）| Normalize | Normalize and warn | Error
  group: ''
```

### **Type of conversion** — 转换类型 `LPCs to cepstral coefficients`（默认）| `Cepstral coefficients to LPCs`

将系数转换的域指定为以下之一：

- `LPCs to cepstral
  coefficients`
- `Cepstral coefficients to
  LPCs`

### **Specify P** — 指定预测误差功率 *P* 的方法 `assume P equals 1`（默认）| `via input port`

使用以下选项之一指定预测误差功率 *P*：

- `assume P equals 1` —— 将所有通道的 *P* 值指定为 1。
- `via input port` —— 使用 **P** 端口输入每个通道的预测误差功率。此向量的长度必须等于输入中的通道数。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`。

### **Output P** — 输出预测误差功率 *P* `off`（默认）| `on`

选中此复选框可从输出端口 **P** 输出每个通道的预测误差功率。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `Cepstral coefficients to LPCs`

### **Output size same as input size** — 输出大小与输入大小相同 `off`（默认）| `on`

当您选中此复选框时，LPC 输入向量的长度等于 CC 输出向量的长度。当您不选中此复选框时，请为 **Length of output cepstral coefficients** 参数输入一个正标量。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`。

### **Length of output cepstral coefficients vector** — 输出倒谱系数向量的长度 `10`（默认）| 正整数

将输出倒谱系数向量的长度指定为正整数。此值决定输出倒谱系数中每个通道的长度。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`

### **If first input value is not 1** — 当第一个输入值不为 1 时采取的操作 `Replace it with 1`（默认）| `Normalize` | `Normalize and warn` | `Error`

指定当 LPC 系数向量的第一个系数不为 1 时采取的操作。您可以将此参数设置为以下选项之一：

- `Replace it with 1` —— 该模块将系数向量的第一个值更改为 1。其余系数值保持不变。
- `Normalize` —— 该模块将整个系数向量除以第一个系数，使 LPC 系数向量的第一个系数为 1。
- `Normalize and Warn` —— 该模块将整个系数向量除以第一个系数，使 LPC 系数向量的第一个系数为 1。该模块显示一条警告消息，说明系数向量已被归一化。
- `Error` —— 该模块显示一个错误，说明 LPC 系数向量的第一个系数不为 1。

#### 依赖关系

要启用此参数，请将 **Type of conversion** 设置为 `LPCs to cepstral coefficients`。
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

将线性预测系数转换为倒谱系数，或将倒谱系数转换为线性预测系数

LPC to/from Cepstral Coefficients 模块可以将线性预测系数 (LPC) 转换为倒谱系数 (CC)，或将倒谱系数转换为线性预测系数。将 **Type of conversion** 参数设置为 `LPCs to cepstral coefficients` 或 `Cepstral coefficients to LPCs`，以选择系数转换的域。有关详细信息，请参阅算法。

考虑信号 *x*(*n*) 作为由 LPC 表示的 FIR 分析滤波器的输入。此分析滤波器的输出 *e*(*n*) 称为预测误差信号。此误差信号的功率记为 *P*，即预测误差功率。
