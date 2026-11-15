---
type: simulink-block
title: 'Reference Component'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Architectures, Requirements, and Allocations / Author Architecture Models'
documentation_page: 'referencecomponent'
documentation_source_path: 'ref/referencecomponent.html'
language: zh-CN
chinese_source: official
---

# Reference Component

## 端口

### 输入

### **Source** — 来自其他组件的输入连接 接口

如果连接到源组件，则端口上的接口是共享的。
### 输出

### **Destination** — 与其他组件的输出连接 接口

如果连接到目标组件，则端口上的接口是共享的。
### 物理

### **Physical** — 与另一个组件的物理连接 物理接口

如果连接到另一个组件，则端口上的物理接口是共享的。

## 参数

R2025b 官方文档未提供。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2019a 中推出**

## 描述

链接到架构定义或 Simulink 行为

使用 Reference Component 模块链接 System Composer™ 组件的架构定义、AUTOSAR 组件的结构定义或 Simulink® 行为。

为模块添加端口，以便与其他组件连接。为端口定义接口，使用构造型添加与组件相关的属性，并定义参数。

Reference Component block

添加或连接 System Composer 组件：

- 从**建模**选项卡或调色板中添加一个 Reference Component 模块。您也可以点击并拖动画布上的方框，然后选择 Reference Component 模块。

  **提示**

  您可以拖动将链接到模型或子系统的引用组件添加到 System Composer 模型中。从文件资源管理器中拖动模型或子系统文件，将引用组件添加到架构模型画布。

  例如，将 SLX 模型文件拖入架构模型画布，就会添加一个 Reference Component 模块，该模块将引用 SLX 文件中的模型。

  要拖动添加的文件必须位于 MATLAB® 路径下。不支持通过将文件从 MATLAB 编辑器拖入模型画布来创建引用组件。
- 双击 Reference Component 模块打开**模块参数**对话框，附加引用模型。
- 在 Reference Component 模块上添加和编辑端口。点击模块边缘添加端口，然后使用属性检查器重新命名端口。
- 要从 System Composer 架构模型导入共享数据字典，请在引用模型的模型资源管理器中，在**模型属性**下的**外部数据**选项卡上点击**浏览**。使用  接口编辑器为引用模型的端口分配接口并编辑接口定义。
- 点击并拖动任何端口即可创建连接。连接到另一个组件。您还可以创建一个新组件来完成连接。
- 要将 Reference Component 模块连接到架构或组合模型根端口，可从组件端口拖动到包含模型的边界。释放连接时，会在边界创建一个根端口。

**注意**

您可以为组件添加封装图标，以说明组件所代表的系统。有关详细信息，请参阅在组件上添加封装图标。

管理 Reference Component 模块内容：

- 创建 Reference Component 模块时，您可以选择右键点击该组件并选择**模块参数**。在这里，您可以指定引用模型或子系统名称（如果已经存在）。引用模型或子系统可以是 System Composer 架构、AUTOSAR 架构或 Simulink 模型或子系统。
- 要从 Reference Component 模块中添加或删除构造型，首先要使用配置文件编辑器将配置文件导入到引用的模型或子系统中。如果对引用组件应用了多个构造型，要更改构造型顺序，请参阅使用“管理配置文件”工具更改构造型顺序。
- 要断开 Reference Component 模块的引用链接，您可以选择右键点击并选择**内联模型**，这将删除指定组件引用的架构模型内容，并断开与引用模型的链接。Reference Component 模块变为普通的 Component 模块。

对于普通的 Component 模块，可以右键点击该模块并将其转换为引用组件。

- 要将组件内容保存为可在多处引用并保持同步的架构模型或子系统，请选择 **创建架构** > **架构**。该组件将成为链接到引用架构模型或子系统的引用组件。

  **注意**

  要在带有接口的架构子系统上键入端口，必须链接一个外部接口数据字典。架构子系统不包含模型工作区。有关详细信息，请参阅使用数据字典管理接口。
- 要将组件内容保存为软件架构模型，请选择 **创建架构** > **软件架构**。**创建架构**，然后选择**软件架构**。有关详细信息，请参阅将架构导出为软件架构。
- 要将组件内容保存为 AUTOSAR 架构模型，请选择 **创建架构** > **AUTOSAR 架构**。有关详细信息，请参阅从组件创建 AUTOSAR 架构。
- 要创建新的 Simulink 引用模型或子系统并与之链接，请选择 **创建行为** > **Simulink 行为**。有关详细信息，请参阅使用 Simulink 实现组件行为。
- 要链接到已知模型或子系统（可以是 System Composer 架构模型、Simulink 模型或 AUTOSAR 架构模型），请选择**链接到模型**。

**注意**

具有物理端口的组件不能保存为架构模型、模型引用、软件架构或 Stateflow® 图行为。具有物理端口的组件只能保存为子系统引用或子系统组件行为。
