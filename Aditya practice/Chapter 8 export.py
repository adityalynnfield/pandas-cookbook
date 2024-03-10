import pandas as pd
popcon = pd.read_csv('../data/popularity-contest', sep=' ', )[:-1]
popcon.columns = ['atime', 'ctime', 'package-name', 'mru-program', 'tag']
popcon['atime'] = popcon['atime'].astype(int)
popcon['ctime'] = popcon['ctime'].astype(int)
popcon['atime'] = pd.to_datetime(popcon['atime'], unit='s')
popcon['ctime'] = pd.to_datetime(popcon['ctime'], unit='s')

popcon = popcon[popcon['atime'] > '1970-01-01']
nonlibraries = popcon[~popcon['package-name'].str.contains('lib')]
nonlibraries.sort_values('ctime', ascending=False)[:10]