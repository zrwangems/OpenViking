---
type: simulink-block
title: 'Spring and Damper Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'springanddamperforce'
documentation_source_path: 'ref/springanddamperforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Spring and Damper Force

## 端口
```yaml
ports: []
```

该模块包含坐标系端口 B 和 F，分别表示基础坐标系和从动坐标系。

在模块对话框中选中 **Sense Force** 复选框会添加一个物理信号端口 **fm**。
## 参数
```yaml
parameters: []
```

**Natural Length**
:   输入基础坐标系和从动坐标系原点之间的平衡距离。这是弹簧力大小为零时的距离。默认值为 `0`。选择或输入一个物理单位。

**Spring Stiffness**
:   输入线性弹簧常数的值。该值必须大于或等于零。默认值为零。选择或输入一个物理单位。

**Damping Coefficient**
:   输入线性阻尼系数的值。该值必须大于或等于零。默认值为零。选择或输入一个物理单位。

**Sense Force**
:   选中此项以检测作用在两个坐标系原点之间的弹簧和阻尼力的带符号大小。该模块会暴露一个额外的物理信号端口以输出力信号。输出信号为标量值。如果力为排斥力，该值为正；如果力为吸引力，该值为负。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

力与两个坐标系原点之间的距离和相对速度成正比

该模块表示一对线性弹簧和阻尼力，在基础坐标系和从动坐标系原点之间相互施加。这对力的大小相等但方向相反。一个力作用在基础坐标系原点上，沿从从动坐标系原点指向基础坐标系原点的向量方向。另一个力作用在从动坐标系原点上，沿从基础坐标系原点指向从动坐标系原点的向量方向。

弹簧力分量的大小与基础坐标系和从动坐标系原点之间的距离成正比。该距离是连接两个原点的直线段的长度。阻尼力分量的大小与从动坐标系原点相对于基础坐标系的相对速度成正比。
