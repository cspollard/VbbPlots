from DProps import *
import ROOT
import re

sampdict = {}

# data
sampdict["DATA"] = DSampleProps("data", DLine(ROOT.kBlack, 0, 0),
        DMarker(ROOT.kBlack, 20, 1), DFill(ROOT.kBlack, 0))

# signal

sampdict["SMVH"] = DSampleProps("SM VH", DLine(ROOT.kGray+1, 1, 3),
        DMarker(ROOT.kGray+1, 0, 0), DFill(ROOT.kGray+1, 0))


# default style for signals:
for m in xrange(500, 6001, 100):
    n = "HVT%0.1fTEVRES" % (m / 1000.0)
    t = "%0.1f TeV HVT" % (m / 1000.0)
    sampdict[n] = DSampleProps(t, DLine(ROOT.kGray+3, 1, 3),
            DMarker(ROOT.kGray+3, 0, 0), DFill(ROOT.kGray+3, 0))

sampdict["HVT1.0TEVRES"] = DSampleProps("1.0 TeV HVT", DLine(ROOT.kAzure, 1, 3),
        DMarker(ROOT.kAzure, 0, 0), DFill(ROOT.kAzure, 0))

sampdict["HVT1.6TEVRES"] = DSampleProps("1.6 TeV HVT", DLine(ROOT.kGreen+3, 1, 3),
        DMarker(ROOT.kGreen+3, 0, 0), DFill(ROOT.kGreen+3, 0))

sampdict["HVT2.0TEVRES"] = DSampleProps("2.0 TeV HVT", DLine(ROOT.kBlack, 1, 3),
        DMarker(ROOT.kBlack, 0, 0), DFill(ROOT.kBlack, 0))


# backgrounds
sampdict["TTBAR"] = DSampleProps("t#bart", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kOrange, 0, 0), DFill(ROOT.kOrange, 1001))

sampdict["TTBARBB"] = DSampleProps("t#bar{t} (bb)", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kOrange, 0, 0), DFill(ROOT.kOrange, 1001))

sampdict["TTBARBC"] = DSampleProps("t#bar{t} (bc)", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kOrange+1, 0, 0), DFill(ROOT.kOrange+1, 1001))

sampdict["TTBARLF"] = DSampleProps("t#bar{t} (other)", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kOrange+2, 0, 0), DFill(ROOT.kOrange+2, 1001))

sampdict["WJETS"] = DSampleProps("W+jets", DLine(ROOT.kBlack, 1, 1),
        DMarker(92, 0, 0), DFill(92, 1001))

sampdict["WB"] = DSampleProps("W+b", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kGreen + 4, 0, 0), DFill(ROOT.kGreen + 4, 1001))

sampdict["WC"] = DSampleProps("W+c", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kGreen + 1, 0, 0), DFill(ROOT.kGreen + 1, 1001))

sampdict["WL"] = DSampleProps("W+lf", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kGreen - 9, 0, 0), DFill(ROOT.kGreen - 9, 1001))

sampdict["ZJETS"] = DSampleProps("Z+jets", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kOrange+5, 0, 0), DFill(ROOT.kOrange+5, 1001))

sampdict["ZB"] = DSampleProps("Z+b", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kAzure+3, 0, 0), DFill(ROOT.kAzure+3, 1001))

sampdict["ZC"] = DSampleProps("Z+c", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kAzure - 4, 0, 0), DFill(ROOT.kAzure - 4, 1001))

sampdict["ZL"] = DSampleProps("Z+lf", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kAzure - 9, 0, 0), DFill(ROOT.kAzure - 9, 1001))

sampdict["DIBOSON"] = DSampleProps("diboson", DLine(ROOT.kBlack, 1, 1),
        DMarker(5, 0, 0), DFill(5, 1001))

sampdict["SINGLETOP"] = DSampleProps("single top", DLine(ROOT.kBlack, 1, 1),
        DMarker(ROOT.kYellow+2, 0, 0), DFill(ROOT.kYellow+2, 1001))

sampdict["QCD"] = DSampleProps("QCD", DLine(ROOT.kBlack, 1, 1),
        DMarker(619, 0, 0), DFill(619, 1001))

# other
sampdict["OTHER"] = DSampleProps("other", DLine(ROOT.kBlack, 1, 1),
        DMarker(619, 0, 0), DFill(619, 1001))



def getprocess(dsid):
    if dsid == 0:
        return "DATA"

    # ttbar
    elif 410000 <= dsid <= 410003:
        return "TTBAR"

    # L/C/B
    hflab = {1 : "L", 2 : "C", 0 : "B"}[dsid % 3]

    # Wenu
    if 361300 <= dsid <= 361323:
        return "W" + hflab

    # Wmunu
    elif 361324 <= dsid <= 361347:
        return "W" + hflab

    # Wmunu
    elif 361348 <= dsid <= 361371:
        return "W" + hflab

    # Zee
    elif 361372 <= dsid <= 361395:
        return "Z" + hflab

    # Zmumu
    elif 361396 <= dsid <= 361419:
        return "Z" + hflab

    # Ztautau
    elif 361420 <= dsid <= 361443:
        return "Z" + hflab

    # Znunu
    elif 361444 <= dsid <= 361462:
        return "Z" + hflab

    return "OTHER"



def fix_style(samp, h):
    t, l, m, f = sampdict[getprocess(samp.mcchanno)]
    h.SetTitle(t)
    setline(h, l)
    setmarker(h, m)
    setfill(h, f)

    return h


# order of histograms on plots
# (top to bottom)
orderlist = map(lambda x: sampdict[x].title,
        ["ZJETS", "ZB", "ZC", "ZL",
        "WJETS", "WB", "WC", "WL",
        "TTBAR", "TTBARBB", "TTBARBC", "TTBARLF",
        "SINGLETOP", "DIBOSON", "QCD", "OTHER"]
        )


orderdict = dict(map(reversed, enumerate(reversed(orderlist))))

# custom ordering for histograms
def histordering(h1, h2):
    return cmp(orderdict.get(h1.GetTitle(), -1),
            orderdict.get(h2.GetTitle(), -1))
