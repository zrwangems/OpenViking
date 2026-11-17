---
type: simulink-block
title: 'Draw Shapes'
family: 'text-graphics'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'drawshapes'
documentation_source_path: 'ref/drawshapes.html'
language: zh-CN
chinese_source: worker-translation
---

# Draw Shapes

## 端口

### 输入

### **Image** — 输入图像或视频流 *M*-by-*N* 强度值矩阵 | *M*-by-*N*-by-*3* 颜色值数组

输入图像，指定为 *M*-by-*N* 强度值矩阵或具有 *3* 个颜色平面的 *M*-by-*N*-by-*3* 颜色值矩阵。

当输入为视频流时，模块逐帧处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **R** — 图像或视频帧的红色通道 *M*-by-*N* 矩阵

图像或视频帧的红色通道，指定为 *M*-by-*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **G** — 图像或视频帧的绿色通道 *M*-by-*N* 矩阵

图像或视频帧的绿色通道，指定为 *M*-by-*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **B** — 图像或视频帧的蓝色通道 *M*-by-*N* 矩阵

图像或视频帧的蓝色通道，指定为 *M*-by-*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Pts** — 形状坐标 *M*-by-3 矩阵 | *M*-by-4 矩阵 | *M*-by-2*L* 矩阵

要绘制在输入上的输入形状的坐标。点的格式取决于通过 **Shape** 参数指定的形状类型。

- `Rectangles` — 形式为 [*x* *y* *width* *height*] 的 *M*-by-4 矩阵。*M* 是矩形数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单个矩形 | 格式为 `[x y width height]` 的四元素行向量，其中：  - `x` 和 `y` 是矩形左上角的坐标。 - `width` 和 `height` 参数是矩形的宽度和高度，以像素为单位。`width` 和 `height` 的值必须大于 0。 |  |
  | *M* 个矩形 | 形式为 [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM] 的 *M*-by-4 矩阵，其中矩阵的每一行对应不同的矩形，且形式与单个矩形的向量相同。 |  |
- `Lines` — 形式为 [*x1*, *y1*, *x2*, *y2*,…,*xL*, *yL*] 的 *M*-by-2*L* 矩阵。*M* 是折线数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单条线 | 格式为 `[x1 y1 x2 y2]` 的四元素行向量，其中：  - `x1` 和 `y1` 是线起点的坐标。 - `x2` 和 `y2` 是线终点的坐标。 |  |
  | *M* 条线 | 形式为 [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2] 的 *M*-by-4 矩阵，其中矩阵的每一行对应不同的线，且形式与单条线的向量相同。 |  |
  | 具有 (*L*-1) 个线段的单条折线 | 大小为 2*L* 的向量，其中 *L* 是顶点数量，格式为 `[x1, y1, x2, y2, ..., xL, yL]`，其中  - x1 和 y1 是第一个线段的起点坐标。 - x2 和 y2 是第一个线段的终点和第二个线段的起点坐标。 - xL 和 yL 是第 (*L*-1) 个线段的终点坐标。  折线始终包含 (*L*-1) 个线段，因为第一个和最后一个顶点不连接。  当列数小于 2 或不是 2 的倍数时，模块会生成错误消息。 |  |
  | 具有 (*L*-1) 个线段的 *M* 条折线 | 形式为 [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML] 的 *M*-by-*2**L* 矩阵，其中矩阵的每一行对应不同的折线，且形式与单条折线的向量相同。当其中一条折线包含的线段少于 (*L*–1) 个时，通过重复最后一个顶点的坐标来填充矩阵。  如果列数小于 2 或不是 2 的倍数，模块会生成错误消息。 |  |
- `Polygons` — 形式为 [*x1*, *y1*, *x2*, *y2*,…,*xL*, *yL*] 的 *M*-by-2*L* 矩阵。*M* 是多边形数量。这些点按连续顺序指定以形成多边形。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 具有 *L* 个线段的单个多边形 | 大小为 2*L* 的行向量，其中 *L* 是顶点数量，格式为 `[x1 y1 x2 y2 ... xL yL]`，其中：  - x1 和 y1 是第一个线段的起点坐标。 - x2 和 y2 是第一个线段的终点和第二个线段的起点坐标。 - xL 和 yL 是第 (*L*-1) 个线段的终点和第 *L* 个线段的起点坐标。  模块连接 `[x1 y1]` 到 `[xL yL]` 以完成多边形。如果列数小于 2 或不是 2 的倍数，模块会生成错误。 |  |
  | *M* 个多边形，其中任意多边形中线段的最大数量为 *L* | 形式为 [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML] 的 *M*-by-2*L* 矩阵，其中矩阵的每一行对应不同的多边形，且形式与单个多边形的向量相同。当其中一个多边形包含的线段少于 *L* 个时，通过重复最后一个顶点的坐标来填充矩阵。  如果列数小于 2 或不是 2 的倍数，模块会生成错误消息。 |  |
- `Circles` — 形式为 [*x* *y* *radius*] 的 *M*-by-3 矩阵。*M* 是圆的数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单个圆 | 格式为 `[x y radius]` 的三元素行向量，其中：  - `x` 和 `y` 是圆心的坐标。 - `radius` 是圆的半径，必须大于 0。 |  |
  | *M* 个圆 | 形式为 [xctr1yctr1radius1xctr2yctr2radius2⋮⋮⋮xctrMyctrMradiusM] 的 *M*-by-3 矩阵，其中矩阵的每一行对应不同的圆，且形式与单个圆的向量相同。 |  |

#### 依赖关系

- 仅当 **Image** 或 **R**、**G** 和 **B** 端口的输入为浮点时，才支持双精度浮点。
- 仅当 **Image** 或 **R**、**G** 和 **B** 端口的输入为浮点时，才支持单精度浮点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ROI** — 感兴趣区域 4 元素向量

感兴趣区域，指定为形式为 [*x* *y* *width* *height*] 的四元素向量。该区域定义用于绘制形状的矩形区域。前两个元素表示该区域左上角的基于 1 的坐标。其余两个元素表示该区域的宽度和高度。

#### 依赖关系

要启用此端口，将 **Draw shapes in** 参数设置为 `Specify region of interest via port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Clr** — 形状颜色 3 元素向量 | *M*-by-*3* 矩阵

形状颜色，指定为 *3* 元素向量或 *M*-by-*3* 矩阵。*M* 是形状数量，3 表示颜色平面数量。可以为 *M* 个形状分别指定不同颜色，或为所有形状指定一种颜色。

#### 依赖关系

要启用此端口，将 **Border color source** 或 **Fill color source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **Port\_1** — 输出图像 *M*-by-*N* 强度值矩阵 | *M*-by-*N*-by-*3* 颜色值数组

输出图像，以 *M*-by-*N* 矩阵或 *M*-by-*N*-by-*3* 数组形式返回。输出图像与输入图像具有相同的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

**主选项卡**

### **Shape** — 要绘制的形状 `Rectangles`（默认）| `Lines` | `Polygons` | `Circles`

要在图像上绘制的一个或多个形状，指定为以下之一：

- `Rectangles` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个矩形。
- `Lines` — 使用指定的形状坐标在输入图像或视频帧上绘制一条或多条线。
- `Polygons` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个多边形。
- `Circles` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个圆。

### **Fill shapes** — 用颜色填充形状 off（默认）| on

选择 **Fill shapes** 以启用用于填充形状的颜色参数。

**注意**

如果正在生成代码并选中 **Fill shapes** 复选框，则模块输入的字长不能超过 16 位。

### **Line width** — 形状的线宽 1（默认）| 正标量

将要绘制的形状的线宽指定为正标量。

### **Fill color source** — 指定填充颜色的输入源 `Specify via dialog`（默认）| `Input port`

指定填充颜色值的输入源。将 **Fill color source** 选择为以下之一：

- `Specify via dialog` — 使用 **Fill color** 参数指定颜色值。
- `Input port` — 使用 **Clr** 端口指定颜色值。

#### 依赖关系

要启用此参数，请选择 **Fill shapes**。

### **Fill color** — 填充形状的颜色 `Black`（默认）| `White` | `User-specified value`

将形状填充颜色指定为 `Black`、`White` 或 `User-specified value`。`User-specified value` 可以是标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

| 用于填充一个形状或多个相同颜色形状的颜色值 | 用于填充多个形状且各具独特颜色的颜色值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状数量。 |
| *3* 元素 RGB 向量 | *R*-by-*3* 矩阵，其中 *3* 是颜色平面数量，*R* 是形状数量。 |

对于 **Color Value(s)** 参数中的每个值，请输入介于输入图像的数据类型所能表示的最小值和最大值之间的数字。如果输入的值超出此范围，模块会生成错误消息。

#### 依赖关系

要启用此参数，请选择 **Fill shapes** 参数。

### **Border color source** — 指定边框颜色的输入源 `Specify via dialog`（默认）| `Input port`

指定边框颜色值的输入源。将 **Border color source** 选择为以下之一：

- `Specify via dialog` — 使用 **Border color** 参数指定颜色值。
- `Input port` — 使用 **Clr** 端口指定颜色值。

### **Border color** — 形状的轮廓颜色 `Black`（默认）| `White` | `User-specified value`

将形状的边框颜色指定为 `Black`、`White` 或 `User-specified value`。`User-specified value` 可以是标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

| 用于绘制一个形状或多个相同颜色形状的颜色值 | 用于绘制多个形状且各具独特颜色的颜色值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状数量。 |
| *3* 元素 RGB 向量 | *R*-by-*3* 矩阵，其中 3 是颜色平面数量，*R* 是形状数量。 |

对于 **Color Value(s)** 参数中的每个值，请输入介于输入图像的数据类型所能表示的最小值和最大值之间的数字。如果输入的值超出此范围，模块会生成错误消息。

### **Color value(s)** — 用于绘制边框或填充形状的颜色值 标量 | 3 元素向量

将用于绘制边框或填充形状的颜色值指定为标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

**可调：** 是

#### 依赖关系

要启用此参数，将 **Border color** 或 **Fill color** 参数设置为 `User-specified value`。

### **Opacity factor (between 0 and 1)** — 颜色值的不透明度，范围 [0,1] | *R* 元素向量

将颜色不透明度指定为范围 [0, 1] 内的正值。`0` 表示透明，`1` 表示不透明。

| 用于填充一个形状或多个相同颜色形状的 Opacity Factor 值 | 用于填充多个形状且各具独特颜色的 Opacity Factor 值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状数量 |

#### 依赖关系

要启用此参数，请选择 **Fill shapes** 参数。

### **Use antialiasing** — 平滑算法 off | on

对线、多边形或圆执行平滑处理。

#### 依赖关系

- 要启用此参数，将 **Shape** 参数设置为 `Lines`、`Polygons` 或 `Circles`。

### **Draw shapes in** — 绘制形状的区域 `Entire image`（默认）| `Specify region of interest via port`

指定绘制指定形状的区域范围。将值选择为以下之一：

- `Entire image` — 在整个图像上绘制形状。
- `Specify region of interest via port` — 在由输入 **ROI** 端口指定的 ROI 内绘制形状。

### **Image signal** — 图像信号的输入端口数量 `One multidimensional signal`（默认）| `Separate color signals`

指定用于指定输入图像的输入端口数量。将值选择为以下之一：

- `One multidimensional signal` — 使用单个端口指定强度或彩色图像。对于 *M*-by-*N*-by-*3* 彩色图像或 *M*-by-*N* 强度图像，模块启用 **Image** 端口。
- `Separate color signals` — 指定输入彩色图像的红色、绿色和蓝色颜色平面。模块启用 **R**、**G** 和 **B** 输入端口。每个端口接受 RGB 彩色图像的 *M*-by-*N* 平面。

**数据类型选项卡**

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
### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

在图像上绘制矩形、线条、多边形或圆形

Draw Shapes 模块通过覆写像素值在图像上绘制矩形、线条、多边形或圆形。因此，形状会绘制到输出图像上。该模块使用 Bresenham 直线绘制算法绘制线条、多边形和矩形，并使用 Bresenham 圆绘制算法绘制圆形。输出信号的大小和数据类型与馈送到 **Image**、**R**、**G** 和 **B** 端口的输入信号相同。

你可以通过输入端口设置形状填充或边框颜色，也可以使用参数手动输入值。使用颜色参数指定矩形、线条、多边形或圆形的外观。
