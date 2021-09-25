# ibm-quantum-challenge-africa-2021--solutions

The IBM Research Lab in South Africa and Wits University have developed a quantum computing challenge showcasing how the technology can be used in the fields of medicine, finance, and logistics. With a focus on problems relevant to Africa for African learners, students, and industry members; the challenge highlights the amazing opportunities available to grow the necessary expertise and communities on the continent. Learn more at the Challenge repo.

# Lab1: Introduction and the Crop-Yield Problem.

![](https://user-images.githubusercontent.com/70172995/134530559-a27f5dc1-6ebe-43c9-852b-1b0e5f8079a2.png)

The notebook is structured as follows:

 1-Initialization

 2-Table of Contents

 3-Qiskit and its parts

 4-Setting up the Qiskit Environment

 5-Quadratic Problems

Some computational problems can be formulated into quadratic equations such that the minimum of the quadratic equations is the optimal solution, if any exist. These problems are encountered in finance, agriculture, operations and production management, and economics.

Quadratic programming is also used to identify an optimal financial portfolio with minimum risk and optimizing the layout of production components in a factory to minimize the travel distance of resources. This notebook focuses on agriculture as it is a relevant application of quantum computing to problems facing the African continent. However, all of these applications share two common characteristics: the system can be modelled as a quadratic equation and the system variables may be constrained, with their values limited to within a given range.

6-Crop-Yield Problem as a Quadratic Problem

To show how to solve your quadratic program using a quantum computer, we will use two algorithms to solve the crop-yield problem. It is a common need to optimize the crops and management of a farm to reduce risk while increasing profits. One of the big challenges facing Africa and the whole world is how to produce enough food for everyone. The problem here focuses not on profits but on the tonnage of crops harvested. Imagine you have a farm with three hectares of land suitable for farming. You need to choose which crops to plant from a selection of four. Furthermore, you also need to determine how many hectares of each you should plant. The four crops you can plant are wheat, soybeans, maize, and a push-pull crop. The fourth cannot be sold once harvested but it can help increase the yield of the other crops.

 7-Solving the Crop-Yield Problem using Quantum Computing

 8-Simulating a Real Quantum Computer for the Crop-Yield Problem

# Lab2: Quantum speedups in finance.

![](https://user-images.githubusercontent.com/70172995/134542720-da08e36f-500f-4ec6-958e-de070ad5b122.png)

The world of finance is a complicated one to model and predict. The financial markets, in particular, are influenced by so many external factors and contain multiple different investors with different objectives. This means that traditional modelling techniques, like multiple linear regression, often struggle when trying to explain investors' behaviours or perform certain tasks in finance, such as predicting the price of a stock. Due to these complexities, we need more sophisticated models and numerous techniques have been proposed to produce such robust models for financial instruments like stocks.

In Africa, the dynamics of the financial markets are arguably even more complicated. In this notebook, we discuss what types of financial instruments we can encounter in the South African market, particularly those that are liquid (meaning they are frequently traded and accurately valued). Illiqid instruments are also prevalent in Africa and are more difficult to evaluate and price, since they are not often traded.

Here, we introduce a common pricing technique for a particular instrument called an option. This technique rests on Monte Carlo sampling which we show can achieve a quadratic speed up in pricing the option by replacing the classical Monte Carlo sampling approach with a quantum algorithm that leverages quantum effects to compute things faster.

In this challenge we will gain the following skills:

 1-Understand the basics of how financial instruments are typically priced using Monte Carlo methods

 2-Implement a quantum algorithm to price a financial instrument (in this case, we consider derivative contracts called options)

 3-Understand the pros/cons of using the quantum approach


# Lab3: Quantum Chemistry for HIV.

![](https://user-images.githubusercontent.com/70172995/134550503-57e14400-2f08-46b8-9a4d-6a6a3f34dd48.png)

HIV is a virus that has presented an immense challenge for public health, globally. The ensuing disease dynamics touch on multiple societal dimensions including nutrition, access to health, education and research funding. To compound the difficulties, the virus mutates rapidly with different strains having different geographic footprints. In particular, the HIV-1-C and HIV-2 strains predominate mostly in Africa. Due to disparities in funding, research for treatments of the African strains lags behind other programmes. African researchers are striving to address this imbalance and should consider adding the latest technologies such as quantum computing to their toolkits.

Quantum computing promises spectacular improvements in drug-design. In particular, in order to design new anti-retrovirals it is important to perform chemical simulations to confirm that the anti-retroviral binds with the virus protein. Such simulations are notoriously hard and sometimes ineffective on classical supercomputers. Quantum computers promise more accurate simulations allowing for a better drug-design workflow.

In detail: anti-retrovirals are drugs that bind with and block a virus protein, called protease, that cleaves virus polyproteins into smaller proteins, ready for packaging. The protease can be thought of as a chemical scissor. The anti-retroviral can be thought of as a sticky obstacle that disrupts the ability of the scissor to cut. With the protease blocked, the virus cannot make more copies of itself.

Mutations in the viral protease changes the binding propensity of a given anti-retroviral. Hence, when a mutation occurs and an anti-retroviral no longer binds well, the goal becomes to adjust the anti-retroviral molecule to again bind strongly.

The main goal of this challenge is to explore whether a toy anti-retroviral molecule binds with a toy virus protease.

Along the way, this challenge introduces state-of-the-art hybrid classical-quantum embedded chemistry modelling allowing the splitting of the work-load between classical approximations and more accurate quantum calculations.

Finally, you need to tweak the setup of the quantum chemistry algorithm (without having to understand the nuts and bolts of quantum computing) to achieve the best performance for ideal quantum computing conditions.

# Introduction

 Step 1 : Defining the Molecular Geometry

 Step 2 : Calculating the Qubit Hamiltonian

 Step 2a: Constructing the Fermionic Hamiltonion

 Step 2b: Getting Ready to Convert to a Qubit Hamiltonian

 Step 3 : Setting up the Variational Quantum Eigensolver (VQE)

 Step 3a: The V in VQE (i.e. the Variational form, a Trial state)

 Step 3b: The Q in VQE: the Quantum environment

 Step 3c: Initializing VQE

 Step 4 : Solving for the Ground-state

# The HIV Challenge

 1. Refining Step 1: Varying the Molecule

 2. Refining Step 2: Reducing the quantum workload

 3. Refining Step 4: Energy Surface

 4. Refining Step 3a

# Exercises

 Exercise 3a: Molecular Definition of Macromolecule with Blocking Approach

 Exercise 3b: Classical-Quantum Treatment Conceptual Questions (Multiple-Choice)

 Exercise 3c: Energy Landscape, To bind or not to bind?

 Exercise 3d: The effect of more repetitions

 Exercise 3e: Open-ended: Find the best hardware_inspired_trial to minimize the Energy Error for the Macromolecule

# Thanks, IBM, Amira Abbas african_mentor for well-prepared notebooks. Looking forward to the next Quantum Challenge! :)

![image](https://user-images.githubusercontent.com/78730355/134781418-010238a4-2792-4092-8059-afcd4c086e87.png)
)
