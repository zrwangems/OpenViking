---
type: simulink-block
title: 'MMF Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Magnetic / Magnetic Sources'
documentation_page: 'mmfsource'
documentation_source_path: 'ref/mmfsource.html'
language: zh-CN
chinese_source: worker-translation
---

# MMF Source

## 端口
```yaml
ports: []
```

该模块具有两个与其端子关联的磁守恒端口。
## 参数
```yaml
parameters: []
```

**Constant mmf**
:   输出磁动势。您可以指定任意实数值。默认值为 `1` A。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2010a 中引入**

## 描述

理想磁动势源

MMF Source 模块表示一个理想磁动势（mmf）源，其强度足以在其输出端子上维持指定的恒定磁动势，无论流过该源的磁通量如何。

您通过 **Constant mmf** 参数指定输出磁动势，该参数可以为正、负或零。
