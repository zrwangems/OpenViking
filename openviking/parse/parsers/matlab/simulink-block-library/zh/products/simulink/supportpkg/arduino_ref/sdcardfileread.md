---
type: simulink-block
title: 'SD Card File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Memory Operations'
documentation_page: 'sdcardfileread'
documentation_source_path: 'supportpkg/arduino_ref/sdcardfileread.html'
language: zh-CN
chinese_source: worker-translation
---

# SD Card File Read

## 端口

### 输入

### **Port\_1** — 读取数据的索引 标量

该端口接受用于读取数据的索引。对于 Raw 和 ASCII 文件，模块从指定索引开始读取数据。对于音频文件，模块从使用指定索引计算出的位置开始读取数据，不包括波形音频文件格式 (WAV) 头。

#### 依赖项

要启用此端口，请选择 **启用按索引读取** 参数。

**数据类型：** `uint8`
### 输出

### **Data** — 来自 SD 卡的音频数据 *M*×*N* 矩阵

模块输出从 SD 卡读取的数据。输出的格式取决于 **文件类型** 参数。如果将 **文件类型** 选择为：

- `Raw` –– 模块以 `uint8` 格式输出数据。
- `ASCII` –– 默认情况下，模块以 `uint8` 格式输出数据。如果选择 **启用分隔符** 参数，模块以 **数据类型** 格式输出数据。
- `Audio (wav)` –– 模块将音频数据输出为 *M*×*N* 矩阵，其中 *M* 是 **帧大小**，*N* 是音频支持的 **通道数**。

模块在遇到文件末尾 (EOF) 时输出零。

**数据类型：** `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Boolean`

### **Status** — 读取操作的状态 标量

模块以 `uint8` 值输出读取操作的状态。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `FILE CANNOT BE OPENED` |
| `2` | `NOT A WAVE FILE` |
| `3` | `BLOCK MASK DATA MISMATCH FOR AUDIO` |
| `4` | `INDEX VALUE EXCEEDS FILE LENGTH` |
| `5` | `FILE HAS CHARACTERS OTHER THAN (0-9, Period, and Delimiter)` |
| `6` | `END OF FILE` |

**数据类型：** `uint8`

## 参数

### **SPI 模块** — SPI 通信模块 `0` (默认) | 标量

指定 Arduino 硬件上用于与 SPI 外设通信的 SPI 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

### **文件类型** — 数据文件的读取格式 `Raw` (默认) | `ASCII` | `Audio(wav)`

指定模块读取文件的格式。

### **文件名** — 音频文件名 `testaudio.wav` (默认)

指定模块从中读取数据的文件的路径和名称。例如，要读取位于 SD 卡 `TestAudio` 文件夹内的 `sample.wav` 文件，请将 **文件名** 指定为 `/TestAudio/sample.wav`

### **读取文件的次数** — 读取音频文件的次数 `Inf` (默认) | 正整数

指定模块从开头读取文件的次数。要读取文件直到停止仿真，请将 **读取文件的次数** 指定为 `Inf`。

### **启用按索引读取** — 启用从给定索引读取 off (默认) | on

当选择 **启用按索引读取** 参数时，模块会配置一个输入端口。在该端口指定索引。

对于 Raw 和 ASCII 文件，模块从指定索引开始读取数据。对于音频文件，模块从使用指定索引计算出的位置开始读取数据，不包括 WAV 头。

### **启用分隔符** — 使用分隔符读取数据的选项 off (默认) | on

- `off` –– 模块读取数据并以 `uint8` 格式输出。
- `on` –– 在每个采样时间，模块读取数据，直到遇到 **分隔符** 参数中指定的下一个分隔符。模块以 **数据类型** 格式输出数据，并省略末尾的分隔符。模块继续读取数据，直到遇到 EOF。

#### 依赖项

要启用此参数，请将 **文件类型** 设置为 `ASCII`。

### **分隔符** — 用于读取数据的分隔符 , (默认)

指定用于读取数据的分隔符。在每个采样时间，模块读取数据，直到遇到下一个分隔符。模块以 **数据类型** 格式输出数据，并省略末尾的分隔符。模块继续读取数据，直到遇到 EOF。

#### 依赖项

要启用此参数，请选择 **启用分隔符** 参数。

### **采样时间** — 读取数据的时间间隔 `-1` (默认) | 正整数

对于 Raw 和 ASCII 文件，指定模块从 SD 卡读取数据的频率。将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

对于 audio (wav) 文件，模块根据所选音频文件的帧大小 (*N*) 和采样率 (*F*s) 计算采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个样本，*F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 秒。

*N* 是你在 **帧大小** 参数中指定的值。*F*s 是你在 **采样率 (Hz)** 参数中指定的值。

### **采样率 (Hz)** — 音频数据每帧的样本数 `44100` (默认) | 介于 `1` 和 `48000` 之间的正整数

指定音频输入设备用于读取音频数据的采样率，以 Hz 为单位。较大的帧大小可能会导致音频输入延迟。确保音频采样频率与输入采样频率匹配，以避免输出中出现任何问题。

**提示**

要查找指定音频文件的采样率，请在 MATLAB® 命令窗口中使用 `audioinfo` 命令。从 `audioinfo` 命令的 `SampleRate` 属性中复制采样率，并将复制的采样率粘贴到 **采样率 (Hz)** 参数。

#### 依赖项

要启用此参数，请将 **文件类型** 设置为 `Audio (wav)`。

### **通道数** — 支持的通道数 `1` (默认) | `2`

指定音频文件是单声道还是立体声。如果音频文件是单声道，请将此参数值设置为 `1`。如果音频文件是立体声，请将此参数值设置为 `2`。

**提示**

要查找指定音频文件支持的通道数，请在 MATLAB 命令窗口中使用 `audioinfo` 命令。将 **通道数** 参数设置为 `audioinfo` 命令的 `NumChannels` 属性中显示的值。

#### 依赖项

要启用此参数，请将 **文件类型** 设置为 `Audio (wav)`。

### **每样本位数** — 位数 `8` (默认) | `16`

指定音频每个样本中的位数。

**提示**

要查找指定音频文件的每样本位数，请在 MATLAB 命令窗口中使用 `audioinfo` 命令。将 **每样本位数** 参数设置为 `audioinfo` 命令的 `BitsPerSample` 属性中显示的值。

#### 依赖项

要启用此参数，请将 **文件类型** 设置为 `Audio (wav)`。

### **帧大小** — 音频数据每帧的样本数 `100` (默认) | 介于 `1` 和 `16384` 之间的正整数

指定一帧中的样本数。较大的帧大小可能会导致音频输出延迟。

#### 依赖项

要启用此参数，请将 **文件类型** 设置为 `Audio (wav)`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

从 SD 卡读取数据

SD Card File Read 模块从连接到硬件的 SD 卡中存储的文件读取数据。硬件通过串行外设接口 (SPI) 与 SD 卡通信。请在“配置参数”对话框中指定用于通信的 SD Card SPI CS Pin。

如果仿真包含 SD Card Read 模块的模型而未连接硬件，则模块输出零。有关更多信息，请参阅“仿真中模块产生零或不执行任何操作”。

单击 **查看引脚映射** 以打开 Arduino 引脚映射表。

要了解如何为该模块分配引脚，请参阅 Arduino 定时器无关模块的引脚映射。

**注意**

现在，您可以将包含 SD Card File Read 模块的 Simulink® 模型部署到兼容 Arduino® 的 ESP32 WROOM 和 ESP32 WROVER 板上。
