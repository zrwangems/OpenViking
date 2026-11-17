---
type: simulink-block
title: 'Lever'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanisms'
documentation_page: 'lever'
documentation_source_path: 'ref/lever.html'
language: zh-CN
chinese_source: worker-translation
---

# Lever

## 端口

### 守恒

### **A** — 杠杆机械平移的节点 A

与杠杆节点 A 关联的机械平移守恒端口。

### **B** — 杠杆机械平移的节点 B

与杠杆节点 B 关联的机械平移守恒端口。

### **C** — 杠杆机械平移的节点 C

与杠杆节点 C 关联的机械平移守恒端口。

## 参数

### **AC arm length** — 节点 A 和 C 之间的臂长 `0.1 m`（默认值）

节点 A 和 C 之间的臂长。

### **BC arm length** — 节点 B 和 C 之间的臂长 `0.1 m`（默认值）

节点 B 和 C 之间的臂长。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

通用机械杠杆

Lever 模块以其通用形式表示机械杠杆，称为自由杠杆或求和杠杆，如下图所示。

求和杠杆方程是在假设与初始位置存在小角度偏差的情况下推导得出的：

vC=KAC·vA+KBC·vB

FA=KAC·FC

FB=KBC·FC

KAC=lBClAC+lBC

KBC=lAClAC+lBC

其中

- *v*A、
  *v*B、
  *v*C 为杠杆关节速度。
- *F*A、
  *F*B、
  *F*C 为杠杆关节力。
- *l*AC、
  *l*BC 为臂长。

上述方程是在假设杠杆在节点 C 处对力和运动求和的情况下推导得出的。该假设是任意的，不对力或运动如何施加到杠杆上施加任何限制。换句话说，根据力的值，杠杆的任何节点都可以是“输入”或“输出”节点。此外，模块的任何节点都可以连接到参考点，从而将三节点杠杆转换为支点在中间的第一类杠杆，或支点在端部的第二类杠杆。

下图显示了支点在中间的第一类杠杆的示意图。

它由以下方程描述：

vA=−lAClBC·vB

FB=−lAClBC·FA

下一幅图显示了支点在节点 A 的第二类杠杆的示意图。

它由以下方程描述：

vC=KBC·vB

FB=KBC·FC

Linkage Mechanism 示例说明了 Lever 模块在三种不同模式下的使用。连杆机构 L\_1 和 L\_4 模拟支点在端部的第一类杠杆。连杆机构 L\_2 表示求和杠杆。连杆机构 L\_3 模拟支点在中间的第二类杠杆。

就模块方向性而言，如果关节的绝对位移与全局指定的正方向一致，则为正值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
