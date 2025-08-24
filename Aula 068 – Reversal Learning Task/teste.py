import numpy as np

def switching(length=150, n_switches=9, intervalo_min=12, intervalo_max=18):
    assert intervalo_min * n_switches <= length <= intervalo_max * n_switches, "Impossível encaixar os switches."

    while True:
        # Amostra os primeiros n_switches - 1 intervalos
        primeiros = np.random.randint(intervalo_min, intervalo_max + 1, size=n_switches - 1)
        soma_parcial = primeiros.sum()
        ultimo = length - soma_parcial

        # Verifica se o último intervalo cabe
        if intervalo_min <= ultimo <= intervalo_max:
            intervalos = list(primeiros) + [ultimo]
            break

    cumulativos = np.cumsum(intervalos)
    switch = [False] * length
    for i in cumulativos:
        switch[i - 1] = True

    return switch

x = switching()
print(np.sum(x))
