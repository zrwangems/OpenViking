---
type: simulink-block
title: 'Heat Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'heatflowratesource'
documentation_source_path: 'ref/heatflowratesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Heat Flow Rate Source

## 端口

### 守恒

### **A** — 源入口热

与源入口关联的热守恒端口。

### **B** — 源出口热

与源出口关联的热守恒端口。

## 参数

### **Heat flow rate** — 通过源的热流量 0 W（默认值）

通过源的恒定热流量。正热流量从端口 A 流向端口 B。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

以热流量为特征的恒定热能源

Heat Flow Rate Source 模块表示一个理想热能源，其功率足以在其出口处维持指定的热流量，而与源两端的温差无关。

该源生成恒定热流量，由 **Heat flow rate** 参数值定义。
