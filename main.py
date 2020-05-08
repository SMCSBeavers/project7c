# Create list object with one string and assign variable.
alpha = ['original value']
print(alpha)
# Create new variable and assign that variable to the original list.
omega = alpha
# We will print to show that omega now has assigned object.
print(omega)
# Now we will add a new string to the new variable.
omega[1:] = ['added value']
# Now we should expect the new variable to have that value added.
print(omega)
# But through this added mutation, we have mutated the object, not just the variable.
print(alpha)

