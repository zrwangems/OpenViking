---
type: simulink-block
title: 'Horizontal Wind Model 14'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Environment / Wind'
documentation_page: 'horizontalwindmodel14'
documentation_source_path: 'horizontalwindmodel14.html'
language: zh-CN
chinese_source: worker-translation
---

# Horizontal Wind Model 14

## 端口
```yaml
ports:
- name: First
  summary: 大地纬度 (μ)、经度 (l) 和位势高度 (h) 的三元素双精度向量
  direction: input
- name: Second
  summary: 年积日标量双精度值
  direction: input
- name: Third
  summary: 经过秒数标量双精度值
  direction: input
- name: Fourth (Optional)
  summary: Ap 指数标量双精度值
  direction: input
- name: First
  summary: 风速向量 1×2 双精度向量
  direction: output
```

### 输入

### **First** — 大地纬度 (μ)、经度 (`l`) 和位势高度 (`h`) 的三元素双精度向量

该输入指定大地纬度 (μ)、经度
(`l`) 和位势高度 (`h`)，
模块在该位置实现模型。

纬度和经度值以度为单位。

高度值使用您在 **Units** 参数中选择的单位。
将高度元素指定为 0 到 500 km 之间的值。超出 0 到 500 km 范围的值
将被保持。

### **Second** — 年积日标量双精度值

该输入指定协调世界时 (UTC) 的年积日。该输入将
日期指定为 1 到 366 之间的值（适用于闰年）。值将被
包裹在 1 到 366 天范围内。

### **Third** — 经过秒数标量双精度值

包含所选日期自午夜起经过的秒数，
以 UTC 计。

### **Fourth (Optional)** — Ap 指数标量双精度值

包含模块评估模型时的世界时 (UT) 对应的 Ap 指数。从 NOAA
国家地球物理数据中心选择该指数，其中包含 3 小时间隔的地磁扰动指数值。如果 Ap 指数值
大于零，软件在模型评估期间会考虑磁效应。
### 输出

### **First** — 风速向量 1×2 双精度向量

风速向量按顺序包含经向和纬向风
分量。
## 参数
```yaml
parameters:
- name: Units
  summary: 输入和输出单位 Metric (MKS)（默认）| English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Model
  summary: 水平风模型 Quiet（默认）| Total | Disturbance
  group: ''
  block_parameter: model
  type: character vector
  values: '''Quiet'' | ''Total'' | ''Disturbance'''
  default: '''Quiet'''
- name: Action for out-of-range input
  summary: 模块行为 Error（默认）| Warning | None
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Error'''
```

### **Units** — 输入和输出单位 `Metric (MKS)`（默认）| `English (Velocity in ft/s)` | `English (Velocity in kts)`

风速和风速的输入和输出单位，指定为：

| Units | Wind Speed | Wind Velocity |
| --- | --- | --- |
| `Metric (MKS)` | 米每秒 | 米每秒 |
| `English (Velocity in ft/s)` | 英尺每秒 | 英尺每秒 |
| `English (Velocity in kts)` | 节 | 节 |

#### 编程使用

|  |
| --- |
| **模块参数**：`units` |
| **类型**：character vector |
| **值**：`'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **默认值**：`'Metric (MKS)'` |

### **Model** — 水平风模型 `Quiet`（默认）| `Total` | `Disturbance`

选择用于计算风分量的水平风模型类型。

- `Quiet`

  计算不含磁扰动的水平风模型。
  对于此模型类型，不要输入 Ap 指数值。
- `Total`

  计算平静期和磁扰动的综合效应。
  对于此模型类型，输入大于或等于零的 Ap 指数值。
- `Disturbance`

  计算风中磁扰动的效应。对于
  此模型类型，输入大于或等于零的 Ap 指数值。

#### 编程使用

|  |
| --- |
| **模块参数**：`model` |
| **类型**：character vector |
| **值**：`'Quiet'` | `'Total'` | `'Disturbance'` |
| **默认值**：`'Quiet'` |

### **Action for out-of-range input** — 模块行为 `Error`（默认）| `Warning` | `None`

指定当模块输入超出范围时的模块行为。

| Value | Description |
| --- | --- |
| `Error`（默认） | MATLAB® 返回异常，模型仿真停止。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Error` 没有效果，模型的行为如同操作设置为 `None`。 |
| `Warning` | 在 Diagnostic Viewer 中显示警告，模型仿真继续。对于 Accelerator 和 Rapid Accelerator 模式，将操作设置为 `Warning` 没有效果，模型的行为如同操作设置为 `None`。 |
| `None` | 不执行操作。模块对输入信号施加上限和下限。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`action` |
| **类型**：character vector |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'Error'` |
## 所属库

Aerospace Blockset / Environment / Wind

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2021b：Horizontal Wind Model 14 模块可能更改返回值

Horizontal Wind Model 14 模块现在接受：

- **day** 端口值为小数、负数、
  `0` 或大于 `366`。
- **sec** 端口值为 `0` 或
  大于 `86400`。

因此，此模块的输出值可能与之前的
版本不同。

## 描述

实现 Horizontal Wind Model 14

Horizontal Wind Model 14 模块实现美国海军研究实验室 (HWM™) 例程，用于计算
一组地理坐标（纬度、经度和高度）下风的经向和纬向分量。
