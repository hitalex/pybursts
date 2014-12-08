# Pybursts

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