---
type: simulink-block
title: 'Video Capture HDMI'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Vision Applications / Develop Algorithms with Live Video Capture'
documentation_page: 'videocapturehdmi'
documentation_source_path: 'ref/videocapturehdmi.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Capture HDMI

## 端口

### 输出

### **Y, Cb, Cr** — 输入视频帧矩阵的颜色分量

该模块为输入视频的每个颜色分量返回一个矩阵。**Y** 矩阵的维度与帧大小匹配。**Cb** 和 **Cr** 矩阵的维度为 *height*-by-`width/2`，因为 4:2:2 格式为帧中的每个像素交替 **Cb** 和 **Cr** 值。

#### 依赖关系

要启用这些端口，请将 **像素格式** 设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **R, G, B** — 输入视频帧矩阵的颜色分量

该模块为输入视频的每个颜色分量返回一个矩阵。每个矩阵的维度与帧大小匹配。

#### 依赖关系

要启用这些端口，请将 **像素格式** 设置为 `RGB`，并将 **图像信号** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Image** — 彩色输入视频帧矩阵

该模块返回一个 3-by-*height*-by-*width* 矩阵，其中 *height* 和 *width* 与帧大小匹配。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `RGB`，并将 **图像信号** 设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Y** — 灰度输入视频帧矩阵

该模块返回一个矩阵，其维度与帧大小匹配。

#### 依赖关系

要启用此端口，请将 **像素格式** 设置为 `Y only`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **视频源** — 视频流的源 `HDMI input`（默认） | `Test pattern generator`

通过 FPGA 逻辑和 ARM 处理器的视频流可以开始于来自相机板 HDMI 端口的输入视频，或来自测试图案生成器 (TPG) 的生成视频。

- `HDMI input`（默认）— FMC-HDMI-CAM 板上的 HDMI 输入端口。将 **帧大小** 参数设置为与所连接相机的分辨率匹配。
- `Test pattern generator` — 片上 TPG。TPG 以请求的分辨率创建输入帧。测试图案是固定的彩条图案。当您选择 TPG 时，无需将相机或其他 HDMI 源连接到 FMC 卡。

  当您将视频源参数设置为 Test pattern generator 时捕获的视频测试图案。

### **帧大小** — 输入视频的分辨率 `480p SDTV (720x480p)` | `576p SDTV (720x576p)` | `720p HDTV (1280x720p)` | `1080p HDTV (1920x1080p)` | `640x480p` | `800x600p` | `1024x768p` | `1280x768p` | `1280x1024p` | `1360x768p` | `1400x1050p` | `1600x1200p` | `1680x1050p` | `1920x1200p`

从 HD 和 SD TV 分辨率以及常见计算机帧大小中进行选择。如果您选择的分辨率与 HDMI 输入源的分辨率不匹配，该模块将返回错误。

### **帧速率** — 连续图像显示的速率（每秒帧数） `24 fps` | `25 fps` | `30 fps` | `50 fps` | `60 fps`

对于大多数帧大小，此参数仅提供信息。帧大小 `576p` 仅支持 `50 fps`。大多数其他帧大小仅支持 `60 fps`，`720p` 和 `1080p` 除外。

当您使用帧大小 `720p` 或 `1080p` 时，可以从可用的帧速率中进行选择。

该模块将捕获视频帧的 Simulink 采样时间设置为 1/**帧速率**。

### **像素格式** — 像素流的格式 `YCbCr 4:2:2`（默认） | `RGB` | `Y only`

将像素流的格式指定为以下值之一。

- `RGB` — 每个像素三个 8 位颜色分量，总共每个像素 24 位。您还可以选择颜色空间转换标准，以及该模块返回多维信号还是三个单独的颜色信号。有关详细信息，请分别参阅 **使用由以下项指定的颜色空间转换** 和 **图像信号** 参数。
- `Y only` — 灰度。每个像素一个 8 位分量。该模块在 **Y** 输出端口上返回帧。
- `YCbCr 4:2:2`（默认）— 也称为 YUYV。一个 8 位 Y 分量和一个交织的 8 位 CbCr 分量。有效像素大小为 16 位。该模块在 **Y**、**Cb** 和 **Cr** 输出端口上返回分量帧。

要从具有自定义 FPGA 用户逻辑的已部署设计的板捕获视频，此参数必须与已部署设计中的视频格式匹配。在生成的软件接口模型中，此参数显示您在生成 HDL 代码之前于 Video Capture HDMI 模块中选择的配置。当您使用默认 FPGA 逻辑时，可以选择任何像素格式。

Zynq 板上的 HDMI 输入视频以 `YCbCr 4:2:2` 格式提供。您对 Video Capture HDMI 模块的配置会将控制信号发送到 FPGA。FPGA 逻辑根据您指定的像素格式转换输入和输出数据。

| 像素格式 | FPGA 逻辑操作 |
| --- | --- |
| `YCbCr 4:2:2` (YUYV) | 直通。 |
| `RGB` | 将 HDMI 输入像素从 YCbCr 4:2:2 转换为 RGB，并将 RGB 转换为 YCbCr 4:2:2 以用于 HDMI 输出。 |
| `Y only` | 使用 YCbCr 4:2:2 中 HDMI 输入像素的 Y 分量，并为 HDMI 输出输出 YCbCr 4:2:2 的 Y 分量。 |

### **使用由以下项指定的颜色空间转换** — RGB 和 YCbCr 颜色空间之间转换的标准 `Rec. 601 (SDTV)`（默认） | `Rec. 709 (HDTV)`

此参数指定用于在 RGB 和 YCbCr 颜色空间之间转换的方程。有关详细信息，请参阅 Color Space Conversion (Computer Vision Toolbox) 模块。

要从具有自定义 FPGA 用户逻辑的已部署设计的板捕获视频，此参数必须与已部署设计中的视频格式匹配。在生成的软件接口模型中，此参数显示您在生成 HDL 代码之前于 Video Capture HDMI 模块中选择的配置。

#### 依赖关系

要启用此参数，请将 **像素格式** 设置为 `RGB`。

### **旁路 FPGA 用户逻辑** — 将输入帧直接发送到 HDMI 输出 `off`（默认） | `on`

选择此参数可绕过 FPGA 的用户逻辑部分，并将输入视频帧直接发送到 HDMI 输出。当您选择此选项时，捕获点 `A` 和 `B` 观察到相同的视频数据。

### **捕获点** — 捕获到处理器的帧的位置 `Input to FPGA user logic (A)`（默认） | `Output from FPGA user logic (B)` | `No capture`

您可以将帧从 FPGA 用户逻辑部分的输入或输出导入 Simulink。在默认 FPGA 映像中，这部分逻辑是直通。从您的 Simulink 子系统生成 HDL，以插入到 FPGA 的用户逻辑部分。本页描述部分中的数据路径图显示了捕获点 `A` 和 `B`。

- `Input to FPGA user logic (A)` — 在转换之后、用户逻辑部分之前捕获帧。
- `Output from FPGA user logic (B)` — 在用户逻辑部分之后、转换回 HDMI 输出之前捕获帧。
- `No capture` — 没有视频数据传递到 Simulink。您仍可以使用该模块控制 FPGA 上的数据路径和视频格式。

### **图像信号** — RGB 输出流格式 `Separate color signals`（默认） | `One multidimensional signal`

将 RGB 输出流格式指定为以下值之一。

- `Separate color signals` — 该模块为每个颜色分量返回单独的 *height*-by-*width* 矩阵。在这种情况下，该模块具有 **R**、**G** 和 **B** 输出端口。
- `One multidimensional signal` — 该模块返回单个 3-by-*height*-by-*width* 矩阵。在这种情况下，该模块具有 **Image** 输出端口。

#### 依赖关系

要启用此参数，请将 **像素格式** 设置为 `RGB`。

### **流式接口** — 像素流接口的硬件实现 `Pixel-stream video`（默认） | `AXI4-stream video`

此参数设置为 `Pixel-stream video`，并且为只读，因为默认 FPGA 映像使用 Vision HDL Toolbox™ 自定义流式接口。此接口的信号协议与 Simulink 模型中仿真的信号协议匹配。

此参数必须与正在其上捕获数据的板的 FPGA 映像的像素流接口实现匹配。要从使用 AXI4-Stream Video 接口的设计捕获数据，请使用生成的定向硬件接口模型，其中此参数设置为 `AXI4-stream video`，或从该模型复制 Video Capture HDMI 模块。

如果您的 FPGA 映像使用 Vision HDL Toolbox 接口，并且您使用 Video Capture HDMI 模块且此参数设置为 `AXI4-stream video`，则该模型返回以下错误消息。

```
command "/mnt/visionzynq-tools/visionzynq-target-dev.elf --write --device=/dev/mwipcore_vht2vs --address=0x00 0x01".

Error evaluating 'StartFcn' callback of SubSystem block (mask) 'gm_vzImageRotation_PixelStream_tgthw_interface/Video Capture HDMI/VisionZynq Internal/FrameCapture_Init/Frame Format Check'.
Callback string is 'visionzynq.internal.vzmask(gcb, 'FrameFormatCheckCb','StartFcn');'
Caused by: Error executing command "/mnt/visionzynq-tools/visionzynq-target-dev.elf --write --device=/dev/mwipcore_vht2vs --address=0x00 0x01".
```

如果您的 FPGA 映像使用 AXI4-Stream 接口，并且您将此参数设置为 `Pixel-stream video`，则该模块不会向模型捕获任何数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU102 SoC Blockset Support Package for AMD FPGA and SoC Devices / MPSoC / ZCU106 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / PicoZed SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC702 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZC706 SoC Blockset Support Package for AMD FPGA and SoC Devices / Zynq-7000 / ZedBoard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

从基于 Zynq 的硬件上的 HDMI FMC 卡导入实时视频帧

Video Capture HDMI 模块从具有 HDMI FMC 卡的基于 Zynq® 的板捕获视频帧，并将帧导入您的 Simulink® 模型。参考设计使用一个映像对 FPGA 进行编程，该映像包括数据路径多路复用器、视频格式转换和视频测试图案生成器 (TPG)。您可以从 Video Capture HDMI 模块控制这些数据路径和转换选项。

图中的点 **`A`** 和 **`B`** 显示了将视频捕获到 Simulink 或 ARM® 处理器中的选项。FPGA 用户逻辑部分是您使用 HDL Workflow Advisor 从设计中生成的 IP 核。您可以在 FPGA 用户逻辑之前捕获输入视频，或在 FPGA 用户逻辑之后捕获输出视频。如果您启用 FPGA 用户逻辑的旁路，或者您尚未生成任何 FPGA 用户逻辑，则两个捕获位置显示相同的数据。

视频数据在 FPGA 上是像素流，但当您将视频导入 Simulink 时，流会转换为基于帧的视频。

显示 HDMI 视频输入被转换为指定格式并路由通过 FPGA 用户逻辑的 FPGA 设计图。

HDMI 参考设计要求整个数据路径具有相同的视频分辨率和颜色格式。您为 Video Capture HDMI 模块选择的分辨率必须与您的相机输入的分辨率匹配。您定向到 FPGA 用户逻辑的设计不得修改数据的帧大小或格式。

当您在部署有默认 FPGA 映像的模型中使用此模块时，您可以更改参考设计捕获到 ARM 处理器的视频格式，从而更改导入到 Simulink 的视频帧的格式。

HDL Workflow Advisor 生成一个包含 Video Capture HDMI 模块的软件接口模型。生成的模块的参数设置与您的原始模型中 Video Capture HDMI 模块的设置匹配。您可以更改输入视频分辨率、在 HDMI 输入或片上测试图案生成器之间切换，以及启用 FPGA 用户逻辑部分的可选旁路。当您更改参数时，该模块会写入板上的 AXI-Lite 寄存器。

您还可以将此模块部署到 ARM 处理器，以将视频从 FPGA 用户逻辑捕获到 ARM 中进行进一步处理。当您以这种方式使用该模块时，该模块上的设置必须与已部署的 FPGA 映像的设置匹配。

要在生成的软件接口模型中使用此模块，或创建您自己的模型以定向到 ARM 处理器，您必须拥有 Embedded Coder® 产品和 Embedded Coder Support Package for AMD SoC Devices。
