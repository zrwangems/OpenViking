---
type: simulink-block
title: 'Internal Force'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Forces and Torques'
documentation_page: 'internalforce'
documentation_source_path: 'ref/internalforce.html'
language: zh-CN
chinese_source: worker-translation
---

# Internal Force

## 端口
```yaml
ports: []
```

该模块包含坐标系端口 **B** 和 **F**，分别表示基础坐标系和从动坐标系。物理信号端口 **fm** 提供了指定作用在两个端口坐标系之间的内部力的途径。
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

**在 R2013a 中引入**

## 描述

作用在两个坐标系原点之间的一般交互力

该模块表示作用在基础坐标系和从动坐标系原点之间的一般力对。力对中的两个力大小相等但方向相反。一个力作用在基础坐标系原点上，方向沿从动坐标系原点指向基础坐标系原点的向量。另一个力作用在从动坐标系原点上，方向沿基础坐标系原点指向从动坐标系原点的向量。

为指定内部力，该模块提供了物理信号端口 **fm**。正输入信号表示排斥力，将基础坐标系和从动坐标系原点推开。负输入信号表示吸引力，将基础坐标系和从动坐标系原点拉近。如果在任意时刻两个坐标系原点重合，则内部力的方向变为未定义，Simscape™ Multibody™ 可能会停止并报错。
