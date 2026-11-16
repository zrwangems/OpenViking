---
type: simulink-block
title: 'Byte Pack'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Utilities'
documentation_page: 'bytepack'
documentation_source_path: 'nucleo/ref/bytepack.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Pack

## 端口

### 输入

### **Port\_1** — *N* 个输入端口中的第一个 标量 | 向量 | 矩阵

输入端口数量及其类型在 **Input port data types (cell array)** 参数中指定为元胞数组。该模块可以有从 `1` 到 *N* 个输入端口。*N* 是元胞数组中指定的输入数据类型数量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 包含打包数据的向量

传输打包数据的向量。

**数据类型：** `uint8` | `uint16` | `uint32`

## 参数

### **Output port (packed) data type** — 打包输出信号的数据类型 `uint8` (default) | `uint16` | `uint32`

输出端口处打包输出信号的数据类型。

### **Input port data types (cell array)** — 未打包输入信号的数据类型 `{'double'}` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输入信号（未打包）的数据类型，指定为元胞数组。该模块按照元胞数组中指定的输入数据类型的顺序创建输入端口。例如，元胞数组中的第一个数据类型对应于顶部端口，最后一个数据类型对应于底部端口。

例如，如果数据类型是 `single`、`uint8` 和 `uint8`，则该模块创建三个输入端口。输入端口数据类型的顺序与元胞数组中指定的数据类型相同。

### **Byte alignment** — 打包后输入信号数据类型的对齐 `1` (default) | `2` | `4` | `8`

输入信号列表中的每个元素从字节对齐值的倍数处开始，该值从向量起始处算起。如果字节对齐值大于数据类型的大小（以字节为单位），则用零填充输入值以填充分配的空间。

例如，如果字节对齐值为 4，则 `uint32` 不需要填充，`uint16` 接收 2 字节填充，`uint8` 接收 3 字节填充。

**提示**

如果模型频繁访问数据项，请考虑选择等于要访问的最大数据类型的字节对齐值。如果模型频繁地将数据项作为一组传输，请考虑选择字节对齐值 `1`，它会将数据打包到尽可能小的空间中。

### 示例

假设您要将四个信号打包为数据类型 `uint8` 或 `uint16` 的向量，并且这些信号具有以下属性。

| 维度 | 大小 | 类型 |
| --- | --- | --- |
| 向量 | `3` | `int8` |
| 向量 | `2` | `int16` |
| 标量 | `1` | `uint8` |
| 标量 | `1` | `uint32` |

要打包信号：

1. 设置 **Output port (packed) data type**。此
   示例比较 `uint8` 和
   `uint16`。
2. 将 **Input port data types (cell array)**
   设置为：

   ```
   {'int8’, ‘int16’, ‘uint8’, ‘uint32’}
   ```
   该模块创建四个输入端口，其顺序与元胞数组中指定的输入信号数据类型的顺序相匹配。
3. 设置所需的字节对齐值。字节对齐值指定从上一个边界开始经过多少字节后开始新字节。

   输出的大小基于打包向量大小、字节对齐值以及处理器的最小内存单元大小。根据字节对齐值，在打包下一个信号之前，输入值会用零填充。最小可寻址内存单元指示处理器中 `char` 或 `uint8` 数据类型占用的位数，并决定数据包的结构。
4. 将输入信号连接到 Byte Pack 模块的输入端口。

对于最小可寻址内存单元为每 char 8 位的处理器，请考虑输入信号的以下值。

| **未打包信号** | | | | |
| --- | --- | --- | --- | --- |
| **维度** | **大小** | **数据类型** | **十进制值** | **十六进制值** |
| 向量 | 3 | `int8` | 35 | 23 |
| 4 | 04 |
| –3 | FD |
| 向量 | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| 标量 | 1 | `uint8` | 112 | 70 |
| 标量 | 1 | `uint32` | 5000 | 00001388 |

数据类型 `uint8` 的打包输出向量为：

红色零表示填充的空内存单元。

对于数据类型 `uint8` 且字节对齐值为 2 的打包输出向量，`int8` 数据值（23 04 FD）占用前三个内存单元，每个单元占用 8 位。因为 3 不是字节对齐值 2 的倍数，所以下一个 `int16` 数据值（00DA FFF4）的输入信号被分配到接下来的四个单元（第五到第八个），使第四个单元留空。该模块用零填充空单元。其余输入信号以类似方式打包。

打包所有输入信号后，Byte Pack 模块计算分配的总包数，并输出大小为 4 + 4 + 2 + 4 = 14 的 `uint8` 向量。这里，`int8` 信号占用前 4 个单元，`int16` 信号占用第二组 4 个单元，`uint16` 信号占用第三组 2 个单元，`uint32` 信号占用第四组 4 个单元。

数据类型 `uint16` 的打包输出向量为：

对于 Texas Instruments® C2000™ 等处理器，其最小可寻址内存单元为每 char 16 位，请考虑输入信号的以下值。如十六进制值所示，`int8` 和 `uint8` 数据值占用 16 位。

| **未打包信号** | | | | |
| --- | --- | --- | --- | --- |
| **维度** | **大小** | **数据类型** | **十进制值** | **十六进制值** |
| 向量 | 3 | `int8` | 35 | 0023 |
| 4 | 0004 |
| –3 | FFFD |
| 向量 | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| 标量 | 1 | `uint8` | 112 | 0070 |
| 标量 | 1 | `uint32` | 5000 | 00001388 |

对于数据类型 `uint8` 的打包输出向量，输出包占用 16 位，尽管该包表示的数据值是 8 位。字节对齐值相对于 16 位可寻址内存计算。

对于数据类型 `uint8` 且字节对齐值为 2 的打包输出向量，`int8` 数据值（0023 0004 00FD）占用前三个内存单元，每个单元占用 16 位。因为 3 不是字节对齐值 2 的倍数，所以下一个数据类型为 `int16` 的信号（00DA 0000 00F4 00FF）被分配到接下来的四个单元（第五到第八个），使第四个单元留空。该模块用零填充空单元。其余输入信号以类似方式打包。打包所有输入信号后，Byte Pack 模块计算分配的总包数，并输出大小为 4 + 4 + 2 + 4 = 14 的 `uint8` 向量。

对于数据类型 `uint16` 的打包输出向量，输出包占用 16 位，且该包表示的数据值也是 16 位。对于大小为 16 及更大的包，字节对齐相对于数据值被打包成的字节数计算。因此，在这种情况下，不允许 1 字节对齐。

对于数据类型 `uint16` 且字节对齐值为 2 的打包输出，三个 `int8` 数据值（0423 FD）作为两个字一起打包在前两个内存单元中。第二个内存单元中的第四个字节为空并用零填充。`int16` 数据值（00DA FFF4）被分配到接下来的两个内存单元（第三个和第四个）。其余输入信号以类似方式打包。打包所有信号后，Byte Pack 模块计算分配的总包数，并输出大小为 2 + 2 + 1 + 2 = 7 的 `uint16` 向量。

## 所属库

Simulink Support Package for Arduino Hardware / Utilities Embedded Coder / Embedded Targets / Host Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Utilities Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities SoC Blockset Support Package for Infineon AURIX Microcontrollers / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

Byte Pack 模块将一个或多个用户可选择数据类型的信号转换为单个 `uint8`、`uint16` 或 `uint32` 向量输出。使用该模块的参数，您可以指定输入数据类型以及输出向量中数据的对齐方式。该模块的输出连接到发送模块（例如 SPI Transmit、SCI Transmit 或 UDP Send）的输入端口。然后，发送模块通过各种通信网络（例如 SPI、SCI、UDP 或 I2C）传输信号。
