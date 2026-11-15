---
type: simulink-block
title: 'VR To Video'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtovideo'
documentation_source_path: 'vrtovideo.html'
language: zh-CN
chinese_source: worker-translation
---

# VR To Video

## 端口

### 输入

### **Input 1** — 输入信号 real scalar | real vector

用于驱动在 **Virtual World Tree** 中所选节点的虚拟现实可视化的输入信号。

**数据类型：** `double`
### 输出

### **Output 1** — 输出视频流 视频信号维度的 3 元素向量

使用输出端口可访问 VR 信号输入的 RGB 视频流。

**数据类型：** `double`

## 参数

### **Source file** — 指定连接到模块的虚拟世界的文件名 string scalar | character vector

默认情况下，关联虚拟世界 3D 文件的完整路径会显示在此文本框中。如果在此框中仅输入文件名，软件会假定该虚拟世界 3D 文件与模型文件位于同一文件夹中。您可以指定 VRML 文件或 X3D 文件。

- 点击 **New** 以打开空的默认虚拟世界
  编辑器。当您输入源文件名或使用
  **Browse** 按钮时，**New** 按钮
  将变为 **Edit** 按钮。
- 点击 **Edit** 以在打开源文件的情况下启动默认虚拟世界编辑器。
- 点击 **View** 以在 Simulink® 3D Animation™ Viewer 或 Web 浏览器中查看该世界。
- 点击 **Reload** 以在更改世界后重新加载它。

### **Open Viewer automatically** — 在模型加载时显示虚拟世界 off | on

启用此参数可在加载 Simulink 模型后显示虚拟世界。

### **Allow viewing from the Internet** — 通过网络查看虚拟世界 off (默认) | on

启用此参数可使虚拟世界可供在客户端计算机上查看。如果未选中此复选框，则该世界仅在主机上可见。此参数等效于 `vrworld` 对象的 `RemoteView` 属性。

### **Description** — 虚拟现实对象描述 string scalar | character vector

该描述会显示在所有虚拟现实对象列表中、Simulink 3D Animation Viewer 的标题栏中，以及 Simulink 3D Animation HTML 页面上的虚拟世界列表中。此参数等效于 `vrworld` 对象的 `Description` 属性。

### **Show video output port** — 将 VR 信号输出到视频 on (默认) | off

启用一个端口以输出 RGB 视频流，用于进一步的 2D 视频处理。

### **Video output signal dimensions** — 指定视频输出大小 `[200 320]` (默认) | 2-element vector

指定视频输出信号的维度 ([height width])，以 pixels 为单位。

### **Show node types** — 在虚拟世界树中显示节点类型 off (默认) | on

启用此参数可在虚拟世界树中显示节点类型。

### **Show field types** — 在虚拟场景树中显示字段类型 off (默认) | on

启用此参数可在虚拟场景树中显示字段类型。

## 所属库

Simulink 3D Animation

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2007b 中引入**

### R2025a: 警告

`VR To Video` 模块将在未来版本中移除。Simulink 3D Animation Viewer 已移除，因此 `VR To Video` 不会打开虚拟世界。有关替代功能，请参阅将虚拟现实世界过渡到 Unreal Engine 3D 环境。

### R2023b: 将被移除

`VR To Video` 运行时不发出警告，并将在未来版本中移除。

## 描述

（将移除）将数据从 Simulink 模型写入虚拟世界（启用视频输出端口）

VR to Video 模块等效于 VR Sink 模块，不同之处在于其 **Show video output port** 默认处于选中状态。

要打开“模块参数”对话框，请双击该模块。

有关详细信息，请参阅 VR Sink 模块。
