---
type: simulink-block
title: 'Check Nichols Characteristics'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Model Verification'
documentation_page: 'checknicholscharacteristics'
documentation_source_path: 'ug/checknicholscharacteristics.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Nichols Characteristics

## 端口

R2025b 中未记录。

## 参数

下表总结了 Nichols Plot 模块参数，可通过模块参数对话框访问。有关详细信息，请参阅 Nichols Plot 模块参考页面中的 Parameters。

| 任务 | | 参数 |
| --- | --- | --- |
| 配置线性化。 | 指定输入和输出（I/O）。 | 在 **Linearizations** 选项卡中： - **Linearization inputs/outputs** - **Click a model signal to add it as a linearization I/O** |
| 指定设置。 | 在 **Linearizations** 选项卡中： - **Linearize on** - **Snapshot times** - **Trigger type** |
| 指定算法选项。 | 在 **Linearizations** 选项卡中： - **Enable zero-crossing detection** - **Use exact delays** - **Linear system sample time** - **Sample time rate conversion method** - **Prewarp frequency (rad/s)** |
| 为线性系统 I/O 和状态名称指定标签。 | 在 **Linearizations** 选项卡中： - **Use full block names** - **Use bus signal names** |
| 为断言的线性系统增益和相位指定边界。 | | 在 **Bounds** 选项卡中： - **Include gain and phase margins in assertion** - **Include closed-loop peak gain in assertion** - **Include open-loop gain-phase bound in assertion** |
| 指定断言选项（仅当为线性系统指定边界时）。 | | 在 **Assertion** 选项卡中： - **Enable assertion** - **Simulation callback when assertion fails (optional)** - **Stop simulation when assertion fails** - **Output assertion signal** |
| 将线性系统保存到 MATLAB 工作区。 | | **Logging** 选项卡中的 **Save data to workspace**。 |
| 在绘图窗口中图形化查看边界违规。 | | **Show Plot** |
| 双击模块时显示绘图窗口而不是模块参数对话框。 | | **Show plot on block open** |

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

## 描述

在仿真期间检查 Nichols 响应上的增益和相位边界是否满足

此模块与 Nichols Plot 模块相同，只是 **Bounds** 选项卡中的默认参数设置不同。

在仿真期间，检查从非线性 Simulink 模型计算得到的线性系统 Nichols 响应上的开环和闭环增益和相位边界是否满足。

Simulink 模型可以是连续时间、离散时间或多速率模型，并且可以具有时间延迟。由于在此模块中只能指定一个线性化输入/输出对，因此线性系统是单输入单输出（SISO）系统。

在仿真期间，软件对模型中指定的线性化输入和输出之间的部分进行线性化，计算幅值和相位，并检查增益和相位是否满足指定的边界：

- 如果所有边界均满足，则模块不执行任何操作。
- 如果某个边界不满足，则模块触发断言，并在 MATLAB® 命令窗口中显示警告消息。您还可以指定模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并将该模块置于焦点。

在仿真期间，模块还可以输出逻辑断言信号。

- 如果所有边界均满足，则信号为 true（`1`）。
- 如果任何边界不满足，则信号为 false（`0`）。

您可以在模型中添加多个 Check Nichols Characteristics 模块，以检查模型各个部分的增益和相位边界。

您还可以在 Nichols 图上绘制线性系统，并以图形方式验证 Nichols 响应是否满足边界。

此模块和其他 Model Verification 模块在仿真期间测试非线性 Simulink 模型的线性化行为是否在指定边界内。

- 当模型未违反任何边界时，您可以通过清除断言选项来禁用模块。如果您修改了模型，可以重新启用断言以确保您的更改不会导致模型违反边界。
- 当模型违反任何边界时，您可以使用 Simulink Design Optimization™ 软件来优化线性系统，以满足此模块中指定的要求。

您可以将线性系统保存为 MATLAB 工作区中的变量。

此模块不支持代码生成，且只能在 `Normal` 仿真模式下使用。
