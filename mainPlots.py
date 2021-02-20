# mainPlots.py
# Plots of data for convergence and white dwarf star parameters.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def convergencePlots():
    # TODO decide if we want ticks, e.g. plusses
    # load in data
    E6nonRelativ = pd.read_csv("convergenceE6nonRelativ.csv")
    E6Relativ = pd.read_csv("convergenceE6Relativ.csv")
    E10nonRelativ = pd.read_csv("convergenceE10nonRelativ.csv")
    E10Relativ = pd.read_csv("convergenceE10Relativ.csv")
    E14nonRelativ = pd.read_csv("convergenceE14nonRelativ.csv")
    E14Relativ = pd.read_csv("convergenceE14Relativ.csv")   

    # mass, non relativistic
    # values to which result converges
    e6convM = sum(E6nonRelativ["massSolMass"][-3:])/3
    e10convM = sum(E10nonRelativ["massSolMass"][-3:])/3
    e14convM = sum(E14nonRelativ["massSolMass"][-3:])/3
    plt.set_cmap("Dark2")
    # plots of delta m / m_conv
    fig1 = plt.figure()
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["massSolMass"]-e6convM)/e6convM)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["massSolMass"]-e10convM)/e10convM)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["massSolMass"]-e14convM)/e14convM)
    plt.xscale("log")
    plt.xlabel("central density $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                 loc="upper right")
    plt.savefig("nonRelativMass.pdf")
    # second fig
    fig2 = plt.figure()
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["massSolMass"]-e6convM)/e6convM)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["massSolMass"]-e10convM)/e10convM)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["massSolMass"]-e14convM)/e14convM)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("central density $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                 loc="upper right")
    #plt.show()
    plt.savefig("nonRelativMassLog.pdf")

    # mass, relativistic
    # converged to values
    e6RconvM = sum(E6Relativ["massSolMass"][-3:])/3
    e10RconvM = sum(E10Relativ["massSolMass"][-3:])/3
    e14RconvM = sum(E14Relativ["massSolMass"][-3:])/3

    # plots of delta m / m_conv
    fig3 = plt.figure()
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["massSolMass"]-e6RconvM)/e6RconvM)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["massSolMass"]-e10RconvM)/e10RconvM)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["massSolMass"]-e14RconvM)/e14RconvM)
    plt.xscale("log")
    plt.xlabel("central density $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                 loc="upper right")
    plt.savefig("RelativMass.pdf")
    # log plot
    fig4 = plt.figure()
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["massSolMass"]-e6RconvM)/e6RconvM)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["massSolMass"]-e10RconvM)/e10RconvM)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["massSolMass"]-e14RconvM)/e14RconvM)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("central density $\\rho_\mathrm{C}$, $\mathrm{kg} \cdot \mathrm{m}^{-3}$")
    plt.ylabel("$\Delta M/M_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                 "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                 loc="upper right")
    plt.savefig("RelativMassLog.pdf")

    # radius, non relativistic
    # converged to values
    e6convR = sum(E6nonRelativ["radiusKM"][-3:])/3
    e10convR = sum(E10nonRelativ["radiusKM"][-3:])/3
    e14convR = sum(E14nonRelativ["radiusKM"][-3:])/3

    # plots of delta m / m_conv
    fig5 = plt.figure()
    plt.plot(E6nonRelativ["NoIter"], abs(E6nonRelativ["radiusKM"]-e6convR)/e6convR)
    plt.plot(E10nonRelativ["NoIter"], abs(E10nonRelativ["radiusKM"]-e10convR)/e10convR)
    plt.plot(E14nonRelativ["NoIter"], abs(E14nonRelativ["radiusKM"]-e14convR)/e14convR)
    plt.xscale("log")
    plt.xlabel("Number of iterations")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")
    plt.savefig("nonRelativRadius.pdf")
    # log plot
    fig6 = plt.figure()
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
    plt.savefig("nonRelativRadiusLog.pdf")

    # radius, relativistic
    # converged to values
    e6RconvR = sum(E6Relativ["radiusKM"][-3:])/3
    e10RconvR = sum(E10Relativ["radiusKM"][-3:])/3
    e14RconvR = sum(E14Relativ["radiusKM"][-3:])/3

    # plots of delta m / m_conv
    fig7 = plt.figure()
    plt.plot(E6Relativ["NoIter"], abs(E6Relativ["radiusKM"]-e6RconvR)/e6RconvR)
    plt.plot(E10Relativ["NoIter"], abs(E10Relativ["radiusKM"]-e10RconvR)/e10RconvR)
    plt.plot(E14Relativ["NoIter"], abs(E14Relativ["radiusKM"]-e14RconvR)/e14RconvR)
    plt.xscale("log")
    plt.xlabel("Number of iterations")
    plt.ylabel("$\Delta R/R_\mathrm{conv}$")
    plt.legend(["$\\rho_\mathrm{C} = 10^6$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{10}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$",
                    "$\\rho_\mathrm{C} = 10^{14}$ $\mathrm{kg} \cdot \mathrm{m}^{-3}$"],
                    loc="upper right")
    plt.savefig("RelativRadius.pdf")
    fig8 = plt.figure()
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
    plt.savefig("RelativRadiusLog.pdf")
    
def whiteDwarfPlots():
    kek = 1

def main():
    convergencePlots()
    whiteDwarfPlots()

if __name__ == "__main__":
    main()
