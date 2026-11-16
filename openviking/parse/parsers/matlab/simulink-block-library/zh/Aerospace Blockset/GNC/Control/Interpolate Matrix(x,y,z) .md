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

### 输入

### **x\_k** — 第一插值索引标量

第一插值索引 *i*，指定为标量。

**数据类型：** `double`

### **x\_f** — 第一插值分数标量

第一插值分数 *λ x*，指定为标量。

**数据类型：** `double`

### **y\_k** — 第二插值索引标量

第二插值索引 *j*，指定为标量。

**数据类型：** `double`

### **y\_f** — 第二插值分数标量

第二插值分数 *λ y*，指定为标量。

**数据类型：** `double`

### **z\_k** — 第三插值索引标量

第三插值索引 *k*，指定为标量。

**数据类型：** `double`

### **z\_f** — 第三插值分数标量

第三插值分数 *λ z*，指定为标量。

**数据类型：** `double`

### 输出

### **Matrix(x,y,z)** — 插值矩阵，矩阵

插值矩阵，指定为矩阵。

**数据类型：** `double`

## 参数

### **Matrix to interpolate** — 要插值的矩阵 `matrix`（默认）

要插值的矩阵，具有五个索引，其中第三、第四和第五个索引标记 *x*、*y* 和 *z* 的插值值。

#### 编程用法

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

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

返回给定输入的插值矩阵

Interpolate Matrix(x,y,z) 模块对三维矩阵数组进行插值。

此三维情况假定矩阵定义为三个独立变量的函数：

*x* = [ *x*1 *x*2 *x*3 ... *x*i *x*i+1 ... *x*n ]

*y* = [ *y*1 *y*2 *y*3 ... *y*j *y*j+1 ... *y*m ]

*z* = [ *z*1 *z*2 *z*3 ... *z*k *z*k+1 ... *z*p ]

对于给定的 *x*、*y* 和 *z* 值，将插值八个矩阵。然后对于

*x*i < x < *x*i+1

*y*j < y < *y*j+1

*z*k < z < *z*k+1

输出矩阵由下式给出

(1−λz){(1−λy)[(1−λx)M(xi,yj,zk)+λxM(xi+1,yj,zk)]             +λy[(1−λx)M(xi,yj+1,zk)+λxM(xi+1,yj+1,zk)]}   +λz{(1−λy)[(1−λx)M(xi,yj,zk+1)+λxM(xi+1,yj,zk+1)]            +λy[(1−λx)M(xi,yj+1,zk+1)+λxM(xi+1,yj+1,zk+1)]}

其中三个插值分数表示为

λx=(x−xi)/(xi+1−xi)λy=(y−yj)/(yj+1−yj)λz=(z−zk)/(zk+1−zk)

在三维情况下，插值首先对 *x* 进行，然后对 *y*，最后对 *z*。

要插值的矩阵应为五维矩阵，前两个维度对应于每个 *x*、*y* 和 *z* 值处的矩阵。例如，如果您有八个矩阵 *A*、*B*、*C*、*D*、*E*、*F*、*G* 和 *H*，它们定义在以下 *x*、*y* 和 *z* 值处，则对应的输入矩阵由下式给出

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
