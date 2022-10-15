import matplotlib.pyplot as plt


x = ["ACB", "ASW", "BEB", "CDX", "CEU", "CHB", "CHS", "CLM", "ESN", "FIN", "GBR", "GIH", "GWD", "IBS", "ITU", "JPT", "KHV", "LWK", "MSL", "MXL", "PEL", "PJL", "PUR", "STU", "TSI", "YRI"]
y = [123, 112, 144, 109, 183, 108, 171, 148, 173, 105, 107, 113, 180, 162, 118, 105, 124, 116, 128, 107, 130, 158, 150, 128, 112, 186]

plt.title("Distribuição de Amostras nas Populações", fontsize=25)
plt.xlabel("Poupulações",fontsize=20)
plt.ylabel("Quantidade de Amostras",fontsize=20)

plt.scatter(x,y)
plt.plot(x, y)

plt.show()


