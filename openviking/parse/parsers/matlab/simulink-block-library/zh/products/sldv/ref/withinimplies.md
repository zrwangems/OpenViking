---
type: simulink-block
title: 'Within Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Specify and Verify Design Requirements'
documentation_page: 'withinimplies'
documentation_source_path: 'ref/withinimplies.html'
language: zh-CN
chinese_source: official
---

# Within Implies

## 端口

R2025b 官方文档未提供。

## 参数

### **外部重置** — 指定是否可以重置模块 off (默认) | on

指定是否可以通过外部布尔复位信号复位 `Obs` 的模块观察。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011a 中推出**

## 描述

验证响应是否在所需时间内发生

Within Implies 模块通过观察 `Obs` 输入在第一个输入 `true` 的每个 `true` 持续时间内是否至少为 `In` 一步来捕获内部蕴涵。每当在特定输入真实持续时间内未检测到 `Obs` 时，输出将在输入 `false` 持续时间之后的步骤中变为一个时间步长的 `true`。

信号*真实持续时间*定义为信号为真实的连续时间步长
