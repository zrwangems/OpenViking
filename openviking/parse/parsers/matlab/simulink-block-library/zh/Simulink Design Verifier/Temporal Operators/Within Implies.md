---
type: simulink-block
title: 'Within Implies'
family: 'sldv'
product_id: 'sldv'
product_name: 'Simulink Design Verifier'
documentation_release: R2025b
official_category: 'Temporal Operators'
documentation_page: 'withinimplies'
documentation_source_path: 'ref/withinimplies.html'
language: zh-CN
chinese_source: worker-translation
---

# Within Implies

## 端口

R2025b 中未记录。

## 参数

### **External reset** — 指定模块是否可以被复位 off（默认）| on

指定 `Obs` 的模块观测是否可以通过外部布尔复位信号进行复位。

## 所属库

Simulink Design Verifier / Temporal Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

验证响应在期望持续时间内发生

Within Implies 模块通过观测 `Obs` 输入是否在第一个输入 `In` 的每个 `true` 持续时间内至少有一个步长为 `true` 来捕获 within implication。每当在某个特定的输入 true 持续时间内未检测到 `Obs` 时，输出会在输入 `true` 持续时间之后的那一步中变为 `false` 并持续一个时间步。

信号的 *True duration* 定义为信号为 true 的连续时间步。
