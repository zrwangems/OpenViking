---
type: simulink-block
title: 'Positive Supply Rail'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'positivesupplyrail'
documentation_source_path: 'ref/positivesupplyrail.html'
language: zh-CN
chinese_source: worker-translation
---

# Positive Supply Rail

## 端口

### 守恒

### **-** — 正电压电气

与正电源轨的正电压关联的电气守恒端口。

## 参数

### **恒定电压** — 恒定输出电压 `1` `V`（默认）

输出端口相对于 Electrical Reference 模块接地端口的电压。

## 所属库

Simscape / Electrical / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

理想正电源轨

Positive Supply Rail 模块表示理想正电源轨。使用此模块而非 Simscape™ DC Voltage Source 模块，以定义相对于必须出现在每个模型中的 Simscape Electrical Reference 模块的输出电压。

**注意**

不要将多个 Positive Supply Rail 模块连接到*任何*相连的线路上。
