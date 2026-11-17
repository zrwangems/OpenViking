---
type: simulink-block
title: 'Mu-Law Expander'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Source Coding'
documentation_page: 'mulawexpander'
documentation_source_path: 'ref/mulawexpander.html'
language: zh-CN
chinese_source: worker-translation
---

# Mu-Law Expander

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

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

实现用于信源编码的 µ-law 扩展器

Mu-Law Expander 模块恢复由 Mu-Law Compressor 模块压缩的数据。µ-law 扩展器的公式如下所示，它是压缩器函数的反函数。

x=Vμ(e|y|log(1+μ)/V−1)sgn(y)

输入可以具有任意形状或帧状态。此模块独立处理每个向量元素。
