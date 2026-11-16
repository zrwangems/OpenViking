---
type: simulink-block
title: 'Deep Learning HDL Processing System'
family: 'deep-learning-hdl'
product_id: 'deep-learning-hdl'
product_name: 'Deep Learning HDL Toolbox'
documentation_release: R2025b
official_category: 'System Integration of Deep Learning Processor IP Core'
documentation_page: 'deeplearninghdlprocessingsystem'
documentation_source_path: 'ref/deeplearninghdlprocessingsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Deep Learning HDL Processing System

## 端口

### 输入

### **RegisterWriteCtrlIn** — 输入写数据控制总线 bus

输入写数据控制总线，指定为 bus。总线控制信号类型为 `BusAXIWriteCtrlM2S`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `wr_addr` | `uint32` 标量 |
| `wr_len` | `uint32` 标量 |
| `wr_valid` | `Boolean` 标量 |

**数据类型：** `BusAXIWriteCtrlM2S`

### **RegisterWriteData** — 输入数据 标量 | 向量

输入数据，指定为标量或向量。

**数据类型：** `uint32`

### **RegisterReadCtrlIn** — 输入读数据控制总线 bus

输入数据读控制总线，指定为 bus。总线控制信号类型为 `BusAXIReadCtrlM2S`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `rd_addr` | `uint32` 标量 |
| `rd_len` | `uint32` 标量 |
| `rd_avalid` | `boolean` 标量 |
| `rd_dready` | `boolean` 标量 |

**数据类型：** `BusAXIReadCtrlM2S`

### **MemoryWriteCtrlIn** — 输入 DDR 内存写数据控制总线 bus

输入 DDR 内存写数据控制总线，指定为 bus。总线控制信号类型为 `BusAXIWriteCtrlM2S`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `wr_addr` | `uint32` 标量 |
| `wr_len` | `uint32` 标量 |
| `wr_valid` | `Boolean` 标量 |

**数据类型：** `BusAXIWriteCtrlm2S`

### **MemoryWriteData** — 输入 DDR 内存数据 标量 | 向量

输入 DDR 内存数据，指定为标量或向量。

**数据类型：** `ufix128`

### **MemoryReadCtrlIn** — 输入 DDR 内存读数据控制总线 bus

输入 DDR 内存读数据控制总线，指定为 bus。总线数据类型为 `BusAXIReadCtrlM2S`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `rd_addr` | `uint32` 标量 |
| `rd_len` | `uint32` 标量 |
| `rd_avalid` | `boolean` 标量 |
| `rd_dready` | `boolean` 标量 |

**数据类型：** `BusAXIReadCtrlM2S`

### **InputStart** — 数据处理启动信号 标量

数据处理启动信号，指定为 boolean。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### **FrameCount** — 输入数据帧数 标量

输入数据帧数，指定为 `int32` 标量。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `int32`

### **InputStop** — 数据流停止信号 标量

数据流停止信号，指定为 boolean。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### **InputNext** — 下一个输入帧就绪信号 标量

下一个输入帧就绪信号，指定为 boolean。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### **OutputNext** — 当前输出数据读取完成信号 标量

当前输出数据读取完成信号，指定为 boolean。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### 输出

### **RegisterWriteCtrlOut** — 输出数据写控制总线 bus

输出数据写控制总线，返回为 bus。总线控制信号类型为 `BusAXIWriteCtrlS2M`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `wr_ready` | `boolean` 标量 |
| `wr_complete` | `boolean` 标量 |

**数据类型：** `BusAXIWriteCtrlS2M`

### **RegisterReadData** — 输出数据 标量 | 向量

输出数据，返回为标量或向量。

**数据类型：** `uint32`

### **RegisterReadCtrlOut** — 输出数据读控制总线 bus

输出数据读控制总线，返回为 bus。总线控制信号类型为 `BusAXIReadCtrlS2M`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `rd_aready` | `boolean` 标量 |
| `rd_dvalid` | `boolean` 标量 |

**数据类型：** `BusAXIReadCtrlS2M`

### **MemoryWriteCtrlOut** — 输出 DDR 内存数据写控制总线 bus

输出 DDR 内存数据写控制总线，返回为 bus。总线控制信号类型为 `BusAXIWriteCtrlS2M`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `wr_ready` | `boolean` 标量 |
| `wr_complete` | `boolean` 标量 |

**数据类型：** `BusAXIWriteCtrlS2M`

### **MemoryReadData** — 输出 DDR 内存数据 标量 | 向量

输出 DDR 内存数据，返回为标量或向量。

**数据类型：** `ufix128`

### **MemoryReadCtrlOut** — 输出 DDR 内存数据读控制总线 bus

输出 DDR 内存数据读控制总线，返回为 bus。总线控制信号类型为 `BusAXIReadCtrlS2M`，并包含以下信号：

| 信号名称 | 数据类型 |
| --- | --- |
| `rd_aready` | `boolean` 标量 |
| `rd_dvalid` | `boolean` 标量 |

**数据类型：** `BusAXIReadCtrlS2M`

### **InputAddr** — 输入数据内存地址信号 标量

输入数据内存地址信号，返回为 `uint32` 标量。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `uint32`

### **InputSize** — 下一个输入数据帧的大小 标量

下一个输入数据帧的大小，返回为 `uint32` 标量。输入数据帧大小以 bytes 为单位。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `uint32`

### **InputValid** — 输入数据有效信号 标量

输入数据有效信号，返回为 boolean。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### **OutputAddr** — 处理后输出数据内存地址信号 标量

处理后输出数据内存地址信号，返回为 `uint32` 标量。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `uint32`

### **OutputSize** — 下一个输出数据帧的大小信号 标量

下一个输出数据帧的大小信号，返回为 `uint32` 标量。当 `OutputValid` 信号为 on 时使用此信号。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `uint32`

### **OutputValid** — 输出数据有效信号 标量

输出数据有效信号，返回为 boolean 标量。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

### **Done** — 数据处理完成信号 标量

数据处理完成信号，返回为 boolean 标量。

#### 依赖关系

要启用此端口，请将 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置为 `"port"`。

**数据类型：** `Boolean`

## 参数

### **Network** — 网络对象的名称 `Network from MATLAB function`（默认） | `Network from MAT-FILE`

网络对象的名称，指定为以下选项之一：

- `Network from MATLAB function` — 提供返回网络对象的 MATLAB 函数的名称。
- `Network from MAT-file` — 提供存储网络对象的 MAT-file 的路径。

### **MATLAB Function** — 网络 MATLAB 函数的名称 `getDigitsNetwork`（默认）

返回网络对象的 MATLAB 函数的名称。

#### 依赖关系

要启用此参数，请将 **Network** 设置为 `Network from MATLAB function`。

### **File Path** — MAT-file 的路径 `untitled.mat`（默认）

包含网络对象的 MAT-file 的路径。

#### 依赖关系

要启用此参数，请将 **Network** 设置为 `Network from MAT-file`。

### **Activation Layer** — 网络激活层的名称 `pool10`（默认）

要仿真的网络激活层名称。默认激活层是由 **Network** 参数指定的网络对象的最后一层。

### **Maximum input frame number limit for memory access allocation** — 最大输入帧数限制 30（默认） | 正标量

用于计算 DDR 内存访问分配的最大输入帧数限制。

### 处理器配置属性

### **Import Processor Configuration from MATLAB workspace** — 启用导入现有 `dlhdl.ProcessorConfig` 对象 `dlhdl.ProcessorConfig`（默认） | `dlhdl.ProcessorConfig('Bitstream','zcu102_single')` | `dlhdl.ProcessorConfig('Bitstream','arria10soc_single')` | `dlhdl.ProcessorConfig('Bitstream','zc706_single')`

导入现有的 `dlhdl.ProcessorConfig` 对象。如果指定函数名，则它必须是 MATLAB 函数。例如，此 MATLAB 函数返回一个名为 `hPCinMATLAB` 的 `dlhdl.ProcessorConfig` 对象。

    function hPCinMATLAB = hPCinMATLAB()
    hPC = dlhdl.ProcessorConfig;
    hPC.RunTimeControl = "port";
    hPCinMATLAB = hPC;
    end

添加 MATLAB 函数名或 `dlhdl.ProcessorConfig` 对象后，点击 **Apply** 以将处理器配置或 MATLAB 配置导入到模块中。

### **Export Processor Configuration to MATLAB workspace** — 启用导出 `dlhdl.ProcessorConfig` 对象 `hPCInSimulink`（默认）

导出 `dlhdl.ProcessorConfig` 对象。默认对象名称为 `hPCInSimulink`。

#### 卷积模块

### **Module Generation** — 启用或禁用卷积模块生成 on（默认） | off

启用或禁用卷积模块生成。使用此参数控制作为深度学习处理器配置一部分的卷积模块的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **LRN Block Generation** — 启用或禁用局部响应归一化 (LRN) 块生成 off（默认） | on

启用或禁用局部响应归一化 (LRN) 块生成。使用此参数控制作为深度学习处理器配置的卷积模块一部分的 LRN 块的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Segmentation Block Generation** — 启用或禁用分割块生成 on（默认） | off

启用或禁用分割块生成。使用此参数控制作为深度学习处理器配置的卷积模块一部分的分割块的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Convolution Thread Number** — 并行卷积处理器内核线程数 16（默认） | 4 | 9 | 16 | 25 | 36 | 49 | 64

并行卷积处理器内核线程数。

此参数是 `dlhdl.ProcessorConfig` 对象中 `conv` 模块一部分的并行 3-by-3 卷积内核线程数。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Input Memory Size** — 输入内存缓存块 RAM (BRAM) 大小 只读：[227 227 3]（默认） | 3-D 正整数数组

此参数为只读。

输入内存缓存 BRAM 大小。此参数是一个 3-D 矩阵，表示 `dlhdl.ProcessorConfig` 对象中 `conv` 模块的 BRAM 所允许的最大输入图像大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Output Memory Size** — 输出内存缓存块 RAM (BRAM) 大小 [227 227 3]（默认） | 3-D 正整数数组

输出内存缓存 BRAM 大小。

此参数是一个 3-D 矩阵，表示 `dlhdl.ProcessorConfig` 对象中 `conv` 模块的 BRAM 所允许的最大输出图像大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Feature Size Limit** — 最大输入和输出特征大小 2048（默认） | 正整数

最大输入和输出特征大小。

此参数是一个正整数，表示 `dlhdl.ProcessorConfig` 对象中 `conv` 模块一部分的最大输入和输出特征大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

#### FC 模块

### **Module Generation** — 启用或禁用全连接模块生成 on（默认） | off

启用或禁用全连接模块生成。使用此参数控制作为深度学习处理器配置一部分的全连接模块的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Softmax Block Generation** — 启用或禁用 Softmax 块生成 off（默认） | on

启用或禁用 Softmax 块生成。使用此参数控制作为深度学习处理器配置的全连接模块一部分的 Softmax 块的生成。清除此参数时，Softmax 层仍以软件方式实现。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **FC Thread Number** — 并行全连接 (fc) MAC 线程数 4（默认） | 4 | 8 | 16

并行全连接 (FC) MAC 线程数。此参数是 `dlhdl.ProcessorConfig` 对象中 `fc` 模块一部分的并行 FC MAC 线程数。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Input Memory Size** — 输入内存缓存块 RAM (BRAM) 大小 25088（默认） | 无符号整数

输入内存缓存 BRAM 大小。此参数是一个无符号整数，表示 `dlhdl.ProcessorConfig` 对象中 `fc` 模块的 BRAM 所允许的输入缓存内存大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Output Memory Size** — 缓存块 RAM (BRAM) 大小 4096（默认） | 无符号整数

输出内存缓存 BRAM 大小。此参数是一个无符号整数，表示 `dlhdl.ProcessorConfig` 对象中 `fc` 模块的 BRAM 所允许的输出缓存内存大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

#### 自定义模块

### **Module Generation** — 启用或禁用自定义模块生成 on（默认） | off

启用或禁用自定义模块生成。使用此参数控制作为深度学习处理器配置一部分的加法器模块的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Addition** — 启用或禁用加法层生成 on（默认） | off

启用或禁用加法层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的加法层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Multiplication** — 启用或禁用乘法层生成 on（默认） | off

启用或禁用乘法层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的乘法层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Resize2D** — 启用或禁用 2-D resize 层生成 off（默认） | on

启用或禁用 2-D resize 层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的 2-D resize 层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Sigmoid** — 启用或禁用 sigmoid 层生成 off（默认） | on

启用或禁用 sigmoid 层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的 sigmoid 层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **TanhLayer** — 启用或禁用 `tanh` 层生成 off（默认） | on

启用或禁用 `tanh` 层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的 `tanh` 层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **MishLayer** — 启用或禁用 `mish` 层生成 off（默认） | on

启用或禁用 `mish` 层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的 `mish` 层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **SwishLayer** — 启用或禁用 `swish` 层生成 off（默认） | on

启用或禁用 `swish` 层生成。使用此参数控制作为深度学习处理器配置的自定义模块一部分的 `swish` 层的生成。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Input Memory Size** — 输入内存缓存块 RAM (BRAM) 大小 40（默认） | 无符号整数

输入内存缓存 BRAM 大小。此参数是一个无符号整数，表示 `dlhdl.ProcessorConfig` 对象中 `custom` 模块的 BRAM 所允许的输入缓存内存大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Output Memory Size** — 输出内存缓存块 RAM (BRAM) 大小 120（默认） | 无符号整数

输出内存缓存 BRAM 大小。此参数是一个无符号整数，表示 `dlhdl.ProcessorConfig` 对象中 `custom` 模块的 BRAM 所允许的输入缓存内存大小。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

#### 处理器顶层

### **Choose Processinf Mode of All Interface Signals** — 为所有深度学习处理器 IP 核接口信号选择接口类型 只读：`register`（默认） | `port`

此参数为只读。

为所有深度学习处理器 IP 核接口信号选择接口类型。指定运行时输入信号、运行时反馈信号、输入接口控制输入信号和输入接口控制反馈信号是实现为寄存器还是端口。

#### 依赖关系

要启用并编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **RunTimeControl** — 深度学习处理器 IP 核模式设置 只读：`register`（默认） | `port`

此参数为只读。

深度学习处理器 IP 核模式设置。指定深度学习处理器 IP 核的运行时输入信号是实现为寄存器还是端口。

### **RunTimeStatus** — 来自深度学习处理器 IP 核控制的反馈信号 只读：`register`（默认） | `port`

此参数为只读。

来自深度学习处理器 IP 核控制的反馈信号。指定来自深度学习处理器 IP 核的运行时输出信号是实现为寄存器还是端口。

### **InputStreamControl** — 深度学习处理器 IP 核输入接口控制 只读：`register`（默认） | `port`

此参数为只读。

深度学习处理器 IP 核输入接口控制。

### **OutputStreamControl** — 深度学习处理器 IP 核输出接口控制 只读：`register`（默认） | `port`

此参数为只读。

深度学习处理器 IP 核输出接口控制。

### **SetupControl** — 深度学习处理器 IP 核用户接口控制 只读：`register`（默认） | `port`

此参数为只读。

深度学习处理器 IP 核用户接口控制。

### **ProcessorDataType** — 深度学习处理器 IP 核模块数据类型 `single`（默认）

深度学习处理器 IP 核模块数据类型。

#### 依赖关系

要编辑此参数，请启用 **Export Processor Configuration to MATLAB Workspace**。

### **Export Deep Learning Processor IP Core Register addresses to MATLAB workspace** — 导出寄存器地址 只读：on（默认） | off

此参数为只读。

启用此选项可将包含地址位置的结构体导出到 MATLAB 工作区。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

仿真深度学习处理器 IP 核接口

Deep Learning HDL Processing System 模块仿真深度学习处理器 IP 核，并对预处理和后处理系统与深度学习处理器 IP 核之间的握手逻辑进行建模、仿真和验证。模块图标根据 `dlhdl.ProcessorConfig` 对象的 `RunTimeControl` 属性设置而变化。要在 MATLAB® 命令行访问该模块，请输入：

    open_system('dlhdllib')

| `RunTimeControl` 设置 | **模块图标** |
| --- | --- |
| `Register` | 寄存器端口 |
| `Port` | 端口输入 |
