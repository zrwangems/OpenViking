---
type: simulink-block
title: 'Thermal Resistor'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'thermalresistor'
documentation_source_path: 'ref/thermalresistor.html'
language: zh-CN
chinese_source: worker-translation
---

# Thermal Resistor

## 端口

### 守恒

### **A** — 表面 A 热

与热量流经的材料的表面 A 关联的热守恒端口。

### **B** — 表面 B 热

与热量流经的材料的表面 B 关联的热守恒端口。

## 参数

### **热阻** — 热阻 `1e-3` `K/W`（默认）

热阻，
*Rthermal*。

## 所属库

Simscape / Electrical / Passive / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

通过材料层的热传导进行的热传递

Thermal Resistor 模块表示通过材料层传导的热传递。热传递：

- 遵循傅里叶定律
- 与材料层两端的温差成正比
- 与材料的热阻成反比

传导热传递方程为：

QAB=TABRthermal,

其中：

- *QAB* 是通过材料的热流量。
- *TAB* 是材料层两端的温差。
- *Rthermal* 是材料的热阻。

热阻可计算为：

Rthermal=DkA,

其中：

- *D* 是材料层的厚度。
- *k* 是材料的热导率。
- *A* 是垂直于热流方向的面积。

使用 Thermal Resistor 模块根据材料层的热阻来参数化等效组件。若要根据材料层的厚度、热导率和面积来参数化等效组件，请使用 Simscape™ Foundation 库中的 Conductive Heat Transfer 模块。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

标称值提供了一种指定模型中变量预期量级的方法。基于标称值使用系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅通过标称值进行系统缩放。
