---
type: simulink-block
title: 'VR Sink'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsink'
documentation_source_path: 'vrsink.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Sink

## 端口

### 输入

### **Input 1** — 输入信号 real scalar | real vector

用于驱动 **虚拟世界树** 中所选节点的虚拟现实可视化的输入信号。

**数据类型：** `double`
### 输出

### **Output 1** — 输出视频流 3-element vector of video signal dimensions

使用输出端口访问 VR 信号输入的 RGB 视频流。

**数据类型：** `double`

## 参数

### **源文件** — 指定连接到模块的虚拟世界的文件名 string scalar | character vector

默认情况下，关联虚拟世界 3D 文件的完整路径会显示在此文本框中。如果在此框中仅输入文件名，软件会假定虚拟世界 3D 文件与模型文件位于同一文件夹中。您可以指定 VRML 文件或 X3D 文件。

- 单击 **新建** 打开空的默认虚拟世界编辑器。当您输入源文件名或使用 **浏览** 按钮时，**新建** 按钮会变为 **编辑** 按钮。
- 单击 **编辑** 以打开默认虚拟世界编辑器并打开源文件。
- 单击 **查看** 以在 Simulink 3D Animation™ Viewer 或 Web 浏览器中查看虚拟世界。
- 单击 **重新加载** 以在更改虚拟世界后重新加载它。

### **自动打开查看器** — 在模型加载时显示虚拟世界 off | on

启用此参数以在加载 Simulink 模型后显示虚拟世界。

### **允许从 Internet 查看** — 通过网络查看虚拟世界 off（默认） | on

启用此参数以使虚拟世界可在客户端计算机上访问查看。如果未选中此复选框，则虚拟世界仅在主机计算机上可见。此参数等效于 `vrworld` 对象的 `RemoteView` 属性。

### **描述** — 虚拟现实对象描述 string scalar | character vector

描述会显示在所有虚拟现实对象列表中、在 Simulink 3D Animation Viewer 的标题栏中，以及在 Simulink 3D Animation HTML 页面上的虚拟世界列表中。此参数等效于 `vrworld` 对象的 `Description` 属性。

### **采样时间** — 用于仿真的模块采样时间 0.1（默认） | scalar | vector

指定模块的采样时间，或指定 `-1` 以继承采样时间。

### **显示视频输出端口** — 将 VR 信号输出到视频 off（默认） | on

启用一个端口以输出 RGB 视频流，用于进一步的 2D 视频处理。

### **视频输出信号维度** — 指定视频输出大小 `[200 320]`（默认） | 2-element vector

以 pixels 为单位指定视频输出信号的维度（[height width]）。

### **虚拟世界树** — 查看虚拟世界节点结构

此框显示虚拟世界 3D 文件和虚拟世界本身的结构。

具有名称的节点用红色箭头标记。您可以从 Simulink 3D Animation 界面访问它们。没有名称但其子节点有名称的节点也用红色箭头标记。此标记方案使您可以通过使用箭头遍历树来找到所有可访问节点。其他节点在其名称前有一个蓝点。

您设置值的字段具有复选框。使用这些复选框选择希望 Simulink 软件更新其值的字段。对于您选择的每个字段，都会在模块中创建一个输入端口。输入端口按与虚拟世界 3D 文件对应的顺序分配给选定的节点和字段。

值无法写入的字段（因为其父节点没有名称，或者因为它们不属于虚拟世界数据类 `eventIn` 或 `exposedField`）具有 X 形图标。

### **显示节点类型** — 在虚拟世界树中显示节点类型 off（默认） | on

启用此参数以在虚拟世界树中显示节点类型。

### **显示字段类型** — 在虚拟场景树中显示字段类型 off（默认） | on

启用此参数以在虚拟场景树中显示字段类型。

## 所属库

Simulink 3D Animation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

### R2025a：警告

`VR Sink` 模块将在未来版本中移除。Simulink 3D Animation Viewer 已被移除，因此 `VR Sink` 不会打开虚拟世界。有关替代功能，请参阅将虚拟现实世界转换到 Unreal Engine 3D 环境。

### R2023b：将被移除

`VR Sink` 运行时不会发出警告，并将在未来版本中移除。

## 描述

（将被移除）将数据从 Simulink 模型写入虚拟世界

要将模型中的数据输出以控制和驱动虚拟世界动画，请使用 VR Sink 模块。VR Sink 模块将其端口的值写入模块参数对话框中指定的虚拟世界字段。

VR Sink 模块等效于 VR To Video 模块，不同之处在于 VR Sink 模块的 **显示视频输出端口** 参数默认处于清除状态。

VR Sink 模块不能由 Simulink® Coder™ 软件编译，但可在主机计算机上用作 SimViewing 设备。

**注意**

当前内部查看器窗口（`vrfigure`）属性会与 Simulink 模型一起保存。下次打开模型时，内部查看器窗口会使用上次保存的相同参数打开，例如位置、大小和导航模式。关闭查看器窗口时，如果这些属性已更改，Simulink 软件不会提醒您。

VR Sink 模块是一种 Sim Viewing Device。您可以将其包含在使用 Simulink Coder 软件编译的模型中。如果使用外部模式在目标平台上编译、构建和部署模型，例如 Simulink Real-Time™ 或 Simulink Desktop Real-Time™，某些 sink 模块和 Sim Viewing Device 模块会在仿真期间保持正常模式，从目标接收数据并显示该数据。有关详细信息，请参阅在外部模式中将 C/C++ S-Functions 用作 Sim Viewing Devices (Simulink)。
