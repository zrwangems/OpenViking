---
type: simulink-block
title: 'Audio Device Reader'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio I/O and Waveform Generation'
documentation_page: 'audiodevicereader'
documentation_source_path: 'ref/audiodevicereader.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Device Reader

## 端口

### 输出

### **A** — 输出信号 标量 | 向量 | 矩阵

Audio Device Reader 模块的输出由该模块的参数确定。如果模块输出为矩阵，则各列对应独立通道。

**数据类型：** `single` | `double` | `int16` | `int32` | `uint8`

### **O** — 溢出样本数 标量

此端口输出采集一帧数据（一个输出矩阵）时溢出的样本数。

#### 依赖关系

要启用此端口，请选择 **Output number of samples overrun** 参数。

**数据类型：** `uint32`

## 参数

#### 主选项卡

### **Driver** — 用于访问音频设备的驱动程序 `DirectSound`（默认）| `ASIO` | `WASAPI`

- ASIO 驱动程序未预装在 Windows 计算机上。要使用 `ASIO` 驱动程序选项，请在 MATLAB® 外部安装 ASIO 驱动程序。

  **注意**

  如果 **Driver** 设置为 `ASIO`，请在 MATLAB 外部打开 ASIO UI，将声卡缓冲区大小设置为 **Samples per frame** 参数指定的值。有关详细信息，请参阅您的 ASIO 驱动程序的文档。
- WASAPI 驱动程序仅支持独占模式。

ASIO 和 WASAPI 驱动程序不提供采样率转换。对于 ASIO 和 WASAPI 驱动程序，请将 **Sample rate (Hz)** 设置为音频设备支持的采样率。

此参数仅适用于 Windows 计算机。Linux 计算机始终使用 ALSA 驱动程序。Mac 计算机始终使用 CoreAudio 驱动程序。

### **Device** — 用于采集音频样本的设备 default audio device（默认）

设备列表由计算机上可用的设备填充。

### **Info** — 查看有关音频输入配置的信息 按钮

此按钮打开一个对话框，其中列出您选择的音频驱动程序、音频设备的完整名称以及您的配置的最大输入通道数。例如：

### **Sample rate (Hz)** — 设备用于采集音频数据的采样率 `44100`（默认）| integer

**Sample rate (Hz)** 的可能范围取决于您的音频硬件。

### **Number of channels** — 音频设备采集的通道数 `1`（默认）| integer

输入通道数也是 Audio Device Reader 模块输出的通道数（矩阵列数）。

#### 依赖关系

要指定音频设备采集哪些输入通道，请在 **高级** 选项卡上选择 **Use default channel mapping** 参数。

### **Samples per frame** — 从音频设备读取的帧大小 `1024`（默认）| integer

**Samples per frame** 也是设备缓冲区大小，以及 Audio Device Reader 模块输出的帧大小（矩阵行数）。

#### 高级选项卡

### **Device bit depth** — 设备用于采集音频数据的数据类型 `16-bit integer`（默认）| `8-bit integer` | `16-bit integer` | `24-bit integer` | `32-bit integer`

设备用于采集音频数据的数据类型，指定为字符向量或字符串。

### **Use default channel mapping** — 切换通道映射源 on（默认）| off

选择此参数时，模块使用声卡输入通道与此模块输出的矩阵列之间的默认映射。清除此参数时，您在 **Device input channels** 中指定映射。

### **Device input channels** — 指定非默认通道映射 `[1:MaximumInputChannels]`（默认）| 标量 | 向量

Audio Device Reader 模块输出的设备通道和矩阵的非默认映射，指定为标量或向量。例如：

如果 **Device input channels** 指定为 `1:3`，则：

- 通道 1 映射到输出矩阵的第一列。
- 通道 2 映射到输出矩阵的第二列。
- 通道 3 映射到输出矩阵的第三列。

如果 **Device input channels** 指定为 `[3,1,2]`，则：

- 通道 3 映射到输出矩阵的第一列。
- 通道 1 映射到输出矩阵的第二列。
- 通道 2 映射到输出矩阵的第三列。

#### 依赖关系

要指定非默认映射，请清除 **Use default channel mapping** 参数。

### **Output number of samples overrun** — 为样本溢出数指定附加输出端口 off（默认）| on

选择此参数时，模块会添加一个附加输出端口 **O**。**O** 端口输出采集一帧数据（一个输出矩阵）时溢出的样本数。

### **Output data type** — 模块输出的数据类型 `double`（默认）| `single` | `int32` | `int16` | `uint8`

输出的数据类型。

**注意**

如果此参数指定为 `double` 或 `single`，则模块输出数据的范围为 [–1, 1]。对于其他数据类型，范围为指定数据类型的 [min, max]。

## 所属库

Audio Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integera` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 支持 16 位和 32 位有符号整数以及 8 位无符号整数。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

从此模块生成的可执行文件依赖 MATLAB 附带的预构建动态库文件（.dll 文件）。使用 `packNGo` 函数将从此对象生成的代码以及所有相关文件打包为压缩的 zip 文件。使用此 zip 文件，您可以在未安装 MATLAB 的另一个开发环境中重定位、解包并重新构建您的项目。有关详细信息，请参阅在 MATLAB 和 Simulink 外部运行音频 I/O 功能。

## 版本历史

**在 R2016a 中引入**

## 描述

从声卡录制

Audio Device Reader 模块使用计算机的音频设备读取音频样本。Audio Device Reader 模块指定驱动程序、设备及其属性，以及从 Audio Device Reader 模块输出的数据类型和大小。
