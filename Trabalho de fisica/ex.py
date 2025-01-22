import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do sistema
M = 1.0  # Massa (kg)
K = 10.0  # Constante da mola (N/m)
B = 0.5  # Coeficiente de amortecimento (N·s/m)
F_ext = 5.0  # Amplitude da força externa (N)
omega_ext = 1.5  # Frequência angular da força externa (rad/s)

# Condições iniciais
x0 = 1.0  # Posição inicial (m)
v0 = 0.0  # Velocidade inicial (m/s)

def solve_motion(t, type="simple"):
    """
    Resolve o movimento para diferentes tipos (simples, amortecido ou com força externa).
    
    Args:
        t: Array de tempos.
        type: Tipo de movimento ('simple', 'damped', 'forced').

    Returns:
        x: Array com a posição ao longo do tempo.
    """
    omega_0 = np.sqrt(K / M)  # Frequência natural (rad/s)
    gamma = B / (2 * M)  # Taxa de amortecimento

    if type == "simple":
        # Movimento Harmônico Simples
        A = x0
        phi = 0
        x = A * np.cos(omega_0 * t + phi)

    elif type == "damped":
        # Movimento Harmônico Amortecido
        A = x0
        x = A * np.exp(-gamma * t) * np.cos(np.sqrt(omega_0**2 - gamma**2) * t)

    elif type == "forced":
        # Movimento Harmônico com Força Externa
        omega_ext = 1.5  # Frequência da força externa
        A_ext = F_ext / np.sqrt((K - M * omega_ext**2)**2 + (B * omega_ext)**2)
        x_homog = x0 * np.exp(-gamma * t) * np.cos(np.sqrt(omega_0**2 - gamma**2) * t)
        x_partic = A_ext * np.cos(omega_ext * t)
        x = x_homog + x_partic

    else:
        raise ValueError("Tipo de movimento inválido. Use 'simple', 'damped' ou 'forced'.")

    return x

def plot_motion():
    """
    Plota os gráficos dos três tipos de movimento.
    """
    # Configuração de tempo
    t = np.linspace(0, 20, 1000)  # Intervalo de tempo (s)

    # Resolver os movimentos
    x_simple = solve_motion(t, type="simple")
    x_damped = solve_motion(t, type="damped")
    x_forced = solve_motion(t, type="forced")

    # Plotar os resultados
    plt.figure(figsize=(12, 8))

    # Movimento Harmônico Simples
    plt.subplot(3, 1, 1)
    plt.plot(t, x_simple, label="Harmônico Simples", color="blue")
    plt.title("Movimento Harmônico Simples")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid()

    # Movimento Harmônico Amortecido
    plt.subplot(3, 1, 2)
    plt.plot(t, x_damped, label="Harmônico Amortecido", color="orange")
    plt.title("Movimento Harmônico Amortecido")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid()

    # Movimento Harmônico com Força Externa
    plt.subplot(3, 1, 3)
    plt.plot(t, x_forced, label="Harmônico com Força Externa", color="green")
    plt.title("Movimento Harmônico com Força Externa")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição (m)")
    plt.grid()

    plt.tight_layout()
    plt.show()

# Comando para mostrar os gráficos
if __name__ == "__main__":
    plot_motion()
