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
```yaml
ports:
- name: Data
  summary: 基带信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
- name: EOF
  summary: 文件结束指示符 逻辑标量
  direction: output
```

### 输出

### **Data** — 基带信号 标量 | 向量 | 矩阵

基带信号，以标量、向量或矩阵形式返回。该信号从 **Baseband file name** 参数指定的文件中读取。采样时间可以从文件继承，也可以通过 **Sample Time (s)** 参数设置。

**数据类型：** `double`
**复数支持：** 是

### **EOF** — 文件结束指示符 逻辑标量

文件结束指示符，以逻辑标量形式返回。当 **Repeatedly read the file** 参数为 `false` 且整个文件已读取完毕时，输出为 `true`。要启用此端口，请选择 **Output end-of-file indicator** 参数。
## 参数
```yaml
parameters:
- name: Baseband file name
  summary: 要读取的基带文件名 example.bb（默认）| 字符向量
  group: ''
- name: Inherit sample time from file
  summary: 选择采样时间来源 on（默认）| off
  group: ''
- name: Sample time (s)
  summary: 模块采样时间 1（默认）| 正标量
  group: ''
- name: Samples per frame
  summary: 每个输出帧的采样点数 100（默认）| 正整数标量
  group: ''
- name: Repeatedly read the file
  summary: 连续循环读取文件数据 off（默认）| on
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### **Baseband file name** — 要读取的基带文件名 `example.bb`（默认）| 字符向量

要读取的基带文件名，指定为字符串标量或字符向量。

- 点击 **Browse** 定位要读取的基带文件。
- 点击 **File Info** 显示以下信息：

  - 文件名，包括绝对路径
  - 采样率
  - 中心频率
  - 采样点数
  - 通道数
  - 数据类型
  - 任何元数据字段

    - - 如果文件没有描述性数据，此属性为空结构体。
      - 如果基带文件写入器通过函数调用定义了对象，bb 文件会存储该函数调用。基带文件读取器执行该函数调用以显示对象。

        - 如果您拥有使用该功能相关软件的许可证，元数据输出包含对象内容。
        - 如果您没有使用该功能相关软件的许可证，元数据输出包含字符串而非对象内容。

### **Inherit sample time from file** — 选择采样时间来源 `on`（默认）| `off`

选中此复选框以从 **Baseband file name** 指定的文件中继承采样时间。

### **Sample time (s)** — 模块采样时间 `1`（默认）| 正标量

以秒为单位指定模块采样时间为正标量。要启用此参数，请清除 **Inherit sample time from file** 复选框。

### **Samples per frame** — 每个输出帧的采样点数 `100`（默认）| 正整数标量

每个输出帧的采样点数，指定为正整数或 `inf`。当此参数为 `inf` 时，输出帧包含基带文件中的所有采样点。

### **Repeatedly read the file** — 连续循环读取文件数据 `off`（默认）| `on`

选中此复选框以重复读取基带文件的内容。当到达文件末尾时：

- 如果未选择 **Repeatedly read the file** 参数（`off`），模块输出零。
- 如果选择了 **Repeatedly read the file** 参数（`on`），模块从文件开头输出采样点。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型发生变化，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

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

### R2024a：支持从元数据读取对象

Baseband File Reader 模块现在支持从保存的元数据中读取对象和结构体嵌套结构。

## 描述

从文件读取基带信号

Baseband File Reader 模块从基带文件中读取信号。基带文件是由 Baseband File Writer 模块写入的一种特定类型的二进制文件。基带信号通常从非零中心频率下变频到 0 Hz。该模块自动读取采样率、中心频率、通道数以及任何描述性数据。
