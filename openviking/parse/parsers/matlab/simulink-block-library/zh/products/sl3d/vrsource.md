---
type: simulink-block
title: 'VR Source'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrsource'
documentation_source_path: 'vrsource.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Source

## 端口

### 输出

### **Output 1** — 输出信号 real scalar | real vector

输出信号，其驱动在 **虚拟世界树** 中选择的节点的虚拟现实可视化。

**数据类型：** `double`

## 参数

### **源文件** — 指定连接到模块的虚拟世界的文件名 string scalar | character vector

默认情况下，关联虚拟世界 3D 文件的完整路径显示在此文本框中。如果在此框中仅输入文件名，软件会假定虚拟世界 3D 文件与模型文件位于同一文件夹中。您可以指定 VRML 文件或 X3D 文件。

- 点击 **New** 打开空的默认虚拟世界编辑器。当您输入源文件名或使用 **Browse** 按钮时，**New** 按钮会变为 **Edit** 按钮。
- 点击 **Edit** 启动默认虚拟世界编辑器并打开源文件。
- 点击 **View** 在 Simulink 3D Animation Viewer 或 Web 浏览器中查看世界。
- 点击 **Reload** 在更改世界后重新加载世界。

### **自动打开查看器** — 模型加载时显示虚拟世界 off | on

启用此参数以在加载 Simulink 模型后显示虚拟世界。

### **允许从 Internet 查看** — 通过网络查看虚拟世界 off（默认） | on

启用此参数以使虚拟世界可在客户端计算机上查看。如果未选中此复选框，则该世界仅在主机上可见。此参数等效于 `vrworld` 对象的 `RemoteView` 属性。

### **描述** — 虚拟现实对象描述 string scalar | character vector

描述显示在所有虚拟现实对象列表中、Simulink 3D Animation Viewer 的标题栏中，以及 Simulink 3D Animation HTML 页面上的虚拟世界列表中。此参数等效于 `vrworld` 对象的 `Description` 属性。

### **采样时间** — 用于仿真的模块采样时间 0.1（默认） | scalar | vector

指定模块的采样时间，或指定 `-1` 以继承采样时间。

### **虚拟世界树** — 查看虚拟世界节点的结构

此框显示虚拟世界 3D 文件和虚拟世界本身的结构。

具有名称的节点用红色箭头标记。您可以从 Simulink 3D Animation 界面访问它们。没有名称但其子节点有名称的节点也用红色箭头标记。此标记方案使您可以通过使用箭头遍历树来找到所有可访问的节点。其他节点在其名称前有一个蓝点。

您设置了值的字段带有复选框。使用这些复选框选择您希望 Simulink 软件更新其值的字段。对于您选择的每个字段，模块中会创建一个输入端口。输入端口按与虚拟世界 3D 文件对应的顺序分配给选定的节点和字段。

其值无法写入的字段（因为其父节点没有名称，或因为它们不属于虚拟世界数据类 `eventIn` 或 `exposedField`）带有一个 X 形图标。

### **显示节点类型** — 在虚拟世界树中显示节点类型 off（默认） | on

启用此参数以在虚拟世界树中显示节点类型。

### **显示字段类型** — 在虚拟场景树中显示字段类型 off（默认） | on

启用此参数以在虚拟场景树中显示字段类型。

## 所属库

Simulink 3D Animation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2011b 中引入**

### R2025a：警告

`VR Source` 模块将在未来版本中移除。Simulink 3D Animation Viewer 已被移除，因此 `VR Source` 不会打开虚拟世界。有关替代功能，请参阅 Transition Virtual Reality World to Unreal Engine 3D Environment。

### R2023b：将移除

`VR Source` 运行时无警告，并将在未来版本中移除。

## 描述

（将移除）从虚拟世界读取数据到 Simulink 模型

使用 VR Source 模块在用户导航虚拟世界与 Simulink® 模型的仿真之间提供交互。VR Source 模块注册用户与虚拟世界的交互，并将该数据传递给模型以影响模型的仿真。VR Source 从 Block Parameters 对话框中指定的虚拟世界字段读取值，并将这些值输入到模型。

可以使用 VR Source 模块将虚拟世界的数据输入到 Simulink 模型的一些方式示例包括：

- 使用虚拟世界中的传感器数据控制仿真。
- 在用户在虚拟世界中的导航和交互与模型仿真之间提供交互。
- 使仿真对虚拟世界事件作出反应，例如时间滴答或脚本输出。
- 使用虚拟世界中的静态信息（例如盒子的尺寸）控制仿真。

例如，您可以在虚拟世界中指定设定点，以便用户可以交互式地指定虚拟世界对象的位置。然后，仿真会对对象位置的变化作出响应。VR Source 模块可以将来自虚拟世界的事件（例如时间滴答或脚本输出）读取到模型中。VR Source 模块还可以将有关虚拟世界的静态信息（例如虚拟世界 3D 文件中定义的盒子尺寸）读取到模型中。

**注意**

当前内部查看器窗口（`vrfigure`）属性会与 Simulink 模型一起保存。下次打开模型时，内部查看器窗口会使用保存的相同参数打开，例如位置、大小和导航模式。关闭查看器窗口时，如果这些属性已更改，Simulink 软件不会提醒您。

要打开 VR Source 模块的 Block Parameters 对话框：

- 首次添加 VR Source 模块且其尚未与虚拟世界关联时，双击该模块。
- 否则，在 Simulink 3D Animation™ Viewer 中，选择 **Simulation****Block parameters**。如果查看器尚未打开，可以通过双击 VR Source 模块将其打开。

不能使用 Simulink Coder™ 软件编译包含 VR Source 模块的模型。
