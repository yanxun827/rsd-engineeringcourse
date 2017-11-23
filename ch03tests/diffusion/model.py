def energy(density, coeff=1.0):
  """ Energy associated with the diffusion model

      Parameters
      ----------

      density: array of positive integers
          Number of particles at each position i in the array
      coeff: float
          Diffusion coefficient.
  """
  # implementation goes here
  energy = 0
  for n_i in density:
  	if type(n_i) != int:
  		raise TypeError('Wrong type!')
  	energy += n_i * (n_i - 1)

  return energy