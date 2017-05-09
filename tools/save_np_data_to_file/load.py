# -*- coding: utf-8 -*-
import numpy as np

loaded = np.load('test.npz')
print loaded['t1']
print loaded.files