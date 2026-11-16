---
type: simulink-block
title: 'ULA Sum and Difference Monopulse'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Direction of Arrival'
documentation_page: 'ulasumanddifferencemonopulse'
documentation_source_path: 'ref/ulasumanddifferencemonopulse.html'
language: en
---

# ULA Sum and Difference Monopulse

## Ports

**Note**

The block input and output ports correspond to the input and
output parameters described in the `step` method of
the underlying System object. See link at the bottom of this page.

| Port | Description | Supported Data Types |
| --- | --- | --- |
| `X` | Input signal.  The size of the first dimension of the input matrix can vary to simulate a changing signal length. A size change can occur, for example, in the case of a pulse waveform with variable pulse repetition frequency. | Double-precision floating point |
| `Steer` | Initial estimate of broadside DOA angles. | Double-precision floating point |
| `Ang` | Estimated broadside DOA angles. | Double-precision floating point |

## Parameters

**Signal Propagation speed (m/s)**
:   Specify the propagation speed of the signal, in meters per second,
    as a positive scalar. You can use the function `physconst` to specify the speed of light.

**Operating frequency (Hz)**
:   Specify the operating frequency of the system, in hertz, as
    a positive scalar.

**Number of bits in phase shifters**
:   The number of bits used to quantize the phase shift component
    of beamformer or steering vector weights. Specify the number of bits
    as a non-negative integer. A value of zero indicates that no quantization
    is performed.

**Simulate using**
:   Block simulation method, specified as `Interpreted Execution` or `Code
    Generation`. If you want your block to use the MATLAB® interpreter,
    choose `Interpreted Execution`. If you want your
    block to run as compiled code, choose `Code Generation`.
    Compiled code requires time to compile but usually runs faster.

    Interpreted execution is useful when you are developing and
    tuning a model. The block runs the underlying System object™ in MATLAB.
    You can change and execute your model quickly. When you are satisfied
    with your results, you can then run the block using `Code
    Generation`. Long simulations run faster than they would
    in interpreted execution. You can run repeated executions without
    recompiling. However, if you change any block parameters, then the
    block automatically recompiles before execution.

    When setting this parameter, you must take into account the
    overall model simulation mode. The table shows how the **Simulate
    using** parameter interacts with the overall simulation mode.

    When the Simulink® model is in `Accelerator` mode, the block mode specified
    using **Simulate using** overrides the simulation mode.

    **Acceleration Modes**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | Block Simulation | Simulation Behavior | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
    | `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

    For more information, see Choosing a Simulation Mode (Simulink).

### Array Parameters

**Specify sensor array as**
:   Specify a ULA sensor array directly or by using a MATLAB expression.

    **Types**

    |  |
    | --- |
    | `Array (no subarrays)` |
    | `MATLAB expression` |

**Number of elements**
:   Specifies the number of elements in the array as an integer.

**Element spacing**
:   Specify the spacing, in meters, between two adjacent elements
    in the array.

**Array axis**
:   This parameter appears when the **Geometry** parameter
    is set to `ULA` or when the block only supports a
    ULA array geometry. Specify the array axis as `x`, `y`,
    or `z`. All ULA array elements are uniformly spaced
    along this axis in the local array coordinate system.

**Taper**
:   Tapers, also known as *element weights*,
    are applied to sensor elements in the array. Tapers are used to modify
    both the amplitude and phase of the transmitted or received data.

    Specify element tapering as a complex-valued scalar or a complex-valued
    1-by-*N* row vector. In this vector, *N* represents
    the number of elements in the array. If **Taper** is
    a scalar, the same weight is applied to each element. If **Taper** is
    a vector, a weight from the vector is applied to the corresponding
    sensor element. A weight must be applied to each element in the sensor
    array.

**Expression**
:   A valid MATLAB expression containing a constructor for
    a uniform linear array, for example, `phased.ULA`.

### Sensor Array Tab: Element Parameters

**Element type**
:   Specify antenna or microphone type as

    - `Isotropic Antenna`
    - `Cosine Antenna`
    - `Custom Antenna`
    - `Omni Microphone`
    - `Custom Microphone`

**Exponent of cosine pattern**
:   This parameter appears when you set **Element type** to `Cosine
    Antenna`.

    Specify the exponent of the cosine pattern as a scalar or a
    1-by-2 vector. You must specify all values as non-negative real numbers.
    When you set **Exponent of cosine pattern** to a
    scalar, both the azimuth direction cosine pattern and the elevation
    direction cosine pattern are raised to the specified value. When you
    set **Exponent of cosine pattern** to a 1-by-2 vector,
    the first element is the exponent for the azimuth direction cosine
    pattern and the second element is the exponent for the elevation direction
    cosine pattern.

**Operating frequency range (Hz)**
:   This parameter appears when **Element type** is
    set to `Isotropic Antenna`, `Cosine Antenna`,
    or `Omni Microphone`.

    Specify the operating frequency range, in hertz, of the antenna
    element as a 1-by-2 row vector in the form `[LowerBound,UpperBound]`.
    The antenna element has no response outside the specified frequency
    range.

**Operating frequency vector (Hz)**
:   This parameter appears when **Element type** is
    set to `Custom Antenna` or `Custom Microphone`.

    Specify the frequencies, in Hz, at which to set the antenna
    and microphone frequency responses as a 1-by-*L* row
    vector of increasing values. Use **Frequency responses** to
    set the frequency responses. The antenna or microphone element has
    no response outside the frequency range specified by the minimum and
    maximum elements of **Operating frequency vector (Hz)**.

**Frequency responses (dB)**
:   This parameter appears when **Element type** is
    set to `Custom Antenna` or `Custom Microphone`.

    Specify this parameter as the frequency response of an antenna
    or microphone, in decibels, for the frequencies defined by **Operating
    frequency vector (Hz)**. Specify **Frequency responses
    (dB)** as a 1-by-*L* vector matching the
    dimensions of the vector specified in **Operating frequency
    vector (Hz)**.

**Input Pattern Coordinate System**
:   Coordinate system of custom antenna pattern, specified
    `az-el` or `phi-theta`.
    When you specify `az-el`, use the **Azimuth
    angles (deg)** and **Elevations angles (deg)**
    parameters to specify the coordinates of the pattern points. When you specify
    `phi-theta`, use the **Phi angles
    (deg)** and **Theta angles (deg)** parameters to
    specify the coordinates of the pattern points.

**Azimuth angles (deg)**
:   This parameter appears when **Element type** is set to
    `Custom Antenna` and the **Input Pattern Coordinate
    System** parameter is set to `az-el`.

    Specify the azimuth angles at which to calculate the antenna radiation pattern as a
    1-by-*P* row vector. *P* must be greater than 2.
    Angle units are in degrees. Azimuth angles must lie between –180° and 180° and
    be in strictly increasing order.

**Elevation angles (deg)**
:   This parameter appears when **Element type** is set to
    `Custom Antenna` and the **Input Pattern Coordinate
    System** parameter is set to `az-el`.

    Specify the elevation angles at which to compute the radiation pattern as a
    1-by-*Q* vector. *Q* must be greater than 2. Angle
    units are in degrees. Elevation angles must lie between –90° and 90° and be in
    strictly increasing order.

**Phi Angles (deg)**
:   This parameter appears when **Element type** is set to
    `Custom Antenna` and the **Input Pattern Coordinate
    System** parameter is set to
    `phi-theta`.

    Phi angles of points at which to specify the antenna radiation pattern,
    specify as a 1-by-*P* row vector. *P* must be
    greater than 2. Angle units are in degrees. Phi angles must lie between 0°
    and 360° and be in strictly increasing order.

**Theta Angles (deg)**
:   This parameter appears when **Element type** is set to
    `Custom Antenna` and the **Input Pattern Coordinate
    System** parameter is set to
    `phi-theta`.

    Theta angles of points at which to specify the antenna radiation pattern,
    specify as a 1-by-*Q* row vector. *Q* must be
    greater than 2. Angle units are in degrees. Theta angles must lie between
    0° and 180° and be in strictly increasing order.

**Magnitude pattern (dB)**
:   This parameter appears when the **Element type** is
    set to `Custom Antenna`.

    Magnitude of the combined antenna radiation pattern, specified as a
    *Q*-by-*P* matrix or a
    *Q*-by-*P*-by-*L* array.

    - When the **Input Pattern Coordinate System** parameter is set to
      `az-el`, *Q* equals the length of the vector
      specified by the **Elevation angles (deg)** parameter and
      *P* equals the length of the vector specified by the
      **Azimuth angles (deg)** parameter.
    - When the **Input Pattern Coordinate System** parameter is set to
      `phi-theta`, *Q* equals the length of the
      vector specified by the **Theta Angles (deg)** parameter and
      *P* equals the length of the vector specified by the **Phi
      Angles (deg)** parameter.

    The quantity *L* equals the length of the **Operating
    frequency vector (Hz)**.

    - If this parameter is a *Q*-by-*P* matrix, the same
      pattern is applied to *all* frequencies specified in the
      **Operating frequency vector (Hz)** parameter.
    - If the value is a *Q*-by-*P*-by-*L*
      array, each *Q*-by-*P* page of the array specifies a pattern
      for the *corresponding* frequency specified in the **Operating
      frequency vector (Hz)** parameter.

**Phase pattern (dB)**
:   This parameter appears when the **Element type** is
    set to `Custom Antenna`.

    Phase of the combined antenna radiation pattern, specified as a
    *Q*-by-*P* matrix or a
    *Q*-by-*P*-by-*L* array.

    - When the **Input Pattern Coordinate System** parameter is set to
      `az-el`, *Q* equals the length of the vector
      specified by the **Elevation angles (deg)** parameter and
      *P* equals the length of the vector specified by the
      **Azimuth angles (deg)** parameter.
    - When the **Input Pattern Coordinate System** parameter is set to
      `phi-theta`, *Q* equals the length of the
      vector specified by the **Theta Angles (deg)** parameter and
      *P* equals the length of the vector specified by the **Phi
      Angles (deg)** parameter.

    The quantity *L* equals the length of the **Operating
    frequency vector (Hz)**.

    - If this parameter is a *Q*-by-*P* matrix, the same
      pattern is applied to *all* frequencies specified in the
      **Operating frequency vector (Hz)** parameter.
    - If the value is a
      *Q*-by-*P*-by-*L* array, each
      *Q*-by-*P* page of the array specifies a pattern for
      the *corresponding* frequency specified in the **Operating
      frequency vector (Hz)** parameter.

    - If this parameter is a *Q*-by-*P* matrix, the same
      pattern is applied to *all* frequencies specified in the
      **Operating frequency vector (Hz)** parameter.
    - If the value is a *Q*-by-*P*-by-*L*
      array, each *Q*-by-*P* page of the array specifies a pattern
      for the *corresponding* frequency specified in the **Operating
      frequency vector (Hz)** parameter.

**MatchArrayNormal**
:   This parameter appears when the **Element type** is set to
    `Custom Antenna`.

    Select this check box to rotate the antenna element pattern to align with the
    array normal. When not selected, the element pattern is not rotated.

    When the antenna is used in an antenna array and the **Input Pattern
    Coordinate System** parameter is `az-el`,
    selecting this check box rotates the pattern so that the
    *x*-axis of the element coordinate system points along the
    array normal. Not selecting uses the element pattern without the
    rotation.

    When the antenna is used in an antenna array and **Input Pattern
    Coordinate System** is set to `phi-theta`,
    selecting this check box rotates the pattern so that the
    *z*-axis of the element coordinate system points along the
    array normal.

    Use the parameter in conjunction with the **Array normal**
    parameter of the `URA` and
    `UCA` arrays.

**Polar pattern frequencies (Hz)**
:   This parameter appears when the **Element type** is
    set to `Custom Microphone`.

    Specify the measuring frequencies of the polar patterns as a 1-by-*M* vector.
    The measuring frequencies lie within the frequency range specified by the
    **Operating frequency vector (Hz)** parameter. Frequency units are
    in Hz.

**Polar pattern angles (deg)**
:   This parameter appears when **Element type** is
    set to `Custom Microphone`.

    Specify the measuring angles of the polar patterns, as a 1-by-*N* vector.
    The angles are measured from the central pickup axis of the microphone,
    and must be between –180° and 180°, inclusive.

**Polar pattern (dB)**
:   This parameter appears when **Element type** is
    set to `Custom Microphone`.

    Specify the magnitude of the microphone element polar pattern
    as an *M*-by-*N* matrix. *M* is
    the number of measuring frequencies specified in **Polar pattern
    frequencies (Hz)**. *N* is the number of
    measuring angles specified in **Polar pattern angles (deg)**.
    Each row of the matrix represents the magnitude of the polar pattern
    measured at the corresponding frequency specified in **Polar
    pattern frequencies (Hz)** and all angles specified in **Polar
    pattern angles (deg)**. Assume that the pattern is measured
    in the azimuth plane. In the azimuth plane, the elevation angle is
    0° and the central pickup axis is 0° degrees azimuth and
    0° degrees elevation. Assume that the polar pattern is symmetric
    around the central axis. You can construct the microphone’s
    response pattern in 3-D space from the polar pattern.

**Baffle the back of the element**
:   This check box appears only when the **Element type** parameter
    is set to `Isotropic Antenna` or `Omni Microphone`.

    Select this check box to baffle the back of the antenna element.
    In this case, the antenna responses to all azimuth angles beyond ±90°
    from *broadside* are set to zero. Define the
    broadside direction as 0° azimuth angle and 0° elevation
    angle.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Sum-and-difference monopulse tracker for ULA

The ULA Sum-and-Difference Monopulse block estimates
the direction of arrival of a narrowband signal on a uniform linear
array based on an initial guess using a sum-and-difference monopulse
algorithm. The block obtains the difference steering vector by phase-reversing
the latter half of the sum steering vector.
