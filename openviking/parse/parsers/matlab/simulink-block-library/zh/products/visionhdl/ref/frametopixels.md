---
type: simulink-block
title: 'Frame To Pixels'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'Video Formats and Interfaces'
documentation_page: 'frametopixels'
documentation_source_path: 'ref/frametopixels.html'
language: zh-CN
chinese_source: worker-translation
---

# Frame To Pixels

## 端口

### 输入

### **frame** — 完整图像帧数组

完整图像帧，指定为 **Active pixels per line**-by-**Active video lines**-by-*N* 数组。数组的前两个维度是由 **Video format** 参数指定的活动图像的高度和宽度。*N* 是用于表示单个像素的 **Number of components**。**Number of components** 可以为 1、3 或 4。

**数据类型：** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`

### 输出

### **pixel** — 图像像素或像素标量 | 向量

对于单像素流，**pixel** 是作为标量或 1×**Number of components** 值向量返回的单个图像像素。对于多像素流，**pixel** 是 **Number of pixels**×**Number of components** 像素强度值的矩阵。

输出数据类型与 **frame** 端口的数据类型相同。

### **ctrl** — 与像素流关联的控制信号 `pixelcontrol` 总线

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅像素控制总线。

对于多像素流，每个像素值向量都有一组控制信号。由于该向量只有一个 `valid` 信号，因此该向量中的像素必须全部有效或全部无效。`hStart` 和 `vStart` 信号适用于向量中索引最低的像素。`hEnd` 和 `vEnd` 信号适用于向量中索引最高的像素。

**数据类型：** `bus`

## 参数

### **Number of components** — 用于表示每个像素的值的数量 `1`（默认） | `3` | `4`

用于表示每个像素的值的数量。每个像素可以有 1、3 或 4 个分量。

- 对于灰度视频，将此参数设置为 `1`。
- 对于彩色视频，例如 {R,G,B} 或 {Y,Cb,Cr}，将此参数设置为 `3`。
- 对于带透明度 alpha 通道的彩色视频，将此参数设置为 `4`。

若要为不支持多分量输入的模块处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线都相同，因此可以将 Frame To Pixels 模块的 **ctrl** 输出连接到每个复制的模块。

### **Number of pixels** — 每个时间步流式传输的像素数 `1`（默认） | `2` | `4` | `8`

每个时间步在流式接口上传输的像素数，指定为 `1`、`2`、`4` 或 `8`。要为高分辨率或高帧率视频启用多像素流并提高吞吐量，请将此参数设置为 `2`、`4` 或 `8`。多像素流以与单像素流接口相同的时钟频率处理更多像素。

| 视频分辨率 | 60 fps 下单像素流所需的时钟频率 | 60 fps 下多像素流所需的时钟频率（4 个像素） |
| --- | --- | --- |
| 1080p | 150 MHz | 37.5 MHz |
| 4k UHD | 600 MHz | 150 MHz |
| 8k UHD | 1200 MHz | 300 MHz |

### **Video format** — 视频帧中活动区域和非活动区域的维度 `1080p`（默认） | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

视频帧中活动区域和非活动区域的维度。要选择预定义格式，请从 **Video format** 列表中选择。实际帧维度显示在 **视频格式参数** 部分中。对于自定义格式，选择 `Custom`，然后将维度指定为整数。

这些维度在图中定义。

**注意**

视频源的采样时间必须与 Frame To Pixels 模块帧中的总像素数匹配。总像素数是 *Total pixels per line* × *Total video lines*，因此请将采样时间设置为该值。

如果帧大小很大，可能会达到 Simulink® 中采样时间的固定步长求解器步长限制，并收到如下错误。

```
The computed fixed step size (1.0) is 1000000.0 times smaller than all
the discrete sample times in the model.
```

您可以通过选择变步长求解器来避免此错误。

| `Video Format` | `Active Pixels Per Line` | `Active Video Lines` | `Total Pixels Per Line` | `Total Video Lines` | `Starting Active Line` | `Ending Active Line` | `Front Porch` | `Back Porch` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `240p` | 320 | 240 | 402 | 324 | 1 | 240 | 44 | 38 |
| `480p` | 640 | 480 | 800 | 525 | 36 | 515 | 16 | 144 |
| `480pH` | 720 | 480 | 858 | 525 | 33 | 512 | 16 | 122 |
| `576p` | 720 | 576 | 864 | 625 | 47 | 622 | 12 | 132 |
| `720p` | 1280 | 720 | 1650 | 750 | 25 | 744 | 110 | 260 |
| `768p` | 1024 | 768 | 1344 | 806 | 10 | 777 | 24 | 296 |
| `1024p` | 1280 | 1024 | 1688 | 1066 | 42 | 1065 | 48 | 360 |
| `1080p`（默认） | 1920 | 1080 | 2200 | 1125 | 42 | 1121 | 88 | 192 |
| `1200p` | 1600 | 1200 | 2160 | 1250 | 50 | 1249 | 64 | 496 |
| `2KCinema` | 2048 | 1080 | 2750 | 1125 | 42 | 1121 | 639 | 63 |
| `4KUHDTV` | 3840 | 2160 | 4400 | 2250 | 42 | 2201 | 88 | 472 |
| `8KUHDTV` | 7680 | 4320 | 8800 | 4500 | 42 | 4361 | 88 | 1032 |
| `Custom` | 用户定义 | 用户定义 | 用户定义 | 用户定义 | 用户定义 | 用户定义 | 用户定义 | 用户定义 |

当使用自定义格式时，为图像的活动维度和非活动维度输入的值之和必须等于总帧维度。如果指定的格式不符合这些规则，该模块会报告错误。

- 对于水平方向，**Total pixels per line** 必须大于或等于 **Front porch** + **Active pixels per line**。该模块计算 **Back porch** = **Total pixels per line** − **Front porch** − **Active pixels per line**。
- 对于垂直方向，**Total video lines** 必须大于或等于 **Starting active line** + **Active video lines** − 1。该模块计算 **Ending active line** = **Starting active line** + **Active video lines** − 1。

当将 Line Buffer 模块或使用内部行缓冲区的模块与自定义视频格式一起使用时，还适用以下要求：

- 水平消隐间隔，即 **Back porch** + **Front porch**，必须满足以下准则：

  - **Back porch** + **Front porch** 的总和必须至少为 Frame To Pixel 模块之后各模块中算法的最大内核大小的 2 倍。
  - 如果内核大小小于 4，并且您使用边缘填充，则总 porch 必须至少为 8 个像素。
  - 如果禁用填充，则总 porch 必须至少为 12 个像素。
  - **Back porch** 必须至少为 6 个像素。此参数是帧中第一个有效像素之前的非活动像素数。

  有关消隐间隔的详细信息，请参阅配置消隐间隔。

当使用多像素流（**Number of pixels** > 1）时，适用以下要求。

- 视频格式的水平维度必须能被 **Number of pixels** 参数值整除。水平维度由以下参数设置：**Active pixels per line**、**Total pixels per line**、**Front porch** 和 **Back porch**。标准视频协议 480p、768p、1024p、1080p、1200p、4k UHD 和 8k UHD 支持 **Number of pixels** 等于 4 或 8。
- 多像素流的最小输入帧大小为 18 行 × 32 列。
- 选择内核大小和 **Active pixels per line**，使 (**Active pixels per line**)/(**Number of pixels**) 至少为内核宽度。

## 所属库
Vision HDL Toolbox / I/O Interfaces

## 模块特性
未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink Accelerator 和 Rapid Accelerator 模式的 C/C++ 代码生成。

## 版本历史

**在 R2015a 中引入**

### R2022a：每时钟周期两个像素的流式传输

该模块现在可以生成每个时钟周期有 2 个像素的多像素流。

### R2020a：多像素-多分量流式传输

该模块现在可以生成多像素-多分量流。多像素-多分量视频流式传输示例展示了如何使用多像素和多分量像素流处理高分辨率彩色图像。

### R2019b：多像素流式传输

该模块现在可以生成多像素流。您可以将 **Number of pixels** 参数设置为 `4` 或 `8`。使用此设置时，该模块的输出在每个时间步都是 4 或 8 个像素值的向量。有关如何使用此功能的示例，请参阅对多像素视频流进行滤波。

多像素流的视频格式的水平维度必须能被 **Number of pixels** 参数值整除。这些水平维度由以下参数设置：**Active pixels per line**、**Total pixels per line**、**Front porch** 和 **Back porch**。标准视频协议 480p、720p、1080p 和 4k UHD 一次支持 4 或 8 个像素。

## 描述

将基于帧的视频转换为像素流

Frame To Pixels 模块将彩色或灰度视频帧转换为像素流和控制信号。控制信号指示每个像素的有效性及其在帧中的位置。像素流格式可以包含活动帧周围的填充像素。您可以通过选择常见视频格式或指定自定义维度来配置帧和填充维度。像素流可以支持单像素流或多像素流。多像素流每个时钟周期提供 2、4 或 8 个像素，以支持高速率或高分辨率格式。有关像素流格式的详细信息，请参阅流式像素接口。

该模块本身不支持 HDL 代码生成。但是，您可以使用该模块为面向 HDL 代码生成的单独子系统生成输入。

如果您的模型将帧转换为像素流，稍后又将该流转换回帧，请为 Frame To Pixels 模块和 Pixels To Frame 模块指定相同的视频格式。
