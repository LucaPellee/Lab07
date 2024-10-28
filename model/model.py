from database.meteo_dao import MeteoDao
class Model:
    def __init__(self):
        self._meteoDao = MeteoDao()

    def getUmidita(self, mese):
        return self._meteoDao.get_umidita(mese)
