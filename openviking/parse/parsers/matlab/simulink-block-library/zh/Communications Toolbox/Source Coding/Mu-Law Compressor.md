---
type: simulink-block
title: 'Mu-Law Compressor'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'mulawcompressor'
documentation_source_path: 'ref/mulawcompressor.html'
language: zh-CN
chinese_source: worker-translation
---

# Mu-Law Compressor

## 端口

R2025b 中未记录。

## 参数

**mu value**
:   压缩器的 µ-law 参数。

**Peak signal magnitude**
:   输入信号的峰值。这也是输出的峰值。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现用于信源编码的 µ-law 压缩器

Mu-Law Compressor 模块对输入信号实现 µ-law 压缩器。µ-law 压缩器的公式为

y=Vlog(1+μ|x|/V)log(1+μ)sgn(x)

其中 µ 是压缩器的 µ-law 参数，*V* 是 *x* 的峰值幅度，log 是自然对数，sgn 是符号函数（MATLAB® 中的 `sign`）。

输入可以具有任意形状或帧状态。该模块独立处理每个向量元素。
