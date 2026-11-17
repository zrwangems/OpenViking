---
type: simulink-block
title: 'MATLAB Discrete-Event System'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'matlabdiscreteeventsystem'
documentation_source_path: 'ref/matlabdiscreteeventsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB Discrete-Event System

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: System object name
  summary: 指定 System object™ 的完整名称 字符向量
  group: ''
  block_parameter: System
  type: character vector
  values: '''<Enter System Class Name>'' | character vector'
  default: '''<Enter System Class Name>'''
- name: New
  summary: 从模板创建 SimEvents System object SimEvents System object
  group: ''
- name: Simulate using
  summary: 指定仿真模式 Code generation（默认）| Interpreted execution
  group: ''
  block_parameter: SimulateUsing
  type: character vector
  values: '''Code generation'' | Interpreted execution'
  default: '''Code generation'''
```

### **System object name** — 指定 System object™ 的完整名称 字符向量

指定用户定义的离散事件 System object 类的完整名称，不带文件扩展名。此条目区分大小写。类名必须存在于 MATLAB 路径上。

您可以通过以下方式之一指定离散事件 System object 名称：

- 在文本框中输入名称。
- 点击文本框附带的列表箭头。如果当前文件夹中存在有效的 System object，名称将出现在列表中。从此列表中选择一个 System object。
- 浏览到包含有效离散事件 System object 的文件夹。如果该文件夹不在您的 MATLAB 路径上，软件会提示您添加它。

如果您需要创建离散事件 System object，可以通过点击 **New** 从模板创建一个。

保存 SimEvents® System object 后，名称将出现在 **System object name** 文本框中。

使用用户定义的离散事件 System object 类名的完整名称。该模块不接受您分配给离散事件 System object 类名的 MATLAB 变量。

#### 编程使用

|  |
| --- |
| **模块参数**：`System` |
| **类型**：character vector |
| **值**：`'<Enter System Class Name>'` | character vector |
| **默认值**：`'<Enter System Class Name>'` |

### **New** — 从模板创建 SimEvents System object SimEvents System object

点击此按钮从模板创建 SimEvents System object。

选择以下选项之一。

- `Basic`

  启动 MATLAB 编辑器并显示一个简单离散事件 System object 的模板，使用最少的 System object 方法。

保存 SimEvents System object 后，您可以在 **System object name** 文本框中输入名称。

### **Simulate using** — 指定仿真模式 `Code generation`（默认）| `Interpreted execution`

将仿真模式指定为 `Code generation` 或 `Interpreted execution`。

- `Interpreted execution`

  此模式基于解释型 MATLAB 语言仿真 System object，并启用调试器。
- `Code generation`

  此代码生成模式减少 SimEvents 模型的仿真时间。在首次模型运行时，MATLAB Discrete-Event System 模块仅使用支持代码生成的 MATLAB 函数进行仿真并生成代码。如果 System object 代码和模块参数未更改，后续模型运行不会重新生成代码。MATLAB Discrete-Event System 模块还支持对具有多个使用相同 System object 源文件的 MATLAB Discrete-Event System 模块的模型进行代码重用。有关详细信息，请参阅 Generate Code for MATLAB Discrete-Event System Blocks。

#### 编程使用

|  |
| --- |
| **模块参数**：`SimulateUsing` |
| **类型**：character vector |
| **值**：`'Code generation'` | `Interpreted execution` |
| **默认值**：`'Code generation'` |
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

MATLAB 离散事件系统模块允许您创建和编写自定义离散事件系统。使用此模块，您可以使用 MATLAB® 编写事件驱动的实体流系统，并在 Simulink® 模型中使用它。有关使用 MATLAB 离散事件系统模块实现 `matlab.DiscreteEventSystem` 类的更多信息，请参阅 Create Custom Blocks Using MATLAB Discrete-Event System Block。

下面有六个示例可帮助您学习如何使用 MATLAB 离散事件系统模块创建自定义模块。

1. 使用自定义实体存储模块延迟实体
2. 创建带迭代事件的自定义实体存储模块
3. 带多个定时器事件的自定义实体存储模块
4. 带信号输入和信号输出的自定义实体生成器模块
5. 构建带多个存储的自定义模块
6. Create a Custom Resource Acquirer Block
