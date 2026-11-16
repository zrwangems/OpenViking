---
type: simulink-block
title: 'Connection Port'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'connectionport'
documentation_source_path: 'ref/connectionport.html'
language: zh-CN
chinese_source: worker-translation
---

# Connection Port

## 端口

### Conserving

### **Port\_1** — Connection port 无类型连接端口

物理建模连接端口。默认情况下，此端口是无类型的。

您可以通过将端口连接到另一个模块的 conserving 端口或 physical signal 端口，或者连接到 Simscape Bus 端口，来定义该端口的类型。建立连接后，父 Subsystem 模块上的端口外观会相应改变，端口会变为有类型，并且只能连接到相同类型的端口。

## 参数

### **端口号** — 子系统连接器标签 `1`（默认） | 表示整数的字符串

为该模块创建的子系统连接器端口添加标签。每个连接器端口都需要一个唯一编号作为标签。如果您未对父子系统进行封装并使用默认模块名称，则此参数的值会显示为父 Subsystem 模块图标上相应端口旁边的标签。如果您更改 Connection Port 模块的名称，则该模块名称会显示为父 Subsystem 模块图标上相应端口旁边的标签。您也可以使用封装来更改子系统端口名称。有关详细信息，请参阅 Masking Fundamentals。

第一个端口的默认值为 `1`。随着您创建更多端口，软件会递增地为其添加标签。如果将端口移动到 Subsystem 模块图标上的其他位置，Simulink Editor 可能会根据其规则对端口重新编号。在这种情况下，相应 Connection Port 模块的 **端口号** 参数值会自动更改，以匹配新的端口编号。

### **父子系统上的端口位置** — 子系统模块图标上的连接器端口位置 `Left`（默认） | `Right`

选择端口位于父子系统模块的哪一侧：`Left` 或 `Right`。如果将端口移动到 Subsystem 模块图标上的其他位置，参数值会自动更改以反映新位置。有关详细信息，请参阅子系统模块上的端口命名和位置。

### **连接类型** — 指定或移除刚性接口 `Inherit: auto`（默认） | `Bus: <object name>` | `CompositeConnection: <domain name>` | `ConnectionBus` 对象、Foundation 域和 Simscape Multibody 连接类型的列表

通过从下拉列表中选择端口类型来指定刚性接口。该列表包含基础工作区或数据字典中存在的 Foundation 域、Simscape Multibody 连接类型和 `ConnectionBus` 对象的名称。为了获得更细粒度的控制，请点击下拉列表旁边的 **显示类型助手** 按钮以显示 **类型助手** 面板。您还可以使用 **类型助手** 面板指定到复合域的刚性连接。

有关详细信息，请参阅指定刚性接口和自定义复合域示例。

要移除刚性接口规范，请将 **连接类型** 参数设置为 `Inherit: auto`。

### **模式** — 指定连接模式 `Inherit`（默认） | `Connection Bus object` | `Connection` | `Composite domain`

与 **连接类型** 参数配合使用，并提供用于指定刚性接口的附加选项：

- `Inherit` — 表示灵活接口。唯一可用的下拉选项是 `auto`。对应于 **连接类型** 参数的设置 `Inherit: auto`。
- `Connection Bus object` — 指定刚性总线连接。在 `<object name>` 字段中键入现有 `ConnectionBus` 对象的名称，或使用 **编辑** 按钮打开类型编辑器并创建或修改 `ConnectionBus` 对象。在这种情况下，Connection Port 模块只能连接到 Simscape Bus 模块的总线（bundle）端口。
- `Connection` — 通过从下拉列表中选择域名或 Simscape Multibody 连接类型来指定刚性连接类型。对话框底部的 **Simscape 域** 链接允许您查看 Foundation 域名和特定于域的线型列表。
- `Composite domain` — 指定到复合域的刚性连接。在 `<domain name>` 字段中键入现有复合域的名称。对应于 **连接类型** 参数的设置 `CompositeConnection: <domain name>`。

#### 依赖关系

要启用此选择，请点击 **连接类型** 参数旁边的 **显示类型助手** 按钮。当您在 **类型助手** 面板中选择值时，**连接类型** 参数设置会相应更新。

## 所属库

Simulink / Signal Routing Simscape / Utilities Powertrain Blockset / Utilities / Simscape RF Blockset / Equivalent Baseband / Input RF Blockset / Circuit Envelope / Utilities Vehicle Dynamics Blockset / Utilities / Simscape

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

用于子系统的物理建模连接器端口

Connection Port 模块跨子系统边界传输物理连接或信号。物理连接包括 Simscape™ conserving 和 physical signal 连接、Simscape Multibody™ 连接以及 Vehicle Dynamics Blockset™ 双向连接端口等。此模块的功能与 Simulink® 库中的 Inport 和 Outport 模块类似。

对于每条穿越子系统边界的物理连接线，子系统都需要一个 Connection Port 模块。您可以手动将 Connection Port 模块放置在子系统内，或者当您在现有网络中创建子系统时，Simulink 可以自动插入 Connection Port 模块。

### 子系统模块上的端口外观

Connection Port 模块会向父 Subsystem 模块添加一个端口。端口类型取决于它传输的连接或信号。Subsystem 模块上的端口外观与 Connection Port 模块在子系统内部所连接的端口匹配。例如，如果该端口传输 Simscape conserving 连接，则它在 Subsystem 模块上显示为 Simscape conserving 端口。

考虑一个带有分别标记为 **In** 和 **Out** 的 Simulink 输入和输出端口的子系统。如果您将一个 Connection Port 模块放置在此子系统内并使其保持未连接，则父 Subsystem 模块上的连接端口会显示为白色圆圈。

已将 Connection Port 模块添加到子系统的框图

子系统图标上连接端口的外观

但是，如果您将 Connection Port 模块连接到 Mass 模块，则父 Subsystem 模块上连接端口的外观会变为 conserving 端口。

Connection Port 模块连接到 Mass 模块的框图

子系统图标上连接端口的已更改外观

连接端口会变为 mechanical translational 类型，也就是说，您只能将其他模块上的 mechanical translational 端口连接到此子系统端口。

### 子系统模块上的端口命名和位置

与 Simulink 输入和输出端口类似，当端口模块使用默认名称时，子系统图标上的连接端口会显示端口编号而不是模块名称。如果您将具有默认名称和参数的 Connection Port 模块添加到子系统，则连接端口会以 **端口号** 参数值作为标签，并位于父 Subsystem 模块图标的左侧。

连接端口显示在子系统图标的左侧

要将端口切换为显示在图标的右侧，请将 **父子系统上的端口位置** 参数值更改为 `Right`。

连接端口显示在子系统图标的右侧

Simulink Editor 中的灵活端口放置允许您通过沿模块图标轮廓点击并拖动端口来移动端口，这样您可以将端口放在 Subsystem 模块的任意一侧，包括顶部和底部。**父子系统上的端口位置** 参数没有单独的顶部或底部值。如果将端口拖动到 Subsystem 模块图标上的其他位置，参数值会自动更改以反映新位置：

- `Left` — 端口显示在子系统图标的左侧或顶部。
- `Right` — 端口显示在子系统图标的右侧或底部。

如果有多个连接端口，则在每次移动后，端口索引会根据需要自动重新编号，以反映新的端口位置。例如，如果 Subsystem 模块有三个连接端口（如图所示），并且您将端口 **2** 移动到模块图标的底部，则端口 **2** 和 **3** 会重新编号。这两个 Connection Port 模块的 **端口号** 参数值会自动更改，以匹配新的端口编号。

连接端口根据子系统模块图标上的位置重新编号

父 Subsystem 模块的方向也会影响端口位置。例如，如果您翻转父 Subsystem 模块，连接端口 **1** 会显示在与其 **父子系统上的端口位置** 参数所指示相反的一侧。

翻转子系统模块时连接端口的一侧会翻转

### 指定刚性接口

您可以通过应用刚性接口规范来锁定模块端口的连接类型。例如，您可以限制该模块仅接受来自其他模块上 mechanical translational 端口的连接。有关 Foundation 域类型的列表，请参阅特定于域的线型。如果您使用 `ConnectionBus` 对象应用刚性接口，则 Connection Port 模块只能连接到 Simscape Bus 模块的总线端口。

使用 **连接类型** 参数指定刚性接口，例如特定域类型或 `ConnectionBus` 对象。应用刚性接口定义后，模块外观会发生变化，如下所示：

1. 灵活连接
2. 刚性域连接
3. 刚性总线连接

不同连接类型的连接端口模块在模型图中的外观

要移除刚性接口规范，请将 **连接类型** 参数设置为 `Inherit: auto`。
