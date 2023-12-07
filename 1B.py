{\rtf1\ansi\ansicpg1252\cocoartf2513
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\tx1145\pardeftab720\ri0\partightenfactor0

\f0\fs24 \cf0 import scipy.stats as stats\
\
mu = 10.3\
sigma = 0.65\
lower_bound = 9.5\
upper_bound = 10.6\
\
z_score_lower = (lower_bound - mu) / sigma\
z_score_upper = (upper_bound - mu) / sigma\
\
percentage_between_9_5_and_10_6_cm = (stats.norm.cdf(z_score_upper) - stats.norm.cdf(z_score_lower)) * 100\
print(f"The percentage of lengths between 9.5cm and 10.6cm is approximately: \{percentage_between_9_5_and_10_6_cm:.2f\}%")\
}