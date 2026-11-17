---
type: simulink-block
title: 'A-Law Expander'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'alawexpander'
documentation_source_path: 'ref/alawexpander.html'
language: zh-CN
chinese_source: worker-translation
---

# A-Law Expander

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

**A value**
:   压缩器的 A-law 参数。

**Peak signal magnitude**
:   输入信号的峰值。这也是输出信号的峰值。

将这些参数与对应的 A-Law Compressor 模块中的参数相匹配。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现用于信源编码的 A-law 扩展器

A-Law Expander 模块恢复 A-Law Compressor 模块压缩的数据。A-law 扩展器的公式如下所示，它是压缩器函数的反函数。

x={y(1+logA)Afor 0≤|y|≤V1+logAexp(|y|(1+logA)/V−1)VAsgn(y)for V1+logA<|y|≤V

输入可以具有任意形状或帧状态。此模块独立处理每个向量元素。
