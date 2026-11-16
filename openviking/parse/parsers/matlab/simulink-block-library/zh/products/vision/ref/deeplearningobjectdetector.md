---
type: simulink-block
title: 'Deep Learning Object Detector'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Recognition, Object Detection, and Semantic Segmentation / Object Detection'
documentation_page: 'deeplearningobjectdetector'
documentation_source_path: 'ref/deeplearningobjectdetector.html'
language: zh-CN
chinese_source: official
---

# Deep Learning Object Detector

## 端口

### 输入

### **Image** — 图像数据 数组

*H*×*W*×*C* 数值数组，其中 *H*、*W* 和 *C* 分别是图像的高度、宽度和通道数。每个时间步只允许使用一个图像作为输入。
### 输出

### **Bboxes** — 检测到的目标的位置 矩阵

在输入图像中检测到的目标的位置，以 *M*×4 或 *M*×5 矩阵形式返回。*M* 是在图像中检测到的边界框的数量。您可以通过指定**最大检测次数**参数来设置 *M* 大小的上界。

下表描述边界框的格式。

| **边界框** | ***Description*** |
| --- | --- |
| **与轴对齐的矩形** | 在空间坐标中定义为 *M*×4 数值矩阵，其行的形式为 [*x* *y* *w* *h*]，其中：  - *M* 是轴对齐矩形的数量。 - *x* 和 `y` 指定矩形的左上角。 - *w* 指定矩形的宽度，即矩形沿 *x* 轴的长度。 - *h* 指定矩形的高度，即矩形沿 *y* 轴的长度。 |
| **旋转矩形** | 在空间坐标中定义为 *M*×5 数值矩阵，其行的形式为 [*xctr* *yctr* *w* *h* *yaw*]，其中：  - *M* 是旋转矩形的数量。 - *xctr* 和 *yctr* 指定矩形的中心。 - *w* 指定矩形的宽度，即旋转前矩形沿 *x* 轴的长度。 - *h* 指定矩形的高度，即旋转前矩形沿 *y* 轴的长度。 - *yaw* 指定旋转角度（以度为单位）。围绕边界框的中心顺时针旋转。  Square rectangle rotated by -30 degrees. |

有关详细信息，请参阅Datastores for Deep Learning (Deep Learning Toolbox)。

### **Labels** — 边界框的标签 向量

边界框的标签，以 *M*×1 枚举向量形式返回。*M* 是在图像中检测到的边界框的数量。

### **Scores** — 检测分数 向量

每个标签的检测置信度分数，以 *M*×1 向量形式返回。*M* 是在图像中检测到的边界框的数量。分数越高，表示检测的置信度越高。

## 参数

### **检测器** — 经过训练的检测器对象的源 **来自 MAT 文件的检测器** (默认) | **来自 MATLAB 函数的检测器**

从以下选项中选择检测器对象的源：

- **来自 MAT 文件的检测器** - 从 MAT 文件中导入检测器对象。例如，选择一个包含 `yolov2ObjectDetector` 对象的 MAT 文件。
- **来自 MATLAB 函数的检测器** - 从 MATLAB 函数中导入检测器对象。例如，指定函数 `vehicleDetectorYOLOv2`，该函数返回一个经过训练的 `yolov2ObjectDetector` 对象。

导入的检测器必须为以下受支持的对象之一：

- `rcnnObjectDetector`
- `fastRCNNObjectDetector`
- `fasterRCNNObjectDetector`
- `rtmdetObjectDetector`
- `ssdObjectDetector`
- `yolov2ObjectDetector`
- `yolov3ObjectDetector`
- `yolov4ObjectDetector`
- `yoloxObjectDetector`

#### 编程用法

|  |
| --- |
| **模块参数：**`Detector` |
| **类型：**字符向量、字符串 |
| **值：**`Detector from MAT file'` | `'Detector from MATLAB function'` |
| **默认值：**`Detector from MAT file'` |

### **文件路径** — 包含检测器对象的 MAT 文件 **untitled.mat** (默认) | MAT 文件名

此参数指定包含要加载的检测器对象的 MAT 文件的名称。如果该文件不在 MATLAB 路径中，请使用**浏览**按钮找到该文件。

#### 依赖关系

要启用此参数，请将**检测器**参数设置为**来自 MAT 文件的检测器**。

#### 编程用法

|  |
| --- |
| **模块参数：**`DetectorFilePath` |
| **类型：**字符向量、字符串 |
| **值：**MAT 文件路径或名称 |
| **默认值：** `'untitled.mat'` |

### **MATLAB 函数** — MATLAB 函数名称 **untitled** (默认) | MATLAB 函数名称

此参数指定返回经过训练的目标检测器的 MATLAB 函数的名称。例如，指定函数 `vehicleDetectorYOLOv2`（它返回经过训练的 `yolov2ObjectDetector` 对象），或指定自定义函数。

#### 依赖关系

要启用此参数，请将**检测器**参数设置为**来自 MATLAB 函数的检测器**。

#### 编程用法

|  |
| --- |
| **模块参数：**`DetectorFunction` |
| **类型：**字符向量、字符串 |
| **值：**MATLAB 函数名称 |
| **默认值：**`'untitled'` |

### **感兴趣区域** — 搜索感兴趣区域 [*x* *y* *width* *height*] 形式的向量

将感兴趣的搜索区域指定为 [*x y width height*] 形式的向量。该向量指定区域的左上角和大小（以像素为单位）。

#### 依赖关系

要启用此参数，请选择**指定感兴趣区域**参数。

#### 编程用法

|  |
| --- |
| **模块参数：**`ROI` |
| **类型：**字符向量、字符串 |
| **值：**指定为 `'[x y width height]'` 的字符向量 |
| **默认值：**`'[1 1 100 100]'` |

### **检测阈值** — 检测阈值 [0, 1] 范围内的标量

将检测阈值指定为 [0, 1] 范围内的标量。分数低于此阈值的检测将被删除。要减少误报，请增大此值。

#### 依赖关系

要启用此参数，您必须使用支持**检测阈值**参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`Threshold` |
| **类型：**字符向量、字符串 |
| **值：**标量 |
| **默认值：**`'0.5'` |

### **最强区域的数量** — 最强区域提议的最大数量 `2000` (默认) | 正整数

将最强区域提议的最大数量指定为整数。减小此值可以加快处理速度，但会降低检测准确度。要使用所有区域提议，请将此参数指定为 `Inf`。

#### 依赖关系

要启用此参数，请使用支持**最强区域的数量**参数的检测器。例如，使用 `rcnnObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`NumStrongestRegions` |
| **类型：**字符向量、字符串 |
| **值：**整数 |
| **默认值：**`'2000'` |

### **最大区域大小** — 最大区域大小 [*height* *width*] 形式的向量

将最大区域大小指定为 [*height* *width*] 形式的向量。单位为像素。最大区域大小定义包含该对象的最大区域的大小。例如，[`50` `50`] 将包含该对象的最大区域的大小设置为 `50`×`50` 像素。要减少计算时间，请将此值设置为在输入测试图像中可检测到该对象的已知最大区域大小。

#### 依赖关系

启用以下参数

- 选择**指定最大区域大小**参数。
- 使用支持**最大区域大小**参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaxSize` |
| **类型：**字符向量、字符串 |
| **值：**指定为 `'[height width]'` 的字符向量 |
| **默认值：**`'[50 50]'` |

### **最小区域大小** — 最小区域大小 [*height* *width*] 形式的向量

将最小区域大小指定为 [*height* *width*] 形式的向量。单位为像素。最小区域大小定义包含该对象的最小区域的大小。例如，[`1` `1`] 将包含该对象的最小区域的大小设置为 `1`×`1` 像素。

#### 依赖关系

启用以下参数

- 选择**指定最小区域大小**参数。
- 使用支持**最小区域大小**参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：**`MinSize` |
| **类型：**字符向量、字符串 |
| **值：**指定为 `'[height width]'` 的字符向量 |
| **默认值：**`'[1 1]'` |

### **最大检测次数** — 最大检测次数 `500` (默认) | 正整数

将最大检测次数指定为正整数。此值是检测次数的上界，必须大于或等于 2。

#### 编程用法

|  |
| --- |
| **模块参数：**`MaxDetections` |
| **类型：**字符向量、字符串 |
| **值：**整数 |
| **默认值：**`'500'` |

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

用法说明和限制：

- **配置参数** > **代码生成**常规类别中的**语言**参数必须设置为 **C++**。
- 有关代码生成支持的网络和层的列表，请参阅代码生成支持的网络和层 (MATLAB Coder)。
- 要使用 YOLOv3、YOLOv4 或 RTMDet 作为目标检测器为深度神经网络 (MKL-DNN) 目标库的数学核心函数库生成代码，请将 `MaxStackSize` 和 `TLCOptions` 模型参数设置为较高的值。例如，您可以使用以下语法将 `MaxStackSize` 和 `TLCOptions` 参数值设置为 '`inf`'。

  ```
  >> set_param(modelName,'MaxStackSize','inf')
  >> set_param(modelName,'TLCOptions','-aMaxStackVariableSize=inf')
  ```

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

用法说明和限制：

- **配置参数** > **代码生成**常规类别中的**语言**参数必须设置为 **C++**。
- 有关 CUDA® 代码生成支持的网络和层的列表，请参阅Supported Networks, Layers, and Classes (GPU Coder)。

## 版本历史

**在 R2021b 中推出**

### R2024b: 支持 RTMDet 目标检测器

从 R2024b 开始，`Deep Learning Object Detector` 模块支持目标检测的实时模型 (RTMDet)。您可以导入预训练的 RTMDet 目标检测器对象 `rtmdetObjectDetector` 来执行目标检测。

### R2024b: 支持 YOLOX 目标检测器

从 R2024b 开始，`Deep Learning Object Detector` 模块支持 You Only Look Once X (YOLOX) 目标检测。您可以导入预训练的 YOLOX 目标检测器对象 `yoloxObjectDetector` 来执行目标检测。

## 描述

使用经过训练的深度学习目标检测器检测目标

Deep Learning Object Detector 模块使用通过模块参数指定的经过训练的目标检测器来预测输入图像的边界框、类标签和分数。此模块允许从 MAT 文件或使用 MATLAB® 函数将预训练目标检测器加载到 Simulink® 模型中。此模块为使用 Simulink 中的检测器对象提供图形界面。要启用 Deep Learning Object Detector 模块的某些参数，您必须选择支持这些参数的目标检测器。例如，将 `yolov2ObjectDetector` 对象与此模块结合使用，您可以选择与关联的 `detect` 对象函数的名称-值参量类似的参数。
