---
type: simulink-block
title: 'Interpolate Matrix(x,y,z)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'GNC / Control'
documentation_page: 'interpolatematrixxyz'
documentation_source_path: 'interpolatematrixxyz.html'
language: zh-CN
chinese_source: worker-translation
---

# Interpolate Matrix(x,y,z)

## 端口
```yaml
ports:
- name: x_k
  summary: 第一个插值索引 标量
  direction: input
  data_types: double
- name: x_f
  summary: 第一个插值分数 标量
  direction: input
  data_types: double
- name: y_k
  summary: 第二个插值索引 标量
  direction: input
  data_types: double
- name: y_f
  summary: 第二个插值分数 标量
  direction: input
  data_types: double
- name: z_k
  summary: 第三个插值索引 标量
  direction: input
  data_types: double
- name: z_f
  summary: 第三个插值分数 标量
  direction: input
  data_types: double
- name: Matrix(x,y,z)
  summary: 插值后的矩阵 矩阵
  direction: output
  data_types: double
```

### 输入

### **x\_k** — 第一个插值索引 标量

第一个插值索引 *i*，指定为标量。

**数据类型：** `double`

### **x\_f** — 第一个插值分数 标量

第一个插值分数 *λ x*，指定为标量。

**数据类型：** `double`

### **y\_k** — 第二个插值索引 标量

第二个插值索引 *j*，指定为标量。

**数据类型：** `double`

### **y\_f** — 第二个插值分数 标量

第二个插值分数 *λ y*，指定为标量。

**数据类型：** `double`

### **z\_k** — 第三个插值索引 标量

第三个插值索引 *k*，指定为标量。

**数据类型：** `double`

### **z\_f** — 第三个插值分数 标量

第三个插值分数 *λ z*，指定为标量。

**数据类型：** `double`
### 输出

### **Matrix(x,y,z)** — 插值后的矩阵 矩阵

插值后的矩阵，指定为矩阵。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Matrix to interpolate
  summary: 要插值的矩阵 matrix（默认值）
  group: ''
  block_parameter: matrix
  type: character vector
  values: matrix
  default: '''matrix'''
```

### **Matrix to interpolate** — 要插值的矩阵 `matrix`（默认值）

要插值的矩阵，具有五个索引，其中第三、第四和第五个索引分别标记 *x*、*y* 和 *z* 的插值取值。

#### 编程使用

|  |
| --- |
| **模块参数**：`matrix` |
| **类型**：character vector |
| **值**：matrix |
| **默认值**：`'matrix'` |
## 所属库

Aerospace Blockset / GNC / Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

为给定输入返回插值后的矩阵

Interpolate Matrix(x,y,z) 模块对三维矩阵数组进行插值。

此三维情况假设矩阵定义为三个自变量的函数：

*x*
= [ *x*
1
*x*
2
*x*
3
... *x*
i
*x*
i+1
... *x*
n
]

*y*
= [ *y*
1
*y*
2
*y*
3
... *y*
j
*y*
j+1
... *y*
m
]

*z*
= [ *z*
1
*z*
2
*z*
3
... *z*
k
*z*
k+1
... *z*
p
]

对于给定的 *x*、*y* 和 *z* 值，对八个矩阵进行插值。然后对于

*x*
i
 *< x < x*
i+1

*y*
j
 *< y < y*
j+1

*z*
k
 *< z < z*
k+1

输出矩阵由下式给出

(1−λz){(1−λy)[(1−λx)M(xi,yj,zk)+λxM(xi+1,yj,zk)]             +λy[(1−λx)M(xi,yj+1,zk)+λxM(xi+1,yj+1,zk)]}   +λz{(1−λy)[(1−λx)M(xi,yj,zk+1)+λxM(xi+1,yj,zk+1)]            +λy[(1−λx)M(xi,yj+1,zk+1)+λxM(xi+1,yj+1,zk+1)]}

其中三个插值分数表示为

λx=(x−xi)/(xi+1−xi)λy=(y−yj)/(yj+1−yj)λz=(z−zk)/(zk+1−zk)

在三维情况下，插值首先在 *x* 上进行，然后在 *y* 上进行，最后在 *z* 上进行。

要插值的矩阵应为五维，前两个维度对应于每个 *x*、*y* 和 *z* 取值处的矩阵。例如，如果您有八个矩阵 *A*、*B*、*C*、*D*、*E*、*F*、*G* 和 *H*，它们定义在以下 *x*、*y* 和 *z* 取值处，则相应的输入矩阵由下式给出

|  |  |
| --- | --- |
| `(x = 0.0,y = 1.0,z = 0.1)` | `matrix(:,:,1,1,1) = A;` |
| `(x = 0.0,y = 1.0,z = 0.5)` | `matrix(:,:,1,1,2) = B;` |
| `(x = 0.0,y = 3.0,z = 0.1)` | `matrix(:,:,1,2,1) = C;` |
| `(x = 0.0,y = 3.0,z = 0.5)` | `matrix(:,:,1,2,2) = D;` |
| `(x = 1.0,y = 1.0,z = 0.1)` | `matrix(:,:,2,1,1) = E;` |
| `(x = 1.0,y = 1.0,z = 0.5)` | `matrix(:,:,2,1,2) = F;` |
| `(x = 1.0,y = 3.0,z = 0.1)` | `matrix(:,:,2,2,1) = G;` |
| `(x = 1.0,y = 3.0,z = 0.5)` | `matrix(:,:,2,2,2) = H;` |
