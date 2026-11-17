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
```yaml
ports:
- name: Image
  summary: 输入视频矩阵 | 3 维数组 | 4 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: R
  summary: 红色通道 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: G
  summary: 绿色通道 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: B
  summary: 蓝色通道 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **Image** — 输入视频矩阵 | 3 维数组 | 4 维数组

输入图像或视频，指定为矩阵、`3` 维数组或 `4` 维数组。信号类型决定输入的维度。输入以 *M*、*N*、*C* 和 *T* 来定义。*M* 和 *N* 分别是信号中的行数和列数。*C* 是信号中的颜色通道数，*T* 是帧数。

**输入 - 输出**

| 信号类型 | 输入维度 | 输出维度 |
| --- | --- | --- |
| 灰度图像 | *M*×*N* | *M*×*N*×2 |
| 彩色图像 | *M*×*N*×3 | *M*×*N*×3×2 |
| 灰度视频 | *M*×*N*×*T* | *M*×*N*×*T* |
| 彩色视频 | *M*×*N*×3×*T* | *M*×*N*×3×*T* |

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 红色通道 标量 | 向量 | 矩阵

输入图像或视频的红色通道，指定为标量、向量或矩阵。

**注意**

端口标签可以使用 `Input port labels` 参数更改。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为大于或等于 `2` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 绿色通道 标量 | 向量 | 矩阵

输入图像或视频的绿色通道，指定为标量、向量或矩阵。

**注意**

端口标签可以使用 `Input port labels` 参数更改。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为大于或等于 `2` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 蓝色通道 标量 | 向量 | 矩阵

输入图像或视频的蓝色分量，指定为标量、向量或矩阵。

**注意**

端口标签可以使用 `Input port labels` 参数更改。

#### 依赖

要启用此端口，请将 **Number of inputs** 参数设置为等于 `3` 的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Variable name
  summary: MATLAB 工作区变量名称 vout（默认）| 有效的 MATLAB 变量名称
  group: ''
- name: Number of inputs
  summary: 输入端口数量 1（默认）| 正整数
  group: ''
- name: Limit data points to last
  summary: 要导出的最大帧数 10（默认）| 正整数
  group: ''
- name: Decimation
  summary: 对视频信号进行下采样 1（默认）| 正整数
  group: ''
- name: Log fixed-point data as a fi object
  summary: 创建定点数值对象 off（默认）| on
  group: ''
- name: Input port labels
  summary: 输入端口名称 R|G|B（默认）
  group: ''
```

### **Variable name** — MATLAB 工作区变量名称 `vout`（默认）| 有效的 MATLAB 变量名称

指定导出的图像或视频的 MATLAB 工作区变量名称。

### **Number of inputs** — 输入端口数量 `1`（默认）| 正整数

指定模块的输入数量。要分离 RBG 图像或视频中的颜色通道，请指定通道数。如果是灰度视频，请输入 1。如果是彩色（R、G、B）视频，请输入 3。

### **Limit data points to last** — 要导出的最大帧数 `10`（默认）| 正整数

指定要导出到 MATLAB 工作区的最大帧数。

### **Decimation** — 对视频信号进行下采样 `1`（默认）| 正整数

输入用于对图像或视频进行下采样的抽取因子。

### **Log fixed-point data as a fi object** — 创建定点数值对象 `off`（默认）| `on`

当输入信号具有定点数据类型时，选择 **Log fixed-point data as a fi object** 以在 MATLAB 工作区中创建 fi 对象。有关 `fi` 对象的详细信息，请参阅 `fi` (Fixed-Point Designer)。

### **Input port labels** — 输入端口名称 `R|G|B`（默认）

使用竖线字符作为分隔符来命名输入端口。

#### 依赖

要启用此参数，请将 **Number of inputs** 参数设置为大于 `1` 的值。
## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

将图像或视频导出到 MATLAB 工作区

Video To Workspace 模块将图像或视频导出到 MATLAB® 工作区。它接受矩阵、3 维数组、4 维数组形式的图像或视频，并将其转换为 3 维或 4 维数组。输入大小决定输出大小。

- *M*×*N*，模块将其导出为 *M*×*N*×2 数组。*M* 和 *N* 分别是图像帧中的行数和列数，2 是图像中的帧数。
- *M*×*N*×3，模块将其导出为 *M*×*N*×3×2 数组。*M* 和 *N* 是图像或视频帧中的行数和列数，3 是颜色通道数，2 是视频中的帧数。
- *M*×*N*×3×*T*，模块将其导出为 *M*×*N*×3×*T* 数组。*M* 和 *N* 是视频帧中的行数和列数，3 表示颜色通道数，*T* 是视频中的帧数。

**注意**

- Simulink® Coder™ 不会为此模块生成代码。
- 该模块支持灰度图像和彩色图像，它们被导出到 MATLAB 工作区时会带有一个表示帧数的额外维度。图像始终以帧值 2 导出。
