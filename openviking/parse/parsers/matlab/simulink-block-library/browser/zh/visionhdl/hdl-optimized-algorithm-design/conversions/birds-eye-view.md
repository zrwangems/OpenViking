---
type: simulink-block
title: 'Birds-Eye View'
family: 'visionhdl'
product_id: 'visionhdl'
product_name: 'Vision HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Algorithm Design / Conversions'
documentation_page: 'birdseyeview'
documentation_source_path: 'ref/birdseyeview.html'
language: zh-CN
chinese_source: worker-translation
---

# Birds-Eye View

## 端口

### 输入

### **pixel** — 输入像素流标量

像素流中的单个图像像素，指定为表示灰度强度的标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`
### 输出

### **pixel** — 输出像素流标量

像素流中的单个图像像素，以表示灰度强度的标量形式返回。输出像素数据类型与输入像素数据类型相同。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `uint` | `int` | `fixed point` | `Boolean` | `double` | `single`

### **ctrl** — 与像素流 `pixelcontrol` 总线关联的控制信号

`pixelcontrol` 总线包含五个信号。这些信号描述像素的有效性及其在帧中的位置。有关详细信息，请参阅 Pixel Control Bus。

**数据类型：** `bus`

## 参数

### **单应性矩阵** — 从相机参数导出的传递函数 `[0.000100990123328 0 0;0.000412396945637 0.001302203393162 1.293171994e-06;-0.103019798961327 -0.255811259450009 -0.000222053779501]` (默认值) | 3×3 矩阵

从相机参数导出的传递函数，指定为 3×3 矩阵。

单应性矩阵 *h* 从物理相机设置的四个固有参数导出：焦距、俯仰、高度和主点（来自针孔相机模型）。默认值是 Lane Detection 示例中使用的相机设置的矩阵。

此矩阵可以根据物理相机属性计算，或通过分析相机拍摄的网格测试图案图像经验推导得出。请参阅 `estimateGeometricTransform` (Computer Vision Toolbox) 或 Using the Single Camera Calibrator App (Computer Vision Toolbox)。

### **最大缓冲区大小，以 pixels 为单位** — 要缓冲的输入像素数 `40000` (默认值) | integer

要缓冲的输入像素数，指定为 integer。根据 **要缓冲的输入行数** × *ActivePixelsPerLine* 计算此值。该模块使用此大小的存储器存储输入像素。如果指定的值不是 2 的幂，则该模块使用下一个更大的 2 的幂。

### **要缓冲的输入行数** — 要变换的行数 `54` (默认值) | integer

要变换的行数，指定为 integer。该模块从由 **单应性矩阵** 确定的消失点开始，存储此数量的行并将其变换为输出鸟瞰图图像。

存储完整输入帧会使用过多内存，以致无法在没有片外存储的情况下实现该算法。因此，对于硬件实现，请选择要存储和变换的较小区域，该区域生成可接受的输出帧大小。

例如，使用默认 **单应性矩阵** 和 640×480 pixels 的输入图像时，全尺寸变换会生成 900×640 的输出图像。对输入到输出 *x* 坐标映射的分析表明，生成鸟瞰图输出图像的前 700 行大约需要输入图像的 50 行。此数量的输入行可以使用片上存储器存储。默认相机设置的消失点大约在第 200 行，该点以上的行不会对生成的鸟瞰图产生影响。因此，该模块可以仅存储输入行 200–250 用于变换。

### **输出有效像素** — 输出帧的水平大小 `640` (默认值) | integer

输出帧的水平大小，指定为 integer。此参数是每个输出行中的有效像素数。

### **输出有效行** — 输出帧的垂直大小 `700` (默认值) | integer

输出帧的垂直大小，指定为 integer。此参数是每个输出帧中的有效行数。

## 所属库

Vision HDL Toolbox / Geometric Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持 Simulink® 加速器和快速加速器模式下的 C/C++ 代码生成，以及 DPI 组件生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

将前视相机图像变换为俯视图

Birds-Eye View 模块将前视相机图像扭曲为俯视图。它使用支持 HDL 代码生成的硬件高效架构。

必须提供描述该变换的单应性矩阵。此矩阵可以根据物理相机属性计算，或通过分析相机拍摄的网格图案图像经验推导得出。该模块使用此矩阵计算每个像素的变换后坐标。该变换不会在像素位置之间进行插值。而是将结果舍入到最近坐标。

该模块对输入图像中消失点下方的梯形区域进行操作。这些图像显示了为变换选择的输入区域以及得到的俯视图。

可以指定变换区域中的行数以及输出帧的大小。如果指定的单应性矩阵无法从请求的行数映射到请求的输出大小，则该模块会返回警告。

由于该模块会复制输入区域中的行以创建更大的输出帧，因此它无法在下一帧到达之前完成一帧的变换。该模块在仍在变换上一帧时会忽略任何新的输入帧。因此，根据存储的行数和输出大小，该模块可能会丢弃输入帧。此计时还使该模块能够保持输入像素流的消隐间隔。
