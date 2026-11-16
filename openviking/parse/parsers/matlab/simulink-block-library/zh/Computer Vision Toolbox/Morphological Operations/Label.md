---
type: simulink-block
title: 'Label'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'label'
documentation_source_path: 'ref/label.html'
language: zh-CN
chinese_source: worker-translation
---

# Label

## 端口

### 输入

### **BW** — 输入二值图像 向量 | 矩阵

输入图像必须是由二值组成的向量或矩阵，每个元素表示图像的一个像素。该模块将值为 `0` 的像素归类为背景像素，并在值为 `1` 的像素中搜索连通分量。

**数据类型：** `Boolean`
### 输出

### **Label** — 已标记对象 向量 | 矩阵

输入图像中的已标记对象，以非负整数的向量或矩阵形式返回。输出向量或矩阵中标记为 `0` 的元素表示背景，标记为 `1` 的元素表示第一个对象，标记为 `2` 的元素表示第二个对象，依此类推。此输出的大小与 **BW** 输入的大小匹配。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `Label matrix` 或 `Label matrix and number of labels`。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Count** — 已标记对象数量 标量

已标记对象的数量，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `Number of labels` 或 `Label matrix and number of labels`。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### **Connectivity** — 像素连通性类型 `8`（默认） | `4`

指定模块如何定义哪些像素彼此连接。如果只想在水平和垂直方向上连接相邻像素，请选择 `4`。如果要在水平、垂直和对角线方向上连接相邻像素，请选择 `8`。这些图显示了模块如何为 4 连通和 8 连通像素定义连通分量。模块将带有黑色圆圈的白色像素视为彼此连接。

| 连通类型 | 连接的像素 |
| --- | --- |
| 4 连通像素 | 3×3 网格，其中中间左侧、中心和中下方方块为白色，且中心带有黑色圆圈。右上角方块为白色，无圆圈，所有其他方块为黑色。 |
| 8 连通像素 | 3×3 网格，其中中间左侧、中心、中下方和右上角方块为白色，且中心带有黑色圆圈。所有其他方块为黑色。 |

### **Output** — 模块输出 `Label matrix and number of labels`（默认） | `Label matrix` | `Number of labels`

将模块输出指定为以下选项之一：

- `Label matrix` — 模块在 **Label** 端口输出已标记的对象。
- `Number of labels` — 模块在 **Count** 端口输出已标记对象的数量。
- `Label matrix and number of labels` — 模块分别将已标记的对象和已标记对象的数量输出到 **Label** 和 **Count** 端口。

### **Output data type** — 输出的数据类型 `Automatic`（默认） | `uint8` | `uint16` | `uint32`

指定 **Label** 和 **Count** 端口输出的数据类型。将此参数指定为 `Automatic` 时，模块会根据图像大小和指定的连通性计算图像内可容纳的最大对象数。使用此计算结果，它选择能保证唯一区域标签的最小输出数据类型。

### **If label exceeds data type size, mark remaining regions using** — 输出标签的溢出模式 `maximum value of the output data type`（默认） | `zero`

使用此参数指定当模块找到的对象数超过输出数据类型可表示的最大可能值时模块的行为。模块使用以下选项之一确定的值标记剩余对象：

- `maximum value of the output data type` — 模块使用输出数据类型的最大值标记剩余对象。
- `zero` — 模块使用 `0` 标记剩余对象。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `uint8` 或 `uint16`。

## 所属库

Computer Vision Toolbox / Morphological Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `integer` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

在二值图像中标记连通分量

Label 模块查找并标记二维二值图像中的连通分量或对象。该模块忽略输入图像中的背景像素，并在剩余像素中搜索连通分量。然后，该模块使用唯一编号标记每个连通分量的所有像素，并计算已标记对象的数量。
