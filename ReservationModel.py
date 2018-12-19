class ReservasiModel:
	def __init__(self):
		self.__NamaPemesan = None
		self.__NRP = None
		self.__Tanggal = None
		self.__WaktuMulai = None
		self.__WaktuSelesai = None

	def setNamaPemesan(self, Name):		self.__NamaPemesan = Name
	def setNRP(self, NRP): 				self.__NRP = NRP
	def setTanggal(self, Tgl): 			self.__Tanggal = Tgl
	def setWaktuMulai(self, Waktu): 	self.__WaktuMulai = Waktu
	def setWaktuSelesai(self, Waktu): 	self.__WaktuSelesai = Waktu

	def getNamaPemesan(self): 			return self.__NamaPemesan
	def getNRP(self): 					return self.__NRP
	def getTanggal(self): 				return self.__Tanggal
	def getWaktuMulai(self): 			return self.__WaktuMulai
	def getWaktuSelesai(self): 			return self.__WaktuSelesai