---
type: simulink-block
title: 'Pixels To Frame'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'pixelstoframe'
documentation_source_path: 'ref/pixelstoframe.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixels To Frame

## 端口

### 输入

### **pixel** — 输入像素流 标量 | 向量 | 矩阵

对于单像素流，将 **pixel** 指定为标量或 1×**Number of components** 个值的向量，这些值表示单个像素。对于多像素流，将 **pixel** 指定为 **Number of pixels**×**Number of components** 像素强度值的矩阵。**Number of pixels** 可以是 2、4 或 8。**Number of components** 可以为 1 到 4。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流式传输，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号应用于该向量中索引最低的像素。`hEnd` 和 `vEnd` 信号应用于该向量中索引最高的像素。

**数据类型：** `bus`

### 输出

### **frame** — 完整图像帧数组

完整图像帧，返回为 **Active pixels per line**×**Active video lines**×*N* 数组。前两个数组维度是由 **Video format** 参数指定的有效图像的高度和宽度。*N* 是用于表示单个像素的 **Number of components**。输出数据类型与 **pixel** 端口的数据类型相同。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `single` | `double`

### **validOut** — 指示输出帧何时就绪 标量

当模块已成功从输入流重新编译出输出帧时，该信号为 1 (`true`)。

**数据类型：** `Boolean`

## 参数

### **Number of components** — 用于表示每个像素的值的数量 `1` (default) | `2` | `3` | `4`

用于表示每个像素的值的数量。每个像素可以有 1 到 4 个分量。

- 对于灰度视频，将此参数设置为 `1`。
- 对于彩色视频，例如 {R,G,B} 或 {Y,Cb,Cr}，将此参数设置为 `3`。
- 对于具有用于透明度的 alpha 通道的彩色视频，将此参数设置为 `4`。

要为不支持多分量输入的模块处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线都相同，因此您可以将 Frame To Pixels 模块的 **ctrl** 输出连接到每个复制的模块。

### **Number of pixels** — 每个时间步流式传输的像素数量 `1` (default) | `2` | `4` | `8`

在流式接口上为每个时间步传输的像素数量，指定为 `1`、`2`、`4` 或 `8`。要启用多像素流式传输并提高高分辨率或高帧率视频的吞吐量，请将此参数设置为 `2`、`4` 或 `8`。多像素流式传输以与单像素流式传输接口相同的时钟频率处理更多像素。

| 视频分辨率 | 60 fps 下单像素流式传输所需的时钟频率 | 60 fps 下多像素流式传输所需的时钟频率（4 个像素） |
| --- | --- | --- |
| 1080p | 150 MHz | 37.5 MHz |
| 4k UHD | 600 MHz | 150 MHz |
| 8k UHD | 1200 MHz | 300 MHz |

### **Video format** — 视频帧中有效区域的维度 `1080p` (default) | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

视频帧中有效区域的维度。要选择预定义格式，请使用 **Video format** 下拉菜单。有效帧维度按表中所示设置。对于自定义格式，选择 `Custom`，然后以整数指定有效帧维度。

| `Video Format` | `Active Pixels Per Line` | `Active Video Lines` |
| --- | --- | --- |
| `240p` | 320 | 240 |
| `480p` | 640 | 480 |
| `480pH` | 720 | 480 |
| `576p` | 720 | 576 |
| `720p` | 1280 | 720 |
| `768p` | 1024 | 768 |
| `1024p` | 1280 | 1024 |
| `1080p` (default) | 1920 | 1080 |
| `1200p` | 1600 | 1200 |
| `2KCinema` | 2048 | 1080 |
| `4KUHDTV` | 3840 | 2160 |
| `8KUHDTV` | 7680 | 4320 |
| `Custom` | 用户定义 | 用户定义 |

## 所属库

Vision HDL Toolbox / I/O Interfaces

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink® Accelerator 和 Rapid Accelerator 模式的 C/C++ 代码生成。

## 版本历史

**在 R2015a 中引入**

### R2022a：每个时钟周期两个像素的流式传输

该模块现在支持每个时钟周期 2 个像素的多像素流。

### R2020a：多像素-多分量流式传输

该模块现在支持多像素-多分量流。该模块接受 *NumPixels* × *NumComponents* 像素的输入矩阵。**ctrl** 端口保持标量，`pixelcontrol` 总线中的控制信号应用于矩阵中的所有像素。MultiPixel-MultiComponent Video Streaming 示例展示了如何使用多像素和多分量像素流处理高分辨率彩色图像。

### R2019b：多像素流式传输

该模块现在接受每个时钟周期 4 或 8 个像素的像素流。您可以将 **Number of pixels** 参数设置为 `4` 或 `8`。使用此设置时，该模块期望每个时间步提供 4 或 8 个像素值的输入向量。有关如何使用此功能的示例，请参阅 Filter Multipixel Video Streams。

## 描述

将像素流转换为基于帧的视频

Pixels To Frame 模块将彩色或灰度像素流以及控制信号转换为基于帧的视频。控制信号总线指示每个像素的有效性及其在帧内的位置。像素流格式可以包含有效帧周围的填充像素。您可以通过选择常见视频格式或指定自定义维度来配置帧和填充维度。像素输入可以支持单像素流式传输或多像素流式传输。多像素流式传输每个时钟周期接受 2、4 或 8 个像素，以支持高速率或高分辨率格式。有关像素流格式的详细信息，请参阅流式像素接口。

此模块本身不支持 HDL 代码生成。但是，您可以使用此模块将针对 HDL 代码生成的单独子系统的输出转换回帧。

如果您的模型将帧转换为像素流，随后又将该流转换回帧，请为 Frame To Pixels 模块和 Pixels To Frame 模块指定相同的视频格式。
