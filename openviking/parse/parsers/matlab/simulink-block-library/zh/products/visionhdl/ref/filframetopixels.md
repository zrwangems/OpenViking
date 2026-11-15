---
type: simulink-block
title: 'FIL Frame To Pixels'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation and Deployment'
documentation_page: 'filframetopixels'
documentation_source_path: 'ref/filframetopixels.html'
language: zh-CN
chinese_source: worker-translation
---

# FIL Frame To Pixels

## 端口

### 输入

### **frame** — 完整图像帧矩阵

完整图像，指定为 (**Active pixels per line**)-by-(**Active video lines**)-by-*N* 矩阵。高度和宽度是在 **Video format** 中指定的活动图像的尺寸。*N* 是用于表示单个像素的 **Number of components**。

**数据类型：** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`
### 输出

### **data1,...,dataN** — 图像像素向量 | 矩阵

图像像素，以 *M*-by-**Number of pixels** 值的矩阵形式返回，其中 *M* 是 **Output vector format** 的宽度。有 *N* 个数据端口，其中 *N* 是 **Number of components**。数据类型与 **frame** 的数据类型相同。

当使用多像素流式传输时，FIL DUT 具有 **Number of pixels** 个数据端口。你必须将输出矩阵拆分为 **Number of pixels** 个长度为 *M* 的行向量，以用于 FIL DUT 输入端口。有关详细信息，请参阅 FPGA-in-the-Loop Simulation with Multipixel Streaming。

类似地，当使用多像素-多分量流式传输时，FIL DUT 具有 **Number of pixels**×**Number of components** 个数据端口。将每个分量的输出矩阵拆分为 **Number of pixels** 个长度为 *M* 的行向量，以用于 FIL DUT 输入端口。

**数据类型：** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`

### **hStartOut** — 帧向量水平行中的第一个像素

帧的水平行中的第一个像素，以 *M* 个值的 `Boolean` 向量形式返回。

对于多像素流式传输，**hStartOut** 应用于对应列中索引最低的像素。

**数据类型：** `Boolean`

### **hEndOut** — 帧向量水平行中的最后一个像素

帧的水平行中的最后一个像素，以 *M* 个值的 `Boolean` 向量形式返回。

对于多像素流式传输，**hEndOut** 应用于对应列中索引最高的像素。

**数据类型：** `Boolean`

### **vStartOut** — 帧向量第一（顶部）行中的第一个像素

帧的第一（顶部）行中的第一个像素，以 *M* 个值的 `Boolean` 向量形式返回。

对于多像素流式传输，**vStartOut** 应用于对应列中索引最低的像素。

**数据类型：** `Boolean`

### **vEndOut** — 帧向量最后（底部）行中的最后一个像素

帧的最后（底部）行中的最后一个像素，以 *M* 个值的 `Boolean` 向量形式返回。

对于多像素流式传输，**vEndOut** 应用于对应列中索引最高的像素。

**数据类型：** `Boolean`

### **validOut** — 有效像素指示符向量

有效像素指示符，以 *M* 个值的 `Boolean` 向量形式返回。

对于多像素流式传输，对应列中的像素要么全部有效，要么全部无效。

**数据类型：** `Boolean`

## 参数

### **Number of components** — 用于表示每个像素的值的数量 `1`（默认） | `3` | `4`

用于表示每个像素的值的数量。每个像素可以有 1、3 或 4 个分量。

- 对于灰度视频，将此参数设置为 `1`。
- 对于彩色视频，例如 {R,G,B} 或 {Y,Cb,Cr}，将此参数设置为 `3`。
- 对于带透明度 alpha 通道的彩色视频，将此参数设置为 `4`。

要为不支持多分量输入的模块处理多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线相同，因此你可以将 Frame To Pixels 模块的 **ctrl** 输出连接到每个复制后的模块。

### **Number of pixels** — 输出矩阵每一列中的像素数量 `1`（默认） | `2` | `4` | `8`

输出矩阵每一列中的像素数量，指定为 `1`、`2`、`4` 或 `8`。

每个数据端口返回一个 *M*-by-**Number of pixels** 矩阵。你必须将此矩阵拆分为 **Number of pixels** 个长度为 *M* 的行向量，以输入到 FIL DUT。有关详细信息，请参阅 FPGA-in-the-Loop Simulation with Multipixel Streaming。

### **Output vector format** — 用于与 FPGA 子系统通信的向量大小 `Frame`（默认） | `Line` | `Pixel`

用于与 FPGA 子系统通信的向量大小。该模块以相同长度的向量返回输入像素和控制信号。该模块根据 **Video format** 参数计算向量的长度。

- `Pixel` — 返回像素和控制信号的标量值。
- `Line` — 返回 (**Total pixels per line**)-by-1 向量。
- `Frame` — 返回 (**Total pixels per line** × **Total video lines**)-by-1 向量。

较大的值会使 FPGA 板与 Simulink 之间的通信更快。请选择你的板卡上的 I/O 和内存资源所能支持的最大选项。

对于多像素流式传输，请为输出大小指定以下选项之一。

- `Pixel` — 返回 1-by-(**Number of pixels**) 的像素值向量，以及应用于每个向量中所有像素的标量控制信号。
- `Line` — 返回 (**Total pixels per line**/**Number of pixels**)-by-**Number of pixels** 的像素值矩阵，以及长度为 (**Total pixels per line**)/(**Number of pixels**) 的控制信号向量。
- `Frame` — 返回 (**Total pixels per line** × **Total video lines**/**Number of pixels**)-by **Number of pixels** 的像素值矩阵，以及长度为 (**Total pixels per line** × **Total video lines**)/**Number of pixels** 的控制信号向量。

#### 依赖关系

当 **Number of pixels** 和 **Number of components** 都大于 1 时，必须将 **Output vector format** 设置为 `Frame`。

### **Video format** — 视频帧中活动区域和非活动区域的尺寸 `1080p`（默认） | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

视频帧中活动区域和非活动区域的尺寸。要选择预定义格式，请从 **Video format** 列表中选择。实际帧尺寸显示在 **Video Format Parameters** 部分中。对于自定义格式，请选择 `Custom`，然后将尺寸指定为整数。

这些尺寸在下表中定义。

**注意**

视频源的采样时间必须与 Frame To Pixels 模块帧中的总像素数匹配。总像素数为 *Total pixels per line* × *Total video lines*，因此请将采样时间设置为该值。

如果你的帧尺寸很大，可能会达到 Simulink 中采样时间的固定步长求解器步长限制，并收到如下错误。

```
The computed fixed step size (1.0) is 1000000.0 times smaller than all
the discrete sample times in the model.
```

你可以通过选择可变步长求解器来避免此错误。

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

使用自定义格式时，你为图像活动和非活动尺寸输入的值之和必须等于总帧尺寸。如果指定的格式不符合这些规则，该模块会报告错误。

- 对于水平方向，**Total pixels per line** 必须大于或等于 **Front porch** + **Active pixels per line**。该模块计算 **Back porch** = **Total pixels per line** − **Front porch** − **Active pixels per line**。
- 对于垂直方向，**Total video lines** 必须大于或等于 **Starting active line** + **Active video lines** − 1。该模块计算 **Ending active line** = **Starting active line** + **Active video lines** − 1。

将 Line Buffer 模块或使用内部行缓冲区的模块与自定义视频格式一起使用时，还适用以下要求：

- 水平消隐间隔，即 **Back porch** + **Front porch**，必须满足以下准则：

  - **Back porch** + **Front porch** 的总和必须至少为 Frame To Pixel 模块之后模块中算法最大内核大小的 2 倍。
  - 如果内核大小小于 4，并且你正在使用边缘填充，则总 porch 必须至少为 8 个像素。
  - 如果禁用填充，则总 porch 必须至少为 12 个像素。
  - **Back porch** 必须至少为 6 个像素。此参数是帧中第一个有效像素之前的非活动像素数。

  有关消隐间隔的详细信息，请参阅 Configure Blanking Intervals。

使用多像素流式传输（**Number of pixels** > 1）时，适用以下要求。

- 视频格式的水平尺寸必须能被 **Number of pixels** 参数值整除。水平尺寸由以下参数设置：**Active pixels per line**、**Total pixels per line**、**Front porch** 和 **Back porch**。标准视频协议 480p、768p、1024p、1080p、1200p、4k UHD 和 8k UHD 支持 **Number of pixels** 等于 4 或 8。
- 多像素流式传输的最小输入帧尺寸为 18 行 × 32 列。
- 选择你的内核大小和 **Active pixels per line**，使得 (**Active pixels per line**)/(**Number of pixels**) 至少为内核宽度。

## 所属库

Vision HDL Toolbox / I/O Interfaces

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink Accelerator 和 Rapid Accelerator 模式的 C/C++ 代码生成。

## 版本历史

**在 R2015a 中引入**

### R2022a：每时钟周期两个像素的流式传输

该模块现在可以生成每个时钟周期 2 个像素的多像素流。

### R2020b：多像素-多分量流式传输

该模块现在可以生成多像素-多分量流。当使用多像素-多分量流式传输时，FIL DUT 具有 **Number of pixels**×**Number of components** 个数据端口。将每个分量的输出矩阵拆分为 **Number of pixels** 个长度为 *M* 的行向量，以用于 FIL DUT 输入端口。

### R2019b：多像素流式传输

该模块现在可以生成多像素流。你可以将 **Number of pixels** 参数设置为 `4` 或 `8`。使用此设置时，该模块的输出在每个时间步上都是 4 或 8 个像素值的向量。有关如何使用此功能的示例，请参阅 FPGA-in-the-Loop Simulation with Multipixel Streaming。

多像素流的视频格式的水平尺寸必须能被 **Number of pixels** 参数值整除。这些水平尺寸由以下参数设置：**Active pixels per line**、**Total pixels per line**、**Front porch** 和 **Back porch**。标准视频协议 480p、720p、1080p 和 4k UHD 一次支持 4 或 8 个像素。

## 描述

将基于帧的视频转换为用于 FPGA-in-the-loop 的像素流

FIL Frame To Pixels 模块执行与 Frame To Pixels 模块相同的帧到像素转换。此外，你可以将输出向量的宽度配置为单个像素、一行或整个帧。该模块以与像素数据宽度相同的向量返回控制信号。当使用 FPGA-in-the-loop (FIL) 时，此优化可以更高效地利用 FPGA 板与 Simulink® 仿真之间的通信链路。要运行 FPGA-in-the-loop，你必须拥有 HDL Verifier™ 许可证。

当你在 Simulink 中为 FIL 目标生成编程文件时，该工具会创建一个模型，以将 FIL 仿真与你的 Simulink 设计进行比较。对于 Vision HDL Toolbox™ 设计，该模型中的 FIL 模块会复制像素流式接口，以一次一个像素发送到 FPGA。你可以修改自动生成的模型，以使用 FIL Frame To Pixels 和 FIL Pixels To Frame 模块，通过一次发送一帧来提高与 FPGA 板的通信带宽。有关如何修改自动生成的模型，请参阅 FPGA-in-the-Loop。

为 FIL Frames To Pixels 模块和 FIL Pixels To Frame 模块指定相同的视频格式和向量大小。
