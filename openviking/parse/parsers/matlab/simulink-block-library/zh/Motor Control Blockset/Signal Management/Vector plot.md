---
type: simulink-block
title: 'Vector plot'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'vectorplot'
documentation_source_path: 'ref/vectorplot.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector plot

## 端口

### 输入

### **Vabc** — 三相电压矢量

*abc* 参考坐标系下三相系统中的电压分量。该端口接受通过 Mux 多路复用的三个电压分量。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Vabc Iabc Theta`。

**数据类型：** `single` | `double`

### **Iabc** — 三相电流矢量

*abc* 参考坐标系下三相系统中的电流分量。该端口接受通过 Mux 多路复用的三个电流分量。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Vabc Iabc Theta`。

**数据类型：** `single` | `double`

### **Theta** — 变换角度标量

旋转参考坐标系与 *α* 轴之间的角度值（对于 `Vabc` 和 `Iabc`，单位为弧度、标幺值或度）。

图中显示了以下情况下的变换角度：

- *d* 轴与 *α* 轴对齐。
- *q* 轴与 *α* 轴对齐。

  在两种情况下，角度均为 *Theta = ωt*，其中：

  - *Theta* 是 *d* 轴对齐时 *α* 轴与 *d* 轴之间的角度，或 *q* 轴对齐时 *α* 轴与 *q* 轴之间的角度。它表示旋转 *dq* 参考坐标系相对于 *α* 轴的角度位置。
  - *ω* 是 *d-q* 参考坐标系中的旋转速度。
  - *t* 是从初始对齐开始的时间，单位为秒。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Vabc Iabc Theta`，并将 **Select reference frame** 设置为 `Rotating Reference Frame`。

**数据类型：** `single` | `double`

### **Vdq** — *dq* 参考坐标系中的电压矢量

旋转 *dq* 参考坐标系中的直轴和交轴电压分量。该端口接受通过 Mux 多路复用的两个电压分量。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Vdq Idq`。

**数据类型：** `single` | `double`

### **Idq** — *dq* 参考坐标系中的电流矢量

旋转 *dq* 参考坐标系中的直轴和交轴电流分量。该端口接受通过 Mux 多路复用的两个电流分量。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Vdq Idq`。

**数据类型：** `single` | `double`

### **Magnitude** — 矢量幅值矢量

要绘制的矢量幅值。该端口接受通过 Mux 多路复用的最多六个矢量幅值。矢量幅值对应于输入到 **Angle** 端口的角度值。

**注意**

多路复用的矢量幅值数量应与输入到 **Angle** 端口的多路复用角度数量相同。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Mag Angle`。

**数据类型：** `single` | `double`

### **Angle** — 矢量角度矢量

要绘制的矢量的角度值（单位为弧度、标幺值或度）。该端口接受通过 Mux 多路复用的最多六个矢量角度。角度值对应于输入到 **Magnitude** 端口的矢量幅值。

**注意**

多路复用的矢量角度数量应与输入到 **Magnitude** 端口的多路复用幅值数量相同。

#### 依赖关系

要启用此端口，请将 **Select input types** 设置为 `Mag Angle`。

**数据类型：** `single` | `double`

## 参数

### **Select input types** — 输入端口类型 `Vabc Iabc Theta`（默认）| `Vdq Idq` | `Mag Angle`

该模块可用的输入端口类型。

### **Select reference frame** — 矢量参考坐标系 `Rotating Reference Frame`（默认）| `Stationary Reference Frame`

选择该模块用于绘制输入矢量所使用的参考坐标系类型：

- `Rotating Reference Frame` — 选择此选项可在旋转 *dq* 参考坐标系中绘制三相电压和电流矢量。
- `Stationary Reference Frame` — 选择此选项可在静止 *αβ* 参考坐标系中绘制三相电压和电流矢量。

#### 依赖关系

要启用此参数，请将 **Select input types** 设置为
`Vabc Iabc Theta`。

### **Alpha (phase-a) axis alignment** — *dq* 参考坐标系对齐 `D-axis`（默认）| `Q-axis`

将旋转参考坐标系的 *d* 轴或 *q* 轴对齐到静止参考坐标系的 *α* 轴。

#### 依赖关系

要启用此参数，请将 **Select input types** 设置为
`Vabc Iabc Theta`，并将 **Select reference
frame** 设置为 `Rotating Reference Frame`。

### **Theta units** — Theta 输入的单位 `Radians`（默认）| `Degrees` | `Per-unit`

**Theta** 输入值的单位。

#### 依赖关系

要启用此参数，请将 **Select input types** 设置为
`Vabc Iabc Theta`，并将 **Select reference
frame** 设置为 `Rotating Reference Frame`。

### **Angle units** — Angle 输入的单位 `Radians`（默认）| `Degrees` | `Per-unit`

**Angle** 输入值的单位。

#### 依赖关系

要启用此参数，请将 **Select input types** 设置为
`Mag Angle`。

### **Open plot at simulation start** — 在仿真开始时打开矢量图 `on`（默认）| `off`

选择此参数可在仿真开始时自动打开矢量图窗口。

**Showplot** — 点击此按钮打开矢量图窗口。

### 矢量图窗口

此示例展示了当您将 **Select input types** 设置为
`Mag Angle` 并提供三个多路复用的幅值和三个多路复用的角度作为输入时的绘图。

您可以使用矢量图窗口上的以下按钮：

- （保存图形）— 点击将绘图保存为图像。
- （首选项）— 点击打开首选项对话框。

  - **Display traces (samples)** — 输入您要为矢量尖端追踪的采样点数。默认情况下，该字段使用值
    `100`。
  - **Auto-Scale** — 选择此字段以自动缩放坐标轴限制。该模块每 `1000`
    个仿真点执行一次自动缩放。
  - **Axes limit** — 输入绘图应使用的 *x* 轴和 *y* 轴的最大值。默认情况下，该字段使用值 `1`。如果您选择
    **Auto-Scale** 且矢量幅值增加到超出所选坐标轴限制，矢量图窗口上的限制会自动扩展以容纳矢量幅值。
- （运行仿真）— 点击以仿真包含矢量图模块的模型。

  （暂停仿真）— 点击以暂停仿真。
- （停止仿真）— 点击以停止仿真。
- （清除数据历史记录）— 点击以清除矢量追踪历史记录。
- （插入图例）— 点击以插入或移除描述矢量的图例。您可以手动更改默认图例描述。
- （自动缩放）— 点击以打开或关闭自动缩放功能。

## 所属库

Motor Control Blockset / Signal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020b 中引入**

## 描述

在空间域中绘制矢量

矢量图模块在空间域中绘制并追踪矢量的变化。您可以使用该模块可视化电气量（如电压和电流）的矢量，并通过矢量尖端留下的轨迹实时追踪其变化。

该模块接受矢量幅值及其角度（以弧度、标幺值或度为单位）作为输入，并提供矢量的图形化表示。该模块还根据选定的点数追踪矢量尖端的绘图历史。

有关如何使用矢量图模块的详细信息，请参阅 Field-Oriented Control of PMSM Using Quadrature Encoder 中的模型
`mcb_pmsm_foc_qep_f28379d`。
