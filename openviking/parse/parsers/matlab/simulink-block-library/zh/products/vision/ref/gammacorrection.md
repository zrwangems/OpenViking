---
type: simulink-block
title: 'Gamma Correction'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Color Space Formatting and Conversions'
documentation_page: 'gammacorrection'
documentation_source_path: 'ref/gammacorrection.html'
language: zh-CN
chinese_source: worker-translation
---

# Gamma Correction

## 端口

### 输入

### **I** — 输入图像矩阵 | 数组

输入图像，指定为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是输入图像中的颜色通道数。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `Gamma`。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **I'** — 伽马校正后的输入图像矩阵 | 数组

伽马校正后的输入图像，指定为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是输入图像中的颜色通道数。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `De-gamma`。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### 输出

### **I'** — 伽马校正后的输出图像矩阵 | 数组

伽马校正后的输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是颜色通道数。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `Gamma`。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **I** — 移除伽马校正后的输出图像矩阵 | 数组

移除伽马校正后的输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*C* 数组，其中 *C* 是颜色通道数。

#### 依赖关系

要启用此端口，请将 **Operation** 参数设置为 `De-gamma`。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

## 参数

### **Operation** — 模块操作 `Gamma`（默认）| `De-gamma`

指定模块执行的伽马操作。

- `Gamma` — 对输入图像应用伽马校正。
- `De-gamma` — 从输入图像移除伽马校正。

### **Gamma** — 伽马值 `2.2`（默认）| 标量

将伽马指定为大于或等于 1 的值。小于 1 的值对图像中的亮度值进行编码，大于 1 的值对图像中的亮度值进行解码，分别表示为伽马压缩和伽马扩展。

### **Linear segment** — 线性段 `on`（默认）| `off`

选择此参数可将伽马曲线定义为原点附近的线性段。有关详细信息，请参阅 Gamma Correction Method。

### **Break point** — 断点值 `0.018`（默认）| 标量

指定标量断点值，该值表示伽马曲线线性段末端处的 *I* 轴值。有关详细信息，请参阅 Gamma Correction Method。

#### 依赖关系

要启用此参数，请选择 **Linear segment** 参数。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed pointa` | `integera` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 支持字长小于或等于 16 bits。 | |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对图像或视频流应用或移除伽马校正

Gamma Correction 模块对图像或视频流应用或移除伽马校正。
