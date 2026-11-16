---
type: simulink-block
title: 'Video Send'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'videosend'
documentation_source_path: 'nvidia/ref/videosend.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Send

## 端口

### 输入

### **Image** — 要流式传输的 RGB 或灰度图像信号 *M*-by-*N*-by-*3* 矩阵 | *M*-by-*N* 矩阵

要流式传输的 RGB 或灰度图像信号，分别指定为 *M*-by-*N*-by-*3* 矩阵或 *M*-by-*N* 矩阵。

#### 依赖关系

`Image Signal` 参数必须设置为 `One multidimensional signal`。

**数据类型：** `uint8` | `uint16`

### **R** — 要流式传输的 RGB 图像的红色通道信号 *M*-by-*N* 矩阵。

要流式传输的 RGB 图像的红色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖关系

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

### **G** — 要流式传输的 RGB 图像的绿色通道信号 *M*-by-*N* 矩阵

要流式传输的 RGB 图像的绿色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖关系

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

### **B** — 要流式传输的 RGB 图像的蓝色通道信号 *M*-by-*N* 矩阵

要流式传输的 RGB 图像的蓝色通道信号，指定为 `M-by-N` 矩阵。

#### 依赖关系

`Image Signal` 参数必须设置为 `Separate color signals`。

**数据类型：** `uint8`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink 工具条中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

#### 视频参数

### **Format** — 输入视频流信号格式 `RGB` (默认) | `Grayscale`

将输入视频流信号格式指定为下列项之一：

- `RGB` - RGB 图像（每个颜色通道 8 位）。
- `Grayscale` - 灰度图像（8 位）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageFormat` |
| **值：** | `'RGB'` (默认) | `'Grayscale'` |

### **Image signal** — RGB 图像输入信号的性质 `One multidimensional signal` (默认) | `Separate color signals`

将 RGB 图像输入信号的性质指定为下列项之一：

- `One multidimensional signal` - 一个输入端口，用于具有 R、G 和 B 颜色通道的 *M*-by-*N*-by-*3* 彩色视频信号。
- `Separate color signals` - 用于 R、G 和 B 通道的三个单独输入端口。每个端口接受一个 *M*-by-*N* 矩阵。

#### 依赖关系

`Format` 参数必须设置为 `RGB`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageSignal` |
| **值：** | `'One multidimensional signal'` (默认) | `'Separate color signal'` |

### **Compression** — 视频流的压缩格式 `JPEG` (默认) | `H264` | `H265` | `VP8` | `VP9` | `None (uncompressed)`

指定视频流的压缩格式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `Compression` |
| **值：** | `'JPEG'` (默认) | `'VP8'` | `'VP9'` | `'H264'` | `'H265'` | `'None (uncompressed)'` |

### **Quality** — 视频流的质量 85 (默认) | [0,100] 范围内的正标量

将 JPEG 视频流的质量指定为正标量。此参数控制视频流的编码速度和压缩比。较高的质量值会提高图像质量，但代价是更高的网络带宽。对于低带宽网络连接，请指定较低的值。

#### 依赖关系

`Compression` 参数必须设置为 `JPEG`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `JPEGQuality` |
| **值：** | 85 (默认) | [0,100] 范围内的正标量 |

### **Enable hardware acceleration** — 使用图形硬件进行编码 `on` (默认) | off

选择此参数可启用 NVIDIA® 目标上用于编码的图形硬件。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `UseHWAcceleration` |
| **值：** | `'on'` (默认) | `'off'` |

#### 连接参数

### **Remote address** — 远程 IP 地址 127.0.0.1 (默认) | 有效 IP 地址

将模块向其发送消息的远程设备的 IP 地址或主机名指定为字符向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RemoteAddress` |
| **值：** | `127.0.0.1` (默认) | 带引号的有效 IP 地址 |

### **Remote port** — 远程 IP 端口 3000 (默认) | 0 到 65535 的整数

指定模块将消息发送到的远程设备的 IP 端口。流式传输视频时，此模块会选择第一个可用的本地 UDP 端口，与您指定的远程端口无关。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

要以编程方式获取模块参数值，请使用 `get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RemotePort` |
| **值：** | `3000` (默认) | 0 到 65535 的整数 |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

将视频流发送到远程硬件

Video Send 模块将视频流从 Simulink® 发送到指定的远程设备。您可以将灰度图像和 RGB 图像发送到远程设备，并指定视频流的压缩格式和质量。此模块使用 GStreamer 框架处理数据流式传输。
