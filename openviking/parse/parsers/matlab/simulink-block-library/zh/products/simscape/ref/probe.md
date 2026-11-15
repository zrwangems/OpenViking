---
type: simulink-block
title: 'Probe'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Utilities / Utility Blocks'
documentation_page: 'probe'
documentation_source_path: 'ref/probe.html'
language: zh-CN
chinese_source: worker-translation
---

# Probe

## 端口

### 输出

### **x** — 所选变量在仿真期间的值 标量 | 向量 | 矩阵

将所选变量的值在仿真期间作为 Simulink 信号输出。端口名称与所选变量的名称匹配。输出信号单位与变量单位匹配。您可以使用属性检查器修改端口标签并更改输出信号单位。

如果选择多个变量，模块会获取额外的输出端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2025a: 跨子系统边界的 Probe

Probe 模块现在具有对话框，您可以使用该对话框将 Probe 模块连接到另一个 Simscape 模块，选择要探测的变量，并自定义 Probe 端口名称和变量的输出单位。

在以前的版本中，您只能将 Probe 模块连接到模型层级同一级别的模块。现在，当您双击 Probe 模块时，其对话框会打开。使用 **连接** 按钮将 Probe 模块附加（绑定）到另一个 Simscape 模块；该模块可位于同一级别、子系统内或模型层级的任何其他级别。点击 **完成连接** 以完成绑定过程。您也可以通过点击模型画布右上角的 X 来结束绑定过程。

### R2024b: 使用属性检查器或命令行界面指定要探测的变量

您现在可以使用 Probe 模块的属性检查器来选择或取消选择变量、更改端口标签或选择不同的输出单位，而不必在模型画布上选择要探测的变量。

此版本中的新命令行界面包括：

- `simscape.probe.defaultVariableTable`
- `simscape.probe.getVariableTable`
- `simscape.probe.setVariableTable`
- `simscape.probe.VariableTable`
- `simscape.probe.VariableConfiguration`

### R2023b: 选择或取消选择所有要探测的变量

为便于处理长变量列表，当您选择要探测的变量时，上下文菜单现在在列表顶部、**键入以过滤** 字段正下方包含一个额外的复选框。切换此复选框可以选择或取消选择当前列出的所有变量。您可以将此复选框与过滤结合使用，以选择或取消选择变量组。

### R2023a: 扩展了可用于探测的变量列表

在以前的版本中，当您选择要输出的变量时，上下文菜单仅包含模块对话框的 **初始目标** 部分中公开的变量，即可用于模块级变量初始化的相同变量。

从 R2023a 开始，上下文菜单包含所有外部可访问的模块变量，无论它们是否在模块对话框的 **初始目标** 部分中公开。外部可访问变量包括：使用 `ExternalAccess` 属性值 `modify` 或 `observe` 声明的模块变量、输入、输出、中间量、modecharts，以及每个节点处的 domain Across 变量。本质上，这些变量与您可以在仿真数据日志中看到的变量相同。

为便于扫描长变量列表，尤其是在复合组件中，上下文菜单中变量的显示格式已从 `Name:id` 反转为 `id:Name`。例如，同一变量现在显示为 `i:Current`，而不是 `Current:i`。此视图与 Variable Viewer、Simscape Results Explorer 和 Simulation Data Inspector 中的变量显示更一致。

上下文菜单现在还在顶部具有过滤字段。在该字段中键入内容，以过滤上下文菜单中显示的变量。

## 描述

在仿真期间将模块变量输出为信号

Probe 模块允许您从模型中的另一个模块选择变量，并将它们输出为 Simulink® 信号。双击 Probe 模块，并使用 **连接** 按钮将 Probe 模块附加（绑定）到另一个 Simscape™ 模块；该模块可位于模型图的同一级别、子系统内或模型层级的任何其他级别。但是，该模块必须位于同一模型中。您不能跨模型引用边界绑定 Probe 模块。

选择要探测的模块后，其变量列表会出现在模型画布上。您可以在模型画布上选择变量，或跳过此步骤。点击 **完成连接** 以完成绑定过程。此时，Probe 对话框会填充来自所附加模块的变量列表。如果您在模型画布上选择了任何变量，它们也会在对话框中处于选中状态。您可以使用该对话框继续选择要探测的变量、自定义端口名称并指定输出单位。

当您选择要探测的变量时：

- 该列表包含所有外部可访问的模块变量，无论它们是否显示在模块对话框的 **初始目标** 部分中。外部可访问变量包括：

  - 组件变量，包括事件变量
  - 每个节点处的 domain Across 变量
  - 输入
  - 输出
  - 中间量
  - Mode chart 元素

  这些成员必须使用 `ExternalAccess` 属性值 `modify` 或 `observe` 进行声明。本质上，这些变量与您可以在仿真数据日志或 instrumentation table 中看到的变量相同。
- 对于条件可见性，如果某个变量仅在部分模块参数化配置中处于活动状态，则无论该变量在当前模块配置中是否处于活动状态，它始终可用于探测。
- 对于条件声明，无论条件分支在当前模块配置中是否处于活动状态，变量都不可用于探测。对于复合组件，此限制包括条件声明组件的所有外部可访问变量。
- 该模块将每个所选变量输出为单独的信号。

Probe 模块输出 Simulink 信号。因此，您可以将其直接连接到 Simulink 模块，例如示波器或总线。

一次只能将一个 Probe 模块附加（绑定）到一个模块。但是，您可以将多个 Probe 模块同时绑定到模型中的同一模块。

### 在模型画布上使用模块

要在模型中使用 Probe 模块：

1. 将 Probe 模块添加到模型层级的任意级别。
2. 双击 Probe 模块。模块对话框打开。

   未连接的 Probe 对话框

   此时，Probe 模块未连接，即未附加到任何其他模块。
3. 点击 **连接** 开始绑定过程。
4. 选择一个 Simscape 模块。该模块可位于模型层级的任意级别。
5. 选择模块时，其变量列表会出现在模型画布上。您可以在模型画布上选择变量，或跳过此步骤，稍后从 Probe 对话框中选择变量。在模型画布上选择变量的好处是，您可以过滤变量并一次选择或取消选择多个变量。

   例如，如果您选择了 Rotational Electromechanical Converter 模块，可用变量包括 current、voltage、torque 和 angular velocity，以及每个电气端口处的 voltage 和端口 **C** 与 **R** 处的 rotational velocity。

   在模型画布上选择要探测的变量

   为便于处理长变量列表，上下文菜单顶部有一个 **键入以过滤** 字段。在该字段中键入内容，以仅显示其名称或 id 中包含过滤字符串的变量。

   您还可以使用位于 **键入以过滤** 字段正下方的顶部复选框，选择或取消选择当前列出的所有变量。
6. 在 Probe 模块对话框中，点击 **连接模式** 旁边的 **完成连接**，以完成绑定过程。

   **注意**

   选择模块时，如果您跨子系统边界导航到未在模型选项卡中打开的子系统，Probe 模块对话框可能会自动关闭。在这种情况下，您可以通过点击模型画布右上角的 X 来结束绑定过程。

   结束绑定过程会将您带到 Probe 模块所在的模型图级别，并重新打开 Probe 对话框。
7. 完成绑定过程后，Probe 对话框会填充来自所附加模块的变量列表。Probe 对话框还包含指向 Probe 所连接模块的链接。如果点击此链接，被探测的模块会突出显示。如果该模块与 Probe 模块处于不同级别，则包含该模块的子系统会打开，并且该模块会突出显示。

   如果您在模型画布上选择了任何变量，它们也会在对话框中处于选中状态。（在此示例中，current 和 angular velocity 处于选中状态。）如果某个变量在对话框中处于选中状态，您可以在列表中展开它，以查看关联的端口标签和单位。您可以使用该对话框继续选择要探测的变量、自定义端口名称并指定输出单位。

   附加到 Rotational Electromechanical Converter 模块的 Probe 对话框
8. 对于每个选中的变量，Probe 模块会获取一个额外的输出端口。（在此示例中，端口名称为 **i** 和 **w**。）最初，端口标签与变量名称匹配，但您可以双击 Probe 对话框中的变量名称，在 **端口标签** 右侧的单元格中编辑它。您还可以点击 **单位** 右侧的单元格，并从下拉列表中为输出信号选择不同的输出单位。
9. 将 Probe 模块输出端口连接到示波器或 Simulink Sinks 库中的其他模块，以在仿真期间查看信号值。

   将 Probe 输出连接到示波器的模块图

   显示仿真结果的 Current 示波器

   显示仿真结果的 RPM 示波器

要将 Probe 模块绑定到模型中的其他模块，或更改所选变量，请再次双击 Probe 模块。

如果将 Probe 模块与其绑定到的模块一起复制，则会保留连接，并且新组合中会自动选择相同的变量。

### 命令行工作流

除了模型画布上的交互式工作流，您还可以使用以下命令绑定 Probe 模块并选择变量：

- `simscape.probe.setBoundBlock(probeBlock,
  boundBlock)` — 将 *`probeBlock`* 绑定到 *`boundBlock`*。*`probeBlock`* 必须是有效的完整模块路径或 Probe 模块的句柄。*`boundBlock`* 必须是有效的完整模块路径，或与 *`probeBlock`* 处于模型层级同一级别的另一模块的句柄。该命令不会检查 *`boundBlock`* 是否为 Simscape 模块，或是否具有要探测的变量。

  `simscape.probe.setBoundBlock(probeBlock,
  [])` 将 Probe 模块返回到未绑定状态。不会影响所选变量。
- `simscape.probe.setVariables(probeBlock,
  variables)` — 选择 *`probeBlock`* 要输出的变量。*`probeBlock`* 必须是有效的完整模块路径或 Probe 模块的句柄。*`variables`* 必须是指定变量的字符向量、字符向量元胞数组或字符串数组。字符向量或字符串必须是唯一的变量标识符，并按字典序排序。该命令不会检查当前选中的 *`boundBlock`* 是否包含这些变量。

  如果不按字典序对变量排序，可以使用以下语法：

  ```
  I = simscape.probe.setVariables(probeBlock, variables, 'Sort', true)
  ```

  然后，该命令会在将变量应用到 *`probeBlock`* 之前对变量排序。变量标识符仍必须唯一。*`I`* 返回排序后的 *`variables`* 在 Probe 模块上作为端口出现的顺序。

在“在模型画布上使用模块”示例中展示的交互式绑定和变量选择的编程等效形式为：

```
simscape.probe.setBoundBlock('PermanentMagnetDCMotor/DC Motor/Probe','PermanentMagnetDCMotor/DC Motor/Rotational Electromechanical Converter');
simscape.probe.setVariables('PermanentMagnetDCMotor/DC Motor/Probe',["i", "w"]);
```

因此，Probe 模块也具有两个输出端口 **i** 和 **w**，分别绑定到 Rotational Electromechanical Converter 模块的 **Current : i** 和 **Angular velocity : w** 变量。

如果提供未排序的变量，该命令会返回排序后的顺序：

```
I = simscape.probe.setVariables('PermanentMagnetDCMotor/DC Motor/Probe', ["w", "i"], 'Sort', true)
```

```
I =

     2     1
```

在此示例中，第二个变量 `i` 在 Probe 模块上作为第一个端口出现，其后是第一个变量 `w`。

您可以使用 `simscape.probe.getBoundBlock(probeBlock)` 和 `simscape.probe.getVariables(probeBlock)` 命令返回其绑定模块和变量，其中 *`probeBlock`* 是有效的完整模块路径或 Probe 模块的句柄。

您还可以使用 `simscape.probe.defaultVariableTable`、`simscape.probe.setVariableTable` 和 `simscape.probe.getVariableTable` 函数构造 `VariableTable` 对象，并将它们附加到 Probe 模块。
