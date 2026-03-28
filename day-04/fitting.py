import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar

exp_data = np.load('I_q_IPA_exp.npy')
mod_data = np.load('I_q_IPA_model.npy')

q_exp, I_exp = exp_data[:, 0], exp_data[:, 1]
q_mod, I_mod = mod_data[:, 0], mod_data[:, 1]

sort_idx = np.argsort(q_mod)
q_mod = q_mod[sort_idx]
I_mod = I_mod[sort_idx]
model_interp = interp1d(q_mod, I_mod, kind='linear', bounds_error=False, fill_value="extrapolate")
I_mod_at_q_exp = model_interp(q_exp)

valid_mask = ~np.isnan(I_mod_at_q_exp) & ~np.isnan(I_exp)
valid_I_exp = I_exp[valid_mask]
valid_I_mod = I_mod_at_q_exp[valid_mask]
def objective(scale):
    """Calculate the error between the scaled model and the experimental data."""
    residuals = valid_I_exp - (scale * valid_I_mod)
    return np.sum(residuals**2)

res = minimize_scalar(objective, bounds=(0, 100), method='bounded')
optimal_scale = res.x

print(f"Optimal scaling factor found: {optimal_scale:.4f}")
plt.figure(figsize=(8, 5))
plt.scatter(q_exp, I_exp, label='Experimental Data', color='black', s=15, alpha=0.6)
plt.plot(q_exp, optimal_scale * I_mod_at_q_exp, label=f'Scaled Model (factor={optimal_scale:.2f})', color='red', linewidth=2)

plt.title("Scattering Strength Fit Optimization")
plt.xlabel("Scattering Vector (q)")
plt.ylabel("Scattering Strength (I)")
plt.yscale('log') 
plt.legend()

ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.savefig('scattering_fit.png', dpi=300, bbox_inches='tight')
plt.show()