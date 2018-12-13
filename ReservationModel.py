class ReservasiModel:
	def __init__(self):
		self.__NamaPemesan = None
		self.__NRP = None
		self.__Fasilitas = None
		self.__Tanggal = None
		self.__Waktu = None

	def setNamaPemesan(self, Name):
		self.__NamaPemesan = Name

	def setNRP(self, NRP):
		self.__NRP = NRP

	def setFasilitas(self, Fasilitas):
		self.__Fasilitas = Fasilitas

	def setTanggal(self, Tgl):
		self.__Tanggal = Tgl

	def setWaktu(self, Waktu):
		self.__Waktu = Waktu

	def getNamaPemesan(self):
		return self.__NamaPemesan

	def getNRP(self):
		return self.__NRP

	def getFasilitas(self):
		return self.__Fasilitas

	def getTanggal(self):
		return self.__Tanggal

	def getWaktu(self):
		return self.__Waktu

		