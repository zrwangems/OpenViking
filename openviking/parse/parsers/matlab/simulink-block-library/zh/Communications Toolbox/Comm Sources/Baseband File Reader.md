---
type: simulink-block
title: 'Baseband File Reader'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources'
documentation_page: 'basebandfilereader'
documentation_source_path: 'ref/basebandfilereader.html'
language: zh-CN
chinese_source: worker-translation
---

# Baseband File Reader

## 端口

### 输出

### **Data** — 基带信号标量 | 向量 | 矩阵

基带信号，以标量、向量或矩阵形式返回。该信号从 **基带文件名** 参数指定的文件中读取。采样时间可以从文件继承，也可以通过 **采样时间 (s)** 参数设置。

**数据类型：** `double`
**复数支持：** Yes

### **EOF** — 文件结束指示符逻辑标量

文件结束指示符，以逻辑标量形式返回。当 **重复读取文件** 参数为 `false` 且整个文件已读取完毕时，输出为 `true`。要启用此端口，请选择 **输出文件结束指示符** 参数。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **基带文件名** — 要读取的基带文件名 `example.bb`（默认） | 字符向量

要读取的基带文件名，指定为字符串标量或字符向量。

- 点击 **Browse** 以定位要读取的基带文件。
- 点击 **File Info** 以显示以下信息：

  - 文件名，包括绝对路径
  - 采样率
  - 中心频率
  - 样本数
  - 通道数
  - 数据类型
  - 任何元数据字段

    - - 如果文件没有描述性数据，此属性为空结构体。
      - 如果 Baseband File Writer 通过函数调用定义了对象，则 bb-file 存储该函数调用。Baseband File Reader 执行该函数调用以显示对象。

        - 如果已获得使用与该功能关联的软件的许可，则元数据输出包含对象内容。
        - 如果未获得使用与该功能关联的软件的许可，则元数据输出包含字符串，而不是对象内容。

### **从文件继承采样时间** — 选择采样时间的来源 `on`（默认） | `off`

选择此复选框以从 **基带文件名** 指定的文件继承采样时间。

### **采样时间 (s)** — 模块采样时间 `1`（默认） | 正标量

以正标量指定模块采样时间，单位为秒。要启用此参数，请清除 **从文件继承采样时间** 复选框。

### **每帧采样数** — 每个输出帧的样本数 `100`（默认） | 正整数标量

每个输出帧的样本数，指定为正整数或 `inf`。当此参数为 `inf` 时，输出帧包含基带文件中的所有样本。

### **重复读取文件** — 从文件连续循环数据 `off`（默认） | `on`

选择此复选框以重复读取基带文件的内容。当到达文件末尾时：

- 如果未选择 **重复读取文件** 参数（`off`），模块输出零。
- 如果选择了 **重复读取文件** 参数（`on`），模块从文件开头输出样本。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时更慢。在此模式下，可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Comm Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2024a: 支持从元数据读取对象

Baseband File Reader 模块现在支持从保存的元数据中读取对象和结构的结构。

## 描述

从文件读取基带信号

Baseband File Reader 模块从基带文件中读取信号。基带文件是由 Baseband File Writer 模块写入的一种特定类型的二进制文件。基带信号通常从非零中心频率下变频到 0 Hz。该模块会自动读取采样率、中心频率、通道数以及任何描述性数据。
