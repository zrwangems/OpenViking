---
type: simulink-block
title: 'Image Pad'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'imagepad'
documentation_source_path: 'ref/imagepad.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Pad

## 端口
```yaml
ports:
- name: I
  summary: 输入图像矩阵 | 数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: PVal
  summary: 填充值标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Port_1
  summary: 输出图像矩阵 | 数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **I** — 输入图像矩阵 | 数组

输入图像，指定为 *M*×*N* 矩阵或 *M*×*N*×*P* 数组，其中 *P* 是输入图像中的颜色平面数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **PVal** — 填充值标量

填充值，指定为标量。该模块将此值用于添加到输入图像的行或列的每个元素。

#### 依赖关系

要启用此端口，请将 **Method** 参数设置为 `Constant`，并将 **Pad value source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像，以填充后的矩阵或数组形式返回。输出图像的维度由 **Specify** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Method
  summary: 填充方法 Constant（默认）| Replicate | Symmetric | Circular
  group: ''
- name: Pad value source
  summary: 常量填充值的来源 Specify via dialog（默认）| Input port
  group: ''
- name: Pad value
  summary: 填充值 0（默认）| 标量
  group: ''
- name: Specify
  summary: 填充尺寸指定格式 Pad size（默认）| Output size
  group: ''
- name: Add columns to
  summary: 列填充位置 Left（默认）| Right | Both left and right | No padding
  group: ''
- name: Output column mode
  summary: 输出列尺寸确定方法 User-specified（默认）| Next power of two
  group: ''
- name: Number of output columns
  summary: 输出图像中的列数 10（默认）| 正整数
  group: ''
- name: Number of added columns
  summary: 添加到输入图像的列数 2（默认）| 正整数 | 正整数二元向量
  group: ''
- name: Add rows to
  summary: 行填充位置 Top（默认）| Bottom | Both top and bottom | No padding
  group: ''
- name: Output row mode
  summary: 输出行尺寸确定方法 User-specified（默认）| Next power of two
  group: ''
- name: Number of output rows
  summary: 输出图像中的行数 12（默认）| 正整数
  group: ''
- name: Number of added rows
  summary: 添加到输入图像的行数 [2 3]（默认）| 正整数 | 正整数二元向量
  group: ''
- name: Action when truncation occurs
  summary: 输入信号被截断时的操作 None（默认）| Warning | Error
  group: ''
```

### **Method** — 填充方法 `Constant`（默认）| `Replicate` | `Symmetric` | `Circular`

使用以下方法之一填充图像：

- `Constant` — 使用常量值填充图像。请参阅使用常量值填充。
- `Replicate` — 通过重复输入图像的边界值来填充图像。请参阅通过重复边界值填充。
- `Symmetric` — 使用输入数据的镜像来填充图像。请参阅使用镜像填充。
- `Circular` — 使用输入图像中元素的循环重复来填充图像。请参阅使用元素循环重复填充。

### **Pad value source** — 常量填充值的来源 `Specify via dialog`（默认）| `Input port`

将填充来源指定为 `Specify via dialog` 或 `Input port`。

- `Specify via dialog` — 使用 **Pad value** 参数指定填充值。
- `Input port` — 使用 **PVal** 输入端口指定填充值。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Constant`。

### **Pad value** — 填充值 `0`（默认）| 标量

指定用于填充图像的标量值。

#### 依赖关系

要启用此参数，请将 **Method** 参数设置为 `Constant`，并将 **Pad value source** 参数设置为 `Specify via dialog`。

### **Specify** — 填充尺寸指定格式 `Pad size`（默认）| `Output size`

从以下两个选项中选择如何指定图像填充的尺寸：

- `Pad size` — 分别使用 **Number of added columns** 和 **Number of added rows** 参数指定用于填充图像的列数和行数。
- `Output size` — 使用 **Output row mode**、**Number of output rows**、**Output column mode** 和 **Number of output columns** 参数的组合指定填充后输出图像的尺寸。

### **Add columns to** — 列填充位置 `Left`（默认）| `Right` | `Both left and right` | `No padding`

选择在输入图像的哪些侧添加列进行填充：

- `Left` — 在输入图像的左侧添加列。
- `Right` — 在输入图像的右侧添加列。
- `Both left and right` — 在输入图像的左侧和右侧都添加列。
- `No padding` — 不向输入图像添加列。

### **Output column mode** — 输出列尺寸确定方法 `User-specified`（默认）| `Next power of two`

使用以下选项之一指定输出图像中的列数：

- `User-specified` — 使用 **Number of output columns** 参数指定输出图像中的列数。
- `Next power of two` — 向输入图像添加列，直到总列数为 2 的幂。

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Output size`。

### **Number of output columns** — 输出图像中的列数 `10`（默认）| 正整数

将输出图像中的列数指定为正整数 *M*。如果此参数的值小于输入图像中的列数，则输出图像仅包含输入图像的最后 *M* 列。

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Output size`，并将 **Output column mode** 参数设置为 `User-specified`。

### **Number of added columns** — 添加到输入图像的列数 `2`（默认）| 正整数 | 正整数二元向量

指定要向输入信号添加多少列。此参数的行为取决于您是仅填充图像的一侧还是两侧。

| **Add columns to** | **Number of added columns** | 描述 |
| --- | --- | --- |
| `Left` | *P* | 在输入图像的左侧添加 *P* 列。 |
| `Right` | *Q* | 在输入图像的右侧添加 *Q* 列。 |
| `Both left and right` | [*P Q*] | 在输入图像的左侧添加 *P* 列，右侧添加 *Q* 列。 |

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Pad size`，并将 **Add columns** to 参数设置为 `Left`、`Right` 或 `Both left and right`。

### **Add rows to** — 行填充位置 `Top`（默认）| `Bottom` | `Both top and bottom` | `No padding`

选择在输入图像的哪些侧添加行进行填充：

- `Top` — 在输入图像的顶部添加行。
- `Bottom` — 在输入图像的底部添加行。
- `Both top and bottom` — 在输入图像的顶部和底部都添加行。
- `No padding` — 不向输入图像添加行。

### **Output row mode** — 输出行尺寸确定方法 `User-specified`（默认）| `Next power of two`

使用以下选项之一指定输出图像中的行数：

- `User-specified` — 使用 **Number of output rows** 参数指定输出图像中的行数。
- `Next power of two` — 向输入图像添加行，直到总行数为 2 的幂。

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Output size`。

### **Number of output rows** — 输出图像中的行数 `12`（默认）| 正整数

将输出图像中的行数指定为正整数 *N*。如果此参数的值小于输入图像中的行数，则输出图像仅包含输入图像的最后 *N* 行。

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Output size`，并将 **Output row mode** 参数设置为 `User-specified`。

### **Number of added rows** — 添加到输入图像的行数 `[2 3]`（默认）| 正整数 | 正整数二元向量

指定要向输入信号添加多少行。此参数的行为取决于您是仅填充图像的一侧还是两侧。

| **Add rows to** | **Number of added rows** | 描述 |
| --- | --- | --- |
| `Top` | *R* | 在输入图像的顶部添加 *R* 行。 |
| `Bottom` | *S* | 在输入图像的底部添加 *S* 行。 |
| `Both top and bottom` | [*R S*] | 在输入图像的顶部添加 *R* 行，底部添加 *S* 行。 |

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Pad size`，并将 **Add rows** to 参数设置为 `Top`、`Bottom` 或 `Both top and bottom`。

### **Action when truncation occurs** — 输入信号被截断时的操作 `None`（默认）| `Warning` | `Error`

您可以将输入信号被截断时模块的行为指定为以下选项之一：

- `None` — 信号被截断时不通知您。
- `Warning` — 输入信号被截断时在 MATLAB® 命令窗口中显示警告消息。
- `Error` — 输入信号被截断时显示错误对话框并终止仿真。

#### 依赖关系

要启用此参数，请将 **Specify** 参数设置为 `Output size`。
## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

通过添加行、列或两者来填充图像

Image Pad 模块通过填充图像的行、列或两者来扩展图像的维度。
