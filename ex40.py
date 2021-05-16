class lagu(object):

    def __init__(self,lirik):
        self.lirik = lirik

    def nyanyikan(self):
        for baris in self.lirik:
            print(baris)

ulangtahun = lagu(["Selamat ulang tahun", "dan bahagia",
                        "selamat panjang umur"])
panjangumur = lagu(["Panjang umurnya",
                    "serta mulia"])

ulangtahun.nyanyikan()
panjangumur.nyanyikan()
