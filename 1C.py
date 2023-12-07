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
\
top_20_percentile_length = stats.norm.ppf(0.8, loc=mu, scale=sigma)\
print(f"The minimum length for the top 20% is approximately: \{top_20_percentile_length:.2f\}cm")\
}