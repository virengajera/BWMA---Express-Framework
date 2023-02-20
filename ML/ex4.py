import numpy as np ;
import sys ;

if sys.argv [1] == "1":
  #a)
  a = np.arange(0,101,2) # assume that 100 is included
  print (a) ;

  #b1) both solutions are equivalent
  b = np.array([[1,1,1],[2,2,2],[3,3,3]]) ;
  b = np.array([1,1,1,2,2,2,3,3,3]).reshape(3,3) ;
  print (b) ;

  #b2) principled solution for large arrays using broadcasting, 10x10 array
  rowCoeffs = np.arange(1,11,1) ; # create a 1d vector with entries from 1 to 3 included
  b2 = np.ones([10,10]) * rowCoeffs.reshape(10,1) ; #   !!
  print(b2) ;

  #c)
  c = np.ones([3,5]) * 55 ;

  #d) 
  d = np.random.uniform(0,1,(5,4,3)) ;
  print (d)
  d = np.random.uniform(0,1,60).reshape(5,4,3);
  print (d) ;

if sys.argv [1] == "2":
  # stack of 2D images of dimensions 20x20
  traind = np.random.uniform(0,255,[2000,20,20]) ;
  #a)
  a = traind[999,:,:] ;
  a = traind[999] ;    # equivalent!
  print (a.shape, a.ravel().shape)

  #b) set topmost and lowermost rows to 0
  # rows
  a[0:5,:] = 0 ;
  a[15:,:] = 0 ;
  """
  # columns, exercise was not totally clear
  a[:, 0:5] = 0 ;
  a[:, 15:] = 0 ;
  """
  #c) 
  # slice out sample/image nr 10
  c = traind[9] ;
  print ("minmax=", c.min(), np.max(c)) ;

  #d)
  d1 = c[::2, :] # or c[::2]
  d2 = c[ :, ::2] ; 
  d3 = c[::-1, ::-1] 
  d4 = c[::-2, ::-2]

  #f) # in-place
  traind *= -1 ;  
  traind +=  1 ;
  # BAD: copy created and original array is discarded
  traind = 1-traind ;

if sys.argv [1] == "3":
  # stack of 2D images of dimensions 20x20
  traind = np.random.uniform(0,255,[2000,20,20]) ;
  #a)
  a = np.sum(traind[:,0,0]) ;
  #b)
  b = np.mean(traind[:,0,0]) ;
  #c) 
  c = np.mean(traind,axis=0)
  #d)
  d = traind.max(axis=2) ;
  #e)
  e = traind.sum(axis=2) ;

if sys.argv [1] == "4":
  vec = np.arange(1,21,1) ;
  #a)
  traind += vec.reshape(1,1,20) ;
  #b) 
  traind += vec.reshape(1,20,1) ;
  #c)
  traind += traind[0].reshape(1,20,20) ;

if sys.argv [1] == "5":
  vec = np.arange(1,21,1) ;
  #a)
  smaller = vec[(vec<10)] ;
  print ("smaller", smaller) ;
  #b) 
  vec[[1,5,19]] = 0 ;
  print(vec) ;