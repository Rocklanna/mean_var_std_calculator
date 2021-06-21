import numpy as np

def calculate(list):

  calculations=dict();

  if len(list)<9:
      raise ValueError("List must contain nine numbers.")
  else: 
      arr = np.array(list);
      newarr=arr.reshape(3,3);   
      calculations["mean"]=[np.mean(newarr,axis=0).tolist(),np.mean(newarr,axis=1).tolist(),np.mean(newarr)];
      calculations["variance"]=[np.var(newarr,axis=0).tolist(),np.var(newarr,axis=1).tolist(),np.var(newarr)];
      calculations["standard deviation"]=[np.std(newarr,axis=0).tolist(),np.std(newarr,axis=1).tolist(),np.std(newarr)];
      calculations["max"]=[np.max(newarr,axis=0).tolist(),np.max(newarr,axis=1).tolist(),np.max(newarr)];
      calculations["min"]=[np.min(newarr,axis=0).tolist(),np.min(newarr,axis=1).tolist(),np.min(newarr)];
      calculations["sum"]=[np.sum(newarr,axis=0).tolist(),np.sum(newarr,axis=1).tolist(),np.sum(newarr)];
      return calculations