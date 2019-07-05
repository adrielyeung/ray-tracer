"""
genpolar
========

Generates a sequence of plane polar coordinates (r and theta).

Functions defined here:

rtpairs       -- generates a list of radii r as specified and angles theta
determined by the number of points as specified

rtuniform     -- generates a list of sequence of radii r and angles theta
uniformly distributed over a disk

"""


import numpy as np


def rtpairs(R, N):
    """
    Return n uniformly distributed pairs with radius r as specified and angles
    theta generated using n.

    Parameters
    ----------
    R : list
        The list of different radii r of the points.
    N : list
        The list containing the number of angles theta for each value of r.
        The sizes of R and N must be equal.

    Returns
    -------
    radius : ndarray
        Shows the radius of each pair. Contains the radii as defined in array R
        repeated a number of times as defined in the corresponding value in
        array N.
    theta : ndarray
        Shows the angle of each pair. For a given radius, the angles are evenly
        spaced out with the number of angles as defined in N.

    Graphical illustration:

    >>> import pylab as pl
    >>> R = [0.0, 0.1, 0.2]
    >>> N = [1, 10, 20]
    >>> for r, n in genpolar.rtpairs(R, N):
            pl.plot(r * cos(n), r * sin(n), 'bo')
    """
    R = np.array(R)
    N = np.array(N)
    if R.size != N.size:
        raise Exception("Size mismatch")
    for r, n in zip(R, N):  # zip takes values from same position in arrays R &
        # N and pairs them up
        theta = np.linspace(0, 2*np.pi, n + 1)  # n + 1 pts needed because 0
        # and 2*pi are same pt
        radius = np.repeat(r, n + 1)
        yield np.array(list(radius)), np.array(list(theta))


def rtuniform(n, rmax, m):
    """
    Return rings of points with radii r and angles theta that are approximately
    uniformly distributed over a disk.

    Parameters
    ----------
    n : integer
        The number of intermediate layers between 0 and rmax (radius = 0 not
        included as a layer).
    rmax : float
        The radius of the outermost ring.
    m : integer
        The number of points in the innermost ring (with radius > 0). The
        number of points in successive rings are multiples of m.

    Returns
    -------
    radius : ndarray
        Shows the radius of each pair. Contains the radii as defined in array R
        repeated a number of times as defined in the corresponding value in
        array N.
    theta : ndarray
        Shows the angle of each pair. For a given radius, the angles are evenly
        spaced out with the number of angles as defined in N.    

    Graphical illustration:

    >>> import pylab as pl
    >>> for r, t in genpolar.rtuniform(n=10, rmax=0.1, m=6):
            pl.plot(r * cos(t), r * sin(t), 'bo')
    """
    R = np.linspace(0, rmax, n + 1)  # n + 1 layers for i = 0, 1, ..., n
    N = np.repeat(1, n + 1)
    for i in range(1, n + 1):
        N[i] = m * i
    return rtpairs(R, N)
