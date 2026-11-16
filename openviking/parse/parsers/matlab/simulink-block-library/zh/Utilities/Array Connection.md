---
type: simulink-block
title: 'Array Connection'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'arrayconnection'
documentation_source_path: '../simscape/ref/arrayconnection.html'
language: zh-CN
chinese_source: worker-translation
---

# Array Connection

## 端口

### 守恒

### **elementNodek** — 用于拼接连接端口的元素连接节点 *k*

由 **Domain** 参数定义的类型的连接端口。此端口表示要拼接的元素，其中 *k* 是范围 [1, *N*] 中的整数。此类端口的数量 *N* 等于 **Number of elements** 参数设置的值（或者，对于标量连接，等于 **Number of scalar elements** 参数设置的值）。这些端口全部位于模块图标的同一侧，并标记为 **1**、**2**，依此类推，直到 *N*。

### **arrayNode** — 拼接后的节点数组 AON 端口

由 **Domain** 参数定义的类型的拼接 AON 端口，位于模块图标上与元素端口相对的一侧。此端口没有标签。

## 参数

### **Domain** — 指定模块连接的域 `Electrical Domain`（默认） | Foundation 域和已注册自定义域的列表 | `<specify domain path>`

指定模块连接的域。您可以从域列表中选择，或使用 `<specify domain path>` 选项并键入自定义域名。自定义域必须位于当前文件夹、位于 MATLAB® 路径上的文件夹中，或位于命名空间中。如果自定义域位于命名空间中，请包含从顶层命名空间文件夹开始的完整路径。命名空间顶层文件夹必须位于当前文件夹或位于 MATLAB 路径上的文件夹中。

### **Concatenate dimension** — 沿其拼接元素节点的数组维度 `2`（默认） | 正标量

指定沿其拼接元素标量或数组的维度：

- `1` — 垂直拼接元素。垂直数组拼接会将元素在拼接后的数组中上下堆叠。
- `2` — 水平拼接元素。水平数组拼接会将元素在拼接后的数组中并排放置。
- `3` 或更大 — 对元素数组执行多维拼接。

元素数组必须具有兼容的大小才能进行拼接。垂直拼接要求元素数组具有相同的列数。水平拼接要求元素数组具有相同的行数。多维拼接要求元素数组除沿其拼接的维度外，所有维度的大小都相同。

### **Mode** — 指定元素节点是标量还是数组 `Scalar Elements`（默认） | `Sized Elements`

指定拼接模式：

- `Scalar Elements` — 当所有被拼接的元素节点都是标量时，可以使用此简化模式。在此模式下，只需指定元素数量，并选择垂直还是水平拼接它们。默认情况下，**Concatenate dimension** 为 `2`，这意味着模块水平拼接元素。要垂直拼接它们，请将 **Concatenate dimension** 参数设置为 `1`。
- `Sized Elements` — 在此模式下，被拼接的元素节点可以是数组或标量。指定元素数量和每个元素的大小，模块会根据 **Concatenate dimension** 参数值执行数组拼接。

### **Number of scalar elements** — 要拼接的标量元素节点数量 `2`（默认） | 正整数

指定要拼接的标量元素节点数量。此数量定义模块图标上的元素端口数量。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Scalar Elements`。

### **Number of elements** — 要拼接的非标量元素节点数量 `2`（默认） | 正标量

指定要拼接的非标量元素节点数量。此数量定义模块图标上的元素端口数量，以及模块对话框中的 **Element size k** 参数数量。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Sized Elements`。

### **Element size k** — 连接节点 *k* 中的数组大小 `[1,1]`（默认） | array

连接节点 *k* 中的元素大小，其中 *k* 是范围 [1, **Number of elements**] 中的整数。此类参数的数量等于为 **Number of elements** 参数设置的值。

#### 依赖关系

要启用此组参数，请将 **Mode** 参数设置为 `Sized Elements`。

## 所属库

Simscape / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

将守恒连接数组拼接为单个节点数组端口

Array Connection 模块将守恒连接数组拼接为单个节点数组（AON）端口。此模块充当 Simscape™ 守恒连接的多路复用器，将模块一侧的所有元素拼接为另一侧的单个 AON 端口。

物理连接线无方向性，因此，该模块可以同时充当守恒连接的多路复用器和多路分用器。例如，可以通过捆绑多个同类型连接，并让两个 Array Connection 模块彼此相对、其 AON 端口相连，来简化模型图。还可以使用 Array Connection 模块连接不同大小的 AON 端口中的单个元素或元素子集。
