class ReservasiView:
	def printReservasiDetail(self, NamaPemesan, NRP, Tanggal, WaktuMulai, WaktuSelesai, resv, biaya):
		print('Pemesan : ' + NamaPemesan)
		print('NRP : '+ NRP)
		print('Tanggal : ' + Tanggal, WaktuMulai, '-', WaktuSelesai)
		print('Fasilitas : ' + str(resv))
		print('Biaya : ' + str(biaya))
		