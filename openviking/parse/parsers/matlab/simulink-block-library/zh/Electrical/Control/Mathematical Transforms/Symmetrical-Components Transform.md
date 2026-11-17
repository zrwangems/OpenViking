---
type: simulink-block
title: 'Symmetrical-Components Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'symmetricalcomponentstransform'
documentation_source_path: 'ref/symmetricalcomponentstransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Symmetrical-Components Transform

## 端口

### 输入

### **abc** — *a*、*b* 和 *c* 相量向量

待分离的三相不平衡相量组，以复信号形式给出。

**数据类型：** `single` | `double`
### 输出

### **+-0** — 平衡的 *a* 相量分量向量

正序、负序和零序 *a* 相量，以复信号形式输出。使用方程部分给出的旋转来计算 *b* 和 *c* 相量组。

**数据类型：** `single` | `double`

## 参数

### **Power invariant** — 变换类型 `off`（默认）| `on`

功率不变切换。选择此参数以使用原始 Fortescue 变换的功率不变替代版本。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

实现 abc 到 +-0 变换

Symmetrical-Components Transform 模块实现一组相量的对称变换。该变换将一组不平衡的三相相量分解为三组平衡的相量组。

在具有平衡阻抗的不平衡系统中，使用此模块可将系统解耦为三个独立的网络。在平衡系统中，使用此模块可将三相相量组简化为等效的单线网络。在这种情况下，正序组表示单线网络。

使用 `Power invariant` 属性在 Fortescue 变换和替代的功率不变版本之间进行选择。

### 方程

对称分量变换将以相量形式给出的不平衡三相信号分离为三组平衡的相量组：

[vavbvc]=[va+vb+vc+]+[va−vb−vc−]+[va0vb0vc0],

其中：

- *va*、*vb* 和 *vc* 构成原始的、不平衡的相量组。
- *va+*、*vb+* 和 *vc+* 构成平衡的正序相量组。
- *va-*、*vb-* 和 *vc-* 构成平衡的负序相量组。
- *va0*、*vb0* 和 *vc0* 构成平衡的零序相量组。

该模块使用以下变换计算对称的 *a* 相：

[Va+Va−Va0]=K3[1aa21a2a111][VaVbVc].

其中 *a* 是复数旋转算子

a=e2πi/3,

*K* 是决定变换类型的常数：

{K=1Fortescue transformK=3Power-invariant transform

要选择功率不变变换并简化 *+-0* 域中的功率计算，请启用 `Power invariant` 属性。

由于其余两组对称相量在计算中不常使用，该模块不计算它们。但是，它们可以用第一组相量的简单旋转来表示：

[Vb+Vb−Vb0]=[a2000a0001][Va+Va−Va0],

以及

[Vc+Vc−Vc0]=[a000a20001][Va+Va−Va0].

### 工作原理

由该变换生成的三组平衡相量具有以下特性：

- 正序组与不平衡相量组 *a-b-c* 具有相同的顺序。
- 负序组与不平衡相量组 *a-c-b* 具有相反的顺序。
- 零序组没有顺序，因为所有三个相量角都相等。

此图直观展示了该变换执行的分离。

在图中，顶部坐标轴显示了具有分量 *a*、*b* 和 *c* 的不平衡三相信号。底部坐标轴组将三相信号分离为对称的正序、负序和零序相量。

请注意，在每种情况下，*a*、*b* 和 *c* 分量都是对称的，并且相隔：

- 正序组为 +120 度。
- 负序组为 *-*120 度。
- 零序组为 0 度。

### 逆变换

对称分量变换是唯一且可逆的：

[VaVbVc]=1K[111a2a1aa21][Va+Va−Va0].

使用 Inverse Symmetrical-Components Transform 模块执行此逆变换。
