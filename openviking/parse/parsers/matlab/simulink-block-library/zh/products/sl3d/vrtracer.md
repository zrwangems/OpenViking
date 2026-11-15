---
type: simulink-block
title: 'VR Tracer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtracer'
documentation_source_path: 'vrtracer.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Tracer

## 端口

### 输入

### **Position** — 节点的位置坐标 3 元素向量

对象位置输入，对应于对象在场景层次结构中的放置。如果被追踪对象作为父对象的子对象存在，请在 **父节点（根节点留空）** 参数中定义父对象名称。

**数据类型：** `double`

### **Color** — 标记颜色 3 元素向量

**注意**

当 **标记颜色选择** 参数设置为 `Block input` 时，此端口启用。

提供用于追踪器标记的颜色，形式为 R、G 和 B 值的 3 元素向量。

**数据类型：** `double`

## 参数

### **关联的 VRML 文件** — 虚拟世界 3D 文件 string scalar | character vector

指定用于 3D 查看器的虚拟世界文件。

### **父节点（根节点留空）** — — 从层次结构中选择节点 VR node

从场景层次结构中选择要追踪的节点。

### **标记形状** — 选择标记形状 `None` (default) | `Tetrahedron` | `Pyramid` | `Box` | `Octahedron` | `Sphere`

从提供的选项中选择一种形状来标记信号轨迹。

### **用线段连接标记** — 显示追踪路径 `on` (default) | `off`

启用此参数以连接被追踪对象路径上的标记。

### **在每个标记位置放置三轴** — 提供方向信息 `on` (default) | `off`

启用此参数以在每个标记位置放置三轴。三轴可帮助您在 *x*-*y*-*z* 平面中确定对象轨迹的方向。

### **标记比例** — 指定标记大小 `[1 1 1]` (default)

指定一个 3 元素向量，用于定义预定义标记形状和三轴的缩放。此参数可适应各种大小的场景。

### **标记颜色选择** — 指定标记颜色的来源 `Block input` (default) | `Selected from color list` | `Defined as RGB values`

- `Block input` — 禁用 **标记颜色** 参数，并依赖第二个模块输入来定义标记颜色。选择此选项会启用第二个模块输入，您可以将标记颜色的信号连接到该输入。
- `Selected from color list` — 启用 **标记颜色** 参数。您可以从列表中为标记选择一种颜色。
- `Defined as RGB values` — 启用 **标记颜色** 参数以接受标记颜色的 RGB 值。

### **标记颜色** — 指定追踪器颜色 `yellow` (default) | `magenta` | `cyan` | `red` | `green` | `blue` | `white` | `black`

从提供的选项中设置追踪器标记颜色。当您将 **标记颜色选择** 设置为 `Selected from color list` 时，此参数启用。

### **标记颜色 (RGB)** — 指定追踪器颜色 `[1 0 0]` (default) | 3-element vector

将追踪器标记颜色设置为由 RGB 值组成的 3 元素向量，每个值的范围为 0-255。

### **采样时间** — 用于仿真的模块采样时间 0.1 (default) | scalar | vector

指定模块的采样时间，或指定 `-1` 以继承采样时间。

### **确保仿真期间查看器窗口打开** — 保持查看器打开 `off` (default) | `on`

选中此复选框以确保 Simulink® 3D Animation™ Viewer 在仿真期间打开。

### **将位置投影到平面** — 将路径投影到平面 `off` (default) | `on`

指定是否显示从对象到平面的线段，以近似对象的轨迹。

### **投影平面方程系数 (ax+by+cz+d=0)** — 以向量 `[0 1 0 0]` (default) 的系数形式指定投影平面

当启用 **将位置投影到平面** 参数时，指定要将对象位置投影到的平面。系数采用 `ax+by+cz+d=0` 形式。

### **将位置投影到点** — 显示从标记到投影的线段 `None` (default) | `Defined in the block mask` | `Defined in the block input`

显示从对象到点的线段，以近似对象的轨迹。

- `None` — （默认）不投影到点。
- `Defined in block mask` — 如果选择此选项，请在 **Projection point coordinates** 编辑框中输入坐标。
- `Defined in the block input` — 如果选择此选项，请在输入到 VR Tracer 模块的模块输出中指定点的坐标。

## 所属库

Simulink 3D Animation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2008b 中引入**

### R2023b：将删除

`VR Tracer` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块来将 MATLAB® 和 Simulink 与 Unreal Engine® 3D 仿真环境连接。要开始使用，请参阅 Create 3D Simulations in Unreal Engine Environment。

## 描述

（将被移除）追踪关联虚拟场景中对象的轨迹

VR Tracer 模块允许您追踪关联虚拟场景中对象的轨迹。

此模块按固定时间步创建标记节点，这些节点可作为指定父节点（**父节点** 参数）的子节点，也可位于场景层次结构的顶层（根节点）。

您可以指定三种类型的标记之一：

- 通用形状
- 连接每个时间步中对象位置的线段
- 用于在 3-D 空间中确定轨迹方向的轴对齐三轴

您还可以将追踪的对象位置投影到平面或点。

对象位置输入必须与对象在场景层次结构中的放置位置相对应。如果被追踪对象作为父对象的子对象存在，请在父节点字段中定义父对象的 DEF 名称。如果被追踪对象位于场景层次结构的顶层（其位置在全局场景坐标中定义），请将该字段留空。

第一个模块输入向量确定标记的位置。第二个模块输入（如果由 **标记颜色选择** 参数启用）表示标记颜色。第二个或第三个模块输入向量（取决于是否启用标记颜色输入向量）指定投影点坐标。

要打开模块参数对话框，请双击该模块。
