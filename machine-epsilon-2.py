import numpy as np
import operator

sampling_points_original = np.arange(-1920, 2081)
sampling_points = sampling_points_original/1000.0

f_p_x_sum = lambda x: x**9 - 18 * x**8 + 144 * x**7 - 672 * x**6 + 2016 * x**5 - 4032 * x**4 + 5376 * x**3 - 4608 * x**2 + 2304 * x - 512
f_p_x_mul = lambda x: (x-2)**9
p_x_sum = [f_p_x_sum(x) for x in sampling_points]
p_x_mul = [f_p_x_mul(x) for x in sampling_points]

p_x_delta = [a-b for a,b in zip(p_x_sum,p_x_mul)]
abs_max = max(map(abs, p_x_delta))
abs_min = min(map(abs, p_x_delta))
