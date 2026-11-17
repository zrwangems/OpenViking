---
type: simulink-block
title: 'Draw Shapes'
family: 'vision'
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
```yaml
ports:
- name: Image
  summary: 输入图像或视频流 *M*×*N* 的强度值矩阵 | *M*×*N*×*3* 的颜色值数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: R
  summary: 图像或视频帧的红色通道 *M*×*N* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: G
  summary: 图像或视频帧的绿色通道 *M*×*N* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: B
  summary: 图像或视频帧的蓝色通道 *M*×*N* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Pts
  summary: 形状坐标 *M*×3 矩阵 | *M*×4 矩阵 | *M*×2*L* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: ROI
  summary: 感兴趣区域 4 元素向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Clr
  summary: 形状的颜色 3 元素向量 | *M*×*3* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出图像 *M*×*N* 的强度值矩阵 | *M*×*N*×*3* 的颜色值数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **Image** — 输入图像或视频流 *M*×*N* 的强度值矩阵 | *M*×*N*×*3* 的颜色值数组

输入图像，指定为 *M*×*N* 的强度值矩阵或具有 *3* 个颜色平面的 *M*×*N*×*3* 的颜色值矩阵。

当输入为视频流时，该模块逐帧处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **R** — 图像或视频帧的红色通道 *M*×*N* 矩阵

图像或视频帧的红色通道，指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **G** — 图像或视频帧的绿色通道 *M*×*N* 矩阵

输入图像或视频帧的绿色通道，指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **B** — 图像或视频帧的蓝色通道 *M*×*N* 矩阵

输入图像或视频帧的蓝色通道，指定为 *M*×*N* 矩阵。**R**、**G** 和 **B** 端口必须具有相同的维度和数据类型。

#### 依赖

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Pts** — 形状坐标 *M*×3 矩阵 | *M*×4 矩阵 | *M*×2*L* 矩阵

要在输入上绘制的输入形状的坐标。点的格式取决于您使用 **Shape** 参数指定的形状类型。

- `Rectangles` — 形式为 [*x* *y* *width* *height*] 的 *M*×4 矩阵。*M* 是矩形的数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单个矩形 | 格式为 `[x y width height]` 的四元素行向量，其中：  - `x` 和 `y` 是矩形左上角的坐标。 - `width` 和 `height` 参数是矩形的宽度和高度，以像素为单位。`width` 和 `height` 的值必须大于 0。 |  |
  | *M* 个矩形 | 格式为 [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM] 的 *M*×4 矩阵，其中矩阵的每一行对应一个不同的矩形，且与单个矩形的向量形式相同。 |  |
- `Lines` — 形式为 [*x1*, *y1*, *x2*, *y2*,…,*xL*, *yL*] 的 *M*×2*L* 矩阵。*M* 是折线的数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单条线 | 格式为 `[x1 y1 x2 y2]` 的四元素行向量，其中：  - `x1` 和 `y1` 是线条起点的坐标。 - `x2` 和 `y2` 是线条终点的坐标。 |  |
  | *M* 条线 | 格式为 [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2] 的 *M*×4 矩阵，其中矩阵的每一行对应一条不同的线，且与单条线的向量形式相同。 |  |
  | 具有 (*L*-1) 个线段的单条折线 | 大小为 2*L* 的向量，其中 *L* 是顶点数，格式为 `[x1, y1, x2, y2, ..., xL, yL]`，其中  - x1 和 y1 是第一个线段起点的坐标。 - x2 和 y2 是第一个线段终点和第二个线段起点的坐标。 - xL 和 yL 是第 (*L*-1) 个线段终点的坐标。  折线始终包含 (*L*-1) 个线段，因为第一个和最后一个顶点不连接。  当列数小于二或不是二的倍数时，该模块会产生错误消息。 |  |
  | 具有 (*L*-1) 个线段的 *M* 条折线 | 格式为 [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML] 的 *M*×*2**L* 矩阵，其中矩阵的每一行对应一条不同的折线，且与单条折线的向量形式相同。当其中一条折线包含的线段数少于 (*L*–1) 时，通过重复最后一个顶点的坐标来填充矩阵。  当列数小于二或不是二的倍数时，该模块会产生错误消息。 |  |
- `Polygons` — 形式为 [*x1*, *y1*, *x2*, *y2*,…,*xL*, *yL*] 的 *M*×2*L* 矩阵。*M* 是多边形的数量。点按连续顺序指定以形成多边形。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 具有 *L* 个线段的单个多边形 | 大小为 2*L* 的行向量，其中 *L* 是顶点数，格式为 `[x1 y1 x2 y2 ... xL yL]`，其中：  - x1 和 y1 是第一个线段起点的坐标。 - x2 和 y2 是第一个线段终点和第二个线段起点的坐标。 - xL 和 yL 是第 (*L*-1) 个线段终点和第 *L* 个线段起点的坐标。  该模块将 `[x1 y1]` 连接到 `[xL yL]` 以完成多边形。如果列数小于二或不是二的倍数，该模块会产生错误。 |  |
  | *M* 个多边形，其中任意行的最大线段数为 *L* | 格式为 [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML] 的 *M*×2*L* 矩阵，其中矩阵的每一行对应一个不同的多边形，且与单个多边形的向量形式相同。  当其中一个多边形包含的线段数少于 *L* 时，通过重复最后一个顶点的坐标来填充矩阵。  当列数小于二或不是二的倍数时，该模块会产生错误消息。 |  |
- `Circles` — 形式为 [*x* *y* *radius*] 的 *M*×3 矩阵。*M* 是圆的数量。

  | 形状 | Pts 端口的输入 | 绘制的形状 |
  | --- | --- | --- |
  | 单个圆 | 格式为 `[x y radius]` 的三元素行向量，其中：  - `x` 和 `y` 是圆心的坐标。 - `radius` 是圆的半径，必须大于 0。 |  |
  | *M* 个圆 | 格式为 [xctr1yctr1radius1xctr2yctr2radius2⋮⋮⋮xctrMyctrMradiusM] 的 **M*×3* 矩阵，其中矩阵的每一行对应一个不同的圆，且与单个圆的向量形式相同。 |  |

#### 依赖

- 仅当 **Image** 或 **R**、**G** 和 **B** 端口的输入为浮点时才支持双精度浮点。
- 仅当 **Image** 或 **R**、**G** 和 **B** 端口的输入为浮点时才支持单精度浮点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ROI** — 感兴趣区域 4 元素向量

感兴趣区域，指定为形式为 [*x* *y* *width* *height*] 的四元素向量。该区域定义了一个用于绘制形状的矩形区域。前两个元素表示该区域左上角的基于一的坐标。其余两个元素表示该区域的宽度和高度。

#### 依赖

要启用此端口，请将 **Draw shapes in** 参数设置为 `Specify region of interest via port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Clr** — 形状的颜色 3 元素向量 | *M*×*3* 矩阵

形状的颜色，指定为 *3* 元素向量或 *M*×*3* 矩阵。*M* 是形状的数量，三表示颜色平面的数量。您可以为 *M* 个形状中的每一个指定不同的颜色，或为所有形状指定一种颜色。

#### 依赖

要启用此端口，请将 **Border color source** 或 **Fill color source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出图像 *M*×*N* 的强度值矩阵 | *M*×*N*×*3* 的颜色值数组

输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*3* 数组。输出图像与输入图像具有相同的维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Shape
  summary: 要绘制的形状 Rectangles（默认） | Lines | Polygons | Circles
  group: ''
- name: Fill shapes
  summary: 用颜色填充形状 off（默认） | on
  group: ''
- name: Line width
  summary: 形状的线宽 1（默认） | 正标量
  group: ''
- name: Fill color source
  summary: 指定填充颜色的输入源 Specify via dialog（默认） | Input port
  group: ''
- name: Fill color
  summary: 填充形状的颜色 Black（默认） | White | User-specified value
  group: ''
- name: Border color source
  summary: 指定边框颜色的输入源 Specify via dialog（默认） | Input port
  group: ''
- name: Border color
  summary: 形状的轮廓颜色 Black（默认） | White | User-specified value
  group: ''
- name: Color value(s)
  summary: 用于绘制边框或填充形状的颜色值 标量 | 3 元素向量
  group: ''
- name: Opacity factor (between 0 and 1)
  summary: 颜色值的不透明度 [0,1] 范围内的值 | *R* 元素向量
  group: ''
- name: Use antialiasing
  summary: 平滑算法 off | on
  group: ''
- name: Draw shapes in
  summary: 绘制形状的区域 Entire image（默认） | Specify region of interest via port
  group: ''
- name: Image signal
  summary: 图像信号的输入端口数量 One multidimensional signal（默认） | Separate color signals
  group: ''
```

**主选项卡**

### **Shape** — 要绘制的形状 `Rectangles`（默认） | `Lines` | `Polygons` | `Circles`

要在图像上绘制的一个或多个形状，指定为以下之一：

- `Rectangles` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个矩形。
- `Lines` — 使用指定的形状坐标在输入图像或视频帧上绘制一条或多条线。
- `Polygons` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个多边形。
- `Circles` — 使用指定的形状坐标在输入图像或视频帧上绘制一个或多个圆。

### **Fill shapes** — 用颜色填充形状 off（默认） | on

选择 **Fill shapes** 以启用颜色参数来填充形状。

**注意**

如果您正在生成代码并选中了 **Fill shapes** 复选框，则模块输入的位宽不能超过 16 位。

### **Line width** — 形状的线宽 1（默认） | 正标量

指定要绘制的形状的线宽，为正标量。

### **Fill color source** — 指定填充颜色的输入源 `Specify via dialog`（默认） | `Input port`

指定填充颜色值的输入源。将 **Fill color source** 选择为以下之一：

- `Specify via dialog` — 使用 **Fill color** 参数指定颜色值。
- `Input port` — 使用 **Clr** 端口指定颜色值。

#### 依赖

要启用此参数，请选择 **Fill shapes**。

### **Fill color** — 填充形状的颜色 `Black`（默认） | `White` | `User-specified value`

将形状填充颜色指定为 `Black`、`White` 或 `User-specified value`。`User-specified value` 可以是标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

| 用于填充一个形状或多个相同颜色形状的颜色值 | 用于填充多个具有唯一颜色形状的颜色值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状的数量。 |
| *3* 元素 RGB 向量 | *R*×*3* 矩阵，其中 *3* 是颜色平面的数量，*R* 是形状的数量。 |

对于 **Color Value(s)** 参数中的每个值，请输入一个介于输入图像数据类型可表示的最小值和最大值之间的数字。如果您输入的值超出此范围，该模块会产生错误消息。

#### 依赖

要启用此参数，请选择 **Fill shapes** 参数。

### **Border color source** — 指定边框颜色的输入源 `Specify via dialog`（默认） | `Input port`

指定边框颜色值的输入源。将 **Border color source** 选择为以下之一：

- `Specify via dialog` — 使用 **Border color** 参数指定颜色值。
- `Input port` — 使用 **Clr** 端口指定颜色值。

### **Border color** — 形状的轮廓颜色 `Black`（默认） | `White` | `User-specified value`

将形状的边框颜色指定为 `Black`、`White` 或 `User-specified value`。`User-specified value` 可以是标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

| 用于绘制一个形状或多个相同颜色形状的颜色值 | 用于绘制多个具有唯一颜色形状的颜色值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状的数量。 |
| *3* 元素 RGB 向量 | *R*×*3* 矩阵，其中三表示颜色平面的数量，*R* 是形状的数量。 |

对于 **Color Value(s)** 参数中的每个值，请输入一个介于输入图像数据类型可表示的最小值和最大值之间的数字。如果您输入的值超出此范围，该模块会产生错误消息。

### **Color value(s)** — 用于绘制边框或填充形状的颜色值 标量 | 3 元素向量

将用于绘制边框或填充形状的颜色值指定为标量或 3 元素向量。使用标量指定强度值，使用 3 元素向量指定 RGB 颜色值。

**可调：** 是

#### 依赖

要启用此参数，请将 **Border color** 或 **Fill color** 参数设置为 `User-specified value`。

### **Opacity factor (between 0 and 1)** — 颜色值的不透明度 [0,1] 范围内的值 | *R* 元素向量

将颜色的不透明度指定为 [0, 1] 范围内的正值。`0` 表示透明，`1` 表示不透明。

| 用于填充一个形状或多个相同颜色形状的不透明度因子值 | 用于填充多个具有唯一颜色形状的不透明度因子值 |
| --- | --- |
| 标量强度值 | *R* 元素向量，其中 *R* 是形状的数量 |

#### 依赖

要启用此参数，请选择 **Fill shapes** 参数。

### **Use antialiasing** — 平滑算法 off | on

对线条、多边形或圆执行平滑处理。

#### 依赖

- 要启用此参数，请将 **Shape** 参数设置为 `Lines`、`Polygons` 或 `Circles`。

### **Draw shapes in** — 绘制形状的区域 `Entire image`（默认） | `Specify region of interest via port`

指定绘制指定形状的区域范围。将值选择为以下之一：

- `Entire image` — 在整个图像上绘制形状。
- `Specify region of interest via port` — 在由输入 **ROI** 端口指定的 ROI 内绘制形状。

### **Image signal** — 图像信号的输入端口数量 `One multidimensional signal`（默认） | `Separate color signals`

指定用于指定输入图像的输入端口数量。将值选择为以下之一：

- `One multidimensional signal` — 使用单个端口指定强度或彩色图像。该模块为 *M*×*N*×*3* 彩色图像或 *M*×*N* 强度图像启用 **Image** 端口。
- `Separate color signals` — 指定输入彩色图像的红色、绿色和蓝色平面。该模块启用 **R**、**G** 和 **B** 输入端口。每个端口接受 RGB 彩色图像的 *M*×*N* 平面。

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

Draw Shapes 模块通过覆盖像素值在图像上绘制矩形、线条、多边形或圆形。因此，形状被绘制在输出图像上。该模块使用 Bresenham 直线绘制算法绘制线条、多边形和矩形，使用 Bresenham 圆形绘制算法绘制圆形。输出信号的大小和数据类型与馈送到 **Image**、**R**、**G** 和 **B** 端口的输入信号相同。

您可以通过输入端口设置形状填充或边框颜色，也可以通过参数手动输入值。使用颜色参数指定矩形、线条、多边形或圆形的外观。
