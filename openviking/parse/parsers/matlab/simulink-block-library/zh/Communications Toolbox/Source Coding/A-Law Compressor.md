---
type: simulink-block
title: 'A-Law Compressor'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'alawcompressor'
documentation_source_path: 'ref/alawcompressor.html'
language: zh-CN
chinese_source: worker-translation
---

# A-Law Compressor

## 端口

R2025b 中未记录。

## 参数

**A value**
:   压缩器的 A-law 参数。

**Peak signal magnitude**
:   输入信号的峰值。这也是输出信号的峰值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现用于信源编码的 A-law 压缩器

A-Law Compressor 模块对输入信号实现 A-law 压缩器。A-law 压缩器的公式为

y={A|x|1+logAsgn(x)for 0≤|x|≤VAV(1+log(A|x|/V))1+logAsgn(x)for VA<|x|≤V

其中 *A* 是压缩器的 A-law 参数，
*V* 是 *x* 的峰值信号幅度，log 是自然对数，*sgn* 是 `sign` 函数。

最常用的 *A* 值是 87.6。

输入可以具有任意形状或帧状态。此模块独立处理每个向量元素。
