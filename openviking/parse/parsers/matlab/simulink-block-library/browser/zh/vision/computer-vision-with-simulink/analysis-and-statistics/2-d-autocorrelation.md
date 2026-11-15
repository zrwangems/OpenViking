---
type: simulink-block
title: '2-D Autocorrelation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Analysis and Statistics'
documentation_page: '2dautocorrelation'
documentation_source_path: 'ref/2dautocorrelation.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Autocorrelation

## 端口

### 输入

### **Port\_1** — 输入数组 向量 | 矩阵

输入数组，指定为向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes
### 输出

### **Port\_1** — 输入向量 | 矩阵的自相关

输入数组的自相关，以向量或矩阵形式返回。输出的数据类型与输入的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** Yes

## 参数

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

输入矩阵的二维自相关

2-D Autocorrelation 模块计算输入向量或矩阵的二维自相关。
