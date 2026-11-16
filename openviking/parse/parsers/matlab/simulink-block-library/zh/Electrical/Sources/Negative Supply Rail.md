---
type: simulink-block
title: 'Negative Supply Rail'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'negativesupplyrail'
documentation_source_path: 'ref/negativesupplyrail.html'
language: zh-CN
chinese_source: worker-translation
---

# Negative Supply Rail

## 端口

### 守恒

### **-** — 负电压电气

与负电源轨的负电压关联的电气守恒端口。

## 参数

### **恒定电压** — 恒定输出电压 `-1` `V`（默认）

输出端口处相对于 Electrical Reference 模块接地端口的电压。

## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

理想负电源轨

Negative Supply Rail 模块表示理想负电源轨。使用此模块代替 Simscape™ DC Voltage Source 模块，以定义相对于必须出现在每个模型中的 Simscape Electrical Reference 模块的输出电压。

**注意**

不要将多个 Negative Supply Rail 模块连接到任何已连接的线路上。
