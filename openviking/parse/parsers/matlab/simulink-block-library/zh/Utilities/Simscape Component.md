---
type: simulink-block
title: 'Simscape Component'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'simscapecomponent'
documentation_source_path: '../simscape/ref/simscapecomponent.html'
language: zh-CN
chinese_source: worker-translation
---

# Simscape Component

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

将 Simscape 语言组件作为自定义模块部署到模型图中

Simscape Component 模块允许您直接从文本组件文件生成 Simscape™ 模块，跳过库构建过程。

您可以使用 `ssc_build` 命令从命名空间中所有 Simscape 组件文件生成自定义模块库。但是，您也可以通过使用 Simscape Component 模块，将组件文件直接即时转换为模型中的自定义模块。

要将组件文件直接部署到框图中：

1. 打开 Simscape > Utilities 库，将 Simscape Component 模块添加到您的模型中。起初，该模块不指向任何组件文件。因此，它没有任何端口，模块图标显示为 `Unspecified`。
2. 双击该模块以打开源文件选择器对话框。
3. 单击 以打开浏览器。浏览器在当前工作目录中打开，仅列出扩展名为 `.ssc` 或 `.sscp` 的文件。

   浏览到所需的 Simscape 语言组件文件。该文件不必位于命名空间中。但是，文件所在的目录必须在 MATLAB® 路径上。如果文件位于命名空间中，则命名空间的父文件夹必须在 MATLAB 路径上。
4. 选择源文件并单击 **Open**。源文件的名称出现在源文件选择器对话框的文本字段中，模块名称、描述和源代码链接出现在 **Description** 窗格中。

   源组件选择会立即应用，无论您是否选中了 **Auto Apply** 复选框。模块图标会改变，模块根据所选源组件获取端口、参数和变量。
5. 如果您现在双击该模块，其对话框具有与通过库构建过程从组件文件生成时相同的所有元素：名称、描述、参数、变量以及指向 **Source code** 的链接。但是，**Description** 窗格具有源选择器字段，显示当前源文件的名称，并允许您将模块指向不同的组件文件。

### Source File Selector

当 Simscape Component 模块指向一个有效的 Simscape 语言组件文件时，其对话框将包含该源文件所定义的名称、描述、参数和变量。**Description** 窗格还包含源选择器字段，用于显示当前源文件的名称，并允许您将模块指向其他组件文件。

源组件文件可以位于：

- 当前工作目录中
- MATLAB 路径上的某个目录中
- 某个命名空间中，且该命名空间的父目录位于 MATLAB 路径上

要指定源文件，您可以浏览到该文件，或直接在选择器对话框的源选择器字段中键入其名称：

- 如果键入文件名，则必须满足上面列出的位置要求。如果文件位于命名空间中，则必须提供相对于命名空间根目录的文件名。如果在键入文件名时不满足这些条件，则无法解析源位置，并会收到错误消息。
- 如果浏览到源文件，则可以选择任何 Simscape 源文件或受保护文件（即任何扩展名为 `.ssc` 或 `.sscp` 的文件）。但是，如果所选文件不满足位置要求，则会打开 File Not On Path 对话框。点击 **Add** 将相应目录添加到 MATLAB 路径并解析源位置。如果点击 **Cancel**，则无法解析源位置，源选择过程将被取消。

源文件选择器对话框中文本框旁边的按钮执行以下操作：

|  |  |
| --- | --- |
|  | 打开文件浏览器，让您选择源组件文件。默认情况下，浏览器仅显示扩展名为 `.ssc` 或 `.sscp` 的文件。如果 Simscape Component 模块当前指向某个源文件，并且源位置已成功解析，则浏览器会在该源文件所在的目录中打开。否则，浏览器会在当前工作目录中打开。 |
|  | 刷新源文件选择器对话框的预览窗格。如果直接在选择器对话框的文本字段中键入源组件名称，预览窗格不会自动更新。如果希望在最终确定选择之前预览源组件的模块名称、描述或源代码，请点击此按钮。 |

### Block Icon Appearance

Simscape Component 模块图标外观会随模块状态而变化。

|  |  |
| --- | --- |
|  | 库中的 Simscape Component 模块。 |
|  | 刚添加到模型中的 Simscape Component 模块，此时尚未指向任何源组件。 |
|  | 指向有效组件文件的 Simscape Component 模块。模块端口由底层组件定义。默认情况下，模块图标显示组件名称（例如 `my_resistor`）。如果源组件文件所在目录中存在同名图像文件（例如 `my_resistor.png`），则该图像将替换默认模块图标。有关详细信息，请参阅 Customizing the Block Icon。 |
|  | 指向未解析组件文件的 Simscape Component 模块。如果源组件文件被移动，或不再位于路径上，则可能发生这种情况。**Add** 按钮仅在当前 MATLAB 会话期间将文件夹添加到路径中。如果不保存路径，然后在后续会话中打开模型，Simscape Component 模块将变为未解析状态。如果源组件位于当前工作目录中，则不需要将其添加到路径中。但是，如果之后尝试从另一个目录打开模型，Simscape Component 模块也会变为未解析状态。 |
