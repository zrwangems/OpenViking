---
type: simulink-block
title: 'Inverse Symmetrical-Components Transform'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Mathematical Transforms'
documentation_page: 'inversesymmetricalcomponentstransform'
documentation_source_path: 'ref/inversesymmetricalcomponentstransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Inverse Symmetrical-Components Transform

## 端口

### 输入

### **+-0** — 平衡 *a* 相量分量向量

正序、负序和零序 *a* 相量，以复信号给出。使用 Symmetrical-Components Transform 节中给出的旋转来计算 *b* 和 *c* 相量集。

**数据类型：** `single` | `double`
### 输出

### **abc** — *a*、*b* 和 *c* 相量向量

重新生成的三相不平衡相量集，作为复信号输出。

**数据类型：** `single` | `double`

## 参数

### **Power invariant** — 变换类型 `off`（默认） | `on`

Power invariant 切换开关。选择此参数以使用原始 Fortescue 变换的功率不变替代版本。

## 所属库

Simscape / Electrical / Control / Mathematical Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

实现 +-0 到 abc 变换

Inverse Symmetrical-Components Transform 模块实现正序、负序和零序相量的逆对称变换。该变换将一组三相对称相量分解为等效的 *a*、*b* 和 *c* 相量不平衡集合。

使用此变换从使用 Symmetrical-Components Transform 模块解耦的系统中重新生成三相信号。

使用 `Power invariant` 属性在 Fortescue 变换和替代的功率不变版本之间进行选择。

### 方程

逆对称分量变换从 *+-0* 域中给出的平衡相量集合的 *a* 分量 [*Va+,Va-,Va0*] 重新生成不平衡三相信号 [*Va,Vb,Vc*]：

[VaVbVc]=1K[111a2a1aa21][Va+Va−Va0].

其中，*a* 是复数旋转算子

a=e2πi/3,

而 *K* 是确定变换类型的常数：

{K=1Fortescue 变换K=3功率不变变换

如果该变换是使用功率不变选项执行的，请启用 `Power invariant` 属性以选择功率不变逆变换，并重新生成正确的 *abc* 信号。

### Symmetrical-Components Transform

对称分量变换将按相量量值给出的不平衡三相信号分离为三个平衡相量集合：

[vavbvc]=[va+vb+vc+]+[va−vb−vc−]+[va0vb0vc0],

其中：

- *va*、*vb* 和 *vc* 构成原始的不平衡相量集合。
- *va+*、*vb+* 和 *vc+* 构成平衡的正序相量集合。
- *va-*、*vb-* 和 *vc-* 构成平衡的负序相量集合。
- *va0*、*vb0* 和 *vc0* 构成平衡的零序相量集合。

对称分量变换按如下方式计算对称 *a* 相：

[Va+Va−Va0]=K3[1aa21a2a111][VaVbVc].

由于其余两组对称相量在计算中不常使用，该变换只生成第一组。但是，您可以根据第一组的简单旋转来计算 *b* 组和 *c* 组：

[Vb+Vb−Vb0]=[a2000a0001][Va+Va−Va0],

和

[Vc+Vc−Vc0]=[a000a20001][Va+Va−Va0].

### 工作原理

由对称分量变换生成的三组平衡相量具有以下特性：

- 正序组与不平衡相量集合 *a-b-c* 具有相同的相序。
- 负序组与不平衡相量集合 *a-c-b* 具有相反的相序。
- 零序组没有相序，因为所有三个相量角度都相等。

此图直观展示了该变换执行的分离。

在图中，顶部坐标轴显示具有 *a*、*b* 和 *c* 分量的不平衡三相信号。底部的一组坐标轴将三相信号分离为对称的正序、负序和零序相量。

请注意，在每种情况下，*a*、*b* 和 *c* 分量都是对称的，并且相隔：

- 正序组为 +120 degrees。
- 负序组为 *-*120 degrees。
- 零序组为 0 degrees。
