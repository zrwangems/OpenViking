---
type: simulink-block
title: 'Belt-Cable End'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Belts and Cables'
documentation_page: 'beltcableend'
documentation_source_path: 'ref/beltcableend.html'
language: zh-CN
chinese_source: worker-translation
---

# Belt-Cable End

## 端口
```yaml
ports:
- name: R
  summary: 局部参考坐标系 frame
  direction: unspecified
- name: E
  summary: 绳索连接点 belt-cable
  direction: unspecified
```

### 坐标系

### **R** — 局部参考坐标系 frame

用于将绳索末端连接到多体模型其余部分的参考坐标系。
### Belt-Cable

### **E** — 绳索连接点 belt-cable

滑轮系统绳索的终止点。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Multibody / Belts and Cables

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

滑轮系统绳索的末端

Belt-Cable End 模块表示绳索的末端，用于锚定、驱动或加载滑轮系统。该末端充当滑轮特有的 belt-cable 域与所有多体组件通用的 frame 域之间的接口。belt-cable 端口（**E**）标识该模块所定义末端的绳索及其在滑轮系统中的相对位置。frame 端口（**R**）标识末端的局部参考坐标系及其在更广泛的多体模型中的位置。

绳索是不可伸长的。其有效长度只有在提供绳索源时才能改变——例如以卷筒的形式。如果绳索的第二个末端是另一个末端，则绳索的长度是固定的，因此从一个末端到另一个末端绕过滑轮的距也必须固定。该距离在仿真期间通过基于滑轮位置和几何形状的计算进行监测。这两个量——长度和距离——必须始终一致。

绳索也始终处于张紧状态。从其末端之一到最近滑轮，绳索必须形成一条直线，该直线与滑轮圆周相切并平行于其旋转平面。末端的参考坐标系放置在该直线上，其 *z* 轴沿该直线方向并远离滑轮。由滑轮系统外部组件施加在末端上的约束必须在不干扰该对齐的情况下起作用。

请注意，frame 端口和 belt-cable 端口属于不同的物理域。通常，端口仅连接到同类端口——frame 端口连接到其他 frame 端口，belt-cable 端口连接到其他 belt-cable 端口。belt-cable 域还施加了特殊要求：每个 belt-cable 连接线网络必须包含一个（且不多于一个）Belt-Cable Properties 模块。滑轮绳索的必要属性通过该模块指定。
