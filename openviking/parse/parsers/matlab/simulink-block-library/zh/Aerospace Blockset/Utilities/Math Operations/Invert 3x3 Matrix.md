---
type: simulink-block
title: 'Invert 3x3 Matrix'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Utilities / Math Operations'
documentation_page: 'invert3x3matrix'
documentation_source_path: 'invert3x3matrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Invert 3x3 Matrix

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入矩阵 3×3 矩阵
  direction: input
  data_types: double
- name: Port_1
  summary: 矩阵逆 3×3 矩阵
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入矩阵 3×3 矩阵

要求逆的输入矩阵，指定为 3×3 矩阵。

**数据类型：** `double`
### 输出

### **Port\_1** — 矩阵逆 3×3 矩阵

输入矩阵的矩阵逆，以 3×3 矩阵形式返回。

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

计算 3×3 矩阵的逆

Invert 3x3 Matrix 模块计算 3×3 矩阵的逆。

如果 *det*(*A*) = 0，则发生错误并停止仿真。
