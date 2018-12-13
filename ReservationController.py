import ReservationModel as rm
import ReservationView as rv

class ReservasiController:
	def __init__(self):
		self.__model = None
		self.__view = None

	def ReservasiController(self, model, view):
		self.__model = model
		self.__view = view

	def setNamaPemesan(self, Nama):
		self.__model.setNamaPemesan(Nama)

	def setNRP(self, NRP):
		self.__model.setNRP = NRP

	def setFasilitas(self, Fasilitas):
		self.__model.setFasilitas = Fasilitas

	def setTanggal(self, Tgl):
		self.__model.setTanggal = Tgl

	def setWaktu(self, Waktu):
		self.__model.setWaktu = Waktu

	def getNamaPemesan(self):
		return self.__model.getNamaPemesan()

	def getNRP(self):
		return self.__model.getNRP()

	def getFasilitas(self):
		return self.__model.getFasilitas()

	def getTanggal(self):
		return self.__model.getTanggal()

	def getWaktu(self):
		return self.__model.getWaktu()

	def list(self):
		self.__view.printReservasiDetail(self.__model.getNamaPemesan(),self.__model.getNRP(),self.__model.getFasilitas(),self.__model.getTanggal(),self.__model.getWaktu())

def R1():
	obj = rm.ReservasiModel()
	obj.setNamaPemesan('Marde Fasma')
	obj.setNRP('5116100046')
	obj.setFasilitas('Lapangan Basket')
	obj.setTanggal('12-12-2018')
	obj.setWaktu('19:00')
	return obj

fasmamodel = R1()
fasmaview = rv.ReservasiView()
fasmacontroller = ReservasiController()
fasmacontroller.ReservasiController(fasmamodel,fasmaview)
fasmacontroller.list()