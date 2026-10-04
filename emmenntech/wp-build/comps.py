"""Re-use Home's component functions on other pages: comps.use(b) rebinds them to a fresh builder."""
import b_home as HM
def use(b):
    HM.b = b; HM.e = b.el
    return HM
