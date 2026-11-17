---
type: simulink-block
title: 'Phase Shift'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'phaseshift'
documentation_source_path: 'ref/phaseshift.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Shift

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Phase shift
  summary: 相移角度 90 deg（默认）| 非负标量整数
  group: ''
```

### **Phase shift** — 相移角度 `90 deg`（默认）| 非负标量整数

相移角度，指定为非负标量整数，单位为度。
相移应用于所有非零仿真频率。对于零
（DC）频率，相移始终为零。

**数据类型：** `double`
## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

对 RF 系统中的相移进行建模

Phase Shift 模块在电路包络环境中对理想相移进行建模。要了解如何使用 Phase Shift 模块测量接收机中的镜像抑制比，请参阅 Measuring Image Rejection Ratio in Receivers 示例。
