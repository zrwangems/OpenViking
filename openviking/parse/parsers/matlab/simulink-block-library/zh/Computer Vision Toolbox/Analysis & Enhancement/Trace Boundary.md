---
type: simulink-block
title: 'Trace Boundary'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'traceboundary'
documentation_source_path: 'ref/traceboundary.html'
language: zh-CN
chinese_source: worker-translation
---

# Trace Boundary

## 端口
```yaml
ports:
- name: BW
  summary: 输入二值图像矩阵
  direction: input
  data_types: Boolean
- name: Start Pt
  summary: 边界起始点坐标 二元素向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Pts
  summary: 边界点坐标 *M*×2 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
```

### 输入

### **BW** — 输入二值图像矩阵

输入二值图像，指定为 *M*×*N* 矩阵。

**数据类型：** `Boolean`

### **Start Pt** — 边界起始点坐标 二元素向量

边界起始点的坐标，指定为 [*X*
*Y*] 形式的二元素向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Pts** — 边界点坐标 *M*×2 矩阵

边界点的坐标，返回为 *M*×2 矩阵，其中每一行表示一个边界像素的坐标，形式为
[*X*
*Y*]。*M* 是输出图像中被追踪的边界像素数。*M* 的值必须小于或等于
**Maximum number of boundary pixels** 参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## 参数
```yaml
parameters:
- name: Connectivity
  summary: 像素连通类型 8（默认）| 4
  group: ''
- name: Initial search direction
  summary: 初始搜索方向类型 North（默认）| East | South | West | Northeast | ...
  group: ''
- name: Trace direction
  summary: 边界追踪方向 Clockwise（默认）| Counterclockwise
  group: ''
- name: Maximum number of boundary pixels
  summary: 最大边界像素数 500（默认）| 标量
  group: ''
```

### **Connectivity** — 像素连通类型 `8`（默认）| `4`

选择这些选项以指定模块如何定义哪些像素彼此连通。

- `8` — 连接水平、垂直和对角方向上的相邻像素。
- `4` — 仅连接水平和垂直方向上的相邻像素。

有关详细信息，请参阅 Connectivity。

### **Initial search direction** — 初始搜索方向类型 `North`（默认）| `East` | `South` | `West` | `Northeast` | ...

指定初始搜索方向的类型，以查找与 **Start Pt** 输入端口指定的起始像素相连的边界像素。这些选项取决于指定的 **Connectivity** 参数。

当 **Connectivity** 参数设置为 `4` 时，模块启用 `North`、`East`、
`South` 和 `West` 搜索方向。下图展示了相对于起始像素的四种可能的初始搜索方向。

Connectivity 设置为 4 时的搜索方向

当 **Connectivity** 参数设置为 `8` 时，模块额外启用 `Northeast`、
`Southeast`、`Southwest` 和 `Northwest` 搜索方向。下图展示了相对于起始像素的八种可能的初始搜索方向。

Connectivity 设置为 8 时的搜索方向

### **Trace direction** — 边界追踪方向 `Clockwise`（默认）| `Counterclockwise`

选择追踪边界的方向为 `Clockwise` 或 `Counterclockwise`。

### **Maximum number of boundary pixels** — 最大边界像素数 500（默认）| 标量

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
