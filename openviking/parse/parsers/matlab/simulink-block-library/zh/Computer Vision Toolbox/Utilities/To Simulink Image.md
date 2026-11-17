---
type: simulink-block
title: 'To Simulink Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'tosimulinkimage'
documentation_source_path: 'ref/tosimulinkimage.html'
language: zh-CN
chinese_source: worker-translation
---

# To Simulink Image

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号矩阵
  direction: input
  data_types: integer | single | double | Boolean
- name: Port_1
  summary: 输出信号 Simulink.ImageType
  direction: output
  data_types: Simulink.ImageType
```

### 输入

### **Port\_1** — 输入信号矩阵

To Simulink Image 模块的输入信号。输入为数值矩阵。

**数据类型：** `integer` | `single` | `double` | `Boolean`
### 输出

### **Port\_1** — 输出信号 `Simulink.ImageType`

To Simulink Image 模块的输出信号。输出为 `Simulink.ImageType` 数据类型的图像。

**数据类型：** `Simulink.ImageType`
## 参数
```yaml
parameters:
- name: Output data type
  summary: '输出信号值的数据类型 Inherit: auto（默认）| Simulink.ImageType(480,640,3)'
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: 'Inherit: auto | Simulink.ImageType(480,640,3) | <data type expression>'
  default: 'Inherit: auto'
```

### **Output data type** — 输出信号值的数据类型 `Inherit: auto`（默认）| `Simulink.ImageType(480,640,3)`

指定图像信号的输出数据类型。

点击 **Show data type
assistant** 按钮以显示 **Data Type
Assistant**，它可帮助您设置数据类型属性。有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

您可以指定以下任一选项：

- 继承数据类型
- Simulink 图像数据类型 — 使用 `Simulink.ImageType` 对象的构造函数并指定属性来描述图像。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式。
- 自定义数据类型 — 使用一个 MATLAB® 表达式，分别表示图像的行、列和通道。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **Value:** `Inherit: auto` | `Simulink.ImageType(480,640,3)` | `<data type expression>` |
| **默认值**：`Inherit: auto` |
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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2022a 中引入**

## 描述

将数值矩阵打包为 Simulink 图像

To Simulink Image 模块将矩阵数据转换为 Simulink® 图像数据。
