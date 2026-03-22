import pandas as pd
import polars as pl
import numpy as np
import time 

#comparing pandas vs polars, speed test on same processing task on same dataset
num_rows = 5_000_000
data = {
    "category": np.random.choice(["A", "B", "C", "D", "E"], num_rows),
    "value": np.random.rand(num_rows)
}

print("Dataset created with 5,000,000 rows. Starting the race...\n")

#===================================================================
#pandas
df_pandas=pd.DataFrame(data)
print(f"pandas_frame is :\n{df_pandas.head()}")
start_time=time.time()
pd_result=df_pandas.groupby('category')['value'].mean()
end_time=time.time()
print(f"pandas time is{end_time-start_time:0.5f} seconds")
print(f"pandas_result is:\n{pd_result.head()}")



#polars
df_pl=pl.DataFrame(data)
print(f"polars_frame is:\n{df_pl.head()}")
start_time=time.time()
pl_result=df_pl.group_by('category').agg(pl.col('value').mean())
end_time=time.time()
print(f"polars time is{end_time-start_time:0.5f} seconds")
print(f"polars_result is:\n{pl_result.head()}")


#conclusion
"""
- Reason 1: Polars is way faster than Pandas as a result of using multithreading (it utilizes all available CPU cores, whereas Pandas is strictly single-threaded).
- Reason 2: Written in Rust. It provides memory safety and C/C++ level performance, bypassing Python's performance bottlenecks.
- Reason 3: Apache Arrow memory format. Polars uses this format for zero-copy data manipulation, drastically reducing memory usage and processing time.
- Reason 4: No Index overhead. Polars drops the Pandas row index concept, which saves memory and eliminates the computational cost of maintaining an index during transformations.
"""