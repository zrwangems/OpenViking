---
type: simulink-block
title: 'Byte Unpack'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Target Communication'
documentation_page: 'byteunpack'
documentation_source_path: 'supportpkg/arduino_ref/byteunpack.html'
language: zh-CN
chinese_source: worker-translation
---

# Byte Unpack

## 端口

### 输入

### **Port\_1** — 打包数据 标量 | 向量 | 矩阵

接收打包数据向量。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — *N* 个输出端口中的第一个 标量 | 向量 | 矩阵

该模块可以有从 `1` 到 *N* 个输出端口，具体由参数 **Output
port data types (cell array)** 中元胞数组的元素指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Output port dimensions (cell array)** — 每个输出端口（未打包）的维度 `{[1]}`（默认） | `{[N], [M], ...}`

输出端口维度指定为向量的元胞数组。

指定与模型中对应 Byte Pack 模块所设置的相同维度。

### **Output port data types (cell array)** — 未打包输出信号的数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输出端口（未打包）的数据类型，针对不同输出信号指定为元胞数组。元胞数组中的元素数量决定此模块实例显示的输出端口数量。

指定与模型中对应 Byte Pack 模块的 **Input port data types (cell array)** 参数所设置的相同数据类型。

### **Byte alignment** — 解包前输出信号数据类型的对齐 `1`（默认） | `2` | `4` | `8`

输入信号列表中的每个元素都从向量起始位置算起的字节对齐值的倍数处开始。如果字节对齐值大于数据类型的大小（以字节为单位），则输出值会用零填充，以填充分配的空间。

例如，如果字节对齐值为 4，则 `uint32` 不需要填充，`uint16` 接收 2 字节填充，`uint8` 接收 3 字节填充。

选择与模型中对应 Byte Pack 模块的 **Byte alignment** 参数所设置的相同字节对齐值。

### 示例

假设您要解包一个数据类型为 `uint8` 或 `uint16` 的向量，并且解包后的信号具有以下属性。

| 维度 | 大小 | 类型 |
| --- | --- | --- |
| 向量 | `3` | `int8` |
| 向量 | `2` | `int16` |
| 标量 | `1` | `uint8` |
| 标量 | `1` | `uint32` |

要解包这些信号：

1. 将 **Output port dimensions (cell array)** 设置为：

   ```
   {'3’, ‘2’, ‘1’, ‘1’}
   ```
2. 将 **Output port data types (cell array)** 设置为：

   ```
   {'int8’, ‘int16’, ‘uint8’, ‘uint32’}
   ```

   该模块创建四个输出端口，其顺序与元胞数组中指定的信号数据类型顺序一致。
3. 设置所需的字节对齐值。字节对齐值指定从上一 boundary 开始经过多少字节后开始一个新字节。

   输出的大小取决于打包向量大小、字节对齐值以及处理器的最小内存单元大小。根据字节对齐值，在解包下一个信号之前，会丢弃用零填充的输出值。最小可寻址内存单元表示处理器中 `char` 或 `uint8` 数据类型占用的位数，并决定数据包的结构。
4. 将传入信号连接到 Byte Unpack 模块的输入端口。

对于每个 char 的最小可寻址内存单元为 8 位的处理器，考虑打包输入向量数据类型 `uint8`。

红色零表示填充的空内存单元。

对于数据类型为 `uint8` 且字节对齐值为 2 的打包输入向量，`int8` 数据值 (23 04 FD) 占用三个内存单元，每个单元占用 8 位。下一个 `int16` 数据值 (00DA FFF4) 的输入信号占用接下来的四个单元（第五到第八），并且第四个单元为空（填充）。Byte Unpack 模块在解包时会考虑单元的对齐和填充。

数据类型为 `uint16` 的打包输入向量为：

解包后的输出信号为：

| **解包后的信号** | | | | |
| --- | --- | --- | --- | --- |
| **维度** | **大小** | **数据类型** | **十进制值** | **十六进制值** |
| 向量 | 3 | `int8` | 35 | 23 |
| 4 | 04 |
| –3 | FD |
| 向量 | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| 标量 | 1 | `uint8` | 112 | 70 |
| 标量 | 1 | `uint32` | 5000 | 00001388 |

对于诸如 Texas Instruments®
C2000™ 等每个 char 的最小可寻址内存单元为 16 位的处理器，考虑打包输入向量数据类型 `uint8`。输出数据包占用 16 位，尽管该数据包表示的数据值为 8 位。字节对齐值相对于 16 位可寻址内存进行计算。

对于数据类型为 `uint8` 且字节对齐值为 2 的打包输入向量，`int8` 数据值 (0023 0004 00FD) 占用三个内存单元，每个单元占用 16 位。下一个数据类型为 `int16` 的信号 (00DA 0000 00F4 00FF) 占用接下来的四个单元（第五到第八），并且第四个单元为空（填充）。Byte Unpack 模块在解包时会考虑单元的对齐和填充。

对于数据类型为 `uint16` 的打包输入向量，输出数据包占用 16 位，并且该数据包表示的数据值也为 16 位。对于 16 及更大的数据包大小，字节对齐相对于数据值必须打包的字节数进行计算。因此，在这种情况下，不允许 1 字节对齐。

对于数据类型为 `uint16` 且字节对齐值为 2 的打包输入，三个 `int8` 数据值 (0423 FD) 占用前两个内存单元。第二个内存单元中的第四个字节为空，并用零填充。`int16` 数据值 (00DA FFF4) 占用接下来的两个内存单元（第三和第四）。Byte Unpack 模块在解包时会考虑单元的对齐和填充。

该表列出解包后的输出信号。如十六进制值所示，`int8` 和 `uint8` 数据值占用 16 位。

| **解包后的信号** | | | | |
| --- | --- | --- | --- | --- |
| **维度** | **大小** | **数据类型** | **十进制值** | **十六进制值** |
| 向量 | 3 | `int8` | 35 | 0023 |
| 4 | 0004 |
| –3 | FFFD |
| 向量 | 2 | `int16` | 218 | 00DA |
| –12 | FFF4 |
| 标量 | 1 | `uint8` | 112 | 0070 |
| 标量 | 1 | `uint32` | 5000 | 00001388 |

## 所属库

Simulink Support Package for Arduino Hardware / Utilities Embedded Coder / Embedded Targets / Host Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Utilities Embedded Coder Support Package for STMicroelectronics STM32 Processors / Utilities Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Utilities SoC Blockset Support Package for Infineon AURIX Microcontrollers / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将 8 位、16 位或 32 位输入向量解包为多个输出向量

Byte Unpack 模块将 `uint8`、`uint16` 或 `uint32` 数据类型的向量转换为一个或多个用户可选择数据类型的信号。此模块是 Byte Pack 模块的逆模块。此模块的输入连接到接收模块（例如 SPI Receive、SCI Receive 或 UDP Receive）的输出端口。然后接收模块通过各种通信网络（例如 SPI、SCI、UDP 或 I2C）传输信号。
