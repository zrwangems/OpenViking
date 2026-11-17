---
type: simulink-block
title: 'Controlled MMF Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'controlledmmfsource'
documentation_source_path: 'ref/controlledmmfsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled MMF Source

## 端口
```yaml
ports: []
```

该模块具有一个物理信号输入端口和两个与其磁端子关联的磁守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

由输入信号驱动的理想磁动势源

Controlled MMF Source 模块表示一个理想磁动势（mmf）源，其足够强大，无论通过它的磁通量如何，都能在其输出端维持指定的 mmf。

输出 mmf 为 *MMF = MMFI*，其中 *MMFI* 是在物理信号端口处给出的数值。
