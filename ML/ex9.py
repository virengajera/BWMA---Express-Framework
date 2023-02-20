import tensorflow as tf, numpy as np, sys, os ;

if __name__ == "__main__":

  # Tensor creation in TF  
  if sys.argv[1] == "1":
    ex1a = tf.range(0,100,2) ;
    print(ex1a) ;
    
    # multiply a column tensor (1,2,3)^T with a 2D tensor of ones
    ex1b = tf.reshape(tf.range(1,4,1, dtype=tf.float64), (3,1)) * tf.ones([3,3],dtype=tf.float64) ;
    print(ex1b) ;
    
    ex1c = tf.ones([3,5]) * 55 ;
    print(ex1c) ;
    
    ex1d = tf.random.uniform((5,4,3), 0, 1) ;
    print(ex1d) ;

  # Reshaping 1
  if sys.argv[1] == "2":
    # c,d are illegal bec they change size of tensor
    pass ;

  # Reshaping 2
  if sys.argv[1] == "3":
    x = tf.ones([10,20,3]) ;
    x = tf.reshape(x, (-1,300)) ; print (x.shape) ;
    x = tf.reshape(x, (300,1,1,1,-1)) ; print (x.shape) ;
    x = tf.reshape(x, (100,-1,1)) ; print (x.shape) ;
    x = tf.reshape(x, (50,2,-1,3)) ; print (x.shape) ;


  """
  # IRRELEVANT!!
  if sys.argv[1] == "4":
    traind = tf.random.uniform([2000,5,5], 0, 255) ;
    
    # 4a
    print("Sample nr 1000", traind[999]) ;
    print("Sample nr 1000, using tf.slice", 
      tf.slice(traind, (999, 0, 0), (1, 5, 5) )) ; # 20, 20
    
    # 4b
    z_sliced = tf.slice(traind, (9,0,0),(1,5,5)) ; # 20, 20
    z = traind[9]
    z = traind[9,:,:]    
    z = traind[9:10,0:5,0:5]
    print (tf.reduce_min(z), tf.reduce_max(z) ) ;
    
    # 4c
    z = traind[9] ;
    z1 = z[::2,:] ;
    z2 = z[::-1,::-1] ;
    z3 = z[::-2,::-2] ;
    """
                
  # A scalar-scalar function in TF 
  if sys.argv[1] == "5":
	  
      def f(x): # x is TF object
        return x + x**2 + x**3 ;
        
      print(f(tf.constant(0.0))) ; # f(0.) works as well
      print(f(tf.constant(1.0))) ;
      print(f(tf.constant(2.0)) ) ;
           
      with tf.GradientTape() as g:
        x1 = tf.Variable(-1.) ;
        y1 = f(x1) ;
        print("Value of y1 ==> ",y1) ;
     
      # f'(x) = 1 + 2x + 3x**2
      print ("Gradient ==> ",g.gradient(y1, x1)) ; # 2
    

  # A vector-scalar function in TF
  if sys.argv[1] == "6":
      def f(x): # assume x is a Tensor
        return tf.reduce_sum(x*x) ;
              
      with tf.GradientTape(persistent=True) as g:
        x1 = tf.constant([1.,2.,3.]) 
        x2 = tf.constant([2.,0.,2.]) 
        g.watch(x1)  
        g.watch(x2) 
        y1 = f(x1)
        y2 = f(x2) 
        
      print (g.gradient(y1, x1)) 
      print (g.gradient(y2, x2))
    

