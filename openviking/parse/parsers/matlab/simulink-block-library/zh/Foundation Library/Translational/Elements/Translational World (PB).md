---
type: simulink-block
title: 'Translational World (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'translationalworldpb'
documentation_source_path: 'ref/translationalworldpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational World (PB)

## 端口

### 守恒端口

### **R** — 绝对零位置和速度 基于位置的机械平移

基于位置的机械平移守恒端口，用于为所连接的回路设置绝对零位置和速度。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Translational / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的平移网络的全局参考坐标系

Translational World (PB) 模块表示静止的全局参考坐标系。该模块为所连接的回路设置绝对零位置和速度。所连接回路中的所有位置均相对于此参考。所有连接到该模块的基于位置的平移端口均为静止。

每个基于位置的平移回路都需要一个 Translational World (PB) 模块

Translational World (PB) 模块表示空间中的一个单点。因此，在大多数情况下，在一个连接的回路中只有一个 Translational World (PB) 模块与物理视图是一致的。
