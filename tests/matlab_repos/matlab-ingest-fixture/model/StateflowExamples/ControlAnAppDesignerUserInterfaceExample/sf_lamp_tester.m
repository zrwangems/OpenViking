% Test the sf_lamp_logic chart object

% 1. Create the chart object and initialize the value of delay to 1.

L = sf_lamp_logic('delay',1);
pause(2)

% 2. Turn lamp on.

ON(L);
pause(2)

% 3. Switch to blinking mode.

BLINKING(L);
pause(2)

% 4. Set value of delay to 0.5.

L.delay = 0.5;
pause(2)

% 5. Switch to solid mode.

SOLID(L);
pause(2)

% 6. Turn lamp off.

OFF(L);
pause(2)

% 7. Delete chart object.

delete(L);
