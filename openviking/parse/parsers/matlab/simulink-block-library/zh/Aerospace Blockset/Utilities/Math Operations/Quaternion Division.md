---
type: simulink-block
title: 'Quaternion Division'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'quaterniondivision'
documentation_source_path: 'quaterniondivision.html'
language: zh-CN
chinese_source: worker-translation
---

# Quaternion Division

## 端口
```yaml
ports:
- name: q
  summary: 被除四元数 四元数 | 四元数向量
  direction: input
  data_types: double
- name: r
  summary: 除数四元数 四元数 | 四元数向量
  direction: input
  data_types: double
- name: q/r
  summary: 输出四元数 四元数 | 向量
  direction: output
  data_types: double
```

### 输入

### **q** — 被除四元数 四元数 | 四元数向量

被除四元数，形式为
[*q*0,
*p*0, ...,
*q*1,
*p*1, ... ,
*q*2,
*p*2, ... ,
*q*3,
*p*3, ...]，指定为
四元数或四元数向量。

**数据类型：** `double`

### **r** — 除数四元数 四元数 | 四元数向量

除数四元数，形式为
[*s*0,
*r*0, ...,
*s*1,
*r*1, ... ,
*s*2,
*r*2, ... ,
*s*3,
*r*3, ...]，指定为
四元数或四元数向量。

**数据类型：** `double`
### 输出

### **q/r** — 输出四元数 四元数 | 向量

输出四元数或除法得到的四元数向量。

**数据类型：** `double`
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Aerospace Blockset / Utilities / Math Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将一个四元数除以另一个四元数

Quaternion Division 模块将一个给定的四元数除以另一个四元数。Aerospace Blockset™ 使用按标量优先约定定义的四元数。输出为除法得到的四元数或除法得到的四元数向量。有关所使用的四元数形式，请参见算法。
