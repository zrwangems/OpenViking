---
type: simulink-block
title: 'FIL Pixels To Frame'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL Code Generation and Deployment'
documentation_page: 'filpixelstoframe'
documentation_source_path: 'ref/filpixelstoframe.html'
language: zh-CN
chinese_source: worker-translation
---

# FIL Pixels To Frame

## 端口

### 输入

### **data1,...,dataN** — 图像像素向量 | 矩阵

图像像素，指定为 *M*-by-**Number of pixels** 值的矩阵，其中 *M* 是 **Output vector format** 的宽度。有 *N* 个数据端口，其中 *N* 是 **Number of components**。

当使用多像素流式传输时，FIL DUT 具有 **Number of pixels** 个数据端口。您必须将来自每个端口的输出向量重新组合为 *M*-by-**Number of pixels** 矩阵。有关详细信息，请参阅使用多像素流式传输的 FPGA-in-the-Loop 仿真。

类似地，当使用多像素-多分量流式传输时，FIL DUT 具有 **Number of pixels**×**Number of components** 个数据端口。将输出向量重新组合为每个分量的 *M*-by-**Number of pixels** 矩阵。

**数据类型：** `single` | `double` | `int` | `uint` | `Boolean` | `fixed point`

### **hStartIn** — 帧水平行中的第一个像素向量

帧水平行中的第一个像素，指定为 *M* 个值的 `Boolean` 向量。

对于多像素流式传输，**hStartIn** 应用于对应列中索引最低的像素。

**数据类型：** `Boolean`

### **hEndIn** — 帧水平行中的最后一个像素向量

帧水平行中的最后一个像素，指定为 *M* 个值的 `Boolean` 向量。

对于多像素流式传输，**hEndIn** 应用于对应列中索引最高的像素。

**数据类型：** `Boolean`

### **vStartIn** — 帧第一（顶部）行中的第一个像素向量

帧第一（顶部）行中的第一个像素，指定为 *M* 个值的 `Boolean` 向量。

对于多像素流式传输，**vStartIn** 应用于对应列中索引最低的像素。

**数据类型：** `Boolean`

### **vEndIn** — 帧最后（底部）行中的最后一个像素向量

帧最后（底部）行中的最后一个像素，指定为 *M* 个值的 `Boolean` 向量。

对于多像素流式传输，**hEndIn** 应用于对应列中索引最高的像素。

**数据类型：** `Boolean`

### **validIn** — 有效像素指示向量

有效像素指示，指定为 *M* 个值的 `Boolean` 向量。

对于多像素流式传输，对应列中的像素要么全部有效，要么全部无效。

**数据类型：** `Boolean`

### 输出

### **frame** — 完整图像帧矩阵

完整图像，指定为 (**Active pixels per line**)-by-(**Active video lines**)-by-*N* 矩阵。高度和宽度是 **Video format** 中指定的活动图像尺寸。*N* 是用于表示单个像素的 **Number of components**。数据类型与 **data1,...,dataN** 相同。

### **validOut** — 指示输出帧何时就绪的标量

`true` (1) 值指示输出帧何时从输入流成功重新编译。

**数据类型：** `Boolean`

## 参数

### **Number of components** — 用于表示每个像素的值的数量 `1` (默认) | `2` | `3` | `4`

用于表示每个像素的值的数量。每个像素可以具有 1 到 4 个分量。

- 对于灰度视频，将此参数设置为 `1`。
- 对于彩色视频，例如 {R,G,B} 或 {Y,Cb,Cr}，将此参数设置为 `3`。
- 对于带有用于透明度的 alpha 通道的彩色视频，将此参数设置为 `4`。

要处理不支持多分量输入的模块的多分量流，请为每个分量复制该模块。所有分量的 `pixelcontrol` 总线都是相同的，因此您可以将 Frame To Pixels 模块的 **ctrl** 输出连接到每个复制的模块。

### **Number of pixels** — 输入矩阵每一列中的像素数量 `1` (默认) | `2` | `4` | `8`

输入矩阵每一列中的像素数量，指定为 `1`、`2`、`4` 或 `8`。

每个数据端口都预期一个 *M*-by-**Number of pixels** 矩阵。您必须重新组合 FIL DUT 输出向量以创建此矩阵。有关详细信息，请参阅使用多像素流式传输的 FPGA-in-the-Loop 仿真。

### **Input vector format** — 用于与 FPGA 子系统通信的向量大小 `Frame` (默认) | `Line` | `Pixel`

用于与 FPGA 子系统通信的向量大小。此模块接受长度相同的向量形式的输入像素和控制信号。此模块基于 **Video format** 参数计算向量长度。

- `Pixel` — 接受像素和控制信号的标量值。
- `Line` — 接受包含 **Total pixels per line** 个值的输入向量。
- `Frame` — 接受包含 **Total pixels per line** × **Total video lines** 个值的输入向量。

较大的值会使 FPGA 板和 Simulink 之间的通信更快。选择您板上的 I/O 和内存资源可以支持的最大选项。

对于多像素流式传输，请为输入大小指定以下选项之一。

- `Pixel` — 接受 1-by-(**Number of pixels**) 的像素值向量，以及适用于每个向量中所有像素的标量控制信号。
- `Line` — 接受 (**Total pixels per line**/**Number of pixels**)-by-**Number of pixels** 的像素值矩阵，以及长度为 (**Total pixels per line**)/(**Number of pixels**) 的控制信号向量。
- `Frame` — 返回 (**Total pixels per line** × **Total video lines**/**Number of pixels**)-by-**Number of pixels** 的像素值矩阵，以及长度为 (**Total pixels per line** × **Total video lines**)/**Number of pixels** 的控制信号向量。

#### 依赖关系

当 **Number of pixels** 和 **Number of components** 都大于 1 时，必须将 **Input vector format** 设置为 `Frame`。

### **Video format** — 视频帧活动区域的尺寸 `1080p` (默认) | `240p` | `480p` | `480pH` | `576p` | `720p` | `768p` | `1024p` | `1200p` | `2KCinema` | `4KUHDTV` | `8KUHDTV` | `Custom`

视频帧活动区域的尺寸。要选择预定义格式，请使用 **Video format** 列表。对于自定义格式，选择 `Custom`，然后将活动帧尺寸指定为整数。

| `Video Format` | `Active Pixels Per Line` | `Active Video Lines` |
| --- | --- | --- |
| `240p` | 320 | 240 |
| `480p` | 640 | 480 |
| `480pH` | 720 | 480 |
| `576p` | 720 | 576 |
| `720p` | 1280 | 720 |
| `768p` | 1024 | 768 |
| `1024p` | 1280 | 1024 |
| `1080p` (默认) | 1920 | 1080 |
| `1200p` | 1600 | 1200 |
| `2KCinema` | 2048 | 1080 |
| `4KUHDTV` | 3840 | 2160 |
| `8KUHDTV` | 7680 | 4320 |
| `Custom` | 用户定义 | 用户定义 |

## 所属库

Vision HDL Toolbox / I/O Interfaces

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink Accelerator 和 Rapid Accelerator 模式的 C/C++ 代码生成。

## 版本历史

**在 R2015a 中引入**

### R2022a: 每时钟周期两个像素的流式传输

此模块现在可以接受每个时钟周期具有 2 个像素的多像素流。

### R2020b: 多像素-多分量流式传输

此模块现在可以接受多像素-多分量流。当使用多像素-多分量流式传输时，FIL DUT 具有 **Number of pixels**×**Number of components** 个数据端口。将输出向量重新组合为每个分量的 *M*-by-**Number of pixels** 矩阵。

### R2019b: 多像素流式传输

此模块现在可以接受多像素流。您可以将 **Number of pixels** 参数设置为 `4` 或 `8`。当使用多像素流式传输时，FIL DUT 具有 **Number of pixels** 个数据端口。您必须将来自每个端口的输出向量重新组合为 *M*-by-**Number of pixels** 矩阵。有关详细信息，请参阅使用多像素流式传输的 FPGA-in-the-Loop 仿真。

## 描述

将像素流从 FPGA-in-the-loop 转换为基于帧的视频

FIL Pixels To Frame 模块执行与 Pixels To Frame 模块相同的像素到帧转换。此外，您可以将输入的宽度配置为每步单个像素、一行或整个帧。此模块预期控制信号输入向量的宽度与像素数据相同。在使用 FPGA-in-the-loop 时，此优化可以加速 FPGA 板与您的 Simulink® 仿真之间的通信链路。要运行 FPGA-in-the-loop，您必须具有 HDL Verifier™ 许可证。

当您为 Simulink 中的 FIL 目标生成编程文件时，该工具会创建一个模型，以将 FIL 仿真与您的 Simulink 设计进行比较。对于 Vision HDL Toolbox™ 设计，该模型中的 FIL 模块会复制像素流式传输接口，以一次向 FPGA 发送一个像素。您可以修改自动生成的模型，以使用 FIL Frame To Pixels 和 FIL Pixels To Frame 模块，通过一次发送一帧来提高与 FPGA 板的通信带宽。有关如何修改自动生成的模型，请参阅 FPGA-in-the-Loop。

为 FIL Frames To Pixels 模块和 FIL Pixels To Frame 模块指定相同的视频格式。
