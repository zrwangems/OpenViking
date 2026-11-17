---
type: simulink-block
title: 'Temperature Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'temperaturesource'
documentation_source_path: 'ref/temperaturesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Temperature Source

## 端口
```yaml
ports:
- name: A
  summary: 源出口热
  direction: unspecified
```

### 守恒

### **A** — 源出口热

与源出口关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Temperature
  summary: 源出口处的绝对温度 293.15 K（默认值）
  group: ''
```

### **Temperature** — 源出口处的绝对温度 293.15 K（默认值）

源出口端口处的恒定绝对温度。
## 所属库

Simscape / Foundation Library / Thermal / Thermal Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

以温度为特征的恒定热能源

Temperature Source 模块表示一个理想热能源，其功率足以在其出口处维持指定温度，无论系统消耗的热流如何。

该源生成由 **Temperature** 参数值定义的恒定绝对温度。
