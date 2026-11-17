---
type: simulink-block
title: 'Audio Device Writer'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'audiodevicewriter'
documentation_source_path: 'ref/audiodevicewriter.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Device Writer

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

如果 Audio Device Writer 模块的输入数据类型为 `double` 或 `single`，则该模块会将超出范围 [–1, 1] 的值截断。对于其他数据类型，允许的输入范围为指定数据类型的 [min, max]。

**数据类型：** `single` | `double` | `int16` | `int32` | `uint8`
### 输出

### **Port\_1** — 欠载样本数 标量

此端口输出写入一帧数据（一个输入矩阵）时欠载的样本数。

#### 依赖关系

要启用此端口，请选中 **Output number of samples underrun** 参数。

**数据类型：** `uint32`

## 参数

#### 主选项卡

### **Driver** — 用于访问音频设备的驱动程序 `DirectSound`（默认）| `ASIO` | `WASAPI`

- ASIO 驱动程序不会预装在 Windows 机器上。要使用 `ASIO` 驱动程序选项，请在 MATLAB® 之外安装 ASIO 驱动程序。

  **注意**

  如果 **Driver** 设置为 `ASIO`，请在 MATLAB 之外打开 ASIO UI，将声卡缓冲区大小设置为输入到 Audio Device Writer 模块的帧大小（行数）。有关更多信息，请参阅 ASIO 驱动程序的文档。
- WASAPI 驱动程序仅支持独占模式。

ASIO 和 WASAPI 驱动程序不提供采样率转换。对于 ASIO 和 WASAPI 驱动程序，请提供音频设备支持的采样率的音频流。

此参数仅适用于 Windows 机器。Linux 机器始终使用 ALSA 驱动程序。Mac 机器始终使用 CoreAudio 驱动程序。

要指定非默认的 **Driver** 值，您必须拥有 Audio Toolbox™ 许可证。

### **Device** — 用于播放音频样本的设备 默认音频设备（默认）

设备列表由您计算机上可用的设备填充。

### **Info** — 查看有关音频输出配置的信息 按钮

此按钮打开一个对话框，列出您选择的音频驱动程序、音频设备的完整名称以及您配置的最大输出通道数。例如：

### **Inherit sample rate from input** — 指定输入采样率的来源 on（默认）| off

选中此参数时，模块从输入信号继承采样率。清除此参数时，您在 **Sample rate (Hz)** 中指定采样率。

### **Sample rate (Hz)** — 设备用于播放音频数据的采样率 `44100`（默认）| 正标量

**Sample rate (Hz)** 的可能范围取决于您的音频硬件。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

#### 高级选项卡

### **Device bit depth** — 设备用于执行数模转换的数据类型 `16-bit integer`（默认）| `8-bit integer` | `24-bit integer` | `32-bit float`

在执行数模转换之前，输入数据会被转换为由此参数指定的数据类型。

**注意**

要指定非默认的 **Device bit depth**，您必须拥有 Audio Toolbox 许可证。

### **Use default channel mapping** — 切换通道映射来源 on（默认）| off

选中此参数时，模块使用输入到此模块的矩阵列与设备通道之间的默认映射。清除此参数时，您在 **Device output channels** 中指定映射。

### **Device output channels** — 指定非默认通道映射 `[1:MaximumOutputChannels]`（默认）| 标量 | 向量

输入到 Audio Device Writer 模块的矩阵列与输出设备通道之间的非默认映射，指定为标量或向量。例如：

如果 **Device output channels** 指定为 `1:3`，则：

- 输入矩阵的第一列映射到通道 1。
- 输入矩阵的第二列映射到通道 2。
- 输入矩阵的第三列映射到通道 3。

如果 **Device output channels** 指定为 `[3,1,2]`，则：

- 输入矩阵的第一列映射到通道 3。
- 输入矩阵的第二列映射到通道 1。
- 输入矩阵的第三列映射到通道 2。

**注意**

要在输入矩阵的列与声卡的输出通道之间进行选择性映射，您必须拥有 Audio Toolbox 许可证。

#### 依赖关系

要启用此参数，请清除 **Use default mapping between columns of input of this block and sound card’s output channels** 参数。

### **Output number of samples underrun** — 指定欠载样本数的输出端口 off（默认）| on

选中此参数时，会向模块添加一个输出端口。该端口输出写入一帧数据（一个输入矩阵）时欠载的样本数。

## 所属库

Audio Toolbox / Sinks DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integera` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 支持 16 位和 32 位有符号整数以及 8 位无符号整数。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

以下代码生成限制适用：

- 仅限主机。不包括 Simulink® Desktop Real-Time™ 代码生成。
- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的其他开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。

## 版本历史

**在 R2016a 中引入**

## 描述

播放到声卡

Audio Device Writer 模块将音频样本写入音频输出设备。

Audio Device Writer 模块的参数指定驱动程序、设备以及设备属性（如采样率和位深度）。

**Audio Device Writer 模块的数据流**

- 音频信号帧输入到 Audio Device Writer 模块。
- Audio Device Writer 模块使用指定的驱动程序将帧（设备输入）传递到您指定的音频设备缓冲区。
- 音频设备以指定的采样率和位深度执行数模转换。
- 音频设备向您的扬声器输出模拟信号块。
