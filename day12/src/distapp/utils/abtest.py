#create a/b test for two versoins of the web application
import random
def ab_test(user_id):
   #A is older version, B is newer version
   user_a=10000
   conversion_a=500
   user_b=10000
   conversion_b=600
   rate_a=conversion_a/user_a
   rate_b=conversion_b/user_b   
   pooled_rate=(conversion_a+conversion_b)/(user_a+user_b)
   standard_error=(pooled_rate*(1-pooled_rate)*(1/user_a+1/user_b))**0.5
   z_score=(rate_b-rate_a)/standard_error
   return z_score