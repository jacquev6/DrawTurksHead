Intuitive construction of the curves to be drawn
================================================

Looking at the [flat form](http://en.wikipedia.org/wiki/File:Turks-head-3-lead-10-bight-doubled.jpg) of Turk's head knots, we see that the string oscillates between the center and the outside while it turns around the center. This is why the first idea is to draw some sine wave is polar coordinates. (Oscillation means sine wave, turning around the center means polar coordinates)

Since we don't want the curve to go through the center of the image, we have to keep the radius strictly positive, so we will draw <code>r=r_0+\delta_r \cdot \cos( \alpha \cdot \theta )</code>, with <code>0 < \delta_r < r_0</code>.

The next question is how to fix <code>\alpha</code>. For a knot with <code>q</code> leads, the string make <code>q</code> turns around the center, so we will draw the wave for <code>\theta \in [0, 2 \cdot q \cdot \pi]</code>. Then, for a knot with <code>p</code> bights, the string touches the center <code>p</code> times, and the outside <code>p</code> times. Thus, the wave must have <code>p</code> maxima and <code>p</code> minima on the range. <code>\cos</code> has exactly one maximum and one minimum on <code>[0,2 \cdot \pi]</code>, so we can use <code>\alpha=p/q</code>. This gives us <code>r=r_0+\delta_r \cdot cos( p \cdot \theta/q )</code>, for <code>\theta \in [0, 2 \cdot q \cdot \pi]</code>.

The next image shows this plot for small values of <code>p</code> and <code>q</code>.

<img src="basic_waves_1.png"/>

This is mainly ok, but some cases look wrong (or example, <code>p=3</code> and <code>q=6</code>). This is due to the known result that, if <code>d=\gcd( p, q )</code>, you need <code>d</code> strings to make a Turk's head knot with <code>p</code> bights and <code>q</code> leads. This mean that we have to draw <code>d</code> curves. The total number of turns around the center is still the same, so each string makes <code>q/d</code> turns, and the range for <code>\theta</code> is reduced to <code>[0,2 \cdot q \cdot \pi / d]</code>.

Since the second curve must draw the second bight, it means that the second curve must be shifted by <code>2 \codt \pi / p</code>. Extending this result tells us that the <code>k^{th}</code> curve must be shifted by <code>2 \cdot k \cdot \pi / p</code>

This give use our final family of curves: <code>r_k=r+\delta_r \cdot \cos \left( \frac { p \cdot ( \theta - 2 \cdot k \cdot \pi / p ) } { q } \right)</code>.

<img src="basic_waves_2.png"/>

Intersections and periodicity
=============================

The string must go once up and once down each time it crosses another string (or itself). So, we need to compute the coordinates of the intersection points.

Let's forget what have been said in previous section, and analyse this from a mathematical point of view.

Given two natural integers <code>p</code> and <code>q</code> and two real numbers <code>r</code> and <code>\delta_r</code> such that <code>0 < \delta_r < r</code>, let <code>d=\gcd( p, q )</code>. Let's define the family of functions <code>r_k : \theta \mapsto r + \delta_r \cdot \cos\left( p \cdot \frac { \theta - \phi_k } q \right)</code> with <code>\phi_k = 2 \cdot k \cdot \pi / p</code> for <code>k \in \mathbb Z</code>. Let <code>\Gamma_k</code> be the graph of <code>r_k</code> in polar coordinates, that is the graph of <code>\vec { r_k } : \theta \mapsto r_k( \theta ) \cdot \vec u( \theta )</code>.

<code>\Gamma_m</code> and <code>\Gamma_n</code> intersect if and only if <code>\exists \theta_1, \theta_2 \in \mathbb R^2, \vec {r_n}( \theta_1 ) = \vec {r_m}( \theta_2 )</code>.

To be done... Thank you for your patience.

This finnally gives us the following intersection points:

<img src="intersections.png"/>
