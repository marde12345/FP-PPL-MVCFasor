import ReservationModel as rm
import ReservationView as rv
import Lapangan as lp

class ReservasiController:
	def __init__(self):
		self.modeluser = rm.ReservasiModel()
		self.view = rv.ReservasiView()
		self.modelresv = lp.ReservasiLapangan()

	def list(self):
		self.view.printReservasiDetail(self.modeluser.getNamaPemesan(),self.modeluser.getNRP(),self.modeluser.getTanggal(),self.modeluser.getWaktuMulai(),self.modeluser.getWaktuSelesai(),self.modelresv.getResv(),self.modelresv.getBiaya())

def main():
	fasma = ReservasiController()

	#ModelUser
	fasma.modeluser.setNamaPemesan('Marde Fasma')
	fasma.modeluser.setNRP('05111640000046')
	fasma.modeluser.setTanggal('12/12/2018')
	fasma.modeluser.setWaktuMulai('19:00')
	fasma.modeluser.setWaktuSelesai('20:00')

	#Decorator
	fasma.modelresv.addLF('AI')
	fasma.modelresv.addLT('AO')

	print(fasma.list())

if __name__ == "__main__":
    main()