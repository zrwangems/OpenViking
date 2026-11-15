---
type: simulink-block
title: '8x8 RGB LED Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: '8x8rgbledmatrix'
documentation_source_path: 'supportpkg/raspberrypi_ref/8x8rgbledmatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# 8x8 RGB LED Matrix

## 端口

### 输入

### **Location** — 要以指定颜色显示的像素的位置 [Nx2] 矩阵

在 Write Pixel 模式下，为每个像素提供行和列的位置值，范围从 1 到 8。

**数据类型：** `uint8`

### **RGB** — 要在指定位置显示的 RGB 颜色 [Nx3] 矩阵

在 Write Pixel 模式下，提供 R、G 和 B 值的 [Nx3] 矩阵，范围从 0 到 255。

**数据类型：** `uint8`

### **Image** — 要在 LED 矩阵上显示的输入图像 [8x8x3] 矩阵

在 `Display Image` 模式下，当将 **Input Image source** 设置为 `One multidimensional signal` 时，提供 [8x8x3] 图像信号。

**数据类型：** `uint8`

### **R,G,B** — 要在 LED 矩阵上显示的输入图像 [8x8] 矩阵

在 `Display Image` 模式下，当将 **Input Image source** 设置为 `Separate color signals` 时，提供三个 [8x8] 图像颜色信号。

**数据类型：** `uint8`

### **Orient** — 图像方向的输入端口 0 | 90 | 180 | 270

在 `Display Image` 模式下，当将 **Orientation source** 设置为 `Input port` 时，以 degrees 提供图像方向。

**数据类型：** `uint8`

## 参数

### **View Pixel Information** — 用于查看 RGB LED 矩阵上像素信息的按钮

单击此按钮可了解 RGB LED 矩阵上的像素位置编号。

### **Mode** — LED 矩阵的工作模式 `Write Pixel`（默认） | `Display Image`

模块在该模式下可以工作在特定位置以特定颜色写入像素，或显示输入图像。

### **Input Image source** — 输入图像的来源 `One multidimensional signal`（默认） | `Separate color signals`

选择输入图像的来源。您可以提供一个 [8x8x3] 多维信号或三个 [8x8] 单独的颜色信号。

#### 依赖关系

仅当您在 **Mode** 参数中选择 `Display Image` 选项时，此参数才会启用。

### **Orientation Source** — LED 矩阵上图像方向的来源 `Block dialog`（默认） | `Input port`

选择图像方向的来源。如果您选择 `Block dialog` 选项，则应在 **Orientation** 参数中选择一个值。在 LED 矩阵上显示的图像将设置为您在此参数中指定的方向。如果您选择 `Input port` 选项，则模块将从 Orient 输入端口获取图像方向值。

#### 依赖关系

仅当您在 **Mode** 参数中选择 `Display Image` 选项时，此参数才会启用。

### **Orientation** — 图像方向 0（默认） | 90 | 180 | 270

从值列表中选择图像方向值。

#### 依赖关系

仅当您在 **Mode** 参数中选择 `Display Image` 值，并且在 **Orientation Source** 参数中选择 `Block dialog` 值时，此参数才会启用。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

控制 8x8 RGB LED Matrix 的像素颜色

控制 8x8 RGB LED 矩阵的像素颜色。您可以将该模块用于 ‘Write Pixel’ 模式或 ‘Display Image’ 模式。

*Write Pixel 模式*

要将某个位置的像素设置为指定的 RGB 值，请将该模块设置为 ‘Write Pixel’ 模式。为每个像素提供 RGB 值以及以行和列表示的位置。

下表显示了 ‘Write Pixel’ 模式为此模块工作的示例。

| Location [row,column] | RGB [red,green,blue] | 输出 |
| --- | --- | --- |
| [1,1] —> 单个像素位置 | [255,0,0] —> 单个像素颜色 | 位于 [1,1] 的像素设置为红色 |
| [1,1;1,2;1,3] —> 3 个像素（多个像素位置） | [255,0,0] —> 所有像素的单一颜色 | 位于 [1,1]、[1,2] 和 [1,3] 的像素设置为红色 |
| [1,1;1,2;1,3] —> 3 个像素（多个像素位置） | [255,0,0; 255,255,255; 0,0,255] —> 3 种颜色（多种颜色） | 位于 1,1 的像素设为红色   位于 1,2 的像素设为白色  位于 1,3 的像素设为蓝色 |

**注意**

在设置多种颜色时，如果颜色数量不等于像素数量，则您提供的第一个颜色将设置到所有像素。

*Display Image 模式*

要在 LED 矩阵上显示图像，请将该模块设置为 ‘Display Image’ 模式。

通过将 **Input Image source** 参数设置为 `One multidimensional signal`，您可以将要显示的图像作为 [8x8x3] 信号提供给 ‘Image’ 输入端口。

**输入图像为单个 [8x8x3] 多维信号**

通过将 **Input Image source** 参数设置为 `Separate color signals`，您可以将要显示的图像作为三个 [8x8] 单独的颜色信号提供给 ‘R’、‘G’ 和 ‘B’ 输入端口。

**输入图像为 3 个单独的 [8x8] 信号**

您可以通过指定 Orientation 来旋转 LED 矩阵上显示的图像。图像可以定向为 0、90、180 或 270 degrees。您可以定向该图像。对于您为图像方向提供的任何其他值，模块会将图像方向默认为 0 degree。

通过将 **Orientation source** 参数设置为 `Block dialog`，您可以在 **Orientation** 参数中的模块掩码上选择方向。

将 **Orientation source** 参数设置为 `Input port` 会增加一个额外的输入端口 ‘Orient’。您可以将所需的方向提供给此端口。如果此信号的值不是 0、90、180 或 270，则方向值默认为 0。

**LED 矩阵上的图像方向**
