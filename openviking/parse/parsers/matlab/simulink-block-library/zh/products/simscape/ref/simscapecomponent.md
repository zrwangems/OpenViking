---
type: simulink-block
title: 'Simscape Component'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'simscapecomponent'
documentation_source_path: 'ref/simscapecomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# Simscape Component

## 端口

R2025b 中未提供文档。

## 参数

R2025b 中未提供文档。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

将 Simscape 语言组件部署为模型框图中的自定义模块

Simscape Component 模块允许您直接根据文本组件文件生成 Simscape™ 模块，而无需执行库构建过程。

您可以使用 `ssc_build` 命令，根据位于某个命名空间中的所有 Simscape 组件文件生成自定义模块库。不过，您也可以使用 Simscape Component 模块，将组件文件即时直接转换为模型中的自定义模块。

要将组件文件直接部署到框图中，请执行以下操作：

1. 打开 Simscape > Utilities 库，并将 Simscape Component 模块添加到模型中。最初，该模块不指向任何组件文件。因此，它没有任何端口，并且模块图标显示为 `Unspecified`。
2. 双击该模块以打开源文件选择器对话框。
3. 点击  打开浏览器。浏览器将在当前工作目录中打开，并且仅列出扩展名为 `.ssc` 或 `.sscp` 的文件。

   浏览到所需的 Simscape 语言组件文件。该文件不必位于命名空间中。但是，该文件所在目录必须位于 MATLAB® 路径上。如果该文件位于命名空间中，则该命名空间的父文件夹必须位于 MATLAB 路径上。
4. 选择源文件并点击 **Open**。源文件的名称将显示在源文件选择器对话框的文本字段中，而模块名称、描述以及指向源代码的链接将显示在 **Description** 窗格中。

   无论是否选中 **Auto Apply** 复选框，源组件选择都会立即应用。模块图标会发生变化，并且该模块会根据所选源组件获得端口、参数和变量。
5. 如果此时双击该模块，其对话框将包含与通过库构建过程从组件文件生成该模块时完全相同的元素：名称、描述、参数、变量以及指向 **Source code** 的链接。但是，**Description** 窗格还包含源选择器字段，该字段显示当前源文件的名称，并允许您将该模块指向其他组件文件。

### 源文件选择器

当 Simscape Component 模块指向有效的 Simscape 语言组件文件时，其对话框将包含由该源文件定义的名称、描述、参数和变量。**Description** 窗格还包含源选择器字段，该字段显示当前源文件的名称，并允许您将该模块指向其他组件文件。

源组件文件可以位于：

- 当前工作目录中
- MATLAB 路径上的某个目录中
- 某个命名空间中，且该命名空间的父目录位于
  MATLAB 路径上

要指定源文件，您可以浏览到该文件，也可以直接在选择器对话框的源选择器字段中键入其名称：

- 如果您键入文件名，则该文件必须满足上面列出的位置要求。如果文件位于命名空间中，则必须提供相对于命名空间根目录的文件名。如果在您键入文件名时不满足这些条件，则无法解析源位置，并且会显示错误消息。
- 如果您浏览到源文件，则可以选择任何 Simscape 源文件或受保护文件（即任何扩展名为 `.ssc` 或 `.sscp` 的文件）。但是，如果所选文件不满足位置要求，则会打开 File Not On Path 对话框。点击 **Add** 可将相应目录添加到 MATLAB 路径并解析源位置。如果点击 **Cancel**，则无法解析源位置，并且源选择过程将被取消。

源文件选择器对话框中文本字段旁的按钮执行以下操作：

|  |  |
| --- | --- |
|  | 打开文件浏览器，以便您选择源组件文件。默认情况下，浏览器仅显示扩展名为 `.ssc` 或 `.sscp` 的文件。如果 Simscape Component 模块当前指向某个源文件，并且源位置已成功解析，则浏览器将在该源文件所在目录中打开。否则，浏览器将在当前工作目录中打开。 |
|  | 刷新源文件选择器对话框的预览窗格。如果您直接在选择器对话框的文本字段中键入源组件名称，预览窗格不会自动更新。如果要在最终确定选择之前预览源组件的模块名称、描述或源代码，请点击此按钮。 |

### 模块图标外观

Simscape Component 模块的图标外观会随模块状态而变化。

|  |  |
| --- | --- |
|  | 库中的 Simscape Component 模块。 |
|  | 刚添加到模型中的 Simscape Component 模块，此时它尚未指向源组件。 |
|  | 指向有效组件文件的 Simscape Component 模块。模块端口由底层组件定义。默认情况下，模块图标显示组件名称（例如 `my_resistor`）。如果源组件文件所在目录中存在名称匹配的图像文件（例如 `my_resistor.png`），则该图像将替换默认模块图标。有关详细信息，请参阅自定义模块图标。 |
|  | 指向无法解析的组件文件的 Simscape Component 模块。如果源组件文件已被移动，或该文件不再位于路径上，就可能出现这种情况。**Add** 按钮仅在当前 MATLAB 会话期间将该文件夹添加到路径中。如果您未保存路径，随后在后续会话中打开模型，Simscape Component 模块将变为未解析状态。如果源组件位于当前工作目录中，则无需将其置于路径上。但是，如果您之后尝试从其他目录打开模型，Simscape Component 模块也会变为未解析状态。 |
