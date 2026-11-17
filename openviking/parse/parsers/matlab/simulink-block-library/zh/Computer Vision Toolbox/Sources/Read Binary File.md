---
type: simulink-block
title: 'Read Binary File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'readbinaryfile'
documentation_source_path: 'ref/readbinaryfile.html'
language: zh-CN
chinese_source: worker-translation
---

# Read Binary File

## 端口

### 输出

### **Y'** — 亮度分量三维数组

从二进制文件读取的视频的亮度分量，指定为三维数组。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component1** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — 蓝色差分量三维数组

从二进制文件读取的视频的蓝色差分量，指定为三维数组。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component2** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — 红色差分量三维数组

从二进制文件读取的视频的红色差分量，指定为三维数组。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component3** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **A** — Alpha 分量三维数组

从二进制文件读取的视频的 Alpha 分量，指定为三维数组。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component4** 参数更改此端口的标签。

#### 依赖关系

要启用此端口，请使用以下选项之一。

- 将 **Video format** 参数设置为 `Four character codes`，并将 **Four character code** 参数设置为 `AYUV` 或 `IF09`。
- 将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `4`。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **T** — 透明度分量三维数组

从二进制文件读取的视频的透明度分量，指定为三维数组。

#### 依赖关系

要启用此端口，请将 **Video format** 参数设置为 `Four character codes`，并将 **Four character code** 参数设置为 `Y41T` 或 `Y42T`。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **EOF** — 最后一个视频帧指示标量

当分量端口输出最后一个视频帧时，该端口输出 `1`。在此之前的所有帧，它输出 `0`。

#### 依赖关系

要启用此端口，请选择 **Output end-of-file indicator** 参数。

**数据类型：** `Boolean`

## 参数

### **File name** — 二进制文件名 `vipmen.bin`（默认）| 文件名

指定要从中读取视频数据的二进制源文件的名称。

### **Video format** — 视频数据格式 `Four character codes`（默认）| `Custom`

将视频数据的格式指定为以下选项之一。

- Four character codes (FOURCC) — 有关这些代码的详细信息，请参阅 `https://en.wikipedia.org/wiki/FourCC`。
- Custom — 从自定义格式的二进制文件中读取视频数据。

### **Four character code** — 二进制文件格式 `I420`（默认）| `AYUV` | `CLJR` | `cyuv` | `GREY` | `IF09` | `IMC1` | `IMC2` | `IMC3` | `IMC4` | `IUYV` | `IY41` | `IYU1` | `IYU2` | `IYUV` | `NV12` | `NV21` | `UYNV` | `UYNY` | `V210` | `Y411` | `Y41P` | `Y41T` | `Y422` | `Y42T` | `Y8` | `Y800` | `YUNV` | `YUY2` | `YUYV` | `YV12` | `YV16` | `YVU9` | `YVYU` | ...

指定二进制文件编解码器的四字符代码。此参数的值还设置输出端口的数量。有关哪些四字符代码启用哪些输出端口的信息，请参阅下表。

**四字符代码的输出端口**

| 四字符代码 | 输出端口 |
| --- | --- |
| I420 | Y'|Cb|Cr |
| AYUV | Y'|Cb|Cr|A |
| CLJR | Y'|Cb|Cr |
| cyuv | Y'|Cb|Cr |
| GREY | Y' |
| IF09 | Y'|Cb|Cr|A |
| IMC1 | Y'|Cb|Cr |
| IMC2 | Y'|Cb|Cr |
| IMC3 | Y'|Cb|Cr |
| IMC4 | Y'|Cb|Cr |
| IUYV | Y'|Cb|Cr |
| IY41 | Y'|Cb|Cr |
| IYU1 | Y'|Cb|Cr |
| IYU2 | Y'|Cb|Cr |
| IYUV | Y'|Cb|Cr |
| NV12 | Y'|Cb|Cr |
| NV21 | Y'|Cb|Cr |
| UYNV | Y'|Cb|Cr |
| UYNY | Y'|Cb|Cr |
| V210 | Y'|Cb|Cr |
| Y411 | Y'|Cb|Cr |
| Y41P | Y'|Cb|Cr |
| Y41T | Y'|Cb|Cr|T |
| Y422 | Y'|Cb|Cr |
| Y42T | Y'|Cb|Cr|T |
| Y8 | Y' |
| Y800 | Y' |
| YUNV | Y'|Cb|Cr |
| YUY2 | Y'|Cb|Cr |
| YUYV | Y'|Cb|Cr |
| YV12 | Y'|Cb|Cr |
| YV16 | Y'|Cb|Cr |
| YVU9 | Y'|Cb|Cr |
| YVYU | Y'|Cb|Cr |

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Four character codes`。

### **FrameSize Rows** — 输出数组中的行数 `120`（默认）| 正整数

将输出数组中的行数指定为正整数。此参数的值必须与文件内数据的维度匹配。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Four character codes`。

### **FrameSize Cols** — 输出数组中的列数 `160`（默认）| 正整数

将输出数组中的列数指定为正整数。此参数的值必须与文件内数据的维度匹配。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Four character codes`。

### **Line ordering** — 输出数组填充方向 `Top line first`（默认）| `Bottom line first`

如果选择 `Top line first`，模块首先用二进制文件的相应内容填充输出数组的第一行。然后按递增顺序填充其他行。当选择 `Bottom line first` 时，模块首先用二进制文件的相应内容填充输出数组的最后一行。然后按递减顺序填充其他行。

### **Number of times to play file** — 播放文件的次数 `1`（默认）| 正整数 | `inf`

将重复二进制文件的次数指定为正整数或 `inf`。对于此参数的任意正整数值 `n`，模块播放二进制文件 `n` 次。对于值 `inf`，模块会无限期地播放文件，直到仿真结束。

### **Output end-of-file indicator** — 指示模块输出何时到达最后一帧 `off`（默认）| `on`

此参数指示模块输出何时到达二进制文件中的最后一个视频帧。选择此参数会启用 **EOF** 端口。当模块输出到达最后一个视频帧时，**EOF** 端口的输出为 `1`。对于所有其他帧，它为 `0`。

### **Sample time** — 输出的采样周期 `1/30`（默认）| 正标量 | `-1`

指定输出的采样周期。采样时间指示在仿真期间模块何时产生输出。此参数的值必须是小于仿真时间的正标量或 `-1`。它不能为 `0`。当设置为 `-1` 时，模块从 simulink 模型继承采样时间。

### **Bit stream format** — 指定数据是平面格式还是打包格式 `Planar`（默认）| `Packed`

将二进制文件的数据格式指定为平面格式或打包格式。如果数据是打包的，请使用 **FrameSize Rows** 和 **FrameSize Cols** 参数来定义输出数组的大小。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Number of output components** — 二进制文件中的分量数 `3`（默认）| `1` | `2` | `4`

指定二进制文件的输出分量数。此参数设置输出端口的数量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Component1** — 亮度分量的名称 `Y'`（默认）| 分量名称

指定输出数组亮度分量的名称。亮度分量是输入二进制文件的第一个分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of output components** 参数设置为 `1` 或更大。

### **Component2** — 蓝色差分量的名称 `Cb`（默认）| 分量名称

指定输出数组蓝色差分量的名称。蓝色差分量是输入二进制文件的第二个分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of output components** 参数设置为 `2` 或更大。

### **Component3** — 红色差分量的名称 `Cr`（默认）| 分量名称

使用此参数指定输出数组红色差分量的名称。红色差分量是输入二进制文件的第三个分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of output components** 参数设置为 `3` 或更大。

### **Component4** — Alpha 分量的名称 `Alpha`（默认）| 分量名称

指定输出数组 Alpha 分量的名称。Alpha 分量是输入二进制文件的第四个分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of output components** 参数设置为 `4`。

### **Bits1** — 亮度分量的大小 `8`（默认）| `16` | `24` | `32`

指定输出数组中亮度分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `1` 或更大。

### **Bits2** — 蓝色差分量的大小 `8`（默认）| `16` | `24` | `32`

指定输出数组中蓝色差分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `2` 或更大。

### **Bits3** — 红色差分量的大小 `8`（默认）| `16` | `24` | `32`

指定输出数组中红色差分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `3` 或更大。

### **Bits4** — Alpha 分量的大小 `8`（默认）| `16` | `24` | `32`

指定输出数组中 Alpha 分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `4`。

### **Rows1** — 亮度分量的行数 `120`（默认）| 正整数

指定输出数组中亮度分量的行数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `1` 或更大。

### **Rows2** — 蓝色差分量的行数 `60`（默认）| 正整数

指定输出数组中蓝色差分量的行数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `2` 或更大。

### **Rows3** — 红色差分量的行数 `60`（默认）| 正整数

指定输出数组中红色差分量的行数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `3` 或更大。

### **Rows4** — Alpha 分量的行数 `288`（默认）| 正整数

指定输出数组中 Alpha 分量的行数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output ports** 参数设置为 `4`。

### **Cols1** — 亮度分量的列数 `160`（默认）| 正整数

指定输出数组中亮度分量的列数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `1` 或更大。

### **Cols2** — 蓝色差分量的列数 `80`（默认）| 正整数

指定输出数组中蓝色差分量的列数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `2` 或更大。

### **Cols3** — 红色差分量的列数 `80`（默认）| 正整数

指定输出数组中亮度分量的列数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `3` 或更大。

### **Cols4** — Alpha 分量的列数 `352`（默认）| 正整数

指定输出数组中 Alpha 分量的列数。此参数的值必须是正整数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，并将 **Number of output components** 参数设置为 `4`。

### **Component order in binary file** — 二进制文件中分量的排列 `[1 2 3]`（默认）| 有效分量标识符向量

指定二进制文件中分量的排列。按所需顺序使用分配的数字（从 1 到 4）标识分量。设置此参数时必须包含所有已启用的分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Interlaced video** — 以隔行方式从文件读取视频数据 `off`（默认）| `on`

当二进制文件包含隔行视频数据时，选择此参数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Input file has signed data** — 文件包含有符号整数 `off`（默认）| `on`

当二进制文件包含有符号整数时，选择此参数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Byte order in binary file** — 二进制文件的字节顺序 `Little endian`（默认）| `Big endian`

将二进制文件的字节顺序指定为小端序或大端序。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

从二进制文件读取视频数据

Read Binary File 模块从二进制文件中读取视频数据，并将其导入 Simulink® 模型。

用户指定的模块参数描述视频数据的格式。这些参数与原始二进制文件一起，为 Simulink 模型创建视频数据。

**注意**

此模块仅支持具有文件 I/O 的平台进行代码生成。该模块不支持使用 Simulink
Desktop Real-Time™ 或 Simulink
Real-Time™ 进行代码生成。
