# simple-random-limits-lifetime-model
The random limits are unknown variables in the lifetime model. Assume the random limits are uniform random variables, we can obtain the parameters of the lifetime model by using maximum likelihood estimation.
The lifetime model:
lnY = a + b ln(x-V) + e, where e ~ N(0, sigma^2), V ~ U(u0, u1), b<0, and 0 < u0 < V < u1 < x.
Let lnY = Y', Y' = a + b ln(x-V) + e
Hence, Y'|V = u ~ N(a+b ln(x-u), sigma^2), V ~ U(u0, u1).
(Y', V) ~ N(a+b ln(x-u), sigma^2)*U(u0, u1)
