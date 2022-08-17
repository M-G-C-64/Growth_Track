from posixpath import split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


def plot(path,smoothness=True, type='line', sheet_name=None):
    if sheet_name:
        var = pd.read_excel(path, sheet_name=sheet_name)
    else:
        var = pd.read_excel(path)
    lst = list(var.columns.values)

    if smoothness and type == 'line':
        for i in (lst[1:]):
            #print(var['Date'][0], var['Date'][var.index[-1]])
            index = pd.date_range(var['Date'][0], var['Date'][var.index[-1]])
            df = pd.DataFrame(list(var[i]), index=index, columns=["values"])
            fig, axe = plt.subplots(1,1, figsize=(10,5))
            x = df.index
            y = df.values
            X_new = np.linspace(0, len(x), 300)
            spline1 = make_interp_spline(
                [j for j in range(0, len(x))],
                y,
                k=3
            )

            y_new = spline1(X_new)

            plt.plot(X_new, y_new, color='red')

            #plt.plot(var['Date'], var[i])
            plt.title(path)
            plt.ylabel(i)
            
            x = list(x.astype(str))
            plt.plot(x, y, linestyle=" ", alpha=0.75)
            xt = [x[i] for i in range(0,len(x),5)]
            plt.xticks(xt,rotation="vertical")

    else:
        for i in lst[1:]:
            var.plot(kind=type, x='Date', y=i)
            plt.title(path)
            plt.ylabel(i)
            plt.legend(lst[1:])
 
        
    plt.show()





plot('growth_log/career/problem_solving.xlsx', False, 'bar')
plot('growth_log/health/nofap.xlsx')
plot('growth_log/health/growth.xlsx')
plot('growth_log/personality/self_help.xlsx')


