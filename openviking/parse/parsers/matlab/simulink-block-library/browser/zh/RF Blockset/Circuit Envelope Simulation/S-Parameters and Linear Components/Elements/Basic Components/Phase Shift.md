---
type: simulink-block
title: 'Phase Shift'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / Elements / Basic Components'
documentation_page: 'phaseshift'
documentation_source_path: 'ref/phaseshift.html'
language: zh-CN
chinese_source: worker-translation
---

# Phase Shift

## 端口

未在 R2025b 中记录。

## 参数

### **Phase shift** — 相移角 `90 deg`（默认） | 非负标量整数

相移角，指定为以度为单位的非负标量整数。
相移应用于所有非零仿真频率。对于零 (DC) 频率，相移始终为零。

**数据类型：** `double`

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2015b 中引入**

## 描述

在 RF 系统中对相移进行建模

Phase Shift 模块在电路包络环境中对理想相移进行建模。要了解如何使用 Phase Shift 模块测量接收机中的镜像抑制比，请参阅 Measuring Image Rejection Ratio in Receivers 示例。
