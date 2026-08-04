# 1D Quantum Well Eigen Solver

---

## Description
This project contains a Python-based 1D Schrödinger equation solver for simulating quantum well heterostructures. Utilizing the `qmsolve` library alongside custom modules, the script calculates and visualizes the energy eigenstates and spatial potential of a user-defined single quantum well. It currently features built-in profiles for **hBN/MoS2** and **hBN/InSe** material systems. Feel free to modify and/or create your own profiles for whatever application.

---

## Features

* **Bias Effects:** Includes the effects of an applied bias on both the wavefunction of the electron and the quantum well barriers. Barriers and the wavefunction bend with the application of a bias.

* **Included Constants:** Includes a 'Contants.py' file with a large table of material and physical constants. Feel free to modify existing materials or add new ones. 

---

## Prerequisites
To run this simulation, you will need Python 3.x installed along with the following dependencies:
*   **qmsolve**: For setting up the Hamiltonian and visualizing eigenstates.
*   **numpy**: For array manipulations.
*   **matplotlib**: For potential well plotting.
*   **QW_Lib.py**: Custom local library handling the quantum well potential generation.
*   **Constants.py**: Custom local library containing material parameters.

You can install the required public packages via pip:
```bash
pip install -r requirements.txt
```

---

## Configuration & Usage
You can adjust the simulation conditions by editing the variables directly at the top of the main script:  
1. **Simulation Parameters:**  
    *    `bias`: Applied voltage across the well (in Volts).  
    *    `resolution`: The number of horizontal segments used to discretize the design.  
    *    `solved_states`: The number of eigen energy states to solve.  
    *    `probe`: The eigen energy state you want to probe.  
    *    `full`: If you want to solve outside of the quantum well, select True.  

2. **Material Selection:**  
    Change the `Selection` variable to toggle between predefined material stacks.  
    *    `0x01`: hBN/MoS2 heterostructure.  
    *    `0x02`: hBN/InSe heterostructure.  
    *    `0xXX`: Define your own stack.  

3. **Run the script:** Execute the Python file or Jupyter cell to generate the Hamiltonian array, compute the energy eigenstates, and output the visualizations.

---

## Adding Custom Materials
You can easily extend this simulation to model other heterostructures by following these steps:
1. **Define Material Constants:** Open `Constants.py` and add the required parameters for your new materials. You will typically need the following for each material:
    *    Electron Affinity ($EA$)  
    *    Effective Mass ($m^*$)  
    *    Monolayer Thickness  
    *    Bandgap (if calculating specific barrier heights)  
2. **Create a New Design Profile:** In your main script, assign a new hex value or ID (e.g., `0x03`) and add a new `elif` block under the `Selection` logic.
3. **Define the `params` Dictionary:** Populate the dictionary with your new constants. Ensure you map the variables for the conductor, left/right barriers, and the quantum well itself.
4. **Update the Selection:** Set the `Selection` variable to your new ID to run the simulation with your custom parameters.

---

## Technical Details
The script constructs the potential profile using electron affinities ($EA$), effective masses ($m^*$), and barrier thicknesses defined in monolayers (ML). The generated potential is normalized to Hartrees before being passed into the 1D Hamiltonian to match `qmsolve`'s internal unit expectations.By default, the simulation solves for a number of eigenstates and automatically plots the probability density of the ground state (`probe = 0`), alongside a secondary plot of the overarching physical potential well.

---

## Expected Output
When executed, the script will:
*    Print a 1D array of the calculated energy eigenvalues to the console.
*    Print the specific energy of the currently probed state.
*    Render two plots:
     1.    The spatial probability density/wavefunction of the selected eigenstate.
     2.    The physical band diagram/potential well structure based on the applied bias and resolution.

---

## License & Acknowledgments

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
* This project relies on [qmsolve](https://github.com/qmsolve/qmsolve), an open-source Python solver for the Schrödinger equation distributed under the MIT License.
