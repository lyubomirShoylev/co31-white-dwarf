# mainPlots.py
# Plots of data for convergence and white dwarf star parameters.
from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def convergencePlots():
    # load in data
    E6nonRelativ = pd.read_csv("convergenceE6nonRelativ.csv")
    E6Relativ = pd.read_csv("convergenceE6Relativ.csv")
    E10nonRelativ = pd.read_csv("convergenceE10nonRelativ.csv")
    E10Relativ = pd.read_csv("convergenceE10Relativ.csv")
    E14nonRelativ = pd.read_csv("convergenceE14nonRelativ.csv")
    E14Relativ = pd.read_csv("convergenceE14Relativ.csv")   

    # subplot setup, tighter spacing
    f, axs = plt.subplots(4,2,figsize=(11.2,17.15),constrained_layout=False)

    # mass, non-relativistic
    # values to which result converges
    e6convM = sum(E6nonRelativ["massSolMass"][-3:])/3
    e10convM = sum(E10nonRelativ["massSolMass"][-3:])/3
    e14convM = sum(E14nonRelativ["massSolMass"][-3:])/3

    # plots of delta m / m_conv
    plt.subplot(4,2,1)
    plt.title("Non-relativistic case")
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["massSolMass"]-e6convM)/e6convM)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["massSolMass"]-e10convM)/e10convM)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["massSolMass"]-e14convM)/e14convM)
    plt.xscale("log")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$", "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$","$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"], loc="upper right")
    # second fig
    plt.subplot(4,2,3)
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["massSolMass"]-e6convM)/e6convM)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["massSolMass"]-e10convM)/e10convM)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["massSolMass"]-e14convM)/e14convM)
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$", "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$","$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"], loc="upper right")

    # mass, relativistic
    # converged to values
    e6RconvM = sum(E6Relativ["massSolMass"][-3:])/3
    e10RconvM = sum(E10Relativ["massSolMass"][-3:])/3
    e14RconvM = sum(E14Relativ["massSolMass"][-3:])/3

    # plots of delta m / m_conv
    plt.subplot(4,2,2)
    plt.title("Relativistic case")
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["massSolMass"]-e6RconvM)/e6RconvM)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["massSolMass"]-e10RconvM)/e10RconvM)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["massSolMass"]-e14RconvM)/e14RconvM)
    plt.xscale("log")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$", "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$","$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"], loc="upper right")
    # log plot
    plt.subplot(4,2,4)
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["massSolMass"]-e6RconvM)/e6RconvM)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["massSolMass"]-e10RconvM)/e10RconvM)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["massSolMass"]-e14RconvM)/e14RconvM)
    plt.xscale("log")
    plt.yscale("log")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$", "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$","$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"], loc="upper right")

    # radius, non relativistic
    # converged to values
    e6convR = sum(E6nonRelativ["radiusKM"][-3:])/3
    e10convR = sum(E10nonRelativ["radiusKM"][-3:])/3
    e14convR = sum(E14nonRelativ["radiusKM"][-3:])/3

    # plots of delta m / m_conv
    plt.subplot(425)
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["radiusKM"]-e6convR)/e6convR)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["radiusKM"]-e10convR)/e10convR)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["radiusKM"]-e14convR)/e14convR)
    plt.xscale("log")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")
    # log plot
    plt.subplot(427)
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["radiusKM"]-e6convR)/e6convR)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["radiusKM"]-e10convR)/e10convR)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["radiusKM"]-e14convR)/e14convR)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of iterations")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")

    # radius, relativistic
    # converged to values
    e6RconvR = sum(E6Relativ["radiusKM"][-3:])/3
    e10RconvR = sum(E10Relativ["radiusKM"][-3:])/3
    e14RconvR = sum(E14Relativ["radiusKM"][-3:])/3

    # plots of delta m / m_conv
    plt.subplot(426)
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["radiusKM"]-e6RconvR)/e6RconvR)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["radiusKM"]-e10RconvR)/e10RconvR)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["radiusKM"]-e14RconvR)/e14RconvR)
    plt.xscale("log")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")
    plt.subplot(428)
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["radiusKM"]-e6RconvR)/e6RconvR)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["radiusKM"]-e10RconvR)/e10RconvR)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["radiusKM"]-e14RconvR)/e14RconvR)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Number of iterations")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")

    # save fig, clip white margins to fit on report page with caption
    plt.savefig("convergencePlot.pdf", bbox_inches="tight")
    
def whiteDwarfPlots():
    # load data
    nonRres = pd.read_csv("nonRelativRes.csv")
    Rres = pd.read_csv("relativRes.csv")

    # fig 1 radius(rhoc)
    plt.figure()
    plt.plot(nonRres["rhoC"], nonRres["radiusKM"])
    plt.plot(Rres["rhoC"], Rres["radiusKM"])
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Central density, $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("Radius, km")
    plt.legend(["Non-relativistic", "Relativistic"])
    plt.savefig("radius-rhoC.pdf")

    # mass(rhoC)
    plt.figure()
    plt.plot(nonRres["rhoC"], nonRres["massSolMass"])
    plt.plot(Rres["rhoC"], Rres["massSolMass"])
    plt.axhline(1.434, c="grey", ls='--', lw=0.5)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Central density, $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("Mass, $M_\mathrm{sol}$")
    plt.legend(["Non-relativistic", "Relativistic", "Ch. Mass limit"])
    plt.savefig("mass-rhoC.pdf")

    # radius(mass)
    plt.figure()
    plt.plot(nonRres["massSolMass"], nonRres["radiusKM"])
    plt.plot(Rres["massSolMass"], Rres["radiusKM"])
    plt.axvline(1.434, c="grey", ls='--', lw=0.5)
    plt.xlim(0, 2.1)
    plt.ylim(0, 20000)
    plt.xlabel("Mass, $M_\mathrm{sol}$")
    plt.ylabel("Radius, km")
    plt.legend(["Non-relativistic", "Relativistic", "Ch. Mass limit"])
    plt.savefig("radius-mass.pdf")

def main():
    convergencePlots()
    whiteDwarfPlots()

if __name__ == "__main__":
    main()
