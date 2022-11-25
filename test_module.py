import os
import tarfile
import pandas as pd


def extract_data(name, where):
    datadir = os.path.join(where, name)
    if not os.path.exists(datadir):
        print("Extracting data ....")

        tar_path = os.path.join(where, name+'.tgz')
        with tarfile.open(tar_path, mode='r:gz') as data:
            data.extractall(where)


# extract_data('daily-stock', 'data')
df = pd.DataFrame({'C1': [10,11,12], 'C2': [20,21,22]},
                  index=[0,1,2])
df.to_hdf('store.hdf5', key='df', mode='w')
df = pd.read_hdf('store.hdf5')
print(df)
