---
type: simulink-block
title: 'Belt-Cable End'
family: 'belts-and-cables'
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

### Frame

### **R** — 局部参考坐标系 frame

用于将绳索的末端连接到多体模型其余部分的参考坐标系。
### Belt-Cable

### **E** — 绳索连接点 belt-cable

用于端接滑轮系统绳索的点。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Multibody / Belts and Cables

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

滑轮系统绳索的末端

Belt-Cable End 模块表示绳索的末端，通过该末端可对滑轮系统进行锚定、驱动或加载。该末端用作滑轮专用的 belt-cable 域与所有多体组件通用的 frame 域之间的接口。belt-cable 端口（**E**）标识此模块定义其末端的绳索及其在滑轮系统中的相对放置位置。frame 端口（**R**）标识末端的局部参考坐标系及其在更广泛多体模型中的放置位置。

绳索不可伸长。仅当提供绳索源（例如以卷筒的形式）时，其有效长度才能改变。如果绳索的第二端点是另一个末端，则绳索长度固定，因此从一个末端到另一个末端绕滑轮的路径距离也必须固定。该距离在仿真期间通过基于滑轮放置位置和几何形状的计算进行监测。这两个量度——长度和距离——必须始终一致。

绳索还始终绷紧。从其末端之一到最近滑轮，绳索必须形成一条直线，该直线与滑轮圆周相切并平行于其旋转平面。末端的参考坐标系放置在该直线上，其 *z* 轴沿该直线指向并背离滑轮。由滑轮系统外部组件施加在末端上的约束必须在不干扰此对准的情况下起作用。

注意，frame 端口和 belt-cable 端口属于不同的物理域。通常，端口仅连接到同类端口——frame 端口连接到其他 frame 端口，belt-cable 端口连接到其他 belt-cable 端口。belt-cable 域还施加了特殊要求：每个 belt-cable 连接线网络必须包含一个（且不超过一个）Belt-Cable Properties 模块。滑轮绳索的必要属性通过此模块指定。
