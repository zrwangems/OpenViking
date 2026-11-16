---
type: simulink-block
title: 'Heat Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Models / Thermal Sources'
documentation_page: 'heatflowratesource'
documentation_source_path: 'ref/heatflowratesource.html'
language: zh-CN
chinese_source: official
---

# Heat Flow Rate Source

## 端口

### 守恒

### **A** — 源入口 热

与源入口相关联的热守恒端口。

### **B** — 源出口 热

与源出口相关联的热守恒端口。

## 参数

### **热流量** — 源两端的热流量 0 W (默认)

源两端的恒定热流量。正热流量从端口 A 流向端口 B。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

恒定热能源，以热流为特征

Heat Flow Rate Source 模块表示理想的热能源，无论该热能源两端的温差多大，它都足以在其出口处维持指定的热流。

源产生恒定的热流量，由**热流量**参数值定义。
