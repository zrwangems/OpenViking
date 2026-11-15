---
type: simulink-block
title: 'Video Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'videoread'
documentation_source_path: 'nvidia/ref/videoread.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Read

## 端口

### 输出

### **Image** — 彩色图像或视频帧数组

彩色图像或视频帧，以 *M*×*N*×*P* 数组形式返回。
*M* 和 *N* 分别是每个图像中的行数和列数。*P* 是每个图像中的颜色通道数。

#### 依赖项

要启用此端口，请将 **图像信号** 参数设置为
`One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Simulink.ImageType`

### **R** — 图像或视频帧矩阵的红色分量

图像或视频帧的红色分量，以 *M*×*N* 矩阵形式返回。*M* 和
*N* 是图像中的行数和列数。

#### 依赖项

要启用此端口，请将 **图像信号** 参数设置为
`Separate color signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — 图像或视频帧矩阵的绿色分量

图像或视频帧的绿色分量，以 *M*×*N* 矩阵形式返回。*M* 和
*N* 是图像中的行数和列数。

#### 依赖项

要启用此端口，请将 **图像信号** 参数设置为
`Separate color signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — 图像或视频帧矩阵的蓝色分量

图像或视频帧的蓝色分量，以 *M*×*N* 矩阵形式返回。*M* 和
*N* 是图像中的行数和列数。

#### 依赖项

要启用此端口，请将 **图像信号** 参数设置为
`Separate color signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **EOF** — 文件结束指示符标量

文件结束指示符，针对每个视频帧以逻辑标量形式返回。当模块输出文件中的最后一个视频帧时，文件结束指示符为 `1`，否则为 `0`。

#### 依赖项

要启用此端口，请选择 **输出文件结束指示符** 参数。

**数据类型：** `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

#### 常规参数

### **文件名** — 多媒体文件的名称 无默认值

目标上供模块读取的多媒体文件的名称。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用
`get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `FileName` |
| **值：** | ' '（默认） | 字符向量 |

### **采样时间** — 模块采样时间 `0.033333333333333333`（默认） | 实正标量

模块的采样时间。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用
`get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `1/30`（默认） | 实正标量 |

#### 视频参数

### **图像大小** — 图像或视频帧的分辨率 `[640, 480]`（默认） | `[width, height]`

图像或视频帧的分辨率，单位为 pixels。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用
`get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageSize` |
| **值：** | `'[640, 480]'`（默认） | `[width, height]` |

### **图像信号** — 输出端口配置 `One multidimensional signal`（默认） | `Separate color signal`

模块如何输出 RGB 彩色视频。如果选择 `One
multidimensional signal`，模块仅使用 **Image** 端口输出视频数据。如果选择 `Separate color
signal`，模块使用三个单独的颜色通道输出视频数据，并分别通过 **R**、**G** 和
**B** 端口输出。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用
`get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `ImageSignal` |
| **值：** | `'One multidimensional signal'`（默认） | `'Separate color signal'` |

### **输出文件结束指示符** — 文件结束指示符 `off`（默认） | `on`

选择此参数可启用 **EOF** 端口，该端口指示输出帧或样本是否为多媒体文件中的最后一个视频帧。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

要以程序化方式获取模块参数值，请使用
`get_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutputEOFIndicator` |
| **值：** | `'off'`（默认） | `'on'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

从 NVIDIA 目标上的多媒体文件中读取视频帧

Video Read 模块从 NVIDIA® 目标平台上的多媒体文件中读取视频帧。

此模块使用 GStreamer 框架处理数据流。您可以使用已安装的 GStreamer 1.0 或更高版本插件支持的视频格式，如 Plugins 中所列。
