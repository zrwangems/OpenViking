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
chinese_source: worker-translation
---

# Deep Learning Object Detector

## 端口

### 输入

### **Image** — 图像数据数组

一个 *H*-by-*W*-by-*C* 数值数组，其中 *H*、*W* 和 *C* 分别是图像的高度、宽度和通道数。每个时间步仅允许输入一幅图像。
### 输出

### **Bboxes** — 检测到的对象位置矩阵

输入图像中检测到的对象位置，返回为 *M*-by-4 或 *M*-by-5 矩阵。
*M* 是图像中检测到的边界框数量。可以通过指定
**Maximum Number of Detections** 参数来为大小 *M* 设置上限。

下表描述边界框的格式。

| **边界框** | ***描述*** |
| --- | --- |
| **轴对齐矩形** | 在空间坐标中定义为 *M*-by-4 数值矩阵，行形式为 [*x* *y* *w* *h*]，其中：  - *M* 是轴对齐矩形的数量。 - *x* 和 `y` 指定矩形的左上角。 - *w* 指定矩形的宽度，即其沿 *x* 轴的长度。 - *h* 指定矩形的高度，即其沿 *y* 轴的长度。 |
| **旋转矩形** | 在空间坐标中定义为 *M*-by-5 数值矩阵，行形式为 [*xctr* *yctr* *w* *h* *yaw*]，其中：  - *M* 是旋转矩形的数量。 - *xctr* 和 *yctr* 指定矩形的中心。 - *w* 指定矩形的宽度，即旋转前其沿 *x* 轴的长度。 - *h* 指定矩形的高度，即旋转前其沿 *y* 轴的长度。 - *yaw* 指定旋转角度，以 degrees 为单位。旋转以边界框中心为基准，顺时针为正。 正方形矩形旋转 -30 degrees。 |

有关详细信息，请参阅 Datastores for Deep Learning (Deep Learning Toolbox)。

### **Labels** — 边界框的标签向量

边界框的标签，返回为 *M*-by-1 枚举向量。*M* 是图像中检测到的边界框数量。

### **Scores** — 检测分数向量

每个标签的检测置信度分数，返回为
*M*-by-1 向量。*M* 是图像中检测到的边界框数量。分数越高表示对检测的置信度越高。

## 参数

### **Detector** — 训练好的检测器对象的来源 `Detector from MAT file` (默认) | `Detector from MATLAB function`

从以下选项中选择检测器对象的来源：

- `Detector from MAT file` — 从 MAT 文件导入检测器对象。例如，选择包含 `yolov2ObjectDetector` 对象的 MAT 文件。
- `Detector from MATLAB function` — 从 MATLAB 函数导入检测器对象。例如，指定函数 `vehicleDetectorYOLOv2`，该函数返回训练好的 `yolov2ObjectDetector` 对象。

导入的检测器必须是以下受支持对象之一：

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
| **模块参数：** `Detector` |
| **类型：** character vector, string |
| **值：** `Detector from MAT file'` | `'Detector from MATLAB function'` |
| **默认：** `Detector from MAT file'` |

### **File path** — 包含检测器对象的 MAT 文件 `untitled.mat` (默认) | MAT 文件名

此参数指定包含要加载的检测器对象的 MAT 文件的名称。如果文件不在 MATLAB 路径上，请使用 **Browse** 按钮定位该文件。

#### 依赖关系

要启用此参数，请将 **Detector** 参数设置为 `Detector from MAT file`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DetectorFilePath` |
| **类型：** character vector, string |
| **值：** MAT 文件路径或名称 |
| **默认：** `'untitled.mat'` |

### **MATLAB function** — MATLAB 函数名称 `untitled` (默认) | MATLAB 函数名称

此参数指定返回训练好的对象检测器的 MATLAB 函数的名称。例如，指定函数 `vehicleDetectorYOLOv2`，该函数返回训练好的 `yolov2ObjectDetector` 对象，或者指定自定义函数。

#### 依赖关系

要启用此参数，请将 **Detector** 参数设置为 `Detector from MATLAB function`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DetectorFunction` |
| **类型：** character vector, string |
| **值：** MATLAB 函数名称 |
| **默认：** `'untitled'` |

### **Region of interest** — 搜索感兴趣区域，形式为 [*x* *y* *width* *height*] 的向量

将搜索感兴趣区域指定为形式 [*x y width height*] 的向量。该向量指定以 pixels 为单位的区域的左上角位置和大小。

#### 依赖关系

要启用此参数，请选择 **Specify region of interest** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `ROI` |
| **类型：** character vector, string |
| **值：** character vector，指定为 `'[x y width height]'` |
| **默认：** `'[1 1 100 100]'` |

### **Detection threshold** — 检测阈值，范围为 [0, 1] 的标量

将检测阈值指定为范围 [0, 1] 内的标量。分数低于此阈值值的检测将被移除。要减少误报，请增大此值。

#### 依赖关系

要启用此参数，必须使用支持 **Detection threshold** 参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `Threshold` |
| **类型：** character vector, string |
| **值：** 标量 |
| **默认：** `'0.5'` |

### **Number of Strongest Regions** — 最强区域提议的最大数量 `2000` (默认) | 正整数

将最强区域提议的最大数量指定为整数。减小此值可加快处理速度，但会以检测精度为代价。要使用所有区域提议，请将此参数指定为 `Inf`。

#### 依赖关系

要启用此参数，请使用支持 **Number of Strongest Regions** 参数的检测器。例如，使用 `rcnnObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `NumStrongestRegions` |
| **类型：** character vector, string |
| **值：** 整数 |
| **默认：** `'2000'` |

### **Maximum Region Size** — 最大区域大小，形式为 [*height* *width*] 的向量

将最大区域大小指定为形式 [*height* *width*] 的向量。单位是 pixels。最大区域大小定义包含对象的最大区域的尺寸。例如，[`50`
`50`] 将包含对象的最大区域大小设置为 `50`-by-`50` pixels。为减少计算时间，请将此值设置为输入测试图像中可检测对象的已知最大区域大小。

#### 依赖关系

要启用此参数

- 选择 **Specify maximum region size** 参数。
- 使用支持 **Maximum Region Size** 参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxSize` |
| **类型：** character vector, string |
| **值：** character vector，指定为 `'[height width]'` |
| **默认：** `'[50 50]'` |

### **Minimum Region Size** — 最小区域大小，形式为 [*height* *width*] 的向量

将最小区域大小指定为形式 [*height* *width*] 的向量。单位是 pixels。最小区域大小定义包含对象的最小区域的尺寸。例如，[`1`
`1`] 将包含对象的最小区域大小设置为 `1`-by-`1` pixels。

#### 依赖关系

要启用此参数

- 选择 **Specify minimum region size** 参数。
- 使用支持 **Minimum Region Size** 参数的检测器。例如，使用 `yolov2ObjectDetector` 对象。

#### 编程用法

|  |
| --- |
| **模块参数：** `MinSize` |
| **类型：** character vector, string |
| **值：** character vector，指定为 `'[height width]'` |
| **默认：** `'[1 1]'` |

### **Maximum Number of Detections** — 检测的最大数量 `500` (默认) | 正整数

将检测的最大数量指定为正整数。此值是检测数量的上限，且必须大于或等于 2。

#### 编程用法

|  |
| --- |
| **模块参数：** `MaxDetections` |
| **类型：** character vector, string |
| **值：** 整数 |
| **默认：** `'500'` |

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- **Configuration Parameters** > **Code Generation** 常规类别中的 **Language** 参数必须设置为 `C++`。
- 有关代码生成支持的网络和层列表，请参阅 Networks and Layers Supported for Code Generation (MATLAB Coder)。
- 要为以 YOLOv3、YOLOv4 或 RTMDet 作为对象检测器的 Math Kernel Library for Deep Neural Networks (MKL-DNN) 目标库生成代码，请将 `MaxStackSize` 和 `TLCOptions` 模型参数设置为更高的值。例如，可以使用以下语法将 `MaxStackSize` 和 `TLCOptions` 参数值设置为 '`inf`'。

        >> set_param(modelName,'MaxStackSize','inf')
        >> set_param(modelName,'TLCOptions','-aMaxStackVariableSize=inf')

### GPU 代码生成 使用 GPU Coder™ 为 NVIDIA® GPU 生成 CUDA® 代码。

使用说明和限制：

- **Configuration Parameters** > **Code Generation** 常规类别中的 **Language** 参数必须设置为 `C++`。
- 有关 CUDA® 代码生成支持的网络、层和类列表，请参阅 Supported Networks, Layers, and Classes (GPU Coder)。

## 版本历史

**在 R2021b 中引入**

### R2024b：支持 RTMDet 对象检测器

从 R2024b 开始，`Deep Learning Object Detector` 模块支持 Real-Time Model for object Detection (RTMDet)。可以导入预训练的 RTMDet 对象检测器对象 `rtmdetObjectDetector` 来执行对象检测。

### R2024b：支持 YOLOX 对象检测器

从 R2024b 开始，`Deep Learning Object Detector` 模块支持 You Only Look Once X (YOLOX) 对象检测。可以导入预训练的 YOLOX 对象检测器对象 `yoloxObjectDetector` 来执行对象检测。

## 描述

使用训练好的深度学习对象检测器检测对象

Deep Learning Object Detector 模块通过使用通过模块参数指定的训练好的对象检测器，预测输入图像的边界框、类别标签和分数。此模块允许从 MAT 文件或 MATLAB® 函数将预训练的对象检测器加载到 Simulink® 模型中。此模块提供了在 Simulink 中使用检测器对象的图形界面。要启用 Deep Learning Object Detector 模块的某些参数，必须选择支持这些参数的对象检测器。例如，将此模块与 `yolov2ObjectDetector` 对象一起使用，使您能够选择与关联 `detect` 对象函数的名称-值参数类似的参数。
