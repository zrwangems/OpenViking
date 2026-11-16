---
type: simulink-block
title: 'From Video Device'
family: 'imaq'
product_id: 'imaq'
product_name: 'Image Acquisition Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'fromvideodevice'
documentation_source_path: 'fromvideodevice.html'
language: zh-CN
chinese_source: worker-translation
---

# From Video Device

## 端口

### 输出

### **Port\_1** — 视频输出信号 *m*-by-*n*-by-3 矩阵

视频输出信号，指定为 *m*-by-*n*-by-3 矩阵，其中 *m* 表示视频图像的高度，*n* 表示视频图像的宽度。

#### 依赖关系

- 要启用此端口，请将 **Ports mode** 设置为 `One multidimensional signal`。
- 要为该端口指定输出视频信号数据类型，请设置 **Data type**。

**数据类型:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **R, G, B** — RGB 视频输出信号 *m*-by-*n* 矩阵

RGB 视频输出信号，指定为 *m*-by-*n* 矩阵，其中 *m* 表示视频图像的高度，*n* 表示视频图像的宽度。R、G 和 B 是单独的输出端口，每个端口具有相同的维度。

#### 依赖关系

- 要启用此端口，请将 **Output color space** 设置为 `rgb`，并将 **Ports mode** 设置为 `Separate color signals`。
- 要为该端口指定输出视频信号数据类型，请设置 **Data type**。

**数据类型:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **Y, Cb, Cr** — YCbCr 视频输出信号 *m*-by-*n* 矩阵

YCbCr 视频输出信号，指定为 *m*-by-*n* 矩阵，其中 *m* 表示视频图像的高度，*n* 表示视频图像的宽度。Y、Cb 和 Cr 是单独的输出端口，每个端口具有相同的维度。

#### 依赖关系

- 要启用此端口，请将 **Output color space** 设置为 `YCbCr`，并将 **Ports mode** 设置为 `Separate color signals`。
- 要为该端口指定输出视频信号数据类型，请设置 **Data type**。

**数据类型:** `single` | `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

以下字段显示在模块参数对话框中。如果您选择的设备不支持某项功能，则该功能不会显示在对话框中。

### **Device** — 图像采集设备 可用设备

要连接的图像采集设备。列表中的项取决于已连接到系统的设备。Image Acquisition Toolbox™ 软件支持的所有视频捕获设备都受该模块支持。

### **Video format** — 设备支持的视频格式 可用视频格式

显示所选设备支持的视频格式。此列表因设备而异。如果您的设备支持使用相机文件，则 `From camera file` 是列表中的选项之一。

#### 依赖关系

- 要启用 **Camera file** 参数，请将 **Video format** 设置为 `From camera file`。此选项仅在所选设备支持相机原始图像文件时出现。输入相机文件路径和文件名，或使用 **Browse** 按钮定位它。

### **Video source** — 设备支持的视频输入源 可用视频输入源

指定设备和格式的可用输入源。单击 **Edit properties...** 按钮以打开 Property Inspector 并编辑源属性。

### **Edit properties...** — 视频源属性 按钮

打开 Property Inspector 以编辑视频源设备特定的属性，例如亮度和对比度。列出的属性因设备而异。可编辑的属性由铅笔图标或表中的下拉列表指示。灰显的属性无法编辑。关闭 Property Inspector 时，您的编辑将被保存。

### **Enable hardware triggering** — 硬件触发采集 `off`（默认）| `on`

此选项仅在所选设备支持硬件触发时出现。选中该复选框以启用硬件触发。启用触发后，您可以选择 **Trigger configuration**。

#### 依赖关系

- 要启用 **Trigger configuration** 参数，请选择 **Enable hardware triggering** 参数。此选项仅在所选设备支持硬件触发时出现。配置选项按触发源/触发条件列出。例如，`TTL/fallingEdge` 表示 TTL 是触发源，信号的下降沿是触发硬件的条件。

### **ROI position** — 视频图像中的感兴趣区域 [0, 0, maximum height, maximum width]（默认）| [row, column, height, width]

使用此字段输入一个行向量，用于指定视频图像中的采集区域。格式为 [row, column, height, width]。row 和 column 的默认值为 0。height 和 width 的默认值设置为最大允许值，由视频格式的分辨率指示。仅当您不希望捕获完整图像大小时，才更改此字段中的值。

### **Output color space** — 视频输出颜色空间 `rgb`（默认）| `grayscale` | `YCbCr` | `bayer`

使用此字段为支持颜色的设备选择颜色空间。如果您的设备支持 Bayer 传感器对齐，则 `bayer` 也可用。

#### 依赖关系

- 要启用 **Bayer sensor alignment** 参数，请将 **Output color space** 设置为 `bayer`。此选项仅在您的设备支持 Bayer 传感器对齐时可用。使用此选项设置 Bayer 传感器的 2-by-2 像素对齐。可能的传感器对齐选项为 `grbg`（默认）、`gbrg`、`rggb` 和 `bggr`。

### **Preview...** — 实时视频数据预览 按钮

预览视频图像。单击此按钮将打开 Video Preview 窗口。预览运行时，图像会根据您在参数对话框中所做的更改进行调整。使用 Video Preview 窗口设置图像采集，使其在运行模型时按您希望的方式由模块采集。

### **Block sample time** — 模块采样率 1/30（默认）| numeric

指定模块在仿真期间的采样时间。采样时间是模块在仿真期间执行的速率。

**注意**

模块采样时间不会设置仿真中所用设备的帧率。帧率由指定的视频格式（标准格式或来自相机文件）决定。某些设备甚至将帧率列为设备特定的源属性。帧率与对话框中的 **Block sample time** 选项无关。模块采样时间定义模块在仿真时间内执行的速率。

### **Ports mode** — 视频输出信号类型 `One multidimensional signal` | `Separate color signals`

此选项仅在您的设备支持为颜色通道使用一个输出端口或多个输出端口时出现。使用此选项指定所有颜色空间使用单个输出端口，或每个通道使用一个端口（例如 R、G 和 B）。当您选择 `One multidimensional signal` 时，输出信号将合并为一行，包含所有颜色信号的信号信息。如果您想使用三个端口分别对应未压缩的红色、绿色和蓝色颜色通道，请选择 `Separate color signals`。请注意，某些设备对单独的颜色信号使用 YCbCr。

**注意**

该模块按指定设备和格式的默认 `ReturnedColorSpace` 设置采集数据。

### **Data type** — 视频输出数据类型 `single`（默认）| `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

模块输出帧时的图像数据类型。此数据类型指示图像帧如何从模块返回到 Simulink。此选项支持所有 MATLAB® 数值数据类型。

### **Read All Frames** — 捕获所有可用图像帧 `off`（默认）| `on`

选择此项以捕获所有可用图像帧。如果您不选择此选项，模块将获取一帧的最新快照，这相当于使用工具箱中的 `getsnapshot` 函数。如果您选择此选项，模块将传入的图像帧排队到 FIFO（先进先出）缓冲区中。模块仍会在每个时间步为您提供一帧，即缓冲区中最旧的一帧，并确保不会丢失任何帧。此选项相当于使用工具箱中的 `getdata` 函数。

#### Kinect for Windows

### **Metadata Output Ports** — Kinect® for Windows® 输出端口

此选项仅在以下情况下出现：

- 您使用 Kinect for Windows 相机
- 您选择 `Kinect Depth Sensor` 作为 **Device**，并且
- 您选择 `Depth Source` 作为 **Video source**。

使用此选项可在仿真和代码生成期间在 Simulink 中返回骨骼信息。您可以在普通、加速和部署仿真模式下输出元数据信息。**Selected Metadata** 列表中的每个元数据项都会成为模块上的一个输出端口。

**All Metadata** 部分列出与 Kinect 深度传感器关联的元数据。

仅当选择了 Kinect 深度传感器时，此部分才可见。**All Metadata** 列表显示可用的元数据。**Selected Metadata** 列表显示哪些元数据项返回到 Simulink。默认情况下此项为空。要使用某个元数据项，请在 **All Metadata** 列表中选择它，然后单击 **Add** 按钮（蓝色箭头图标），将其从 **All Metadata** 添加到 **Selected Metadata** 列表中。**Remove** 按钮（红色 X 图标）会从 **Selected Metadata** 列表中移除某项。您还可以使用 **Move up** 和 **Move down** 按钮更改 **Selected Metadata** 列表中各项的顺序。您可以一次选择多个项。

您可以在上面的示例中看到，三个元数据项已放入 **Selected Metadata** 列表。当您单击 **Apply** 时，模块上会为这些元数据创建输出端口，如下所示。第一个端口是深度帧。

有关这些元数据字段的说明和信息，以及如何将 Kinect for Windows 与 Image Acquisition Toolbox 一起使用，请参阅 Acquire Image and Body Data Using Kinect V2。

## 所属库

Image Acquisition Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

请参阅 Code Generation with From Video Device Block。

## 版本历史

**在 R2007a 中引入**

## 描述

从图像采集设备捕获实时图像数据

From Video Device 模块允许您从图像采集设备（如相机和帧采集器）捕获图像和视频数据流，以便将图像数据引入 Simulink® 模型。该模块还允许您直接通过 Simulink 配置和预览采集。

From Video Device 模块打开、初始化、配置并控制采集设备。该模块仅在模型执行开始时打开、初始化和配置一次。当选择 Read All Frames 选项时，模块将传入的图像帧排队到 FIFO（先进先出）缓冲区中，并为每个仿真时间步提供一个图像帧。如果缓冲区下溢，模块将等待最多 10 seconds，直到缓冲区中有新帧。

该模块没有输入端口。您可以将模块配置为具有一个输出端口，或三个输出端口分别对应未压缩的颜色通道红色、绿色和蓝色，或 Y、Cb 和 Cr。有关配置输出端口的详细信息，请参阅“输出”部分。

有关如何使用此模块的示例，请参阅 Save Video Data to a File。

### 其他支持的功能

- From Video Device 模块支持使用 Simulink Accelerator 模式。此功能可加速 Simulink 模型的执行。
- From Video Device 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。
- From Video Device 模块支持将代码生成与 `packNGo` 函数一起使用，以将所需源代码和依赖的共享库分组。
