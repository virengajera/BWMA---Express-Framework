import numpy as np ;
import requests ;
import os ;


class LinClass(object):

  ## allocate weight and bias arrays and store ref 2 train data/labels
  def __init__(self, n_in, n_out, X, T):
    self.W = np.ones([n_in,n_out]) * 0.1 ;
    self.b = np.ones([1,n_out])* 0.1 ;
    self.X = X ;
    self.T = T ;
    self.N = X.shape[0] ;
    
  # nomal cross-entropy loss. Fill in your code here!
  def loss(self, Y, T): 
    return - (np.log(Y) * T).sum(axis=1).mean() ;

  def dLdb(self,Y,T):
    return -(T-Y).mean(axis=0) ;

  # fill in your code here!
  def dLdW(self, X, Y, T):
    n_in, n_out = self.W.shape ;
    return -((T-Y).reshape(-1,1,n_out) *X.reshape(-1, n_in, 1)).mean(axis=0) ;
    
  # softmax: fill in your code here!
  def S(self,X):   # X is N,d
    e = np.exp(X) ;  # N,d
    row_sums = e.sum(axis = 1) ;   # (N, )
    row_sums_bc = row_sums.reshape(-1,1) ; # N,1
    #row_sums_bc = row_sums.reshape(2,1) ;  # less elegant bec. requires knowledge of rows in X
    
    return e / row_sums_bc;  # N,d / N,1 = N,d
       
  # dummy model, fill in your code!
  def f(self,X):
    return self.S (np.matmul(X, self.W) + self.b) ;

  # performs a single gradient descent step
  # works with any size of X and T
  def train_step(self, X, T, eps):
    Y = self.f(X) ;
    loss = self.loss(Y,T) ;
    dLdb = self.dLdb(Y,T) ;      
    dLdW = self.dLdW(X, Y, T) ;  
    self.b -= eps * dLdb ;       ## b(i+1) = b(i) - eps * gradL
    self.W -= eps * dLdW ;       ## same
    return loss ;

  # perform multiple gradient descent steps and display loss. Does it go down??
  def train(self,max_it,eps):
    for it in range(0,max_it):
      print ("iut=", it, "loss=", self.train_step(self.X, self.T, eps)) ;

if __name__ == "__main__":

  ## download MNIST if not present in current dir!
  if os.path.exists("./mnist.npz") == False:
    print ("Downloading MNIST...") ;
    fname = 'mnist.npz'
    url = 'http://www.gepperth.net/alexander/downloads/'
    r = requests.get(url+fname)
    open(fname , 'wb').write(r.content)
  
  ## read it into 
  data = np.load("mnist.npz")
  traind = data["arr_0"] ;
  trainl = data["arr_2"] ;
  traind = traind.reshape(60000,784)

  # your code from here!!
  N = 1000
  lc = LinClass(784,10,traind[0:N],trainl[0:N]) ;
  x = np.array([[-1,-1,5],[1,1,2.]]) ;
  y = lc.S(x) ;
  print("S is", lc.S(x)) ;
  print ("Checking S...", y.sum(axis=1))

  print ("f is ", lc.f(traind[0,:])) ;
  # small value added because log(0) will give a MathError
  Y_test = np.array([[0,0,0,0,0.5, 0,0.3, 0, 0.2,0,0]])+0.00000000001 ; 
  T_test = np.array([[0,0,0,0,1. , 0,0  , 0, 0  ,0,0]])
  print("Cross-Entropy", lc.loss(Y_test, T_test)) ;
  lc.train(100, 0.01) ;

      



