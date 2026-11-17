---
type: simulink-block
title: 'Simscape Bus'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'simscapebus'
documentation_source_path: '../simscape/ref/simscapebus.html'
language: zh-CN
chinese_source: worker-translation
---

# Simscape Bus

## 端口

### 守恒

### **Bus** — Simscape Bus 端口总线

连接到 Simscape Bus 线路的端口，该线路表示一组守恒连接线。该组包含连接到模块另一侧的所有线路。

默认情况下，该另一侧没有端口。您可以通过将连接线拖到模块的该侧，或使用模块对话框来添加端口。进入子侧模块的元素可以是守恒连接线或 Simscape Bus 线路。每次在子侧添加端口时，相应的连接会添加到模块内部的连接列表中。

## 参数

### **Connection type** — 指定或移除刚性接口 `Inherit: auto`（默认）| `Bus: <object name>` | `CompositeConnection: <domain name>` | `ConnectionBus` 对象列表

通过从下拉列表中选择端口类型来指定刚性接口。该列表包含基础工作区或数据字典中存在的 `ConnectionBus` 对象的名称。如果您向基础工作区或数据字典中添加新的 `ConnectionBus` 对象，请单击下拉列表中的 **Refresh data types**，使新对象可供选择。要创建或修改 `ConnectionBus` 对象，请单击下拉列表旁边的 **Show type assistant** 按钮以显示 **Type Assistant** 面板。有关详细信息，请参阅 Specifying Rigid Interfaces。

要指定与复合域的刚性连接，请选择 `CompositeConnection: <domain name>`，然后单击下拉列表旁边的 **Show type assistant** 按钮。在 **Type Assistant** 面板中，将 **Mode** 设置为 `Composite domain`，并在 `<domain name>` 字段中键入现有复合域的名称。

要移除刚性接口规范，请将 **Connection type** 参数设置为 `Inherit: auto`。

### **Mode** — 指定连接模式 `Inherit`（默认）| `Connection Bus object` | `Composite domain`

与 **Connection type** 参数配合使用，并提供用于指定刚性接口的附加选项：

- `Inherit` — 表示柔性接口。唯一可用的下拉选项是 `auto`。对应于 **Connection type** 参数设置 `Inherit: auto`。
- `Connection Bus object` — 指定刚性总线连接。在 `<object name>` 字段中键入现有 `ConnectionBus` 对象的名称，或使用 **Edit** 按钮打开 Type Editor 并创建或修改 `ConnectionBus` 对象。对应于 **Connection type** 参数设置 `Bus: <object name>`。
- `Composite domain` — 指定与复合域的刚性连接。在 `<domain name>` 字段中键入现有复合域的名称。对应于 **Connection type** 参数设置 `CompositeConnection: <domain name>`。

#### 依赖关系

要启用此选择，请单击 **Connection type** 参数旁边的 **Show type assistant** 按钮。当您在 **Type Assistant** 面板中选择值时，**Connection type** 参数设置会相应更新。

### **Hierarchy Strings** — 连接名称列表 空（默认）| 连接名称

与连接到 Simscape Bus 模块的守恒线相对应的连接名称列表。默认情况下，此列表为空。每次添加连接时，模块的子侧会出现一个守恒端口。使用模块对话框中的 或 按钮来添加或移除连接。

您也可以直接在模型画布上添加和移除连接，如 Working with the Block on Model Canvas 中所述。

## 所属库

Simscape / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

用于汇聚守恒连接的总线

Simscape Bus 模块将守恒连接捆绑为一条 Simscape Bus 线。您也可以使用此模块从现有的 Simscape Bus 线中访问一个或多个连接。物理连接线是无方向的，因此该模块既可以作为总线创建器，也可以作为总线选择器。通常，一个模型会有两个 Simscape Bus 模块，面对面放置，其总线端口相连。

然而，一个模型也可以包含 Simscape Bus 模块的层次结构。

捆绑到 Simscape Bus 线中的守恒连接可以属于不同的域。

该模块仅捆绑 Simscape™ 守恒连接，即 Simscape 守恒端口或 Simscape Multibody™ 端口之间的无方向连接线。它不适用于其他类型的连接，例如物理信号线。
有关守恒连接的更多信息，请参阅 Physical Conserving Ports。

Simscape Bus 模块可以在两侧具有端口：

- 父级（捆绑）侧，由黑色带状标记指示。此侧包含一个总线端口，用于捆绑从子级侧进入模块的所有连接。
- 子级（元素）侧，与父级侧相对。此侧默认没有任何端口。您可以通过将连接线拖到模块的该侧，或使用模块对话框来添加端口。从子级侧进入模块的元素可以是守恒连接线或 Simscape Bus 线。每次在子级侧添加端口时，相应的连接会被添加到模块内部的连接列表中。

连接的名称显示在模块图标上，位于子级侧相应端口旁边，并显示在模块对话框的 **Hierarchy Strings** 列表中。如有需要，您可以在对话框中或直接在图标上编辑这些名称，方法是单击并键入新名称。

模块对话框包含以下按钮：

|  |  |
| --- | --- |
|  | 向 **Hierarchy Strings** 列表添加新的连接名称。默认连接名称为 `Connection1`、`Connection2` 等。如有需要，您可以通过选择一行，然后再次单击它并键入新名称来编辑这些名称。当您使用此按钮添加连接时，模块的子级侧会出现一个圆形守恒端口，类似于 Connection Port 模块的端口。此守恒端口的域类型在您将其连接到另一个模块上的守恒端口时定义。之后，您只能将相同类型的端口连接到第二个总线上的相应连接。您也可以直接在画布上添加连接，方法是将连接线从另一个模块上的守恒端口拖到 Simscape Bus 模块的子级侧。 |
|  | 从 **Hierarchy Strings** 列表中删除选定的连接。对于未连接的端口，您也可以直接在画布上删除它们或编辑其名称。 |
|  | 在画布上添加或删除连接后，刷新 **Hierarchy Strings** 列表。 |

### 在模型画布上使用模块

要向 Simscape Bus 模块添加连接：

1. 选择另一个模块上的一个守恒端口。或者，要创建 Simscape Bus 模块的层次结构，请选择另一个 Simscape Bus 模块父侧的母线端口。
2. 从所选端口拖动一条连接线到第一个 Simscape Bus 模块的子侧。
3. 一个新连接将以默认名称自动添加到模块连接列表中。您可以根据需要在上方蓝色字段中编辑连接名称。编辑完成后，在下方蓝色字段中选择连接名称以创建连接。

**注意**

- 一个 Simscape Bus 模块不能有多个子连接连接到同一个端口。换句话说，您不能将另一个模块上的守恒端口多次连接到同一个 Simscape Bus 模块。
- 您可以通过将一个 Simscape Bus 模块父侧的母线端口连接到另一个 Simscape Bus 模块的子端口来创建 Simscape Bus 模块的层次结构，但禁止不同 Simscape Bus 模块之间的子连接。换句话说，您不能将一个模块上的守恒端口连接到多个 Simscape Bus 模块。

当您删除一条连接线时，模块子侧对应的端口不会被删除。您可以通过连接另一个模块来复用它。

要删除未使用的端口：

- 选择 Simscape Bus 模块子侧的一个圆形守恒端口。确保只选择该端口，而不是整个模块。
- 从省略号菜单中，选择 **Delete Port**。删除端口也会删除模块连接列表中对应的名称。

### 指定刚性接口

您可以通过定义刚性接口规范来锁定 Simscape Bus 模块的连接类型。通过使用 `Simulink.ConnectionBus` 和 `Simulink.ConnectionElement` 对象或通过声明复合域，为保持连接设计刚性接口规范。当您将此类刚性规范应用于 Simscape Bus 模块时，模块端口将由接口确定类型，并且不接受连接到不同的域类型。此功能有助于确保模型架构中的正确连接类型。

使用 **Connection type** 参数应用刚性接口规范。有关详细信息，请参阅 Apply a Rigid Interface Specification to a Simscape Bus Block 和 Example of a Custom Composite Domain。

当您将刚性接口规范应用于 Simscape Bus 模块时：

- 如果该模块之前在子级侧没有端口，则该模块会自动添加与接口定义对应的子级端口。在嵌套总线定义的情况下，仅顶层总线的第一级子级端口会自动出现。
- 如果该模块在子级侧已有端口，则这些端口不会被覆盖，并且新端口不会自动出现。相反，该模块会根据接口定义验证现有端口的名称和类型，并在发现连接错误时报告。

当您将刚性接口规范应用于 Simscape Bus 模块时，模块外观会发生变化以指示刚性总线。总线（父级）端口具有白色中心，并且模块图标在左下角具有 Refresh 徽章。

模型图中的刚性 Simscape Bus 模块外观

在应用刚性接口时，如果两个 Simscape Bus 模块的总线（父级）端口都是刚性的并且使用相同的接口定义，或者其中一个模块是使用 `ConnectionBus` 对象的刚性总线，而另一个是柔性的（**Connection type** 参数设置为 `Inherit: auto`），则您可以连接这两个模块的总线（父级）端口。在这两种情况下，连接线样式（双线）表示刚性总线连接。

两个刚性 Simscape Bus 模块之间的连接线

您不能连接使用复合域接口的刚性总线和柔性总线的总线端口。

要移除刚性接口规范，请将 **Connection type** 参数设置为 `Inherit: auto`。
