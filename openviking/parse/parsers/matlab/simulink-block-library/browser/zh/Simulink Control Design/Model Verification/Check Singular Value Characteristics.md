---
type: simulink-block
title: 'Check Singular Value Characteristics'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checksingularvaluecharacteristics'
documentation_source_path: 'ug/checksingularvaluecharacteristics.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Singular Value Characteristics

## 端口

R2025b 中未提供文档。

## 参数

下表总结了 Singular Value Plot 模块的参数，可通过模块参数对话框访问。有关详细信息，请参阅 Singular Value Plot 模块参考页中的参数。

| 任务 | | 参数 |
| --- | --- | --- |
| 配置线性化。 | 指定输入和输出 (I/O)。 | 在 **Linearizations** 选项卡中：  - **Linearization inputs/outputs** - **Click a model signal to add it as a   linearization I/O** |
| 指定设置。 | 在 **Linearizations** 选项卡中：  - **Linearize on** - **Snapshot times** - **Trigger type** |
| 指定算法选项。 | 在 **Linearizations** 选项卡中：  - **Enable zero-crossing detection** - **Use exact delays** - **Linear system sample time** - **Sample time rate conversion   method** - **Prewarp frequency (rad/s)** |
| 指定线性系统 I/O 和状态名称的标签。 | 在 **Linearizations** 选项卡中：  - **Use full block names** - **Use bus signal names** |
| 指定用于断言的线性系统界限。 | | 在 **Bounds** 选项卡中：  - **Include upper singular value bound in   assertion** - **Include lower singular value bound in   assertion** |
| 指定断言选项（仅在指定线性系统界限时）。 | | 在 **Assertion** 选项卡中：  - **Enable assertion** - **Simulation callback when assertion fails   (optional)** - **Stop simulation when assertion   fails** - **Output assertion signal** |
| 将线性系统保存到 MATLAB 工作区。 | | **Logging** 选项卡中的 **Save data to workspace**。 |
| 在绘图窗口中以图形方式查看违反界限的情况。 | | **Show Plot** |
| 双击模块时显示绘图窗口，而不是模块参数对话框。 | | **Show plot on block open** |

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2010b 中推出**

## 描述

检查仿真过程中是否满足奇异值界限

除 **Bounds** 选项卡中的默认参数设置外，此模块与 Singular Value Plot 模块相同：

检查在仿真过程中，根据非线性 Simulink 模型计算得到的线性系统的奇异值是否满足上界和下界。

Simulink 模型可以是连续时间、离散时间或多速率模型，并且可以包含时延。
计算得到的线性系统可以是单输入单输出 (SISO) 系统，也可以是多输入多输出 (MIMO) 系统。

在仿真过程中，软件对指定的线性化输入与输出之间的模型部分进行线性化，计算奇异值，并检查这些值是否满足指定的界限：

- 如果满足所有界限，模块不执行任何操作。
- 如果某个界限不满足，模块将触发断言，并在 MATLAB® 命令行窗口中显示警告消息。您还可以指定该模块执行以下操作：

  - 计算 MATLAB 表达式。
  - 停止仿真并将焦点移至该模块。

在仿真过程中，模块还可以输出逻辑断言信号。

- 如果满足所有界限，则信号为 true (`1`)。
- 只要有界限不满足，信号就为 false (`0`)。

对于 MIMO 系统，这些界限适用于针对所有输入/输出组合计算的奇异值。

您可以在模型中添加多个 Check Singular Value Characteristics 模块，以检查模型不同部分的奇异值上界和下界。

您还可以在奇异值图上绘制奇异值，并通过图形验证这些值是否满足界限。

此模块和其他 Model Verification 模块用于检验非线性 Simulink 模型的线性化行为在仿真过程中是否处于指定界限内。

- 当模型未违反任何界限时，您可以通过清除断言选项来禁用该模块。如果修改模型，可以重新启用断言，以确保所做的更改不会导致模型违反界限。
- 当模型违反任何界限时，您可以使用 Simulink Design Optimization™ 软件来优化线性系统，使其满足此模块中指定的要求。

您可以将线性系统保存为 MATLAB 工作区中的变量。

该模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
