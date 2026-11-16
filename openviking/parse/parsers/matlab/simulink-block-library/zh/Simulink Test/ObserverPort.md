---
type: simulink-block
title: 'Observer Port'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: ''
documentation_page: 'observerport'
documentation_source_path: 'ref/observerport.html'
language: zh-CN
chinese_source: official
---

# Observer Port

## 端口

### 输出

### **Port\_1** — 映射信号 标量 | 向量

通过 Observer Port 流入 Observer 模型的映射信号。

**数据类型:** `double` | `single` | `Boolean` | `base integer` | `fixed point` | `enumerated` | `non-virtual bus`

## 参数

R2025b 官方文档未提供。

## 所属库

Simulink Test

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2019a 中推出**

## 描述

无线链接信号以用于验证

在 Observer 模型内添加 Observer Port 模块，以将信号从系统模型映射到 Observer 模型。Observer Port 模块只能在链接到 Observer Reference 模块的模型中使用。
