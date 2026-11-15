---
type: simulink-block
title: 'Lever'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
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

### **AC 臂长** — 节点 A 和 C 之间的臂长 `0.1 m`（默认）

节点 A 和 C 之间的臂长。

### **BC 臂长** — 节点 B 和 C 之间的臂长 `0.1 m`（默认）

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

Lever 模块表示通用形式的机械杠杆，称为自由杠杆或求和杠杆，如下图所示。

求和杠杆方程是在假设与初始位置存在小角度偏差的情况下推导出来的：

vC=KAC·vA+KBC·vB

FA=KAC·FC

FB=KBC·FC

KAC=lBClAC+lBC

KBC=lAClAC+lBC

其中

- *v*A、
  *v*B、
  *v*C 是杠杆关节
  速度。
- *F*A、
  *F*B、
  *F*C 是杠杆关节力。
- *l*AC、
  *l*BC 是臂长。

上面的方程是在假设杠杆在节点 C 处对力和运动求和的情况下推导出来的。该假设是任意的，并不限制如何将力或运动施加到杠杆上。换句话说，根据力的值，杠杆的任意节点都可以是“输入”或“输出”节点。此外，模块的任意节点都可以连接到参考点，从而将三节点杠杆转换为第一类杠杆（支点在中间）或第二类杠杆（支点在端部）。

下图显示了第一类杠杆的示意图，支点在中间。

它由以下方程描述：

vA=−lAClBC·vB

FB=−lAClBC·FA

下一张图显示了第二类杠杆的示意图，支点在节点 A。

它由以下方程描述：

vC=KBC·vB

FB=KBC·FC

Linkage Mechanism 示例说明了 Lever 模块在三种不同模式下的使用。连杆机构 L\_1 和 L\_4 模拟支点在端部的第一类杠杆。连杆机构 L\_2 表示求和杠杆。连杆机构 L\_3 模拟支点在中间的第二类杠杆。

就模块方向性而言，如果关节的绝对位移与全局指定的正方向一致，则为正。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅修改模块变量的标称值。
