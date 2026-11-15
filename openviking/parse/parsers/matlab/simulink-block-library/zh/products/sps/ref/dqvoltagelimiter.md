---
type: simulink-block
title: 'd-q Voltage Limiter'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Protection\u200b'
documentation_page: 'dqvoltagelimiter'
documentation_source_path: 'ref/dqvoltagelimiter.html'
language: zh-CN
chinese_source: worker-translation
---

# d-q Voltage Limiter

## 端口

### 输入

### **vdRefUnsat** — *vdunsat* scalar

未饱和的直轴参考电压。

**示例：** 示例

**数据类型：** `single` | `double`

### **VqRefUnsat** — *vqunsat* scalar

未饱和的交轴参考电压。

**示例：** 示例

**数据类型：** `single` | `double`

### **VphMax** — *Vph\_max* scalar

最大相电压。

**数据类型：** `single` | `double`
### 输出

### **vdRef** — *vdsat* scalar

饱和后的直轴参考电压。

**数据类型：** `single` | `double`

### **vqRef** — *vdsat* scalar

饱和后的交轴参考电压。

**示例：** 示例

**数据类型：** `single` | `double`

## 参数

### **轴优先级** — 优先选择 *d* 轴或 *q* 轴 `Q-axis`（默认） | `D-axis` | `D-Q equivalence`

优先选择直轴、交轴，或两者都不优先。

### **采样时间（-1 表示继承）** — 采样间隔 `-1`（默认） | 默认值或正数

采样之间的时间间隔。如果该模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果该模块位于连续可变步长模型中，请显式指定采样时间。有关详细信息，请参阅什么是采样时间？和指定采样时间。

## 所属库

Simscape / Electrical / Control / Protection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

限制转子直-交参考坐标系中的电压

d-q Voltage Limiter 模块在转子直-交（*d*-*q*）参考坐标系中实现电压限制器。

### 方程

该图显示了限制 *d*-*q* 电压矢量的圆。

即，

vd2+vq2≤Vph\_max

其中：

- *vd* 是 *d* 轴电压。
- *vq* 是 *q* 轴电压。
- *Vph\_max* 是最大相电压。

电压限制可能有三种情况：

- *d* 轴优先
- *q* 轴优先
- *d*-*q* 等效

如果一个轴优先于另一个轴，则约束后或饱和后的电压定义为

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

和

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

其中：

- v2\_max=(Vph\_max)2−(v1sat)2
- *v1* 是优先轴的电压。
- *v2* 是非优先轴的电压。

如果两个轴都不优先，则约束后的电压定义为

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

和

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

其中：

- Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2
- Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2
