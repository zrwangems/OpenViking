---
type: simulink-block
title: 'IDWT'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Transforms'
documentation_page: 'idwt'
documentation_source_path: 'ref/idwt.html'
language: zh-CN
chinese_source: worker-translation
---

# IDWT

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

DSP System Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入执行离散小波逆变换（IDWT），或从具有较小带宽和较慢采样率的子带重建信号

您可以配置此模块来计算离散小波逆变换（IDWT），或从具有较小带宽和较慢采样率的子带重建信号。当该模块计算输入的离散小波逆变换（IDWT）时，输出与输入具有相同的维度。输出的每一列都是对应输入列的 IDWT。重建信号时，该模块使用一系列高通和低通 FIR 滤波器从输入子带重建信号，如多级滤波器组（Asymmetric 型）中所示。重建后的信号比输入子带具有更宽的带宽和更快的采样率。

您可以通过提供滤波器系数向量来指定滤波器组的高通和低通滤波器。您可以直接在模块对话框中执行此操作。如果您拥有 Wavelet Toolbox™ 许可证，可以通过从 **Filter** 参数中选择小波来指定基于小波的滤波器。您必须将滤波器组结构设置为 asymmetric 或 symmetric，并指定滤波器组中的级数。

**注意**

IDWT 模块与 Dyadic Synthesis Filter Bank 模块相同，只是默认设置不同。有关模块端口和参数的详细信息，请参阅 Dyadic Synthesis Filter Bank 模块参考页。
