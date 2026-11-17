---
type: simulink-block
title: 'Infinite Flow Resistance (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'infiniteflowresistance2p'
documentation_source_path: 'ref/infiniteflowresistance2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (2P)

## 端口
```yaml
ports: []
```

该模块具有一对两相流体守恒端口 A 和 B，表示相邻两相流体网络的分支。
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

**在 R2015b 中引入**

## 描述

两相流体网络中的完全隔热断口

Infinite Flow Resistance (2P) 模块表示两相流体网络中的一个断口。断口处没有质量或能量流动。但是，连接到回路的 Two-Phase Fluid Properties (2P) 模块所指定的流体属性在断口两侧是相同的。使用此模块可设置端口 **A** 和端口 **B** 之间压力差和比内能差的优先级及初始目标值。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
