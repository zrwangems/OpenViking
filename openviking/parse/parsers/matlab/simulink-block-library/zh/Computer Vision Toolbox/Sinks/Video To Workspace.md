---
type: simulink-block
title: 'Video To Workspace'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'videotoworkspace'
documentation_source_path: 'ref/videotoworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Video To Workspace

## 端口

### 输入

### **Image** — 输入视频矩阵 | 3-D 数组 | 4-D 数组

输入图像或视频，指定为矩阵、`3`-D 数组或 `4`-D 数组。信号类型决定输入的维度。输入根据 *M*、*N*、*C* 和 *T* 定义。*M* 和 *N* 分别是信号中的行数和列数。*C* 是信号中的颜色通道数，*T* 是帧数。

**输入 - 输出**

| 信号类型 | 输入维度 | 输出维度 |
| --- | --- | --- |
| 灰度图像 | *M*-by-*N* | *M*-by-*N*-by-2 |
| 彩色图像 | *M*-by-*N*-by-3 | *M*-by-*N*-by-3-by-2 |
| 灰度视频 | *M*-by-*N*-by-*T* | *M*-by-*N*-by-*T* |
| 彩色视频 | *M*-by-*N*-by-3-by-*T* | *M*-by-*N*-by-3-by-*T* |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 红色通道标量 | 向量 | 矩阵

输入图像或视频的红色通道，指定为标量、向量或矩阵。

**注意**

端口标签可使用 `Input port labels` 参数更改。

#### 依赖项

要启用此端口，请将 **输入数目** 参数设置为大于或等于 `2` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 绿色通道标量 | 向量 | 矩阵

输入图像或视频的绿色通道，指定为标量、向量或矩阵。

**注意**

端口标签可使用 `Input port labels` 参数更改。

#### 依赖项

要启用此端口，请将 **输入数目** 参数设置为大于或等于 `2` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 蓝色通道标量 | 向量 | 矩阵

输入图像或视频的蓝色分量，指定为标量、向量或矩阵。

**注意**

端口标签可使用 `Input port labels` 参数更改。

#### 依赖项

要启用此端口，请将 **输入数目** 参数设置为等于 `3` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **变量名称** — MATLAB 工作区变量名称 `vout`（默认） | 有效的 MATLAB 变量名称

为导出的图像或视频指定 MATLAB 工作区变量名称。

### **输入数目** — 输入端口数 `1`（默认） | 正整数

指定模块的输入数目。要分离 RBG 图像或视频中的颜色通道，请指定通道数。如果是灰度视频，请输入 1。如果是彩色 (R, G, B) 视频，请输入 3。

### **将数据点限制为最后** — 要导出的最大帧数 `10`（默认） | 正整数

指定要导出到 MATLAB 工作区的最大帧数。

### **抽取** — 对视频信号进行下采样 `1`（默认） | 正整数

输入用于对图像或视频进行下采样的抽取因子。

### **将定点数据记录为 fi 对象** — 创建定点数值对象 `off`（默认） | `on`

选择 **将定点数据记录为 fi 对象**，以在输入信号具有 fixed point 数据类型时在 MATLAB 工作区中创建 fi 对象。有关 `fi` 对象的更多信息，请参阅 `fi` (Fixed-Point Designer)。

### **输入端口标签** — 输入端口名称 `R|G|B`（默认）

使用竖线字符作为分隔符来命名输入端口。

#### 依赖项

要启用此参数，请将 **输入数目** 参数设置为大于 `1` 的值。

## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**R2006a 之前引入**

## 描述

将图像或视频导出到 MATLAB 工作区

Video To Workspace 模块将图像或视频导出到 MATLAB® 工作区。它接受矩阵、3-D 数组、4-D 数组形式的图像或视频，并将它们转换为 3-D 或 4-D 数组。输入大小决定输出大小。

- *M*-by-*N* 时，模块将其导出为
  *M*-by-*N*-by-2 数组。*M* 和 *N* 分别是图像帧中的行数和列数，2 是图像中的帧数。
- *M*-by-*N*-by-3 时，模块将其导出为
  *M*-by-*N*-by-3-by-2 数组。*M* 和 *N* 是图像或视频帧中的行数和列数，3 是颜色通道数，2 是视频中的帧数。
- *M*-by-*N*-by-3-by-*T* 时，模块将其导出为
  *M*-by-*N*-by-3-by-*T* 数组。*M* 和 *N* 是视频帧中的行数和列数，3 表示颜色通道数，*T* 是视频中的帧数。

**注意**

- Simulink® Coder™ 不为该模块生成代码。
- 该模块支持灰度图像和彩色图像，这些图像导出到
  MATLAB 工作区时会带有一个表示帧数的额外维度。图像始终以帧值 2 导出。
