---
type: simulink-block
title: 'Wideband Transmit Array'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'widebandtransmitarray'
documentation_source_path: 'ref/widebandtransmitarray.html'
language: en
---

# Wideband Transmit Array

## Ports
```yaml
ports: []
```

**Note**

The block input and output ports correspond to the input and
output parameters described in the `step` method of
the underlying System object. See link at the bottom of this page.

| Port | Description | Supported Data Types |
| --- | --- | --- |
| `X` | Radiated signals input port  The size of the first dimension of the input matrix can vary to simulate a changing signal length. A size change can occur, for example, in the case of a pulse waveform with variable pulse repetition frequency. | Double-precision floating point |
| `Ang` | Radiating directions of signals input port. | Double-precision floating point |
| `W` | Array or subarray weights input port. To enable this port, select the **Enable weights input** check box. | Double-precision floating point |
| `WS` | Subarray element weights input port. To enable this port select `Custom` from the **Subarray steering method** pull down menu. |  |
| `Steer` | Steering angle input port. To enable this port, select `Phase` or `Time` from the **Subarray steering method** pull down menu. |  |
| `Out` | Radiated signals. | Double-precision floating point |
## Parameters
```yaml
parameters: []
```

**Signal Propagation speed (m/s)**
:   Specify the propagation speed of the signal, in meters per second,
    as a positive scalar. You can use the function `physconst` to specify the speed of light.

**Inherit sample rate**
:   Select this check box to inherit the sample rate from upstream blocks. Otherwise,
    specify the sample rate using the **Sample rate (Hz)**
    parameter.

**Sample rate (Hz)**
:   Specify the signal sampling rate (in hertz) as a positive scalar.
    This parameter appears only when the **Inherit sample rate** parameter
    is not selected.

**Assume modulated input**
:   Select this check this box to indicate that the input signal
    is demodulated at a carrier frequency.

**Carrier frequency**
:   This parameter appears when the **Assume modulated input** check
    box is selected. The parameter specifies the carrier frequency, in
    hertz, as a positive scalar.

**Number of subbands**
:   The number of subbands used for subband processing, specified
    as a positive integer.

**Sensor gain measure**
:   Sensor gain measure, specified as `dB` or
    `dBi`.

    - When you set this parameter to `dB`,
      the input signal power is scaled by the sensor power pattern (in
      dB) at the corresponding direction and then combined.
    - When you set this parameter to `dBi`,
      the input signal power is scaled by the directivity pattern (in
      dBi) at the corresponding direction and then combined. This
      option is useful when you want to compare results with the
      values computed by the radar equation that uses dBi to specify
      the antenna gain. The computation using the
      `dBi` option is expensive as it
      requires an integration over all directions to compute the total
      radiated power of the sensor. The default value is
      `dB`.

**Enable weights input**
:   Select this check box to specify array weights using the input
    port `W`. The input port appears only when this box
    is checked.

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
:   Specify sensor element or sensor array. A sensor array can also contain subarrays or be a
    partitioned array. This parameter can also be expressed as a MATLAB expression.

    **Types**

    |  |
    | --- |
    | `Single element` |
    | `Array (no subarrays)` |
    | `Partitioned array` |
    | `Replicated subarray` |
    | `MATLAB expression` |

**Geometry**
:   Specify the array geometry as one of the following:

    - `ULA` — Uniform linear array
    - `URA` — Uniform rectangular
      array
    - `UCA` — Uniform circular array
    - `Conformal Array` — arbitrary
      element positions

**Number of elements**
:   Number of array elements.

    Number of array elements, specified as a positive integer. This parameter appears when the
    **Geometry** is set to `ULA` or
    `UCA`. If **Sensor Array** has a
    `Replicated subarray` option, this parameter applies to the
    subarray.

**Array size**
:   This parameter appears when **Geometry** is
    set to `URA`. When **Sensor Array** is
    set to `Replicated subarray`, this parameter applies
    to the subarrays.

    Specify the size of the array as a positive integer or 1-by-2
    vector of positive integers.

    - If **Array size** is a 1-by-2 vector,
      the vector has the form `[NumberOfArrayRows,NumberOfArrayColumns]`.
    - If **Array size** is an integer,
      the array has the same number of rows and columns.

    For a URA, elements are indexed from top to bottom
    along a column and continuing to the next columns from left to right.
    In this figure, an **Array size** of `[3,2]` produces
    an array of three rows and two columns.

**Element spacing (m)**
:   This parameter appears when **Geometry** is
    set to `ULA` or `URA`. When **Sensor
    Array** has the `Replicated subarray` option,
    this parameter applies to the subarrays.

    - For a `ULA`, specify the spacing,
      in meters, between two adjacent elements in the array as a scalar.
    - For a `URA`, specify the element
      spacing of the array, in meters, as a 1-by-2 vector or a scalar. If **Element
      spacing** is a 1-by-2 vector, the vector has the form `[SpacingBetweenRows,SpacingBetweenColumns]`.
      For a discussion of these quantities, see `phased.URA`. If **Element
      spacing** is a scalar, the spacings between rows and columns
      are equal.

**Array axis**
:   This parameter appears when the **Geometry** parameter
    is set to `ULA` or when the block only supports a
    ULA array geometry. Specify the array axis as `x`, `y`,
    or `z`. All ULA array elements are uniformly spaced
    along this axis in the local array coordinate system.

**Array normal**,
:   This parameter appears when you set **Geometry** to
    `URA` or `UCA`. Specify the
    **Array normal** as `x`,
    `y`, or `z`. All URA and UCA array
    elements are placed in the *yz*, *zx*, or
    *xy*-planes, respectively, of the array coordinate
    system.

**Radius of UCA (m)**
:   Radius of a uniform circular array specified as a positive scalar.
    Units are meters.

    This parameter appears when the **Geometry** is
    set to `UCA`.

**Taper**
:   Tapers, also known as *element weights*,
    are applied to sensor elements in the array. Tapers are used to modify
    both the amplitude and phase of the transmitted or received data.

    This parameter applies to all array types, but when you set **Sensor
    Array** to `Replicated subarray`, this parameter
    applies to subarrays.

    - For a `ULA` or `UCA`,
      specify element tapering as a complex-valued scalar or a complex-valued
      1-by-*N* row vector. In this vector, *N* represents
      the number of elements in the array. If **Taper** is
      a scalar, the same weight is applied to each element. If **Taper** is
      a vector, a weight from the vector is applied to the corresponding
      sensor element. A weight must be applied to each element in the sensor
      array.
    - For a `URA`, specify element tapering
      as a complex-valued scalar or complex-valued *M*-by-*N* matrix.
      In this matrix, *M* is the number of elements along
      the *z*-axis, and *N* is the number
      of elements along the *y*-axis. *M* and *N* correspond
      to the values of `[NumberofArrayRows,NumberOfArrayColumns]` in
      the **Array size** matrix. If `Taper` is
      a scalar, the same weight is applied to each element. If **Taper** is
      a matrix, a weight from the matrix is applied to the corresponding
      sensor element. A weight must be applied to each element in the sensor
      array.
    - For a `Conformal Array`, specify
      element tapering as a complex-valued scalar or complex-valued 1-by-*N* vector.
      In this vector, *N* is the number of elements in
      the array as determined by the size of the **Element positions** vector.
      If **Taper** is a scalar, the same weight is applied
      to each element. If the value of **Taper** is a vector,
      a weight from the vector is applied to the corresponding sensor element.
      A weight must be applied to each element in the sensor array.

**Element lattice**
:   This parameter appears when **Geometry** is
    set to `URA`. When **Sensor Array** is
    set to `Replicated subarray`, this parameter applies
    to the subarray.

    Specify the element lattice as `Rectangular` or `Triangular`

    - `Rectangular` — Aligns all
      the elements in row and column directions.
    - `Triangular`— Shifts the even-row
      elements of a rectangular lattice toward the positive-row axis direction.
      The displacement is one-half the element spacing along the row dimension.

**Element positions (m)**
:   This parameter appears when **Geometry** is
    set to `Conformal Array`. When **Sensor Array** is
    set to `Replicated subarray`, this parameter applies
    to subarrays.

    Specify the positions of conformal array elements as a 3-by-*N* matrix,
    where *N* is the number of elements in the conformal
    array. Each column of **Element positions (m)** represents
    the position of a single element, in the form `[x;y;z]`,
    in the array’s local coordinate system. The local coordinate
    system has its origin at an arbitrary point. Units are in meters.

**Element normals (deg)**
:   This parameter appears when **Geometry** is
    set to `Conformal Array`. When **Sensor Array** is
    set to `Replicated subarray`, this parameter applies
    to subarrays.

    Specify the normal directions of the elements in a conformal
    array as a 2-by-*N* matrix or a 2-by-1 column vector
    in degrees. The variable *N* indicates the number
    of elements in the array. If **Element normals (deg)** is
    a matrix, each column specifies the normal direction of the corresponding
    element in the form `[azimuth;elevation]`, with respect
    to the local coordinate system. The local coordinate system aligns
    the positive *x*-axis with the direction normal to
    the conformal array. If **Element normals (deg)** is
    a 2-by-1 column vector, the vector specifies the same pointing direction
    for all elements in the array.

    You can use the **Element positions (m)** and **Element
    normals (deg)** parameters to represent any arrangement in
    which pairs of elements differ by certain transformations. You can
    combine translation, azimuth rotation, and elevation rotation transformations.
    However, you cannot use transformations that require rotation about
    the normal.

**Subarray definition matrix**
:   This parameter appears when **Specify sensor array as** is set to
    `Partitioned array`.

    Specify the subarray selection as an *M*-by-*N*
    matrix. *M* is the number of subarrays and *N* is the
    total number of elements in the array. Each row of the matrix corresponds to a subarray
    and each entry in the row indicates whether or not an element belongs to the subarray.
    When the entry is zero, the element does not belong the subarray. A nonzero entry
    represents a complex-valued weight applied to the corresponding element. Each row must
    contain at least one nonzero entry.

    The phase center of each subarray is its geometric center. **Subarray
    definition matrix** and **Geometry** determine
    the geometric center.

**Subarray steering method**
:   This parameter appears when the **Specify sensor array as** parameter is set
    to `Partitioned array` or `Replicated
    subarray`.

    Specify the subarray steering method as either

    - `None`
    - `Phase`
    - `Time`
    - `Custom`

    Selecting `Phase` or `Time` opens the
    `Steer` input port on the Narrowband Receive Array,
    Narrowband Transmit Array, Wideband Receive Array,
    Wideband Transmit Array blocks, Constant Gamma
    Clutter, and GPU Constant Gamma Clutter blocks.

    Selecting `Custom` opens the `WS` input port on the
    Narrowband Receive Array, Narrowband Transmit Array,
    Wideband Receive Array, Wideband Transmit Array
    blocks, Constant Gamma Clutter, and GPU Constant Gamma
    Clutter blocks.

**Phase shifter frequency (Hz)**
:   This parameter appears when you set **Sensor array** to `Partitioned
    array` or `Replicated subarray` and you
    set **Subarray steering method** to `Phase`.

    Specify the operating frequency, in hertz, of phase shifters
    to perform subarray steering as a positive scalar.

**Number of bits in phase shifters**
:   This parameter appears when you set **Sensor array** to `Partitioned
    array` or `Replicated subarray` and you
    set **Subarray steering method** to `Phase`.

    The number of bits used to quantize the phase shift component
    of beamformer or steering vector weights. Specify the number of bits
    as a non-negative integer. A value of zero indicates that no quantization
    is performed.

**Subarrays layout**
:   This parameter appears when you set **Sensor array** to `Replicated
    subarray`.

    Specify the layout of the replicated subarrays as `Rectangular` or `Custom`.

**Grid size**
:   This parameter appears when you set **Sensor array** to `Replicated
    subarray` and **Subarrays layout** to `Rectangular`.

    Rectangular subarray grid size, specified as a single positive
    integer or a positive integer-valued 1-by-2 row vector.

    If **Grid size** is an integer scalar, the
    array has an equal number of subarrays in each row and column. If **Grid
    size** is a 1-by-2 vector of the form `[NumberOfRows,
    NumberOfColumns]`, the first entry is the number of subarrays
    along each column. The second entry is the number of subarrays in
    each row. A row is along the local *y*-axis, and
    a column is along the local *z*-axis. The figure
    here shows how you can replicate a 3-by-2 URA subarray using a **Grid
    size** of `[1,2]`.

**Grid spacing**
:   This parameter appears when you set **Sensor array** to `Replicated
    subarray` and **Subarrays layout** to `Rectangular`.

    Specify the rectangular grid spacing of subarrays as a real-valued
    positive scalar, a 1-by-2 row vector, or `Auto`.
    Grid spacing units are expressed in meters.

    - If **Grid spacing** is a scalar,
      the spacing along the row and the spacing along the column is the
      same.
    - If **Grid spacing** is a 1-by-2
      row vector, the vector has the form `[SpacingBetweenRows,SpacingBetweenColumn]`.
      The first entry specifies the spacing between rows along a column.
      The second entry specifies the spacing between columns along a row.
    - If **Grid spacing** is set to `Auto`,
      replication preserves the element spacing of the subarray for both
      rows and columns while building the full array. This option is available
      only when you specify **Geometry** as `ULA` or `URA`.

**Subarray positions (m)**
:   This parameter appears when you set **Sensor array** to `Replicated
    subarray` and **Subarrays layout** to `Custom`.

    Specify the positions of the subarrays in the custom grid as
    a 3-by-*N* matrix, where *N* is
    the number of subarrays in the array. Each column of the matrix represents
    the position of a single subarray, in meters, in the array’s
    local coordinate system. The coordinates are expressed in the form `[x;
    y; z]`.

**Subarray normals**
:   This parameter appears when you set the **Sensor array** parameter
    to `Replicated subarray` and the **Subarrays
    layout** to `Custom`.

    Specify the normal directions of the subarrays in the array.
    This parameter value is a 2-by-*N* matrix, where *N* is
    the number of subarrays in the array. Each column of the matrix specifies
    the normal direction of the corresponding subarray, in the form `[azimuth;
    elevation]`. Each angle is in degrees and is defined in the
    local coordinate system.

    You can use the **Subarray positions** and **Subarray
    normals** parameters to represent any arrangement in which
    pairs of subarrays differ by certain transformations. The transformations
    can combine translation, azimuth rotation, and elevation rotation.
    However, you cannot use transformations that require rotation about
    the normal.

**Expression**
:   A valid MATLAB expression containing an array constructor,
    for example, `phased.URA`.

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

**Introduced in R2015b**

## Description

Wideband transmit array

The Wideband Transmit Array block transmits wideband
plane waves from the elements of a sensor array. The block divides
the transmitted signals into subbands and then applies a phase shift
for each subband according to the radiating direction. The resulting
subband signals are then combined to form the output.
