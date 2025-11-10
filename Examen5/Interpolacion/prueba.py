import numpy as np
import sympy as sp

x = sp.symbols('x')  # Variable simbólica
fs = sp.sin((sp.pi*x)/2)

dfs = sp.diff(fs, x)
dfs2= sp.diff(dfs, x)
dfn = sp.lambdify(x, dfs, 'numpy')
dfn2 = sp.lambdify(x, dfs2, 'numpy')

p=sp.simplify(dfs2)
print(p)