Intuitive construction of the curves to be drawn
================================================

Looking at the [flat form](http://en.wikipedia.org/wiki/File:Turks-head-3-lead-10-bight-doubled.jpg) of Turk's head knots, we see that the string oscillates between the center and the outside while it turns around the center. This is why the first idea is to draw some sine wave is polar coordinates. (Oscillation means sine wave, turning around the center means polar coordinates)

Since we don't want the curve to go through the center of the image, we have to keep the radius strictly positive, so we will draw \\(r=r_0+\\delta_r \\cdot \\cos( \\alpha \\cdot \\theta )\\), with \\(0 < \\delta_r < r_0\\).

The next question is how to fix \\(\\alpha\\). For a knot with \\(q\\) leads, the string make \\(q\\) turns around the center, so we will draw the wave for \\(\\theta \\in [0, 2 \\cdot q \\cdot \\pi]\\). Then, for a knot with \\(p\\) bights, the string touches the center \\(p\\) times, and the outside \\(p\\) times. Thus, the wave must have \\(p\\) maxima and \\(p\\) minima on the range. \\(\\cos\\) has exactly one maximum and one minimum on \\([0,2 \\cdot \\pi]\\), so we can use \\(\\alpha=p/q\\). This gives us \\(r=r_0+\\delta_r \\cdot \\cos( p \\cdot \\theta/q )\\), for \\(\\theta \\in [0, 2 \\cdot q \\cdot \\pi]\\).

The next image shows this plot for small values of \\(p\\) and \\(q\\).

<img src="/static/basic_waves_1.png"/>

This is mainly ok, but some cases look wrong (or example, \\(p=3\\) and \\(q=6\\)). This is due to the known result that, if \\(d=\\gcd( p, q )\\), you need \\(d\\) strings to make a Turk's head knot with \\(p\\) bights and \\(q\\) leads. This mean that we have to draw \\(d\\) curves. The total number of turns around the center is still the same, so each string makes \\(q/d\\) turns, and the range for \\(\\theta\\) is reduced to \\([0,2 \\cdot q \\cdot \\pi / d]\\).

Since the second curve must draw the second bight, it means that the second curve must be shifted by \\(2 \\cdot \\pi / p\\). Extending this result tells us that the \\(k^{th}\\) curve must be shifted by \\(2 \\cdot k \\cdot \\pi / p\\)

This give use our final family of curves: \\(r_k=r+\\delta_r \\cdot \\cos \\left( \\frac { p \\cdot ( \\theta - 2 \\cdot k \\cdot \\pi / p ) } { q } \\right)\\).

<img src="/static/basic_waves_2.png"/>

Intersections and periodicity
=============================

The string must go once up and once down each time it crosses another string (or itself). So, we need to compute the coordinates of the intersection points.

Let's forget what have been said in previous section, and analyse this from a mathematical point of view.

Given two natural integers \\(p\\) and \\(q\\) and two real numbers \\(r\\) and \\(\\delta_r\\) such that \\(0 < \\delta_r < r\\), let \\(d=\\gcd( p, q )\\). Let's define the family of functions \\(r_k : \\theta \\mapsto r + \\delta_r \\cdot \\cos\\left( p \\cdot \\frac { \\theta - \\phi_k } q \\right)\\) with \\(\\phi_k = 2 \\cdot k \\cdot \\pi / p\\) for \\(k \\in \\mathbb Z\\). Let \\(\\Gamma_k\\) be the graph of \\(r_k\\) in polar coordinates, that is the graph of \\(\\vec { r_k } : \\theta \\mapsto r_k( \\theta ) \\cdot \\vec u( \\theta )\\).

\\(\\Gamma_m\\) and \\(\\Gamma_n\\) intersect if and only if \\(\\exists \\theta_1, \\theta_2 \\in \\mathbb R^2, \\vec {r_n}( \\theta_1 ) = \\vec {r_m}( \\theta_2 )\\).

To be done... Thank you for your patience.

This finally gives us the following intersection points:

<img src="/static/intersections.png"/>

Special thanks to [MathJax](http://www.mathjax.org) for client-side rendering of math formulas.
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
