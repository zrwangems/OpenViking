---
type: simulink-block
title: 'Signal Combiner'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'signalcombiner'
documentation_source_path: 'ref/signalcombiner.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Combiner

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Ground and hide negative terminals
  summary: 将射频电路端子接地 on（默认）| off
  group: ''
```

### **Ground and hide negative terminals** — 将射频电路端子接地 on（默认）| off

选择此参数可将负极端子接地并隐藏。要暴露负极端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算射频信号之和

Signal Combiner 模块在电路包络仿真环境中对每个载波频率的信号进行求和。
