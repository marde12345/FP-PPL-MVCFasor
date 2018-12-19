import LapanganBasket as lb
import LapanganBuluTangkis as lbt
import LapanganFutsal as lf
import LapanganTennis as lt
import LapanganSepakBola as lsb

class ReservasiLapangan:
	def __init__(self):
		self.__resv = []
		self.__biaya = 0

	def getResv(self): return self.__resv
	def getBiaya(self): return self.__biaya

	def addLB(self, k):
		if k == 'AO':
			lap, cost = lb.LapanganBasket().AO()
		else :
			lap, cost = lb.LapanganBasket().BO()

		self.__resv.append(lap)
		self.__biaya += cost

	def addLBT(self, k):
		if k == 'AO':
			lap, cost = lbt.LapanganBuluTangkis().AO()
		elif k == 'BO':
			lap, cost = lbt.LapanganBuluTangkis().BO()
		elif k == 'AI':
			lap, cost = lbt.LapanganBuluTangkis().AI()
		else :
			lap, cost = lbt.LapanganBuluTangkis().BI()

		self.__resv.append(lap)
		self.__biaya += cost

	def addLF(self, k):
		if k == 'AI':
			lap, cost = lf.LapanganFutsal().AI()
		elif k == 'AO':
			lap, cost = lf.LapanganFutsal().AO()
		else:
			lap, cost = lf.LapanganFutsal().BO()

		self.__resv.append(lap)
		self.__biaya += cost

	def addLT(self, k):
		if k == 'AO':
			lap, cost = lt.LapanganTennis().AO()
		else:
			lap, cost = lt.LapanganTennis().BO()

		self.__resv.append(lap)
		self.__biaya += cost

	def addLSB(self, k):
		lap, cost = lsb.LapanganSepakBola().AO()

		self.__resv.append(lap)
		self.__biaya += cost

# def main():
# 	a = ReservationLapangan()
# 	a.addLBT('AI')
# 	a.addLB('AI')
# 	a.addLF('AO')
# 	a.addLT('AO')
# 	a.addLSB('AO')
# 	print(a.__dict__)

# if __name__ == "__main__":
#     main()