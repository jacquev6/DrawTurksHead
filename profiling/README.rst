For a start we focus on the total time needed to produce this image:

.. image:: reference.png

with the following command::

    $ time python -m DrawTurksHead --width=1600 --height=1200 --leads=9 --bights=12 --radius-variation=450 --line-width=39 --output=profiling/reference.png

    real    0m5.511s
    user    0m5.484s
    sys     0m0.024s

We've modified the step for theta to reach a reasonable reference time (5s).
This step MUST NOT be modified between experience to be able to compare results.
This should be checked by comparing the visible color areas in the reference image and the produced image.
