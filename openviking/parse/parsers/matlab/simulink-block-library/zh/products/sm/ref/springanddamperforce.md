---
type: simulink-block
title: 'Spring and Damper Force'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Multibody Dynamics / Loads'
documentation_page: 'springanddamperforce'
documentation_source_path: 'ref/springanddamperforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Spring and Damper Force

## 端口

该模块包含坐标系端口 B 和 F，分别表示基础坐标系和从动坐标系。

选中模块对话框中的**检测力**复选框会添加一个物理信号端口 **fm**。

## 参数

**自然长度**
:   输入基础坐标系原点与从动坐标系原点之间的平衡距离。在该距离下，弹簧力的大小为零。默认值为 `0`。选择或输入物理单位。

**弹簧刚度**
:   输入线性弹簧常数的值。该值必须大于或等于零。默认值为零。选择或输入物理单位。

**阻尼系数**
:   输入线性阻尼系数的值。该值必须大于或等于零。默认值为零。选择或输入物理单位。

**检测力**
:   选中此项可检测作用在两个坐标系原点之间的弹簧和阻尼器力的带符号量值。该模块会显示一个额外的物理信号端口，用于输出力信号。输出信号为标量值。如果力为排斥力，则该值为正；如果力为吸引力，则该值为负。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

与两个坐标系原点之间的距离和相对速度成正比的力

此模块表示一对线性弹簧和阻尼器力，它们在基础坐标系原点与从动坐标系原点之间相互作用。这对力大小相等、方向相反。一个力作用于基础坐标系原点，方向沿从动坐标系原点指向基础坐标系原点的矢量。另一个力作用于从动坐标系原点，方向沿基础坐标系原点指向从动坐标系原点的矢量。

弹簧力分量的大小与基础坐标系原点和从动坐标系原点之间的距离成正比。该距离是连接两个原点的直线段的长度。阻尼力分量的大小与从动坐标系原点相对于基础坐标系的相对速度成正比。
