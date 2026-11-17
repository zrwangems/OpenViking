---
type: simulink-block
title: 'Horizontal Wind Model 07'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel07'
documentation_source_path: 'horizontalwindmodel07.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model 07

## 端口
```yaml
ports:
- name: μ l h
  summary: 大地纬度、经度和位势高度三元向量 | 高度为 0 到 500 km 之间的值
  direction: input
  data_types: double
- name: day
  summary: 年积日 标量 | 值介于 1 到 366 之间
  direction: input
  data_types: double
- name: sec
  summary: 经过秒数 标量
  direction: input
  data_types: double
- name: Ap
  summary: Ap 指数 标量 | 范围从 0 到 400
  direction: input
  data_types: double
- name: Vwind
  summary: 风速向量 1×2 向量
  direction: output
  data_types: double
```

### 输入

### **μ l h** — 大地纬度、经度和位势高度三元向量 | 高度为 0 到 500 km 之间的值

大地纬度 (μ)、经度 (l) 和位势高度 (h)，
指定为三元向量。

纬度和经度值以度为单位。

高度值保持在 0 到 500 km 范围之外。高度值使用在**单位**中选择的
单位。

**数据类型：** `double`

### **day** — 年积日 标量 | 值介于 1 到 366 之间

协调世界时 (UTC) 的年积日，指定为 1 到 366 之间的值
（闰年）。值被包裹在 1 到 366
天的范围内。

**数据类型：** `double`

### **sec** — 经过秒数 标量

指定日期自午夜起经过的秒数，以 UTC 计。

**数据类型：** `double`

### **Ap** — Ap 指数 标量 | 范围从 0 到 400

世界时 (UT) 的 Ap 指数，指定为标量，范围
从 0 到 400。从 NOAA
国家地球物理数据中心选择该指数，其中包含 3 小时
间隔的地磁扰动指数值。如果 Ap 指数值
大于零，软件在模型评估期间会考虑磁
效应。

#### 依赖关系

要启用此端口，请将**模型**设置为
`Total` 或
`Disturbance`。

**数据类型：** `double`
### 输出

### **Vwind** — 风速向量 1×2 向量

风速向量，返回为 1×2 向量，包含
经向和纬向风分量，按此顺序。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: 字符向量
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Model
  summary: 水平风模型类型 Quiet（默认）| Total | Disturbance
  group: ''
  block_parameter: model
  type: 字符向量
  values: '''Quiet'' | ''Total'' | ''Disturbance'''
  default: '''Quiet'''
- name: Action for out-of-range input
  summary: 超出范围时的模块行为 Error（默认）| Warning | None
  group: ''
  block_parameter: action
  type: 字符向量
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
```

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

输入和输出单位，指定为：

| 单位 | 风速 | 风速 |
| --- | --- | --- |
| `Metric (MKS)` | 米每秒 | 米每秒 |
| `English (Velocity in ft/s)` | 英尺每秒 | 英尺每秒 |
| `English (Velocity in kts)` | 节 | 节 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：字符向量 |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Model** — 水平风模型类型 `Quiet`（默认）| `Total` | `Disturbance`

用于计算风分量的水平风模型类型，
指定为：

- `Disturbance`

  仅计算磁扰动对风的
  影响。
- `Quiet`

  计算无磁扰动的水平风
  模型。
- `Total`

  计算平静和磁扰动的
  综合影响。

#### 编程使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：字符向量 |
| **值**：`'Quiet'` | `'Total'` | `'Disturbance'` |
| **默认值**：`'Quiet'` |

### **Action for out-of-range input** — 超出范围时的模块行为 `Error`（默认）| `Warning` | `None`

超出范围时的模块行为，指定如下。

| 值 | 描述 |
| --- | --- |
| `None` | 不执行操作。模块对输入信号施加上限和下限。 |
| `Warning` | 在诊断查看器中发出警告，模型仿真继续。对于加速和快速加速模式，将操作设置为 `Warning` 无效，模型的行为如同操作设置为 `None`。 |
| `Error` | MATLAB® 返回异常，模型仿真停止。对于加速和快速加速模式，将操作设置为 `Error` 无效，模型的行为如同操作设置为 `None`。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：字符向量 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Warning'` |
## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：Horizontal Wind Model 07 模块可能更改返回值

Horizontal Wind Model 07 模块现在接受：

- **day** 端口值为小数、负数、
  `0` 或大于 `366`。
- **sec** 端口值为 `0` 或
  大于 `86400`。

因此，此模块的输出值可能与之前的
版本不同。

## 描述

实现 Horizontal Wind Model 07

Horizontal Wind Model 07 模块实现美国海军研究
实验室 HWM™ 例程，用于计算一组地理坐标的经向和纬向风分量：
纬度、经度和高度。
