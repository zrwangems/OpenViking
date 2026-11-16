---
type: simulink-block
title: 'DWT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'dwt'
documentation_source_path: 'ref/dwt.html'
language: zh-CN
chinese_source: official
---

# DWT

## 端口

R2025b 官方文档未提供。

## 参数

R2025b 官方文档未提供。

## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成代码在某些条件下依赖 `memcpy` 或 `memset` 函数 (`string.h`)。

## 版本历史

**在 R2006a 之前推出**

## 描述

计算输入的离散小波变换 (DWT) 或将信号分解为具有较小带宽和较慢采样率的子带

您可以配置此模块来计算输入信号的离散小波变换 (DWT) 或将信号分解为具有较小带宽和较慢采样率的子带。该模块使用一系列高通和低通 FIR 滤波器反复划分输入频率范围，如Multilevel Filter Banks中所示（不对称型）。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块封装上执行此操作。如果您有 Wavelet Toolbox™ 许可证，您可以通过从**滤波器**参数选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为不对称或对称，并指定滤波器组中的级数。

对于相同的输入，此模块的 DWT 配置不会产生与 Wavelet Toolbox `dwt` 函数相同的结果。由于 DSP System Toolbox™ 是为实时实现而设计的，Wavelet Toolbox 是为分析而设计的，因此产品处理边界条件和滤波器状态的方式不同。要使 `dwt` 函数的输出与此模块的 DWT 输出匹配，请完成以下步骤：

1. 将 `dwt` 函数的边界条件设置为零填充。为此，请在 MATLAB® 命令行中键入 `dwtmode('zpd')`。
2. 为了匹配模块（使用 FIR 滤波器实现）的延迟，向 `dwt` 函数的输入添加零。您添加的零的数量必须等于滤波器长度的一半。

**注意**

DWT 模块与 Dyadic Analysis Filter Bank 模块相同，只是默认设置不同。有关模块端口和参数的详细信息，请参阅 Dyadic Analysis Filter Bank 模块参考页。
