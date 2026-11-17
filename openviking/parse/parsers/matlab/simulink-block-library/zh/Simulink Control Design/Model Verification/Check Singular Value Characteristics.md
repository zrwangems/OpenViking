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
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters: []
```

下表汇总了 Singular Value Plot 模块参数，可通过模块参数对话框访问。有关详细信息，请参阅 Singular Value Plot 模块参考页面中的 Parameters。

| 任务 | | 参数 |
| --- | --- | --- |
| 配置线性化。 | 指定输入和输出（I/O）。 | 在 **Linearizations** 选项卡中：  - **Linearization inputs/outputs** - **Click a model signal to add it as a   linearization I/O** |
| 指定设置。 | 在 **Linearizations** 选项卡中： - **Linearize on** - **Snapshot times** - **Trigger type** |
| 指定算法选项。 | 在 **Linearizations** 选项卡中： - **Enable zero-crossing detection** - **Use exact delays** - **Linear system sample time** - **Sample time rate conversion   method** - **Prewarp frequency (rad/s)** |
| 为线性系统 I/O 和状态名称指定标签。 | 在 **Linearizations** 选项卡中： - **Use full block names** - **Use bus signal names** |
| 为断言指定线性系统的边界。 | | 在 **Bounds** 选项卡中： - **Include upper singular value bound in   assertion** - **Include lower singular value bound in   assertion** |
| 指定断言选项（仅当您为线性系统指定边界时）。 | | 在 **Assertion** 选项卡中： - **Enable assertion** - **Simulation callback when assertion fails   (optional)** - **Stop simulation when assertion   fails** - **Output assertion signal** |
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

在仿真期间检查奇异值边界是否满足

此模块与 Singular Value Plot 模块相同，只是 **Bounds** 选项卡中的默认参数设置不同：

在仿真期间检查从非线性 Simulink 模型计算得到的线性系统奇异值的上下界是否满足。

Simulink 模型可以是连续时间、离散时间或多速率模型，并且可以包含时间延迟。计算得到的线性系统可以是单输入单输出（SISO）或多输入多输出（MIMO）。

在仿真期间，软件会对指定线性化输入和输出之间的模型部分进行线性化，计算奇异值，并检查这些值是否满足指定的边界：

- 如果所有边界均满足，则该模块不执行任何操作。
- 如果某个边界不满足，则该模块会触发断言，并在 MATLAB® 命令窗口中显示警告消息。您还可以指定该模块：

  - 计算 MATLAB 表达式。
  - 停止仿真并将该模块置于焦点。

在仿真期间，该模块还可以输出一个逻辑断言信号。

- 如果所有边界均满足，则该信号为 true（`1`）。
- 如果任一 boundary 不满足，则该信号为 false（`0`）。

对于 MIMO 系统，边界适用于针对所有输入/输出组合计算得到的奇异值。

您可以在模型中添加多个 Check Singular Value Characteristics 模块，以检查模型各个部分的奇异值上下界。

您还可以在奇异值图上绘制奇异值，并以图形方式验证这些值是否满足边界。

此模块和其他 Model Verification 模块用于在仿真期间测试非线性 Simulink 模型的线性化行为是否处于指定边界内。

- 当模型未违反任何边界时，您可以通过清除断言选项来禁用该模块。如果您修改了模型，可以重新启用断言，以确保您的更改不会导致模型违反边界。
- 当模型违反任何边界时，您可以使用 Simulink Design Optimization™ 软件来优化线性系统，以满足此模块中指定的要求。

您可以将线性系统保存为 MATLAB 工作区中的变量。

该模块不支持代码生成，并且只能在 `Normal` 仿真模式下使用。
