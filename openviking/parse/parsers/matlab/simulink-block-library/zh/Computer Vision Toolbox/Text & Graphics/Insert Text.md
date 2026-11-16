---
type: simulink-block
title: 'Insert Text'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'inserttextblock'
documentation_source_path: 'ref/inserttextblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Insert Text

## 端口

### 输入

### **Image** — 输入图像矩阵 | 数组

输入图像或视频，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 输入图像矩阵的红色分量 | 数组

输入图像或视频的红色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输入视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 输入图像矩阵的绿色分量 | 数组

输入图像或视频的绿色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输入视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 输入图像矩阵的蓝色分量 | 数组

输入图像或视频的蓝色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输入视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Select** — 选择显示文本，正整数

选择显示文本，指定为正整数。

当 **Text** 参数的输入是字符向量元胞数组时，使用此端口从该元胞数组中选择一个显示文本。例如，当 **Text** 参数是 *S* 个字符向量的元胞数组时，**Select** 端口的值必须在 `[1, S]` 范围内。

#### 依赖关系

要启用此端口，请将 **Text** 参数指定为字符向量元胞数组。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Color** — 文本颜色值 标量 | 向量 | 矩阵

文本颜色值，指定为标量、向量或矩阵。使用此表确定输入到此端口的值类型。

| **输入图像** | 所有文本使用相同颜色 | 每个字符向量使用不同颜色 |
| --- | --- | --- |
| 灰度图像 | 标量值 | *S* 元素向量。*S* 是指定给 **Text** 参数的元胞数组中的字符向量数。 |
| 彩色图像 | 三元素向量 | *S*×3 矩阵。*S* 是指定给 **Text** 参数的元胞数组中的字符向量数。 |

输入图像的数据类型决定颜色值的范围。例如，对于浮点输入图像数据类型，颜色值范围是 [`0`, `1`]。对于 `uint8` 数据类型的输入图像，值范围是 [`0`, `255`]。

**注意**

此端口的输入必须与输入图像具有相同的数据类型。

#### 依赖关系

要启用此端口，请将 **Color value source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Location** — 位置索引 向量 | 矩阵

位置索引，指定为 `[x y]` 形式的二元素向量或 *S*×2 矩阵。`[x y]` 指定输入图像中用于显示文本的坐标。将其指定为 *S*×2 矩阵，以在图像中的不同位置显示 *S* 个字符向量。

#### 依赖关系

要启用此端口，请将 **Location source** 参数设置为 `Input port`。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Opacity** — 不透明度因子 标量 | 向量

不透明度因子，指定为标量或 *S* 元素向量。

- 标量 — 为所有显示文本指定相同的不透明度值。
- *S* 元素向量 — 为 **Text** 参数中指定的 *S* 个字符向量指定不同的不透明度值。

在 `[0`, `1]` 范围内指定不透明度值。

**注意**

**Image**、**R**、**G**、**B** 和 **Color** 端口的输入必须与此端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请将 **Opacity source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

### **Variables** — 文本变量值 标量 | 向量

文本变量值，指定为标量或向量。该模块将 **Text** 参数中的格式说明符（例如 `%d`、`%f` 或 `%s`）替换为 **Variables** 端口指定的元素。

使用 **Variables** 端口在输入图像或视频帧的 *S* 个位置同时显示 *S* 个字符向量或数值。此端口的输入取决于指定给 **Text** 参数的格式说明符类型。

| 显示文本 | 数据类型 | 格式说明符 | **Variables** 端口的输入 |
| --- | --- | --- | --- |
| 字符向量 | `uint8` | `'%s', '%c'` | `['Text1' 0 'Text2' 0 .... 0 'Text`*S*`']` |
| 整数 | `uint8`, `uint16`, `uint32`, `int8`, `int16`, `int32` | `'%d', '%i', '%o', '%x', '%X'` | `[x1 x2 x3.... xS]` |
| 浮点数 | `single`, `double` | `'%f', '%e', '%E', '%g', '%G'` | `[x1 x2 x3.... xS]` |

有关格式说明符的详细信息，请参阅 `sprintf`。

#### 依赖关系

要启用此端口，请在 **Text** 参数中输入 ANSI C `printf` 样式的格式说明符，例如 `'%d'`、`'%f'` 或 `'%s'`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像或视频，返回为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 输出图像矩阵的红色分量 | 数组

输出图像或视频的红色分量，返回为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输出视频中的帧数。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 输出图像矩阵的绿色分量 | 数组

输出图像或视频的绿色分量，返回为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输出视频中的帧数。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 输出图像矩阵的蓝色分量 | 数组

输出图像或视频的蓝色分量，返回为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组，其中 *T* 是输出视频中的帧数。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### 主要

### **Text** — 要插入的文本 `'Text'` (默认) | 字符向量 | 字符向量元胞数组

将要插入图像中的文本指定为字符向量或字符向量元胞数组。您可以使用 **Text** 参数显示单个文本或同时显示多个文本。

- 单个文本 — 您可以将 **Text** 参数指定为字符向量或 *S* 个字符向量的元胞数组。如果指定元胞数组，请使用 **Select** 输入端口从该元胞数组中选择 *S* 个字符向量中的一个。
- 同时显示多个文本 — 您可以在 **Text** 参数中指定 ANSI C `printf` 样式的格式说明符。然后可以使用 **Variable** 输入端口指定这些文本。支持的格式说明符包括 `%d`、`%i`、`%u`、`%o`、`%x`、`%X`、`%c`、`%s`、`%f`、`%e`、`%E`、`%g` 和 `%G`。有关格式说明符的详细信息，请参阅 `sprintf`。

使用此表确定输入到 **Text** 参数的值类型。

| 显示 | **Text** 参数的输入 | **Select** 端口的状态 | **Variables** 端口的状态 |
| --- | --- | --- | --- |
| 一个字符向量 | 单个字符向量，例如 `'Text'` | `Disabled` | `Disabled` |
| *S* 个字符向量中的一个 | *S* 个字符向量的元胞数组，例如 `{'Text1', 'Text2',...., 'TextS'}` | `Enabled` | `Disabled` |
| *S* 个字符向量 | 格式说明符，例如 `'%s'` | `Disabled` | `Enabled` |

### **Color value source** — 文本颜色的来源 `Specify via dialog` (默认) | `Input port`

选择文本颜色来源为 `Specify via dialog` 或 `Input port`。您可以将此参数指定为 `Specify via dialog`，以使用 **Color value** 参数指定插入文本的颜色。您可以将此参数指定为 `Input port`，以使用 **Color** 输入端口指定文本颜色。

### **Color value** — 文本颜色值 `[0 0 0]` (默认) | 标量 | 向量 | 矩阵

文本颜色值，指定为标量、向量或矩阵。使用此表确定输入到此端口的值类型。

| **输入图像** | 所有文本使用相同颜色 | 每个字符向量使用不同颜色 |
| --- | --- | --- |
| 灰度图像 | 标量值 | *S* 元素向量。*S* 是指定给 **Text** 参数的元胞数组中的字符向量数。 |
| 彩色图像 | 三元素向量 | *S*×*3* 矩阵。*S* 是指定给 **Text** 参数的元胞数组中的字符向量数。 |

输入图像的数据类型决定颜色值的范围。例如，对于浮点输入图像数据类型，颜色值范围是 [`0`, `1`]。对于 `uint8` 数据类型的输入图像，值范围是 [`0`, `255`]。

#### 依赖关系

要启用此参数，请将 **Color value source** 参数设置为 `Specify via dialog`。

### **Location source** — 位置索引的来源 `Specify via dialog` (默认) | `Input port`

将显示文本的位置坐标来源指定为以下选项之一：

- `Specify via dialog` — 使用 **Location [x y]** 参数指定显示文本的位置坐标。
- `Input port` — 使用 **Location** 输入端口指定显示文本的位置坐标。

### **Location [x y]** — 文本位置索引 `[1,1]` (默认) | 向量 | 矩阵

文本位置索引，指定为二元素向量 `[x y]` 或 *S*×2 矩阵。`[x y]` 指定输入图像中用于显示文本的坐标。将该值指定为 *S*×2 矩阵，以在图像中的不同位置显示 *S* 个字符向量。

#### 依赖关系

要启用此参数，请将 **Location source** 参数设置为 `Specify via dialog`。

### **Opacity source** — 不透明度因子的来源 `Specify via dialog` (默认) | `Input port`

将不透明度因子来源指定为以下选项之一：

- `Specify via dialog` — 使用 **Opacity** 参数指定不透明度因子。
- `Input port` — 使用 **Opacity** 输入端口指定不透明度因子。

### **Opacity** — 不透明度因子 `1` (默认) | 标量 | 向量

不透明度因子，指定为标量或 *S* 元素向量。

- 标量 — 为显示文本指定相同的不透明度值。
- *S* 元素向量 — 为指定给 **Text** 参数的 *S* 个字符向量指定不同的不透明度值

在 `[0`, `1]` 范围内指定不透明度值。

#### 依赖关系

要启用此参数，请将 **Opacity source** 参数设置为 `Specify via dialog`。

### **Image signal** — 输入和输出信号格式 `One multidimensional signal` (默认) | `Separate color signals`

使用以下选项指定模块输入和输出图像的格式：

- `One multidimensional signal` — 该模块启用单个输入端口和单个输出端口。
- `Separate color signals` — 该模块为图像的相应颜色通道启用 R、G 和 B 输入和输出信号端口。

### **Input image is transposed (data order is row major)** — 镜像文本和文本位置 `off` (默认) | `on`

启用此参数可镜像文本字符串，并将其在图像中的位置从 `[x y]` 反转为 `[y x]`。

### 字体

### **Font face** — 文本字体 `LucidaSansRegular` (默认) | `Agency FB` | `Agency FB Bold` | `Algerian` | `Ariel` | `Arial Black` | `Arial Bold` | `Arial Bold Italic` | ...

指定插入文本的字体。该模块使用系统上安装的字体填充此列表。在 Windows® 上，该模块搜索系统注册表以查找字体文件。在 UNIX 上，该模块搜索 X Server 的字体路径以查找字体文件。

### **Font size (points)** — 字体大小 `12` (默认) | 正标量

指定插入文本的字体大小。

### **Anti-aliased** — 平滑文本边缘 `on` (默认) | `off`

启用此参数可平滑插入文本的边缘。平滑过程的计算开销较大。

## 所属库

Computer Vision Toolbox / Text & Graphics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 支持字长小于或等于 32 位。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

在图像或视频帧上绘制文本

Insert Text 模块在输入图像或视频流上绘制格式化文本。该模块使用开源字体引擎 Free Type 2.3.5 库生成样式化文本位图。有关该库的详细信息，请参阅 The FreeType Project 网站。

**注意**

此模块仅支持 ASCII 字符。

此模块使您能够插入：

- 单个文本实例
- 同一文本的多个实例
- 文本的多个实例，每个位置使用不同文本
