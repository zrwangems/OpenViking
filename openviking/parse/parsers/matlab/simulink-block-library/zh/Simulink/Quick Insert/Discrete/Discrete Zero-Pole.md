---
type: simulink-block
title: 'Discrete Zero-Pole'
family: 'simulink-extras'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Additional Discrete'
documentation_page: 'discretezeropole'
documentation_source_path: 'slref/discretezeropole.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Zero-Pole

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量
  direction: input
  data_types: single | double
- name: Port_1
  summary: 离散系统模型 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号 标量

输入信号，指定为实值标量。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 离散系统模型 标量 | 向量

由离散传递函数的零点、极点和增益定义的系统模型。输出的宽度等于 **Zeros** 矩阵的列数，如果 **Zeros** 是向量则为 1。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Zeros
  summary: 零点矩阵 [1]（默认）| 向量 | 矩阵
  group: 主要
  block_parameter: Zeros
  type: character vector
  values: vector
  default: '''[1]'''
- name: Poles
  summary: 极点向量 [0 0.5]（默认）| 向量
  group: 主要
  block_parameter: Poles
  type: character vector
  values: vector
  default: '''[0 0.5]'''
- name: Gain
  summary: 增益值 1（默认）| 标量 | 向量
  group: 主要
  block_parameter: Gain
  type: character vector
  values: scalar | vector
  default: '''1'''
- name: Sample time (-1 for inherited)
  summary: 采样间隔 -1 | 标量 | 向量
  group: 主要
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''-1'''
- name: State name
  summary: 模块状态的唯一名称 ''（默认）| 字母数字字符串
  group: 状态属性
  block_parameter: StateName
  type: character vector
  values: unique name
  default: ''''''
- name: State name must resolve to Simulink signal object
  summary: 要求状态名称解析为信号对象 off（默认）| on
  group: 状态属性
  block_parameter: StateMustResolveToSignalObject
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
```

### 主要

### **Zeros** — 零点矩阵 `[1]`（默认）| 向量 | 矩阵

指定零点向量或矩阵。零点数量必须小于或等于极点数量。如果极点和零点为复数，则它们必须为共轭复数对。

- 对于单输出系统，输入传递函数零点的向量。
- 对于多输出系统，输入一个矩阵。矩阵的每一列包含一个传递函数的零点，该传递函数将系统输入与其中一个输出相关联。

#### 编程使用

|  |
| --- |
| **模块参数**：`Zeros` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'[1]'` |

### **Poles** — 极点向量 `[0 0.5]`（默认）| 向量

指定极点向量。极点数量必须大于或等于零点数量。如果极点和零点为复数，则它们必须为共轭复数对。

- 对于单输出系统，输入传递函数极点的向量。
- 对于多输出系统，输入系统所有传递函数共有的极点的向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`Poles` |
| **类型**：character vector |
| **值**：vector |
| **默认值**：`'[0 0.5]'` |

### **Gain** — 增益值 `1`（默认）| 标量 | 向量

指定增益值的向量。

- 对于单输出系统，输入传递函数增益的标量或 1×1 向量。
- 对于多输出系统，输入增益的向量。每个元素是 **Zeros** 中对应传递函数的增益。

#### 编程使用

|  |
| --- |
| **模块参数**：`Gain` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'1'` |

### **Sample time (-1 for inherited)** — 采样间隔 `-1` | 标量 | 向量

指定采样之间的时间间隔。有关详细信息，请参阅 Specifying Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'-1'` |

### 状态属性

### **State name** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **Apply** 时，此参数会启用 **State name must resolve to Simulink signal object**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateName` |
| **类型**：character vector |
| **值**：unique name |
| **默认值**：`''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框以要求状态名称解析为 Simulink® 信号对象。

#### 依赖关系

要启用此参数，请为 **State name** 指定一个值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，此参数才会显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateMustResolveToSignalObject` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |
## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前推出**

## 描述

对由离散传递函数的零点和极点定义的系统进行建模

Discrete Zero-Pole 模块对由 *z* 域传递函数的零点、极点和增益定义的离散系统进行建模。此模块假设传递函数具有以下形式：

H(z)=KZ(z)P(z)=K(z−Z1)(z−Z2)...(z−Zm)(z−P1)(z−P2)...(z−Pn)，

其中 *Z* 表示零点向量，*P* 表示极点向量，*K* 表示增益。极点数量必须大于或等于零点数量（*n* ≥ *m*）。如果极点和零点为复数，则它们必须为共轭复数对。

模块显示传递函数的方式取决于参数的指定方式。有关详细信息，请参阅 Zero-Pole。

### 对单输出系统建模

对于单输出系统，模块的输入和输出为标量时域信号。要对此系统建模：

1. 在 **Zeros** 字段中输入传递函数零点的向量。
2. 在 **Poles** 字段中输入传递函数极点的向量。
3. 在 **Gain** 字段中输入传递函数增益的 1×1 向量。

### 对多输出系统建模

对于多输出系统，模块输入为标量，输出为向量，其中每个元素是系统的一个输出。要对此系统建模：

1. 在 **Zeros** 字段中输入零点矩阵。

   此矩阵的每一*列*包含一个传递函数的零点，该传递函数将系统输入与其中一个输出相关联。
2. 在 **Poles** 字段中输入系统所有传递函数共有的极点的向量。
3. 在 **Gain** 字段中输入增益的向量。

   每个元素是 **Zeros** 中对应传递函数的增益。

输出向量的每个元素对应于 **Zeros** 中的一列。
