import numpy as np
import matplotlib.pyplot as plt

def plot_constraints(constraints, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = np.linspace(y_range[0], y_range[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = np.zeros_like(X)
    
    for i, (A, b) in enumerate(constraints):
        if A[1] != 0:
            Y_constraint = (b - A[0]*X) / A[1]
        else:
            Y_constraint = np.full_like(X, b / A[0])
        plt.plot(x, Y_constraint, label=f'{A[0]}*x1 + {A[1]}*x2 <= {b}')
        Z += (A[0]*X + A[1]*Y <= b).astype(int)
    
    Z = Z == len(constraints)
    plt.contourf(X, Y, Z, levels=[0, 1], colors=['none', 'lightgrey'], alpha=0.5)
    plt.xlabel('$x_1$')
    plt.ylabel('$x_2$')
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.legend()

def plot_objective_function(c, x_range, y_range):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = np.linspace(y_range[0], y_range[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = c[0]*X + c[1]*Y
    plt.contour(X, Y, Z, levels=20, cmap='viridis')

def main():
    # Solicitar al usuario que ingrese las restricciones
    num_constraints = int(input("Ingrese el número de restricciones: "))
    constraints = []
    for _ in range(num_constraints):
        A1 = float(input("Ingrese el coeficiente de x1: "))
        A2 = float(input("Ingrese el coeficiente de x2: "))
        b = float(input(f"Ingrese el término independiente: "))
        constraints.append(([A1, A2], b))
    
    # Solicitar al usuario que ingrese la función objetivo
    c1 = float(input("Ingrese el coeficiente de x1 en la función objetivo: "))
    c2 = float(input("Ingrese el coeficiente de x2 en la función objetivo: "))
    c = [c1, c2]
    
    x_range = (0, 12)
    y_range = (0, 12)
    
    plt.figure(figsize=(10, 8))
    
    # Graficar las restricciones
    plot_constraints(constraints, x_range, y_range)
    
    # Graficar la función objetivo
    plot_objective_function(c, x_range, y_range)
    
    plt.title('Método gráfico para maximización')
    
    # Añadir el mensaje de resultado 
    plt.figtext(0.5, 0.92,
                "El gráfico muestra la región factible en gris\n"
                "y las líneas de nivel de la función objetivo.\n"
                "Busca el punto en la región factible que toca la\n"
                "línea de nivel más alta para encontrar el óptimo.",
                horizontalalignment='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))
    
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
