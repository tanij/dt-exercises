

[ ] Lower overshoot.
[ ] Faster system reaction times.
[x] Disturbance rejection.
[ ] Increased stability.

[explanation]
The I term allows the controller to take into account the history of the tracking error, allowing to compensate for biases (too high, too low). Integral control has the potential to eliminate steady-state error (in some systems) and most importantly brings to the table "disturbance rejection", i.e., the ability to recover from external unexpected perturbations to the system's behavior.
[explanation]

>> How many industrial applications do you think implement some form of PID control, today? <<

( ) Less than 50%.
( ) Between 50% and 60%.
( ) Between 60% and 75%.
( ) Between 75% and 90%.
(x) More than 90%.
( ) More than 95%.


[explanation]
We're not sure about the correct answer as of today, but it is "common knowledge" (and reported in the 2001 paper below) that >90% of industrial automation applications are controlled through PID, or variations thereof. Some sources report up to 97%. Although the data is a little old (and difficult to verify), it is safe to take away that the great majority of real-world control problems are solved through PID.  

K.J. Åström, T. Hägglund, The future of PID control, Control Engineering Practice, Volume 9, Issue 11, 2001, Pages 1163-1175, ISSN 0967-0661, https://doi.org/10.1016/S0967-0661(01)00062-4.
[explanation]
