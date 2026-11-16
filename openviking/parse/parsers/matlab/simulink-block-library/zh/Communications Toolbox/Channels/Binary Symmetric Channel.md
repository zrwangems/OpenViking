---
type: simulink-block
title: 'Binary Symmetric Channel'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Channels'
documentation_page: 'binarysymmetricchannel'
documentation_source_path: 'ref/binarysymmetricchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Binary Symmetric Channel

## 端口

### Input

### **Input** — 输入信号 列向量 | 矩阵

输入信号，指定为列向量或由 `Boolean` 值组成的 *N*S-by-*N*C 矩阵。*N*S 是每个通道的样本数。*N*C 是独立数据通道的数量。有关详细信息，请参阅提示。

### Output

### **Output** — 二进制输出信号 列向量 | 矩阵

二进制输出信号，返回为与 `Input` 具有相同维度的列向量或矩阵。输出信号是输入信号的一个版本，已根据指定的 Error probability 引入随机错误进行了修改。要设置输出数据类型，请使用 Output data type。

### **Err** — 错误位置 列向量 | 矩阵

错误位置，返回为与 `Input` 具有相同维度的列向量或矩阵。`Err` 中的元素值为 `1` 或 `0`，其中：

- `1` 表示 `Output` 中的对应元素有错误。
- `0` 表示 `Output` 中的对应元素没有错误。

`Err` 的数据类型与 Output 相同，由 Output data type 设置。

#### 依赖项

要启用此端口，请选择 Output error vector。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Error probability** — 错误发生概率 `0.05`（默认） | 标量

输入信号元素的错误发生概率，指定为范围 [0,1] 中的标量。错误概率独立应用于每个元素。

### **Output error vector** — 用于输出错误位置的选项 `on`（默认） | `off`

要为模块启用 `Err` 输出端口，请选择此参数。

### **Output data type** — 输出数据类型 `double`（默认） | `single` | `boolean`

选择输出数据类型为 `double`、`single` 或 `boolean`。此参数设置 **Output** 和 **Err** 端口的输出数据类型。

### **Initial seed** — 初始种子 `71`（默认） | integer

模块使用的随机数生成器的初始种子值，指定为整数。该模块使用 `mt19937ar` 算法生成均匀分布的随机数。有关 `mt19937ar` 算法的详细信息，请参阅创建和控制随机数流。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为：

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间。在 `Interpreted execution` 模式下，可以调试模块的源代码。

## 所属库

Communications Toolbox / Channels

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

### R2018b: 随机数生成

为了提高统计特性，Binary Symmetric Channel 模块使用带有 `RandStream` 的 `mt19937ar` 算法。Binary Symmetric Channel 模块为 Initial seed 参数接受单个标量值。

## 描述

引入二进制错误

Binary Symmetric Channel 模块对通过二进制对称信道传输的输入信号引入错误。根据指定的 Error probability 引入错误。有关详细信息，请参阅提示。
