---
type: simulink-block
title: 'Video Input'
family: 'simulink-desktop-real-time'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: 'Simulink Desktop Real-Time'
documentation_page: 'videoinput'
documentation_source_path: 'ref/videoinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Input

## 端口

### 输入

### **ROI Input Data** — 感兴趣区域原点坐标 ROI 输入数据

如果将 **ROI 原点来源** 配置为 `External`，则模块上会提供 **ROI Input Data** 端口。该数据输入是 ROI 原点坐标的向量。其元素对应于 ROI 区域左上角的 X（水平）和 Y（垂直）坐标。如果 **ROI 原点来源** 为 `Internal`，则 ROI 原点坐标由 **ROI 原点** 参数设置。

### 输出

### **Data** — 视频数据输出 `RGB` 数据 | `Luminance` 数据

Data 输出提供视频数据输出。端口的维度和格式取决于 ROI 参数的配置和输出格式。

如果输出格式设置为 `RGB`，则视频数据输出是 uint8 值的 height x width x 3 矩阵。height 和 width 是 ROI 区域的高度和宽度。输出矩阵在坐标 [y,x,c] 处的值对应于图像在颜色通道 c 的坐标 [y,x] 处的值。

如果输出格式设置为 `Luminance`，则视频数据输出是 UINT8 值的 height x width 矩阵。height 和 width 是 ROI 区域的高度和宽度。输出矩阵在坐标 [y,x] 处的值对应于坐标 [y,x] 处像素的亮度。

### **Frame Ready** — 指示视频帧就绪 boolean

**Frame Ready** 输出是 Boolean 输出，当且仅当来自摄像头的新帧已就绪时，其值为 True (1)。如果启用 **显示 "Frame Ready" 端口** 参数，则 **Frame Ready** 端口在模块上可用。

**数据类型：** `Boolean`

### **Frame Error** — 指示数据采集帧错误 boolean

**Frame Error** 输出是 Boolean 输出。如果在帧采集期间发生错误，则值为 True (1)；如果未发生错误，则值为 False (0)。错误条件包括：

- 当采集的帧可能已损坏时
- 当 ROI 区域超出帧边界时

如果启用 **显示 "Frame Error" 端口** 参数，则 **Frame Error** 端口在模块上可用。

**数据类型：** `Boolean`

### **Timestamp** — 提供视频帧时间戳 double

**Timestamp** 输出以秒为单位，是 Double 输出，其值对应于视频数据输出上帧的呈现时间戳。帧时间戳相对于仿真开始时间。如果启用 **显示帧时间戳端口** 参数，则 **Timestamp** 端口在模块上可用。

**数据类型：** `double`

### **Missed Ticks** — 丢失节拍计数（可选） double

在 **Connected IO** 模式下，返回模型落后实时内核的定时器节拍数。当模型落后超过 **最大丢失节拍数** 时，软件会报告错误并停止仿真。

#### 依赖关系

当您选择 **显示 “Missed Ticks” 端口** 时，此端口可见。

**数据类型：** `double`

## 参数

### **采样时间** — 模块的采样时间 `0.1` (默认) | double

输入一个以秒为单位的值，表示您希望模块执行并与 I/O 硬件交互的频率。模块以该采样率将模型与实时时钟同步。

如果您使用的是固定步长求解器，请输入您在 **固定步长** 配置参数中输入的值，或该值的整数倍。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **最大丢失节拍数** — 模型可以落后内核的定时器节拍数 `10` (默认) | integer

在 **Connected IO** 模式下，输入模型可以落后实时内核的定时器节拍数。当模型落后此数量或更少的定时器节拍时，软件假定该滞后是临时的。它允许模型赶上，即使模型丢失了一些节拍。当模型落后超过此数量时，软件会报告错误并停止仿真。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxMissedTicks` |

### **显示 “Missed Ticks” 端口** — 将丢失节拍数发送到端口 `Missed Ticks` `'off'` (默认) | `'on'`

在 **Connected IO** 模式下，选中此复选框以将丢失节拍数发送到输出端口 `Missed Ticks`。

在 **Run in Kernel** 模式下，`Missed Ticks` 端口为零。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowMissedTicks` |

### **等待时让出 CPU** — 内核等待硬件时让出 CPU `'off'` (默认) | `'on'`

在 **Connected IO** 模式下，选中此复选框以在内核等待硬件响应时向其他程序授予更多 CPU 时间。

在 **Run in Kernel** 模式下，软件忽略此值。

#### 编程用法

|  |
| --- |
| **模块参数：** `YieldWhenWaiting` |

### **ROI 原点来源** — 选择感兴趣区域原点来源 `Internal` (默认) | `External`

选择 ROI 区域原点（其左上角的像素坐标）值是否由外部源控制。

- 当选择 `Internal` 时，原点由模块参数控制。
- 当选择 `External` 时，原点由模块输入端口控制。

#### 编程用法

|  |
| --- |
| **模块参数：** `ROIOriginSource` |

### **ROI 原点** — 选择感兴趣区域原点 [X Y] 值 `[1 1]` (默认) | 2 元素向量

**ROI 原点** 指定 ROI 区域左上角的坐标；X 表示水平，Y 表示垂直。如果将 **ROI 原点来源** 配置为 `Internal`，则可以在模块参数对话框中选择 **ROI 原点** 的 2 元素向量值，以指定左上角原点。

#### 编程用法

|  |
| --- |
| **模块参数：** `RoiOrigin` |

### **ROI 尺寸** — 选择感兴趣区域尺寸 [W H] 值 全帧宽度和高度尺寸（默认） | `[640 480]`（如果未配置设备则为默认） | 2 元素向量

**ROI 尺寸** 指定已配置设备的 ROI 区域的宽度-高度尺寸；W 表示宽度，H 表示高度。

#### 编程用法

|  |
| --- |
| **模块参数：** `RoiDimensions` |

### **帧格式** — 选择视频数据格式 `RGB` (默认) | `Luminance`

帧格式决定视频数据是以 RGB 格式提供还是以亮度格式提供。更改输出格式会更改输出视频数据信号的维度；RGB 为 `HxWx3`，Luminance 为 `HxW`。

#### 编程用法

|  |
| --- |
| **模块参数：**`Channels` |

### **显示 "Frame Ready" 端口** — 启用 "Frame Ready" 输出端口 `off` (默认) | `on`

当设置为 `on` 时，模块包含一个 Frame Ready 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowReady` |

### **显示 "Frame Error" 端口** — 启用 "Frame Error" 输出端口 `off` (默认) | `on`

当设置为 `on` 时，模块包含一个 Frame Error 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowError` |

### **显示帧时间戳端口** — 启用时间戳输出端口 `off` (默认) | `on`

当设置为 `on` 时，模块包含一个 Timestamp 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowTimestamp` |

## 所属库

Simulink Desktop Real-Time

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

### R2024b：对带端口名称的模块的更新

在 R2024b 中，当您启用可选端口（例如 **显示 “Missed Ticks” 端口**）时，这些 Simulink® Desktop Real-Time™ 模块端口会随标签一起显示。

## 描述

从系统视频设备获取视频数据

Video Input 模块允许您从系统视频设备获取视频数据。摄像头设备支持包括从标准 USB video class 设备（网络摄像头）进行视频输入的支持。该模块还可以输出视频帧状态（就绪或损坏），并包含帧呈现时间戳。您可以选择输出格式和感兴趣区域 (ROI)。

该模块从数据采集板的配置中获取摄像头分辨率，例如，通过模块选项 **Install new board** > **Standard Devices** > **Camera** 安装的系统摄像头。

摄像头的设备配置界面由摄像头 ID、帧尺寸（宽度和高度）以及可选的亮度通道切换组成。

- 摄像头 ID 是大于或等于 1 的整数，用于指定系统中被访问摄像头的顺序。例如，系统列出的第一个主摄像头的 ID 为 1。摄像头 ID 的默认值为 1。
- 帧宽度和高度决定所需的视频输入分辨率。允许的最大分辨率为 FHD (1920x1080)。默认尺寸为 VGA (640x480)。
- 亮度通道切换是一个复选框，用于确定摄像头设备是否应在 RGB 通道之外还计算视频的亮度通道。其默认值为 TRUE（选中）。

您可以使用 **Test** 和 **OK** 按钮测试或接受配置。如果摄像头配置无效，测试或设置过程将失败并显示错误消息。摄像头配置可能因多种原因失败，例如系统中不存在具有指定 ID 的摄像头、摄像头不支持指定的分辨率或硬件故障。
