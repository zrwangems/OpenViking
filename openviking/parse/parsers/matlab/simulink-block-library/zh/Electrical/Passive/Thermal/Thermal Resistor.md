---
type: simulink-block
title: 'Thermal Resistor'
family: 'sps'
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
```yaml
ports:
- name: A
  summary: 表面 A 热端口
  direction: conserving
- name: B
  summary: 表面 B 热端口
  direction: conserving
```

### 守恒端口

### **A** — 表面 A 热端口

与热量流经材料的表面 A 相关联的热守恒端口。

### **B** — 表面 B 热端口

与热量流经材料的表面 B 相关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Thermal resistance
  summary: 热阻 1e-3 K/W（默认值）
  group: ''
```

### **Thermal resistance** — 热阻 `1e-3` `K/W`（默认值）

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

通过材料层进行热传导的热传递

Thermal Resistor 模块表示通过材料层进行热传导的热传递。热传递：

- 由傅里叶定律支配
- 与材料层两侧的温差成正比
- 与材料的热阻成反比

热传导的方程为：

QAB=TABRthermal，

其中：

- *QAB* 是通过材料的热流。
- *TAB* 是材料层两侧的温差。
- *Rthermal* 是材料的热阻。

热阻可计算为：

Rthermal=DkA，

其中：

- *D* 是材料层的厚度。
- *k* 是材料的热导率。
- *A* 是垂直于热流方向的面积。

使用 Thermal Resistor 模块可根据材料层的热阻来参数化等效组件。若要根据材料层的厚度、热导率和面积来参数化等效组件，请使用 Simscape™ Foundation 库中的 Conductive Heat Transfer 模块。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
