# Navier-Stokes mid-latitude weather systems vs thermal (bubble)

Based on [notes](https://atoc.colorado.edu/~cassano/atoc4720/chapter_summaries/chapter05.pdf)

## Scales

| Scale | Symbol  |  mid-latitude weather systems | thermal |
|-------|---------|-----------|------|
|Horizontal wind scale |U |10 ms<sup>-1</sup> |1 ms<sup>-1</sup>|
|Vertical wind scale|W |10<sup>-2</sup> ms<sup>-1</sup> |1 ms<sup>-1</sup>
|Horizontal length scale| L |10<sup>6</sup> m| 10<sup>2</sup> m|
|Vertical length scale| H | 10<sup>4</sup> m | 10<sup>2</sup> m|
|Time scale (L/U) | T | 10<sup>5</sup> s |   10 s |
|Kinematic viscosity | nu | 10<sup>-5</sup> m<sup>2</sup>s<sup>-1</sup> |10<sup>-5</sup> m<sup>2</sup>s<sup>-1</sup> |
|Dynamic pressure scale| δp/ρ | 10<sup>3</sup> m<sup>2</sup>s<sup>-2</sup> | ??? |
|Total pressure scale | P/ρ | 10<sup>5</sup> m<sup>2</sup>s<sup>-2</sup> | 10<sup>5</sup> m<sup>2</sup>s<sup>-2</sup> |
| Gravity |g | 10 ms<sup>-2</sup> | 10 ms<sup>-2</sup> |
| Coriolis | f = 2 Omega sin 45 | 10<sup>-4</sup> | 10<sup>-4</sup>|
| density variation | δρ/ρ, δT/T  | 10<sup>-2</sup> |  10<sup>-2</sup> |

## Horizontal wind equations

| Feature | Acceleration | Hor. advection | Vert. advection | Pressure gradient |Viscosity | Coriolis |
|----|----|----|----|----|----|----|
| scale | U<sup>2</sup>/ L | U<sup>2</sup>/L | UW/H| δp/ρL| nu U/L<sup>2</sup> | f0 U |
| wheather | 10<sup>-4</sup>|10<sup>-4</sup>|10<sup>-5</sup>|10<sup>-3</sup>|10<sup>-16</sup>|10<sup>-3</sup>|
| thermal | 10<sup>-2</sup> | 10<sup>-2</sup> | 10<sup>-2</sup> | ? 10<sup>-3</sup> | 10<sup>-10</sup> | 10<sup>-4</sup>|

## Vertical wind equations

| Feature |Acceleration | Hor. advection | Vert. advection | Hydrostatic Pressure gradient | Gravity | Buoyancy | Viscosity | Coriolis |
|----|----|----|----|----|----|----|----|----|
| scale | UW / L | UW / L | W<sup>2</sup> / H | P / ρH | g | g δρ/ρ  | nu W/ L<sup>2</sup> | f0 U |
| wheather | 10<sup>-7</sup>  | 10<sup>-7</sup>  | 10<sup>-8</sup> | 10 | 10 | ? | 10<sup>-19</sup> |  10<sup>-3</sup> |
| thermal | 10<sup>-2</sup> |  10<sup>-2</sup> |  10<sup>-2</sup> | 100 | 10 |   10<sup>-1</sup> | 10<sup>-9</sup>  |  10<sup>-4</sup> |