---
type: simulink-block
title: 'From Simulink Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'fromsimulinkimage'
documentation_source_path: 'ref/fromsimulinkimage.html'
language: zh-CN
chinese_source: worker-translation
---

# From Simulink Image

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 Simulink.ImageType
  direction: input
  data_types: Simulink.ImageType
- name: Port_1
  summary: 输出信号矩阵
  direction: output
  data_types: integer | single | double | Boolean
```

### 输入

### **Port\_1** — 输入信号 `Simulink.ImageType`

From Simulink Image 模块的输入信号。输入为 Simulink 图像数据类型。

**数据类型：** `Simulink.ImageType`
### 输出

### **Port\_1** — 输出信号矩阵

From Simulink Image 模块的输出信号。输出为矩阵或数组，具体取决于输入的格式。

- *M*×*N* 矩阵 — 输入为 `Grayscale` 图像。*M* 和 *N* 分别为图像的高度和宽度，以像素为单位。
- *M*×*N*×*C* 矩阵 — 输入为 `RGB` 或 `BGR` 图像。*M* 和 *N* 分别为图像的高度和宽度，以像素为单位。*C* 为颜色通道数。

**数据类型：** `integer` | `single` | `double` | `Boolean`
## 参数
```yaml
parameters:
- name: Output dimensions
  summary: 模块输出信号的维度 [480 640 3]（默认）
  group: ''
  block_parameter: ImageSize
  type: character vector
  values: character vector
  default: '[480 640 3]'
```

### **Output dimensions** — 模块输出信号的维度 `[480 640 3]`（默认）

指定输出图像信号的维度。表达式必须为三元素数值行向量，形式为：`[Rows Columns Channels]`。

#### 编程使用

|  |
| --- |
| **模块参数**：`ImageSize` |
| **类型**：character vector |
| **Value:** character vector |
| **默认值**：`[480 640 3]` |
## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` | `integer` | `Boolean` | `image` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2022a 中引入**

## 描述

从 Simulink 图像中解包数值矩阵

From Simulink Image 模块将 Simulink® 图像数据转换为矩阵数据。
