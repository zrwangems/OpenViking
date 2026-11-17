---
type: simulink-block
title: 'Write Binary File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'writebinaryfile'
documentation_source_path: 'ref/writebinaryfile.html'
language: zh-CN
chinese_source: worker-translation
---

# Write Binary File

## 端口
```yaml
ports:
- name: Y'
  summary: 输入视频流的亮度分量 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cb
  summary: 输入视频流的蓝色差分量 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Cr
  summary: 输入视频流的红色差分量 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: A
  summary: 输入视频流的 Alpha 分量 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: T
  summary: 输入视频流的透明度分量 标量 | 向量 | 矩阵
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
```

### 输入

### **Y'** — 输入视频流的亮度分量 标量 | 向量 | 矩阵

输入视频流的亮度分量，指定为标量、向量或矩阵。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component1** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — 输入视频流的蓝色差分量 标量 | 向量 | 矩阵

输入视频流的蓝色差分量，指定为标量、向量或矩阵。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component2** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — 输入视频流的红色差分量 标量 | 向量 | 矩阵

输入视频流的红色差分量，指定为标量、向量或矩阵。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component3** 参数更改此端口的标签。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **A** — 输入视频流的 Alpha 分量 标量 | 向量 | 矩阵

输入视频流的 Alpha 分量，指定为标量、向量或矩阵。当 **Video format** 参数设置为 `Custom` 时，可以使用 **Component4** 参数更改此端口的标签。

#### 依赖关系

要启用此端口，请使用以下选项之一。

- 将 **Video format** 参数设置为 `Four character codes`，并将 **Four character code** 参数设置为 `AYUV` 或 `IF09`。
- 将 **Video format** 参数设置为 `Custom`，并将 **Number of inputs** 参数设置为 `4`。在这种情况下，此端口的名称为 **Alpha**。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **T** — 输入视频流的透明度分量 标量 | 向量 | 矩阵

输入视频流的透明度分量，指定为标量、向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Video format** 参数设置为 `Four character codes`，并将 **Four character code** 参数设置为 `Y41T` 或 `Y42T`。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
## 参数
```yaml
parameters:
- name: File name
  summary: 二进制文件的名称 output.bin（默认）| 文件名
  group: ''
- name: Video format
  summary: 视频数据的格式 Four character codes（默认）| Custom
  group: ''
- name: Four character code
  summary: 二进制文件的格式 I420（默认）| AYUV | CLJR | cyuv | GREY | IF09 | IMC1 | IMC2 | IMC3 | IMC4 | IUYV | IY41 | IYU1 | IYU2 | IYUV
    | NV12 | NV21 | UYNV | UYNY | V210 | Y411 | Y41P | Y41T | Y422 | Y42T | Y8 | Y800 | YUNV | YUY2 | YUYV | YV12 | YV16 |
    YVU9 | YVYU | ...
  group: ''
- name: Line ordering
  summary: 二进制文件填充方向 Top line first（默认）| Bottom line first
  group: ''
- name: Bit stream format
  summary: 二进制文件的数据格式 Planar（默认）| Packed
  group: ''
- name: Number of inputs
  summary: 输入视频流中的分量数量 3（默认）| 1 | 2 | 4
  group: ''
- name: Inherit size of components from input data type
  summary: 所有分量具有相同的位数 on（默认）| off
  group: ''
- name: Component1
  summary: 亮度分量输入端口的名称 Y'（默认）| 分量名称
  group: ''
- name: Component2
  summary: 蓝色差分量的名称 Cb（默认）| 分量名称
  group: ''
- name: Component3
  summary: 红色差分量的名称 Cr（默认）| 分量名称
  group: ''
- name: Component4
  summary: Alpha 分量的名称 Alpha（默认）| 分量名称
  group: ''
- name: Bits1
  summary: 亮度分量的大小 8（默认）| 0 | 16 | 24 | 32
  group: ''
- name: Bits2
  summary: 蓝色差分量的大小 8（默认）| 0 | 16 | 24 | 32
  group: ''
- name: Bits3
  summary: 红色差分量的大小 8（默认）| 0 | 16 | 24 | 32
  group: ''
- name: Bits4
  summary: Alpha 分量的大小 8（默认）| 0 | 16 | 24 | 32
  group: ''
- name: Component order in binary file
  summary: 二进制文件中分量的排列顺序 [1 2 3]（默认）| 有效分量标识符的向量
  group: ''
- name: Interlaced video
  summary: 将视频数据读取为隔行扫描 off（默认）| on
  group: ''
- name: Write signed data to output file
  summary: 将有符号数据写入输出二进制文件 off（默认）| on
  group: ''
- name: Byte order in binary file
  summary: 输出二进制文件中的字节顺序 Little endian（默认）| Big endian
  group: ''
```

### **File name** — 二进制文件的名称 `output.bin`（默认）| 文件名

指定视频数据的输出二进制文件的名称，扩展名为 `.bin`。单击 **Save As** 以指定文件的位置。

### **Video format** — 视频数据的格式 `Four character codes`（默认）| `Custom`

将视频数据的格式指定为以下选项之一。

- Four character codes (FOURCC) — 有关这些代码的详细信息，请参阅 `https://en.wikipedia.org/wiki/FourCC`。
- Custom — 从自定义格式的二进制文件中读取视频数据。

### **Four character code** — 二进制文件的格式 `I420`（默认）| `AYUV` | `CLJR` | `cyuv` | `GREY` | `IF09` | `IMC1` | `IMC2` | `IMC3` | `IMC4` | `IUYV` | `IY41` | `IYU1` | `IYU2` | `IYUV` | `NV12` | `NV21` | `UYNV` | `UYNY` | `V210` | `Y411` | `Y41P` | `Y41T` | `Y422` | `Y42T` | `Y8` | `Y800` | `YUNV` | `YUY2` | `YUYV` | `YV12` | `YV16` | `YVU9` | `YVYU` | ...

选择二进制文件所需编解码器的 four character code。此参数的值还决定了模块上的输入端口数量。有关哪些 four character codes 启用哪些输入端口的信息，请参阅下表。

**Four Character Codes 的输入端口**

| Four Character Codes | 输入端口 |
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

要启用此参数，请将 **Video Format** 参数设置为 `Four character codes`。

### **Line ordering** — 二进制文件填充方向 `Top line first`（默认）| `Bottom line first`

如果选择 `Top line first`，模块从视频帧的第一行开始填充二进制文件。然后按递增顺序用其他行填充文件。如果选择 `Bottom line first`，模块从视频帧的最后一行开始填充二进制文件。然后按递减顺序用其他行填充文件。

### **Bit stream format** — 二进制文件的数据格式 `Planar`（默认）| `Packed`

将二进制文件的数据格式指定为 `Planar` 或 `Packed`。

#### 依赖关系

要启用此参数，请将 **Video Format** 参数设置为 **Custom**。

### **Number of inputs** — 输入视频流中的分量数量 `3`（默认）| `1` | `2` | `4`

指定输入视频流中的分量数量。此参数设置输入端口的数量。

#### 依赖关系

要启用此参数，请将 **Video Format** 参数设置为 `Custom`。

### **Inherit size of components from input data type** — 所有分量具有相同的位数 `on`（默认）| `off`

选择 **Inherit size of components from input data type** 参数以指示所有分量具有与输入数据类型相同的位数。如果清除此参数，可以使用关联的 **Bits** 参数为每个启用的分量指定位数。

#### 依赖关系

要启用此参数，请将 **Video Format** 参数设置为 `Custom`。

### **Component1** — 亮度分量输入端口的名称 `Y'`（默认）| 分量名称

指定输入视频流亮度分量的输入端口的名称。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `1` 或更大。

### **Component2** — 蓝色差分量的名称 `Cb`（默认）| 分量名称

指定输入视频流蓝色差分量的输入端口的名称。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `2` 或更大。

### **Component3** — 红色差分量的名称 `Cr`（默认）| 分量名称

指定输入视频流红色差分量的输入端口的名称。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `3` 或更大。

### **Component4** — Alpha 分量的名称 `Alpha`（默认）| 分量名称

指定输入视频流 Alpha 分量的输入端口的名称。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `4`。

### **Bits1** — 亮度分量的大小 `8`（默认）| `0` | `16` | `24` | `32`

指定输入视频流中亮度分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `1` 或更大，并选择 **Inherit size of components from input data type** 参数。

### **Bits2** — 蓝色差分量的大小 `8`（默认）| `0` | `16` | `24` | `32`

指定输入视频流中蓝色差分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `2` 或更大，并选择 **Inherit size of components from input data type** 参数。

### **Bits3** — 红色差分量的大小 `8`（默认）| `0` | `16` | `24` | `32`

指定输入视频流中红色差分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `3` 或更大，并选择 **Inherit size of components from input data type** 参数。

### **Bits4** — Alpha 分量的大小 `8`（默认）| `0` | `16` | `24` | `32`

指定输入视频流中 Alpha 分量的大小。此参数的值决定视频流数据被解释为 `8` 位、`16` 位、`24` 位还是 `32` 位。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`，将 **Number of inputs** 参数设置为 `4`，并选择 **Inherit size of components from input data type** 参数。

### **Component order in binary file** — 二进制文件中分量的排列顺序 [`1 2 3`]（默认）| 有效分量标识符的向量

指定二进制文件中分量的排列顺序。按所需顺序使用分配的数字（从 1 到 4）标识分量。设置此参数时必须包含所有已启用的分量。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Interlaced video** — 将视频数据读取为隔行扫描 `off`（默认）| `on`

当视频流包含隔行扫描视频数据时，选择此参数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Write signed data to output file** — 将有符号数据写入输出二进制文件 `off`（默认）| `on`

当输入数据为有符号数据时，选择此参数。

#### 依赖关系

要启用此参数，请将 **Video format** 参数设置为 `Custom`。

### **Byte order in binary file** — 输出二进制文件中的字节顺序 `Little endian`（默认）| `Big endian`

将输出二进制文件中的字节顺序指定为 little endian 或 big endian。

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

将二进制视频数据写入文件

Write Binary File 模块从 Simulink® 模型获取视频数据并将其导出到二进制文件。

此模块生成不带头信息的原始二进制文件。它没有提供数据类型、帧率或维度的编码信息。此模块的视频数据以行主序格式显示。

**注意**

此模块仅对具有文件 I/O 可用的平台支持代码生成。该模块不支持使用 Simulink Desktop Real-Time™ 或 Simulink Real-Time™ 进行代码生成。
