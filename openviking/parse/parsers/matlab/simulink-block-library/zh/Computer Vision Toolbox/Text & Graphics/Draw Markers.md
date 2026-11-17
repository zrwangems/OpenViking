---
type: simulink-block
title: 'Draw Markers'
family: 'text-graphics'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'drawmarkers'
documentation_source_path: 'ref/drawmarkers.html'
language: zh-CN
chinese_source: worker-translation
---

# Draw Markers

## 端口

### 输入

### **Image** — 输入图像矩阵 | 数组

将输入图像指定为强度值的 *M*×*N* 矩阵，或具有 *P* 个颜色平面的颜色值的 *M*×*N*×*P* 数组。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 图像矩阵的红色分量

将输入 RGB 图像的红色分量指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 图像矩阵的绿色分量

将输入 RGB 图像的绿色分量指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 图像矩阵的蓝色分量

将输入 RGB 图像的蓝色分量指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Pts** — 标记坐标向量 | 矩阵

将标记坐标指定为以下选项之一：

- 单个标记 — 指定标记中心 *x* 和 *y* 坐标的二元素向量。
- 多个标记 — *K*×2 矩阵。*K* 是标记数。矩阵的每一行指定一个标记中心的 *x* 和 *y* 坐标。

**注意**

除非输入图像也是浮点型，否则该模块不支持此参数的单精度或双精度浮点数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Clr** — 标记颜色标量 | 向量 | 矩阵

指定标记的颜色值。使用下表确定在此端口输入的值类型。

| **输入图像类型** | 所有标记使用相同颜色 | 每个标记使用不同颜色 |
| --- | --- | --- |
| 强度图像 | 标量值 | *K* 元素向量。*K* 是标记数。 |
| 彩色图像 | *P* 元素向量。*P* 是颜色平面数。 | *K*×*P* 矩阵。*P* 是颜色平面数，*K* 是标记数。 |

#### 依赖关系

要启用此端口，请使用以下选项之一：

- **标记形状** 参数设置为 `X-mark`、`Plus` 或 `Star`，或者清除 **填充** 参数 — 将 **边框颜色来源** 参数设置为 `Input port`。
- **标记形状** 参数设置为 `Circle` 或 `Square`，并且选中 **填充** 参数 — 将 **填充颜色来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **ROI** — 感兴趣区域向量

将矩形感兴趣区域 (ROI) 指定为形式为 [*x*
*y*
*width*
*height*] 的四元素向量。*x* 和 *y* 元素是 ROI 左上角的坐标。

#### 依赖关系

要启用此端口，请将 **绘制标记位置** 参数设置为 `Specify region of interest via port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像，返回为强度值的 *M*×*N* 矩阵或颜色值的 *M*×*N*×*P* 数组。*P* 是输出图像中的颜色平面数。输出图像的大小和数据类型与输入图像相同。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 输出图像矩阵的红色分量

输出 RGB 图像的红色分量，返回为 *M*×*N* 矩阵。输出图像的红色分量与输入图像的红色分量具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 输出图像矩阵的绿色分量

输出 RGB 图像的绿色分量，返回为 *M*×*N* 矩阵。输出图像的绿色分量与输入图像的绿色分量具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 输出图像矩阵的蓝色分量

输出 RGB 图像的蓝色分量，返回为 *M*×*N* 矩阵。输出图像的蓝色分量与输入图像的蓝色分量具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **主要**

### **标记形状** — 标记的形状 `Circle` (默认) | `X-mark` | `Plus` | `Star` | `Square`

指定要绘制的标记的形状。您可以将 `Circle` 和 `Square` 标记渲染为轮廓或填充形状。

### **标记大小** — 标记的大小 `3` (默认) | 正整数

将标记的大小指定为正整数 *M*，它定义一个边长为 2*M*+1 的正方形区域，标记将放入该区域。

### **填充** — 填充标记 `off` (默认) | `on`

选择此参数以使用指定的强度值或颜色填充标记。

#### 依赖关系

要启用此参数，请将 **标记形状** 参数设置为 `Circle` 或 `Square`。

### **边框颜色来源** — 标记边框的颜色来源 `Specify via dialog` (默认) | `Input port`

将标记边框颜色的来源指定为以下选项之一：

- `Specify via dialog` — 使用 **边框颜色** 参数指定标记边框的颜色。
- `Input port` — 使用 **Clr** 输入端口指定标记边框的颜色。

#### 依赖关系

要启用此参数，请清除 **填充** 参数，或将 **标记形状** 参数设置为 `X-mark`、`Plus` 或 `Star`。

### **边框颜色** — 标记的颜色值 `Black` (默认) | `White` | `User-specified value`

将标记边框的颜色值指定为 `Black`、`White` 或 `User-specified value`。

#### 依赖关系

要启用此参数，请清除 **填充** 参数，并将 **边框颜色来源** 参数设置为 `Specify via dialog`。

### **填充颜色来源** — 填充标记的颜色来源 `Specify via dialog` (默认) | `Input port`

指定用于填充标记的颜色来源，为以下选项之一：

- `Specify via dialog` — 使用 **填充颜色** 参数指定用于填充标记的颜色。
- `Input port` — 使用 **Clr** 输入端口指定用于填充标记的颜色。

#### 依赖关系

要启用此参数，请将 **标记形状** 参数设置为 `Circle` 或 `Square`，并选中 **填充** 参数。

### **填充颜色** — 填充标记的颜色值 `Black` (默认) | `White` | `User-specified value`

将用于填充标记的颜色值指定为 `Black`、`White` 或 `User-specified value`。

#### 依赖关系

要启用此参数，请将 **标记形状** 参数设置为 `Circle` 或 `Square`，选中 **填充** 参数，并将 **填充颜色来源** 参数设置为 `Specify via dialog`。

### **不透明度因子（介于 0 和 1 之间）** — 不透明度因子 `0.6` (默认) | 范围 [`0`, `1`] 内的标量 | *K* 元素向量

在 [`0`, `1`] 范围内指定标记的不透明度因子，其中 `0` 表示完全透明，`1` 表示完全不透明。将此参数指定为以下选项之一：

- 标量 — 将指定的不透明度因子应用于所有标记。
- *K* 元素向量 — 为每个标记应用不同的不透明度因子。*K* 是标记数。

#### 依赖关系

要启用此参数，请将 **标记形状** 参数设置为 `Circle` 或 `Square`，并选中 **填充** 参数。

### **颜色值** — 用户指定的颜色值 `[200 255 100]` (默认) | 标量 | *P* 元素向量 | *K*×*P* 矩阵

指定标记的颜色值。使用下表确定要为该参数输入的值类型。

| **输入图像类型** | 所有标记使用相同颜色 | 每个标记使用不同颜色 |
| --- | --- | --- |
| 强度图像 | 标量值 | *K* 元素向量。*K* 是标记数。 |
| 彩色图像 | *P* 元素向量。*P* 是颜色平面数。 | *K*×*P* 矩阵。*P* 是颜色平面数，*K* 是标记数。 |

#### 依赖关系

要启用此参数，请使用以下选项之一：

- **标记形状** 参数设置为 `X-mark`、`Plus` 或 `Star`，或者清除 **填充** 参数 — 将 **边框颜色来源** 参数设置为 `Specify via dialog`，并将 **边框颜色** 参数设置为 `User-specified value`。
- **标记形状** 参数设置为 `Circle` 或 `Square`，并且选中 **填充** 参数 — 将 **填充颜色来源** 参数设置为 `Specify via dialog`，并将 **填充颜色** 参数设置为 `User-specified value`。

### **绘制标记位置** — 标记的区域 `Entire image` (默认) | `Specify region of interest via port`

指定在何处绘制标记。默认情况下，您可以在整个图像中绘制标记。要指定矩形 ROI 内的标记，请将此参数设置为 `Specify region of interest via port`，并向 **ROI** 输入端口指定形式为 [*x*
*y*
*width*
*height*] 的四元素向量。

### **使用抗锯齿** — 平滑算法 `off` (默认) | `on`

选择此参数以对 `Circle`、`X-mark` 或 `Star` 标记形状执行平滑算法。

#### 依赖关系

要启用此参数，请将 **标记形状** 参数设置为 `Circle`、`X-mark` 或 `Star`。

### **图像信号** — RGB 图像的端口配置 `One multidimensional signal` (默认) | `Separate color signals`

指定如何输入和输出 RGB 彩色图像。

- `One multidimensional signal` — 该模块仅使用 **Image** 端口接受输入，并仅使用 **Port\_1** 端口返回输出。
- `Separate color signals` — 该模块使用三个单独的颜色通道接受并返回彩色图像，这些通道分布在 **R**、**G** 和 **B** 输入和输出端口上。

### **数据类型**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Text & Graphics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

在图像上绘制标记

Draw Markers 模块通过覆盖输入图像中的像素值，在图像或视频帧上绘制标记。这会将标记嵌入输出图像中。该模块支持五种类型的标记：`Circle`、`X-mark`、`Plus`、`Star` 和 `Square`。

该模块使用 Bresenham 圆形绘制算法绘制圆，并使用 Bresenham 直线绘制算法绘制所有其他标记。
