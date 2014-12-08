# Pybursts

## Changelog

### 0.1.1
* Update readme [view commit](http://github.com/rpoddighe/pybursts/commit/92e695f30ab8faf7375d81030f1124b73b903fa5)
* Tidy up module imports [view commit](http://github.com/rpoddighe/pybursts/commit/c665e5ffee63d3087eae99bc6781773ea4d64aef)
* Add .gitignore [view commit](http://github.com/rpoddighe/pybursts/commit/d8ed0480afe89193e4f56c008a7edf4922571855)

## Description
This is a Python port of the [R implementation](http://cran.r-project.org/web/packages/bursts/index.html) of Kleinberg's algorithm (described in ['Bursty and Hierarchical Structure in Streams'](http://www.cs.cornell.edu/home/kleinber/bhs.pdf)). The algorithm models activity bursts in a time series as an infinite hidden Markov model.

## Installation

```shell
pip install pybursts
```

or

```shell
easy_install pybursts
```

## Dependencies
* [NumPy](http://www.numpy.org/)


## Usage
```python

import pybursts

offsets = [4, 17, 23, 27, 33, 35, 37, 76, 77, 82, 84, 88, 90, 92]
print pybursts.kleinberg(offsets, s=2, gamma=0.1)

```

## Input

* *offsets*: a list of time offsets (numeric)
* *s*: the base of the exponential distribution that is used for modeling the event frequencies
* *gamma*: coefficient for the transition costs between states

## Output

An array of intervals in which a burst of activity was detected. The first column denotes the level within the hierarchy; the second column the start value of the interval; the third column the end value. The first row is always the top-level activity (the complete interval from start to finish).

## References

* [CRAN - Package bursts](http://cran.r-project.org/web/packages/bursts/index.html)
* [J. Kleinberg. Bursty and Hierarchical Structure in Streams. Proc. 8th ACM SIGKDD Intl. Conf. on Knowledge Discovery and Data Mining, 2002.](http://www.cs.cornell.edu/home/kleinber/bhs.pdf)
