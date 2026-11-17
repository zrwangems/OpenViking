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
language: en
---

# Design Neural Network Predictive Controller in Simulink

The neural network predictive controller that is implemented in the Deep Learning Toolbox™ software uses a neural network model of a nonlinear plant to predict future plant performance. The controller then calculates the control input that will optimize plant performance over a specified future time horizon. The first step in model predictive control is to determine the neural network plant model (system identification). Next, the plant model is used by the controller to predict future performance. (See the Model Predictive Control Toolbox™ documentation for complete coverage of the application of various model predictive control strategies to linear systems.)

The neural network predictive controller that is implemented
in the Deep Learning Toolbox™ software uses a neural network model
of a nonlinear plant to predict future plant performance. The controller
then calculates the control input that will optimize plant performance
over a specified future time horizon. The first step in model predictive
control is to determine the neural network plant model (system identification).
Next, the plant model is used by the controller to predict future
performance. (See the Model Predictive Control Toolbox™ documentation
for complete coverage of the application of various model predictive
control strategies to linear systems.)

The following section describes the system identification process.
This is followed by a description of the optimization process. Finally,
it discusses how to use the model predictive controller block that
is implemented in the Simulink® environment.

**Note**

To design a neural network predictive controller, you can also use System Identification Toolbox™ and Model Predictive Control Toolbox. Use System Identification Toolbox for plant modeling using a neural network and Model Predictive Control Toolbox to design the controller.

This workflow is recommended because of these advantages:

- Decouple the plant modeling and control design.
- Easy integration with Simulink using dedicated Simulink blocks for neural network plants and
  controllers.
- Several built-in solvers for linear and nonlinear predictive
  control.
- Supports code generation.

For an example showing how to use these tools, see Control House Heating Using Nonlinear MPC with Neural State-Space Prediction Model (Model Predictive Control Toolbox).

### System Identification

The first stage of model predictive control is to train a neural
network to represent the forward dynamics of the plant. The prediction
error between the plant output and the neural network output is used
as the neural network training signal. The process is represented
by the following figure:

System identification diagram with input u and output y\_p.

The neural network plant model uses previous inputs and previous
plant outputs to predict future values of the plant output. The structure
of the neural network plant model is given in the following figure.

Two layer neural network diagram with inputs y\_p(t) and u(t), and output y\_m(t+1).

This network can be trained offline in batch mode, using data
collected from the operation of the plant. You can use any of the
training algorithms discussed in Multilayer Shallow Neural Networks and Backpropagation Training for network training. This process is
discussed in more detail in following sections.

### Predictive Control

The model predictive control method is based on the receding
horizon technique [SoHa96].
The neural network model predicts the plant response over a specified time horizon. The predictions
are used by a numerical optimization program to determine the control
signal that minimizes the following performance criterion over the
specified horizon

J=∑j=N1N2(yr(t+j)−ym(t+j))2+ρ∑j=1Nu(u′(t+j−1)−u′(t+j−2))2

where *N*1, *N*2,
and *Nu* define the horizons
over which the tracking error and the control increments are evaluated.
The *u*′ variable is the tentative control
signal, *yr* is the desired
response, and *ym* is the
network model response. The ρ value determines the contribution
that the sum of the squares of the control increments has on the performance
index.

The following block diagram illustrates the model predictive
control process. The controller consists of the neural network plant
model and the optimization block. The optimization block determines
the values of *u*′ that minimize *J*,
and then the optimal *u* is input to the plant. The
controller block is implemented in Simulink, as described in
the following section.

Block diagram with inputs y\_r and output y\_p

### Use the Neural Network Predictive Controller Block

This section shows how the NN Predictive Controller block is
used. The first step is to copy the NN Predictive Controller block
from the Deep Learning Toolbox block library to the Simulink Editor.
See the Simulink documentation if you are not sure how to do
this. This step is skipped in the following example.

An example model is provided with the Deep Learning Toolbox software
to show the use of the predictive controller. This example uses a
catalytic Continuous Stirred Tank Reactor (CSTR). A diagram of the
process is shown in the following figure.

Process diagram with w\_1, C\_b1, w\_2, and C\_b2, and outputs w\_0 and C\_b

The dynamic model of the system is

dh(t)dt=w1(t)+w2(t)−0.2h(t)dCb(t)dt=(Cb1−Cb(t))w1(t)h(t)+(Cb2−Cb(t))w2(t)h(t)−k1Cb(t)(1+k2Cb(t))2

where *h*(*t*) is the liquid
level, *Cb*(*t*)
is the product concentration at the output of the process, *w*1(*t*)
is the flow rate of the concentrated feed *Cb*1,
and *w*2(*t*)
is the flow rate of the diluted feed *Cb*2.
The input concentrations are set to *Cb*1 = 24.9 and *Cb*2 = 0.1. The constants associated with
the rate of consumption are *k*1 = 1 and *k*2 = 1.

The objective of the controller is to maintain the product concentration
by adjusting the flow *w*1(*t*).
To simplify the example, set *w*2(*t*) = 0.1. The level of the tank *h*(*t*)
is not controlled for this experiment.

To run this example:

1. Start MATLAB®.
2. Type `predcstr` in
   the MATLAB Command Window. This command opens the Simulink Editor
   with the following model.

   Screenshot of predstr model in Simulink.

   The Plant block contains the Simulink CSTR plant model. The
   NN Predictive Controller block signals are connected as follows:

   - Control Signal is connected to the input of the Plant
     model.
   - The Plant Output signal is connected to the Plant
     block output.
   - The Reference is connected to the Random Reference
     signal.
3. Double-click the NN Predictive Controller
   block. This opens the following window for designing the model predictive
   controller. This window enables you to change the controller horizons *N*2 and *Nu*.
   (*N*1 is fixed at 1.) The
   weighting parameter ρ, described earlier, is also defined in
   this window. The parameter α is used to control the optimization.
   It determines how much reduction in performance is required for a
   successful optimization step. You can select which linear minimization
   routine is used by the optimization algorithm, and you can decide
   how many iterations of the optimization algorithm are performed at
   each sample time. The linear minimization routines are slight modifications
   of those discussed in Multilayer Shallow Neural Networks and Backpropagation Training.

   Screenshot of Neural Network Predictive Control dialogue box
4. Select **Plant
   Identification**. This opens
   the following window. You must develop the neural network plant model
   before you can use the controller. The plant model predicts future
   plant outputs. The optimization algorithm uses these predictions to
   determine the control inputs that optimize future performance. The
   plant model neural network has one hidden layer, as shown earlier.
   You select the size of that layer, the number of delayed inputs and
   delayed outputs, and the training function in this window. You can
   select any of the training functions described in Multilayer Shallow Neural Networks and Backpropagation Training to train
   the neural network plant model.

   Screenshot of Plant Identification dialogue box
5. Click **Generate
   Training Data**. The program generates training data by
   applying a series of random step inputs to the Simulink plant
   model. The potential training data is then displayed in a figure similar
   to the following.

   Screenshot of Plant Input-Output Data dialogue box
6. Click **Accept
   Data**, and then click **Train Network** in
   the Plant Identification window. Plant model training begins. The
   training proceeds according to the training algorithm (`trainlm` in this case) you selected. This
   is a straightforward application of batch training, as described in Multilayer Shallow Neural Networks and Backpropagation Training. After
   the training is complete, the response of the resulting plant model
   is displayed, as in the following figure. (There are also separate
   plots for validation and testing data, if they exist.)

   Screenshot of Training Data for NN Predictive Control dialogue box

   You can then continue training with the same data set by selecting **Train Network** again, you can **Erase
   Generated Data** and generate a new data set, or you can
   accept the current plant model and begin simulating the closed loop
   system. For this example, begin the simulation, as shown in the following
   steps.
7. Select **OK** in
   the Plant Identification window. This loads the trained neural network
   plant model into the NN Predictive Controller block.
8. Select **OK** in
   the Neural Network Predictive Control window. This loads the controller
   parameters into the NN Predictive Controller block.
9. Return to the Simulink Editor
   and start the simulation by choosing the menu option **Simulation** > **Run**. As the simulation runs, the plant output and the reference
   signal are displayed, as in the following figure.

   2-D line plot with title "X Y Plot". The horizontal axis is labeled "X Axis". The vertical axis is labeled "Y Axis".

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

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

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
