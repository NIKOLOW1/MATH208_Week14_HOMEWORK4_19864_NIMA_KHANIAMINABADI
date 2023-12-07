{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx1145\pardeftab720\ri0\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import matplotlib.pyplot as plt\
\
n = 100\
p = 0.2\
\
# Generate binomial and normal distributions\
binomial_dist = np.random.binomial(n, p, 10000)\
normal_approx = np.random.normal(n * p, np.sqrt(n * p * (1 - p)), 10000)\
\
# Plot histograms for comparison\
plt.hist(binomial_dist, bins=20, alpha=0.5, label='Binomial Distribution')\
plt.hist(normal_approx, bins=20, alpha=0.5, label='Normal Approximation')\
plt.legend()\
plt.show()\
}