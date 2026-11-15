---
type: simulink-block
title: 'Trace Boundary'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'traceboundary'
documentation_source_path: 'ref/traceboundary.html'
language: zh-CN
chinese_source: worker-translation
---

# Trace Boundary

## 端口

### 输入

### **BW** — 输入二值图像矩阵

输入二值图像，指定为 *M*×*N* 矩阵。

**数据类型：** `Boolean`

### **Start Pt** — 边界起始点的坐标，二元素向量

边界起始点的坐标，指定为形式为 [*X* *Y*] 的二元素向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Pts** — 边界点的坐标 *M*×2 矩阵

边界点的坐标，返回为 *M*×2 矩阵，其中每行以 [*X* *Y*] 的形式表示一个边界像素的坐标。*M* 是输出图像中追踪到的边界像素数。*M* 的值必须小于或等于由 **Maximum number of boundary pixels** 参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Connectivity** — 像素连通性类型 `8`（默认） | `4`

选择这些选项以指定模块如何定义哪些像素彼此连接。

- `8` — 连接水平、垂直和对角方向上的相邻像素。
- `4` — 仅连接水平和垂直方向上的相邻像素。

有关详细信息，请参阅 Connectivity。

### **Initial search direction** — 初始搜索方向的类型 `North`（默认） | `East` | `South` | `West` | `Northeast` | ...

指定初始搜索方向的类型，以查找连接到 **Start Pt** 输入端口所指定起始像素的边界像素。这些选项取决于指定的 **Connectivity** 参数。

当 **Connectivity** 参数设置为 `4` 时，模块启用 `North`、`East`、`South` 和 `West` 搜索方向。此图说明了相对于起始像素的四种可能初始搜索方向。

Connectivity 设置为 4 时的搜索方向

当 **Connectivity** 参数设置为 `8` 时，模块还会启用 `Northeast`、`Southeast`、`Southwest` 和 `Northwest` 搜索方向。此图说明了相对于起始像素的八种可能初始搜索方向。

Connectivity 设置为 8 时的搜索方向

### **Trace direction** — 边界追踪方向 `Clockwise`（默认） | `Counterclockwise`

选择将边界追踪为 `Clockwise` 或 `Counterclockwise` 的方向。

### **Maximum number of boundary pixels** — 最大边界像素数 500（默认） | 标量

将起始点的最大边界像素数指定为标量。**Pts** 输出端口的行数必须小于或等于此值。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

在二值图像中追踪对象边界

Trace Boundary 模块在二值图像中追踪对象边界，其中非零像素表示对象，零值像素表示背景。
