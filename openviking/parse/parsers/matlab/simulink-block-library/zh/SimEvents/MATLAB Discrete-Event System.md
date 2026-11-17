---
type: simulink-block
title: 'MATLAB Discrete-Event System'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'SimEvents'
documentation_page: 'matlabdiscreteeventsystem'
documentation_source_path: 'ref/matlabdiscreteeventsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB Discrete-Event System

## 端口

R2025b 中未记录。

## 参数

### **System object name** — 指定 System object™ 的完整名称（character vector）

指定用户定义的离散事件 System object 类的完整名称，不带文件扩展名。此项区分大小写。类名必须存在于 MATLAB 路径上。

您可以通过以下方式之一指定离散事件 System object 名称：

- 在文本框中输入名称。
- 单击文本框附带的列表箭头。如果当前文件夹中存在有效的 System object，这些名称将出现在列表中。从此列表中选择一个 System object。
- 浏览到包含有效离散事件 System object 的文件夹。如果该文件夹不在您的 MATLAB 路径上，软件会提示您添加它。

如果您需要创建离散事件 System object，可以通过单击 **New** 从模板创建一个。

保存 SimEvents® System object 后，名称将出现在 **System object name** 文本框中。

使用用户定义的离散事件 System object 类名的完整名称。该模块不接受您已分配给离散事件 System object 类名的 MATLAB 变量。

#### 编程用法

|  |
| --- |
| **模块参数**: `System` |
| **类型**: character vector |
| **值**: `'<Enter System Class Name>'` | character vector |
| **默认值**: `'<Enter System Class Name>'` |

### **New** — 从模板 SimEvents System object 创建 SimEvents System object

单击此按钮以从模板创建 SimEvents System object。

选择以下选项之一。

- `Basic`

  启动 MATLAB Editor 并显示一个简单离散事件 System object 的模板，该模板使用最少的 System object 方法。

保存 SimEvents System object 后，您可以在 **System object name** 文本框中输入名称。

### **Simulate using** — 指定仿真模式 `Code generation`（默认）| `Interpreted execution`

将仿真模式指定为 `Code generation` 或 `Interpreted execution`。

- `Interpreted execution`

  此模式基于解释型 MATLAB 语言并在启用调试器的情况下仿真 System object。
- `Code generation`

  此代码生成模式可减少 SimEvents 模型的仿真时间。在首次模型运行时，MATLAB Discrete-Event System 模块仅使用支持代码生成的 MATLAB 函数来仿真并生成代码。如果 System object 代码和模块参数没有变化，后续模型运行不会重新生成代码。对于具有多个使用相同 System object 源文件的 MATLAB Discrete-Event System 模块的模型，MATLAB Discrete-Event System 模块还支持代码重用。有关详细信息，请参阅为 MATLAB Discrete-Event System 模块生成代码。

#### 编程用法

|  |
| --- |
| **模块参数**: `SimulateUsing` |
| **类型**: character vector |
| **值**: `'Code generation'` | `Interpreted execution` |
| **默认值**: `'Code generation'` |

## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

MATLAB 离散事件系统

MATLAB Discrete-Event System 模块允许您创建和编写自定义离散事件系统。使用此模块，您可以使用 MATLAB® 编写事件驱动的实体流系统，并将其用于 Simulink® 模型中。有关使用 MATLAB Discrete-Event System 模块实现 `matlab.DiscreteEventSystem` 类的详细信息，请参阅使用 MATLAB Discrete-Event System 模块创建自定义模块。

下面有六个示例，可帮助您学习如何使用 MATLAB Discrete-Event System 模块创建自定义模块。

1. 使用自定义 Entity Storage 模块延迟实体
2. 创建带迭代事件的自定义 Entity Storage 模块
3. 带多个定时器事件的自定义 Entity Storage 模块
4. 带信号输入和信号输出的自定义 Entity Generator 模块
5. 构建具有多个存储的自定义模块
6. 创建自定义 Resource Acquirer 模块
