{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx1587\pardeftab720\ri0\partightenfactor0

\f0\fs24 \cf0 import numpy as np\
import matplotlib.pyplot as plt\
\
# Generate 100 random numbers in T distribution with df=10\
t_distribution = np.random.standard_t(df=10, size=100)\
\
# Calculate mean and standard deviation of 100 random numbers\
mean_t = np.mean(t_distribution)\
std_dev_t = np.std(t_distribution)\
\
# Create 1000 sampling groups with 30 samples each\
num_sampling_groups = 1000\
sampling_groups = [np.random.choice(t_distribution, size=30) for _ in range(num_sampling_groups)]\
\
# Calculate means of the sampling groups and verify CLT\
means_sampling_groups = [np.mean(sample) for sample in sampling_groups]\
mean_means = np.mean(means_sampling_groups)\
std_dev_means = std_dev_t / np.sqrt(30)\
\
# Plot histogram of means of sampling groups\
plt.hist(means_sampling_groups, bins=30, alpha=0.7)\
plt.xlabel('Sample Means')\
plt.ylabel('Frequency')\
plt.title('Sampling Distribution of Sample Means')\
\pard\pardeftab720\ri0\partightenfactor0
\cf0 plt.show()}