import numpy as np

from topokin.graph.rings import ring_count_by_size


def test_triangle():
    a = np.array([[0,1,1],[1,0,1],[1,1,0]])
    c = ring_count_by_size(a, 6)
    assert c[3] == 1


def test_square():
    a = np.array([[0,1,0,1],[1,0,1,0],[0,1,0,1],[1,0,1,0]])
    c = ring_count_by_size(a, 6)
    assert c[4] == 1


def test_pentagon():
    n=5
    a=np.zeros((n,n),dtype=int)
    for i in range(n):
        a[i,(i+1)%n]=1;a[(i+1)%n,i]=1
    c=ring_count_by_size(a,6)
    assert c[5]==1


def test_chorded_square_not_primitive():
    a = np.array([[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]])
    c=ring_count_by_size(a,6)
    assert c[4]==0
