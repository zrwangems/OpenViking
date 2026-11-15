---
type: simulink-block
title: 'Pixy2 Vision Sensor'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Sensor Blocks'
documentation_page: 'pixy2visionsensor'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/pixy2visionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Pixy2 Vision Sensor

## 端口

### 输出

### **X** — 检测到的物体像素中心的 *x* 位置 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著物体（色块）的 *x* 位置。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Y** — 检测到的物体像素中心的 *y* 位置 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著物体（色块）的 *y* 位置。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Width** — 检测到的物体像素的宽度 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著物体（色块）的宽度。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Height** — 检测到的物体像素的高度 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著物体（色块）的高度。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Object Count** — 检测到的物体数量，正整数，范围 [1, 255]

Pixy2 视觉传感器检测到的基于视场的物体（色块）数量。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Signature`、`Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint8`

### **Signature** — 检测到的物体的颜色或颜色代码签名，正整数，范围 [1, 7]

Pixy2 视觉传感器检测到的基于视场的颜色或颜色代码物体（色块）的签名。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color Code Signature` 或 `Color and Color Code Signature (Mixed)`。

**数据类型：** `uint16`

### **Angle** — 检测到的物体的角度，整数，范围 [-180, +180]

Pixy2 视觉传感器检测到的基于视场的物体（色块）的颜色或颜色代码签名的角度。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Color and Color Code Signature (Mixed)`。

**数据类型：** `int16`

### **Xstart** — 检测到的线像素的 *x* 坐标起点 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著线的 *x* 坐标起点。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Ystart** — 检测到的线像素的 *y* 坐标起点 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著线的 *y* 坐标起点。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Xend** — 检测到的线像素的 *x* 坐标终点 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著线的 *x* 坐标终点。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Yend** — 检测到的线像素的 *y* 坐标终点 | 标量

Pixy2 视觉传感器检测到的基于视场的最显著线的 *y* 坐标终点。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Line`。

**数据类型：** `uint16`

### **Intersection Flag** — 相交线的存在 1 (true) 或 0 (false)

Pixy2 视觉传感器视场中相交线的存在。`1` 表示存在相交线。

#### 依赖关系

要启用此端口，请将 **跟踪模式** 参数设置为 `Line`。

**数据类型：** `uint8`

## 参数

### **EV3 主机输入端口** — 连接到 Pixy2 视觉传感器的输入端口 `4`（默认）| 正整数，范围 [1, 4]

选择 LEGO MINDSTORMS EV3 硬件上连接 Pixy2 视觉传感器的输入端口。硬件上有四个端口，您可以选择其中任意一个端口。为模型中的每个 Pixy2 Vision Sensor 模块指定唯一的输入端口。

### **I2C 地址** — I2C 总线标识符 `0x54`（默认）| 地址，范围 [`0x54`, `0x57`]

输入连接到 Pixy2 视觉传感器的 I2C 总线的十六进制地址。确保在 PixyMon 实用程序中配置了相同的 I2C 地址。

### **跟踪模式** — 选择跟踪模式 `Color Signature`（默认）| `Color Code Signature` | `Color and Color Code Signature (Mixed)` | `Line`

选择跟踪模式，以检测与 PixyMon 实用程序中配置的颜色签名或颜色代码签名匹配的物体。对于 `Color Signature`、`Color Code Signature` 和 `Color and Color Code Signature (Mixed)` 跟踪模式，检测到的物体的 *xy* 坐标、宽度和高度保持不变。

### **颜色签名** — 要跟踪物体的颜色签名 `1`（默认）| 正整数，范围 [1, 7] | `ALL`

选择要在 PixyMon 实用程序中配置的、要跟踪物体的颜色签名。选择 `ALL` 以跟踪所有已配置的颜色签名。

### **采样时间** — 时间采样间隔 `0.1`（默认）| 正标量，范围 [`0.001`, `1`]

输入模块从 Pixy2 视觉传感器读取值的时间间隔。

## 所属库

LEGO MINDSTORMS EV3 硬件的 Simulink 支持包

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

表示已连接的 CMUcam5 Pixy2 视觉传感器并跟踪物体（色块）

Pixy2 Vision Sensor 模块允许您扩展 LEGO® MINDSTORMS® EV3 硬件的功能，并读取 Pixy2 视觉传感器检测到的物体（色块）的坐标。

**注意**

此模块支持 Pixy2 LEGO 固件版本 3.0.14。

### 功能模式

Pixy2 Vision Sensor 模块有四种功能模式：

- Color Signature：检测与 PixyMon 实用程序中配置的颜色签名匹配的物体。
- Color Code Signature：检测与 PixyMon 实用程序中配置的颜色代码签名匹配的物体。
- Color and Color Code Signature (Mixed)：检测与 PixyMon 实用程序中配置的颜色和颜色代码签名匹配的物体。
- Line：检测并跟踪线。

### 启动 PixyMon

如果您已安装 LEGO MINDSTORMS EV3 硬件的支持包，并按照安装 LEGO MINDSTORMS EV3 硬件支持中所述完成了其他硬件设置，则 PixyMon 实用程序将自动启动。
