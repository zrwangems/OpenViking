---
type: simulink-block
title: 'Simulation 3D Joystick'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Hardware Interface'
documentation_page: 'simulation3djoystick'
documentation_source_path: 'simulation3djoystick.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation 3D Joystick

## 端口
```yaml
ports:
- name: Force
  summary: 力反馈输入 标量 | 向量
  direction: input
  data_types: double
- name: Axes
  summary: 沿任意给定轴的操纵杆位置 向量，每个元素在范围 [-1,1] 内
  direction: output
  data_types: double
- name: Buttons
  summary: 操纵杆按钮的状态 由 0 和 1 组成的向量
  direction: output
  data_types: double
- name: Point of view
  summary: 操纵杆视角选择器的当前状态 -1（选择器未激活） | 标量
  direction: output
  data_types: double
```

### 输入

### **Force** — 力反馈输入 标量 | 向量

以标量或向量形式提供沿支持的操纵杆轴施加的力反馈，范围为 [-1,1]。

**Force** 向量的长度对应于支持力反馈的操纵杆轴的数量。提供给操纵杆的力反馈输入是一个缩放值。该值随后乘以设备的最大力能力。

#### 依赖关系

要启用此参数，请选择 **Enable force-feedback input** 参数。

**数据类型：** `double`
### 输出

### **Axes** — 沿任意给定轴的操纵杆位置 向量，每个元素在范围 [-1,1] 内

第一个操纵杆轴元素是 `x`，第二个元素是 `y`，依此类推，直到轴的总数。
`x` 轴代表什么取决于操纵杆的类型和形状。Simulation 3D Joystick 模块使用操纵杆驱动程序和操纵杆之间的映射。

**数据类型：** `double`

### **Buttons** — 操纵杆按钮的状态 由 0 和 1 组成的向量

操纵杆按钮的状态。

**数据类型：** `double`

### **Point of view** — 操纵杆视角选择器的当前状态 -1（选择器未激活） | 标量

输出信号是视角选择器（或 POV Hat）的角度，以度为单位，从 0 到 360。如果选择器未激活，信号为 -1。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Joystick ID
  summary: 分配给给定操纵杆设备的 ID 1（默认值）
  group: ''
- name: Adjust I/O ports according to joystick capabilities
  summary: 动态调整端口以对应操纵杆能力的选项 on（默认值） | off
  group: ''
- name: Enable force-feedback input
  summary: 支持具有力反馈的操纵杆的选项 on（默认值） | off
  group: ''
```

### **Joystick ID** — 分配给给定操纵杆设备的 ID `1`（默认值）

您可以在系统控制面板的 Game Controllers 部分找到连接到系统的操纵杆的属性。

### **Adjust I/O ports according to joystick capabilities** — 动态调整端口以对应操纵杆能力的选项 `on`（默认值） | `off`

如果启用此参数，Simulink
3D Animation 软件会在您每次打开模型时动态调整端口，以对应所连接操纵杆的能力。如果所连接的设备不具有力反馈能力，选择此复选框会从模块中移除力反馈输入，即使您启用了 **Enable force-feedback input** 参数。

模块端口不具有 Windows® Game Controllers 接口提供的完整宽度。

### **Enable force-feedback input** — 支持具有力反馈的操纵杆的选项 `on`（默认值） | `off`

如果选择此复选框，Simulink
3D Animation 软件可以支持力反馈操纵杆、方向盘和触觉（一种能够提供触觉反馈的）设备。
## 所属库

Simulink 3D Animation / Simulation 3D / Hardware Interface

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

### R2025a：从 Joystick Input 重命名

为反映 Simulink 库的更改，Joystick Input 模块现在称为
Simulation 3D Joystick。行为保持不变。

## 描述

处理来自异步操纵杆设备的输入

Simulation 3D Joystick 模块提供 Simulink® 模型与关联到 Simulink
3D Animation™ 模块的虚拟世界之间的交互。此模块使用轴、按钮以及视角选择器（如果存在）。您可以像使用任何其他 Simulink 源模块一样使用此模块。其输出端口反映操纵杆轴和按钮控件的状态。该模块还支持力反馈设备。

Simulation 3D Joystick 模块支持所有使用 Microsoft® API `DirectInput` 和 `XInput`
组件作为其通信协议的操纵杆设备。
