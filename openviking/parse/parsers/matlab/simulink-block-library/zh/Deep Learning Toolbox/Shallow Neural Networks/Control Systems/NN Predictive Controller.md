---
type: simulink-block
title: 'Design Neural Network Predictive Controller in Simulink'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Shallow Neural Networks / Control Systems'
documentation_page: 'design-neural-network-predictive-controller-in-simulink'
documentation_source_path: 'ug/design-neural-network-predictive-controller-in-simulink.html'
language: zh-CN
chinese_source: official
---

# Design Neural Network Predictive Controller in Simulink

在 Deep Learning Toolbox™ 软件中实现的神经网络预测控制器使用非线性被控对象的神经网络模型来预测被控对象将来的性能。然后，控制器计算控制输入，该控制输入将在指定的将来时间范围内优化被控对象性能。模型预测控制的第一步是确定神经网络被控对象模型（系统辨识）。接下来，控制器使用被控对象模型来预测将来的性能。（请参阅 Model Predictive Control Toolbox™ 文档，了解各种模型预测控制策略在线性系统中的应用的完整内容。）

在 Deep Learning Toolbox™ 软件中实现的神经网络预测控制器使用非线性被控对象的神经网络模型来预测被控对象将来的性能。然后，控制器计算控制输入，该控制输入将在指定的将来时间范围内优化被控对象性能。模型预测控制的第一步是确定神经网络被控对象模型（系统辨识）。接下来，控制器使用被控对象模型来预测将来的性能。（请参阅 Model Predictive Control Toolbox™ 文档，了解各种模型预测控制策略在线性系统中的应用的完整内容。）

下一节说明系统辨识过程。接下来是对优化过程的说明。最后，讨论如何使用在 Simulink® 环境中实现的模型预测控制器模块。

**注意**

要设计神经网络预测控制器，您还可以使用 System Identification Toolbox™ 和 Model Predictive Control Toolbox。使用 System Identification Toolbox 通过神经网络进行被控对象建模，并使用 Model Predictive Control Toolbox 设计控制器。

建议使用此工作流，因为它具有以下优势：

- 将被控对象建模和控制设计解耦。
- 通过用于神经网络被控对象和控制器的专用 Simulink 模块，轻松与 Simulink 集成。
- 具有多个内置求解器，用于线性和非线性预测控制。
- 支持代码生成。

有关如何使用这些工具的示例，请参阅Control House Heating Using Nonlinear MPC with Neural State-Space Prediction Model (Model Predictive Control Toolbox)。

### 系统辨识

模型预测控制的第一阶段是训练神经网络来表示被控对象的前向动态。被控对象输出和神经网络输出之间的预测误差用作神经网络训练信号。该过程如下图所示：

System identification diagram with input u and output y\_p.

神经网络被控对象模型使用先前的输入和先前的被控对象输出来预测被控对象输出的将来值。下图给出了神经网络被控对象模型的结构。

Two layer neural network diagram with inputs y\_p(t) and u(t), and output y\_m(t+1).

该网络可以在批量模式下使用从被控对象运行中采集的数据进行离线训练。您可以使用在多层浅层神经网络与反向传播训练中讨论的任何训练算法进行网络训练。此过程将在以下各节中详细讨论。

### 预测控制

模型预测控制方法基于滚动时域法 [SoHa96]。神经网络模型预测在指定时域内的被控对象响应。数值优化程序使用预测来确定控制信号，该控制信号最小化在指定时域内的以下性能条件

J=∑j=N1N2(yr(t+j)−ym(t+j))2+ρ∑j=1Nu(u′(t+j−1)−u′(t+j−2))2

其中，*N*1、*N*2 和 *Nu* 定义计算跟踪误差和控制增量的时域。*u*′ 变量是暂定控制信号，*yr* 是期望响应，*ym* 是网络模型响应。ρ 值决定控制增量的平方和对性能指数的贡献。

以下模块图说明模型预测控制过程。控制器由神经网络被控对象模型和优化模块组成。优化模块确定最小化 *J* 的 *u*′ 的值，然后将最佳 *u* 值输入被控对象。控制器模块在 Simulink 中实现，如下节中所述。

Block diagram with inputs y\_r and output y\_p

### 使用神经网络预测控制器模块

本节说明如何使用 NN Predictive Controller 模块。第一步是将 Deep Learning Toolbox 模块库中的 NN Predictive Controller 模块复制到 Simulink Editor 中。如果您不确定如何操作，请参阅 Simulink 文档。在以下示例中跳过此步骤。

Deep Learning Toolbox 软件附带示例模型，以说明如何使用预测控制器。此示例使用具有催化作用的连续搅拌釜反应器 (CSTR)。下图显示过程图。

Process diagram with w\_1, C\_b1, w\_2, and C\_b2, and outputs w\_0 and C\_b

系统的动态模型是

dh(t)dt=w1(t)+w2(t)−0.2h(t)dCb(t)dt=(Cb1−Cb(t))w1(t)h(t)+(Cb2−Cb(t))w2(t)h(t)−k1Cb(t)(1+k2Cb(t))2

其中，*h*(*t*) 是液面，*Cb*(*t*) 是处理过程输出的产品浓度，*w*1(*t*) 是浓缩进料 *Cb*1 的流速，*w*2(*t*) 是稀释进料 *Cb*2 的流速。输入浓度设置为 *Cb*1 = 24.9，*Cb*2 = 0.1。与消耗速率相关联的常量是 *k*1 = 1 和 *k*2 = 1。

控制器的目标是通过调节流量 *w*1(*t*) 来保持产品浓度。为了简化示例，请将 *w*2(*t*) 设置为 0.1。在本试验中，水箱 *h*(*t*) 的液位不受控制。

要运行此示例，请执行下列步骤：

1. 启动 MATLAB®。
2. 在 MATLAB 命令行窗口中键入 `predcstr`。该命令打开 Simulink Editor 并显示以下模型。

   Screenshot of predstr model in Simulink.

   Plant 模块包含 Simulink CSTR 被控对象模型。NN Predictive Controller 模块信号的连接如下：

   - Control Signal 连接到 Plant 模型的输入。
   - Plant Output 信号连接到 Plant 模块输出。
   - Reference 连接到 Random Reference 信号。
3. 双击 NN Predictive Controller 模块。这将打开以下用于设计模型预测控制器的窗口。此窗口使您能够更改控制器时域 *N*2 和 *Nu*。（*N*1 固定为 1。）前面所述的加权参数 ρ 也在此窗口中定义。参数 α 用于控制优化。它决定性能降低多少才算一个成功的优化步。您可以选择优化算法使用哪个线性最小化例程，还可以决定在每个采样时间内执行优化算法的迭代次数。这些线性最小化例程是基于多层浅层神经网络与反向传播训练中所述的那些例程进行了稍微修改的版本。

   Screenshot of Neural Network Predictive Control dialogue box
4. 选择**被控对象辨识**。这将打开以下窗口。您必须开发神经网络被控对象模型，才能使用控制器。被控对象模型预测将来的被控对象输出。优化算法使用这些预测来确定用于优化将来性能的控制输入。如前所示，被控对象模型神经网络有一个隐含层。您可以在此窗口中选择该层的大小、延迟输入和延迟输出的数目以及训练函数。您可以选择多层浅层神经网络与反向传播训练中所述的任何训练函数来训练神经网络被控对象模型。

   Screenshot of Plant Identification dialogue box
5. 点击**生成训练数据**。该计划通过将一系列随机阶跃输入应用于 Simulink 被控对象模型来生成训练数据。然后，潜在的训练数据将显示在与以下类似的图窗中。

   Screenshot of Plant Input-Output Data dialogue box
6. 点击 **Accept Data**，然后点击 Plant Identification 窗口中的 **Train Network**。被控对象模型训练开始。训练将根据您选择的训练算法（在本例中为 `trainlm`）进行。这是批量训练的简单应用，如多层浅层神经网络与反向传播训练中所述。训练完成后，将显示生成的被控对象模型的响应，如以下图窗中所示。（如果存在验证数据和测试数据，也会分别有单独的图。）

   Screenshot of Training Data for NN Predictive Control dialogue box

   然后，您可以通过再次选择 **Train Network** 继续使用相同的数据集进行训练，您可以选择 **Erase Generated Data** 并生成新数据集，也可以接受当前被控对象模型并开始仿真闭环系统。对于此示例，开始仿真，如以下步骤所示。
7. 在 Plant Identification 窗口中选择 **OK**。这会将经过训练的神经网络被控对象模型加载到 NN Predictive Controller 模块中。
8. 在 Neural Network Predictive Control 窗口中选择 **OK**。这会将控制器参数加载到 NN Predictive Controller 模块中。
9. 返回 Simulink 编辑器，选择菜单选项**仿真** > **运行**开始仿真。当仿真运行时，显示被控对象输出和参考信号，如以下图窗中所示。

   2-D line plot with title "X Y Plot". The horizontal axis is labeled "X Axis". The vertical axis is labeled "Y Axis".

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
