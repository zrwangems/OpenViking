---
type: simulink-block
title: 'PS Ramp'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Sources'
documentation_page: 'psramp'
documentation_source_path: 'ref/psramp.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Ramp

## 端口
```yaml
ports:
- name: O
  summary: 输出物理信号，类型由模块参数值和单位决定 physical signal
  direction: output
```

### 输出

### **O** — 输出物理信号，类型由模块参数值和单位决定 physical signal

输出物理信号。信号单位由 **Initial output** 参数的单位决定。信号大小与 **Initial output** 和 **Slope** 参数值的大小一致。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **Description** 选项卡中的 **Source code** 链接，在底层源文件中查看此名称。
## 参数
```yaml
parameters:
- name: Slope
  summary: 信号增加或减少速率 1 1/s（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: Start time
  summary: 时间偏移 0 s（默认）| 标量
  group: ''
- name: Initial output
  summary: 初始信号值和单位 0 1（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: Enable zero-crossing detection
  summary: 是否启用过零检测 on（默认）| off
  group: ''
```

### **Slope** — 信号增加或减少速率 `1 1/s`（默认）| 标量 | 向量 | 矩阵

端口 **O** 处输出信号的增加或减少速率。第一个编辑框表示信号增加或减少速率值。您可以指定标量、向量或矩阵。默认情况下，该值为标量 `1`。如果您指定向量或矩阵，**Initial output** 也必须是相同大小的向量或矩阵，或者为标量。

您可以指定正值和负值。正值表示增加速率，负值表示减少速率。

第二个组合框表示单位。默认情况下，单位为 `1/s`。下拉列表包含一组标准单位。您可以选择一个单位，或输入所需的单位名称（如 `rpm`），或输入有效表达式（如 `m^2/s`）。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。指定的单位乘以时间单位后，必须与 **Initial output** 参数的单位一致。

### **Start time** — 时间偏移 `0 s`（默认）| 标量

信号开始增加或减少的时间。在仿真开始到 **Start time** 之间，模块的输出保持在 **Initial output** 值。

### **Initial output** — 初始信号值和单位 `0 1`（默认）| 标量 | 向量 | 矩阵

仿真开始时端口 **O** 处输出信号的值和单位。第一个编辑框表示信号值。您可以指定标量、向量或矩阵。默认情况下，该值为标量 `0`。如果您指定向量或矩阵，**Slope** 也必须是相同大小的向量或矩阵，或者为标量。

第二个组合框表示输出信号的单位。默认情况下，单位为 `1`（无量纲）。下拉列表包含一组标准单位。您可以选择一个单位，或输入所需的单位名称（如 `Pa`），或输入有效表达式（如 `m^2`）。有关更多信息以及单位缩写列表，请参阅 How to Specify Units in Block Dialogs 和 Unit Definitions。

### **Enable zero-crossing detection** — 是否启用过零检测 `on`（默认）| `off`

清除以禁用过零检测并提高仿真速度。有关更多信息，请参阅 Managing Zero Crossings in Simscape Models。
## 所属库

Simscape / Foundation Library / Physical Signals / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2025a：可选的过零检测

从 R2025a 开始，该模块包含 **Enable zero-crossing detection** 复选框。清除此复选框可以禁用过零检测并提高仿真速度。

## 描述

生成持续增加或减小的物理信号

PS Ramp 模块生成一个物理信号，该信号在指定的初始值处保持不变，然后在指定的时间开始，以指定的速率变化。**Slope**、**Start time** 和 **Initial output** 参数决定了输出信号的特性：

- **Initial output** 和 **Slope** 参数值决定了输出信号是标量、向量还是矩阵。如果其中之一是向量或矩阵，则另一个必须是相同大小的向量或矩阵，或者是标量。此时输出信号也是相同大小的向量或矩阵。
- **Initial output** 的单位决定了输出信号的单位。
- **Slope** 的单位乘以时间单位必须与 **Initial output** 的单位一致。

输出在 **Start time** 之前保持在 **Initial output**，然后根据 **Slope** 增加或减小：

- 正的 **Slope** 值表示增加速率。
- 负的 **Slope** 值表示减小速率。

下表展示了标量和非标量模块参数值的各种组合下的模块输出示例。

| 模块参数 | 输出 |
| --- | --- |
| **Slope** `[1 2; 3 4] m/s`  **Start time** `2 s`  **Initial input** `1 m` | 信号输出值图 |
| **Slope** `1 m/s`  **Start time** `2 s`  **Initial input** `[1 2; 3 4] m` | 信号输出值图 |
| **Slope** `[1 2; 3 4] m/s`  **Start time** `2 s`  **Initial input** `[1 2; 3 4] m` | 信号输出值图 |
