---
type: simulink-block
title: 'Block Matching'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Tracking and Motion Estimation'
documentation_page: 'blockmatching'
documentation_source_path: 'ref/blockmatching.html'
language: zh-CN
chinese_source: worker-translation
---

# Block Matching

## 端口

### 输入

### **I/I1** — 图像或视频帧 标量 | 向量 | 矩阵

图像或视频帧，指定为标量、向量或矩阵。如果 Estimate motion between 参数设置为 Two images，则此端口的名称将变为 **I1**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **I2** — 图像或视频帧 标量 | 向量 | 矩阵

图像或视频帧，指定为标量、向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Estimate motion between** 参数设置为 `Two images`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **|V|^2** — 速度幅值 标量 | 向量 | 矩阵

速度幅值，以标量、向量或矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **V** — 复数形式的速度分量 标量 | 向量 | 矩阵

复数形式的速度分量，以标量、向量或矩阵形式返回。

#### 依赖关系

要显示此端口，请将 **Velocity output** 参数设置为 `Horizontal and vertical components in complex form`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

**主选项卡**

### **Estimate motion between** — 在图像或帧之间估计运动 `Current frame and N-th frame back`（默认）| `Two images`

指定是在两个图像还是两个视频帧之间估计运动。选择 `Two images` 以估计两个图像之间的运动。选择 `Current frame and N-th frame back` 以估计相隔 N 帧的两个视频帧之间的运动。

#### 依赖关系

将此参数设置为 `Current frame and N-th frame back` 以显示 **N** 参数。

### **N** — 帧数 `1`（默认）| 标量

指定一个标量值，表示参考帧与当前帧之间的帧数。

#### 依赖关系

要启用此参数，请将 **Estimate motion between** 参数设置为 `Current frame and N-th frame back`。

### **Search method** — 块匹配搜索方法 `Exhaustive`（默认）| `Three-step`

指定该模块如何在当前帧和下一帧中定位与像素块最匹配的像素块。

- `Exhaustive` — 该模块通过一次将像素块在搜索区域上移动一个像素，来选择下一帧中像素块的位置。此过程的计算成本很高。
- `Three-step` — 该模块通过使用逐步减小的步长来搜索下一帧中与当前帧中像素块最匹配的像素块。该模块从约等于最大搜索范围一半的步长开始。在每一步中，该模块将搜索区域的中心点与位于区域边界上的八个搜索点进行比较，并将中心点移动到其值最接近中心点值的搜索点。然后该模块将步长减小一半，并再次开始该过程。此选项的计算成本较低，但可能找不到最优解。

### **Block matching criteria** — 块匹配准则 `Mean square error (MSE)`（默认）| `Mean absolute difference (MAD)`

指定该模块如何衡量当前帧中的像素块与下一帧中的像素块的相似性。

如果选择 `Mean square error (MSE)`，则该模块将像素块中心像素的位移估计为使此 MSE 方程最小化的 (d1,d2) 值：

MSE(d1,d2)=1N1×N2∑(n1,n2),∑∈B[s(n1,n2,k)−s(n1+d1,n2+d2,k+1)]2

在前面的方程中，*B* 是 N1×N2 像素块，*s*(*x,y,k*) 表示帧 *k* 中 (*x,y*) 处的像素位置。

如果选择 `Mean absolute difference (MAD)`，则 Block Matching 模块将像素块中心像素的位移估计为使此 MAD 方程最小化的 (d1,d2) 值：

MAD(d1,d2)=1N1×N2∑(n1,n2),∑∈B|s(n1,n2,k)−s(n1+d1,n2+d2,k+1)|

### **Block size [height width]** — 块大小 `[17 17]`（默认）| 二元素向量

指定像素块的大小。

### **Overlap size [r c]** — 块重叠 `[0 0]`（默认）| 二元素向量

指定输入图像的两个子区域的重叠（以像素为单位）。

### **Maximum displacement [r c]** — 最大位移 `[7 7]`（默认）| 二元素向量

指定像素块中任何中心像素在图像之间或帧之间可能移动的最大像素数。该模块使用此值来确定搜索区域的大小。

### **Velocity output** — 速度输出 `Magnitude-squared`（默认）| `Horizontal and vertical components in complex form`

指定输出。如果选择 `Magnitude-squared`，则该模块输出一个光流矩阵，其中每个元素的形式为 *u2+v2*。如果选择 `Horizontal and vertical components in complex form`，则该模块输出一个光流矩阵，其中每个元素的形式为 u+jv。每个值的实部是水平速度分量，每个值的虚部是垂直速度分量。

**数据类型选项卡**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

估计图像或视频帧之间的运动

Block Matching 模块通过比较像素块来估计两个图像或两个视频帧之间的运动。该模块通过将像素块在搜索区域上移动来匹配帧之间的像素块。
