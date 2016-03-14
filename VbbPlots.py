import ROOT
from array import array
from collections import namedtuple
from itertools import combinations

from DPlot import DPlot

mu_pt_plot = DPlot("mu_pt", "muon p_{T} [MeV]", "mu_pt",
        range(0, 1000001, 25000),
        True) # include overflow


mu_eta_plot = DPlot("mu_eta", "muon #eta", "mu_eta",
        [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5],
        False) # no overflow

mu_phi_plot = DPlot("mu_phi", "muon #phi", "mu_phi",
        [-4, -3, -2, -1, 0, 1, 2, 3, 4],
        False) # no overflow

el_pt_plot = DPlot("el_pt", "electron p_{T} [MeV]", "el_pt",
        range(0, 1000001, 25000),
        True) # include overflow


el_eta_plot = DPlot("el_eta", "electron #eta", "el_eta",
        [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5],
        False) # no overflow

el_phi_plot = DPlot("el_phi", "electron #phi", "el_phi",
        [-4, -3, -2, -1, 0, 1, 2, 3, 4],
        False) # no overflow


lep_plots = [[mu_pt_plot], [mu_eta_plot], [mu_phi_plot],
             [el_pt_plot], [el_eta_plot], [el_phi_plot]
            ]


ljet0_pt_plot = DPlot("ljet0_pt", "leading large-R jet p_{T} [MeV]", "ljet_pt[0]",
        range(0, 1000001, 25000),
        True) # include overflow

ljet0_eta_plot = DPlot("ljet0_eta", "leading large-R jet #eta", "ljet_eta[0]",
        [-2.5, -2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5],
        False) # no overflow

ljet0_m_plot = DPlot("ljet0_m", "leading large-R jet mass [MeV]", "ljet_m[0]",
        range(0, 200001, 5000),
        False) # no overflow

ljet0_sd12_plot = DPlot("ljet0_sd12", "leading large-R jet #sqrt{d_{12}} [MeV]", "ljet_sd12[0]",
        range(0, 100001, 5000),
        False) # no overflow

ljet_plots = [[ljet0_pt_plot], [ljet0_eta_plot], [ljet0_m_plot], [ljet0_sd12_plot]]


met_met_plot = DPlot("met_met", "E_{T}^{miss} [MeV]", "met_met",
        range(0, 1000001, 25000),
        True) # include overflow

mu_plot = DPlot("mu", "<#mu>", "mu",
        range(0, 100, 5),
        True) # include overflow

event_plots = [[met_met_plot], [mu_plot]]

plots = lep_plots + ljet_plots + event_plots
