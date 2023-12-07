{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx1145\pardeftab720\ri0\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
\
p = 0.05\
n = 100  # Choose n > 50, for instance\
\
# Verify mean and standard deviation for binomial distribution\
mean = n * p\
std_dev = np.sqrt(n * p * (1 - p))\
\
print(f"Mean (\uc0\u956 ) = \{mean\}")\
print(f"Standard Deviation (\uc0\u963 ) = \{std_dev\}")\
}