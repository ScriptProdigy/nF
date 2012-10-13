
class GSI:
    def __init__(self, GaiaZomgLib):
        self.GaiaZomgLib = GaiaZomgLib

    def fetch_gsi(self, m, v="json"):
        return self.GaiaZomgLib.HTTP.Req(self.GaiaZomgLib.GaiaConstants.GSI + "?X=0&v=" + str(v) + "&m=" + str(m))

    def get_gsid(self):
        Page = self.fetch_gsi(v="sushi", m="109")
        Split1 = Page.rsplit(chr(5))
        Split2 = Split1[len(Split1)-1].rsplit(chr(1))
        return Split2[len(Split2)-1]