---
type: simulink-block
title: 'Discrete Wind Gust Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'discretewindgustmodel'
documentation_source_path: 'discretewindgustmodel.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Wind Gust Model

## 端口
```yaml
ports:
- name: V
  summary: 空速标量
  direction: input
  data_types: double
- name: Vwind
  summary: 风速标量
  direction: output
  data_types: double
```

### 输入

### **V** — 空速标量

空速，指定为标量，采用所选单位。

**数据类型：** `double`
### 输出

### **Vwind** — 风速标量

风速，返回为标量，采用所选单位。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Gust in u-axis
  summary: 作用于 *u* 轴的阵风 on（默认）| off
  group: ''
  block_parameter: Gx
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Gust in v-axis
  summary: 作用于 *v* 轴的阵风 on（默认）| off
  group: ''
  block_parameter: Gy
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Gust in w-axis
  summary: 作用于 *w* 轴的阵风 on（默认）| off
  group: ''
  block_parameter: Gz
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''on'''
- name: Gust start time (sec)
  summary: 阵风开始时间 5（默认）| 标量
  group: ''
  block_parameter: t_0
  type: 字符向量
  values: 标量
  default: '''5'''
- name: Gust length [dx dy dz] (m)
  summary: 阵风长度 [120 120 80]（默认）
  group: ''
  block_parameter: d_m
  type: 字符向量
  values: 向量
  default: '''[120 120 80]'''
- name: Gust amplitude [ug vg wg] (m/s)
  summary: 阵风幅值 [3.5 3.5 3.0]（默认）
  group: ''
  block_parameter: d_m
  type: 字符向量
  values: 向量
  default: '''[3.5 3.5 3.0]'''
```

### **Units** — 单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

阵风的单位，指定为：

| 单位 | 风 | 高度 |
| --- | --- | --- |
| `Metric (MKS)` | 米/秒 | 米 |
| `English (Velocity in ft/s)` | 英尺/秒 | 英尺 |
| `English (Velocity in kts)` | 节 | 英尺 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Gust in u-axis** — 作用于 *u* 轴的阵风 `on`（默认）| `off`

要将阵风施加到机体坐标系中的 *u* 轴，请选中此复选框。否则，清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`Gx` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Gust in v-axis** — 作用于 *v* 轴的阵风 `on`（默认）| `off`

要将阵风施加到机体坐标系中的 *v* 轴，请选中此复选框。否则，清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`Gy` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Gust in w-axis** — 作用于 *w* 轴的阵风 `on`（默认）| `off`

要将阵风施加到机体坐标系中的 *w* 轴，请选中此复选框。否则，清除此复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`Gz` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

### **Gust start time (sec)** — 阵风开始时间 `5`（默认）| 标量

阵风开始的模型时间，指定为标量，单位为秒。

#### 编程使用

|  |
| --- |
| **模块参数**：`t_0` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'5'` |

### **Gust length [dx dy dz] (m)** — 阵风长度 `[120 120 80]`（默认）

阵风在每个轴上累积的长度，单位为米或英尺（取决于所选单位）。这些值必须为正。

#### 编程使用

|  |
| --- |
| **模块参数**：`d_m` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[120 120 80]'` |

### **Gust amplitude [ug vg wg] (m/s)** — 阵风幅值 `[3.5 3.5 3.0]`（默认）

阵风在每个轴上引起的风速增量的幅值。这些值可以为正或负。

#### 编程使用

|  |
| --- |
| **模块参数**：`d_m` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[3.5 3.5 3.0]'` |
## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成离散阵风

Discrete Wind Gust Model 模块实现标准“1-cosine”形状的阵风。此模块实现了军用规范 MIL-F-8785C [1] 中的数学表示。阵风可分别施加到每个轴，或同时施加到所有三个轴。您可以指定阵风幅值（阵风产生的风速增量）、阵风长度（阵风累积的长度，单位为米）以及阵风开始时间。有关阵风形状的详细信息，请参阅算法。

Discrete Wind Gust Model 模块可以以英尺/秒、米/秒或节为单位表示风速。
