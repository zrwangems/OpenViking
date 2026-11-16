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

### 输入

### **Port\_1** — 输入信号矩阵

输入到 To Simulink Image 模块的输入信号。输入是数值矩阵。

**数据类型：** `integer` | `single` | `double` | `Boolean`
### 输出

### **Port\_1** — 输出信号 `Simulink.ImageType`

来自 To Simulink Image 模块的输出信号。输出是 `Simulink.ImageType` 数据类型的图像。

**数据类型：** `Simulink.ImageType`

## 参数

### **输出数据类型** — 输出信号值的数据类型 `Inherit: auto` (默认) | `Simulink.ImageType(480,640,3)`

指定图像信号的输出数据类型。

单击 **显示数据类型助手** 按钮 以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

您可以指定以下任一选项：

- 继承的数据类型
- Simulink 图像数据类型 — 使用 `Simulink.ImageType` 对象的构造函数，并指定用于描述图像的属性。默认情况下，数据类型使用 `Simulink.ImageType(480,640,3)` 表达式。
- 自定义数据类型 — 使用一个 MATLAB® 表达式，分别表示图像的行、列和通道。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `Inherit: auto` | `Simulink.ImageType(480,640,3)` | `<data type expression>` |
| **默认值：** `Inherit: auto` |

## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` | `integer` | `Boolean` | `image` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2022a 中引入**

## 描述

将数值矩阵打包为 Simulink 图像

To Simulink Image 模块将矩阵数据转换为 Simulink® 图像数据。
