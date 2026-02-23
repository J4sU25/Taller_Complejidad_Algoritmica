"""
=============================================================
  MÓDULO 1: EL RIGOR MATEMÁTICO (Criterio del Límite)
=============================================================
Fórmula: lim(n→∞) f(n)/g(n) = L
  Si L = 0  → f(n) = O(g(n))   [g crece más rápido]
  Si L = c  → f(n) = Θ(g(n))   [crecen igual]
  Si L = ∞  → g(n) = O(f(n))   [f crece más rápido]
=============================================================
"""

import math

# -------------------------------------------------------------
# Ejercicio 1.1 (Nivel Básico)
# Demuestra que f(n) = 7n² + 5n + 2 es de orden O(n²)
# -------------------------------------------------------------
# Demostración matemática:
#   lim(n→∞) (7n² + 5n + 2) / n²
#   = lim(n→∞) 7 + 5/n + 2/n²
#   = 7 + 0 + 0 = 7
#
# L = 7 (constante ≠ 0) → f(n) = Θ(n²), por lo tanto también O(n²)
# -------------------------------------------------------------

def ejercicio_1_1():
    print("--- Ejercicio 1.1: f(n) = 7n² + 5n + 2 es O(n²) ---")

    def f(n): return 7*n**2 + 5*n + 2
    def g(n): return n**2

    valores_n = [10, 100, 1000, 10_000, 100_000]
    print(f"{'n':>10} | {'f(n)':>15} | {'g(n)':>15} | {'L = f(n)/g(n)':>15}")
    print("-" * 62)
    for n in valores_n:
        L = f(n) / g(n)
        print(f"{n:>10} | {f(n):>15} | {g(n):>15} | {L:>15.6f}")

    print("\n✔ El límite tiende a 7 (constante ≠ 0)")
    print("✔ Por el criterio del límite: f(n) = Θ(n²) → también O(n²)\n")

# -------------------------------------------------------------
# Ejercicio 1.2 (Nivel Intermedio)
# Demuestra que ln(n) = O(n)
# -------------------------------------------------------------
# Demostración matemática:
#   lim(n→∞) ln(n) / n
#   Aplicando L'Hôpital (∞/∞):
#   = lim(n→∞) (1/n) / 1 = 0
#
# L = 0 → ln(n) = O(n)  [n crece más rápido que ln(n)]
# -------------------------------------------------------------

def ejercicio_1_2():
    print("--- Ejercicio 1.2: ln(n) = O(n) ---")

    def f(n): return math.log(n)   # ln(n)
    def g(n): return n

    valores_n = [10, 100, 1000, 10_000, 100_000]
    print(f"{'n':>10} | {'f(n)=ln(n)':>12} | {'g(n)=n':>12} | {'L = f(n)/g(n)':>15}")
    print("-" * 58)
    for n in valores_n:
        L = f(n) / g(n)
        print(f"{n:>10} | {f(n):>12.4f} | {g(n):>12} | {L:>15.8f}")

    print("\n✔ El límite tiende a 0")
    print("✔ Por el criterio del límite: ln(n) = O(n)")
    print("  (n crece MUCHO más rápido que ln(n))\n")

# -------------------------------------------------------------
# Ejercicio 1.3 (Nivel Avanzado)
# Determina la relación asintótica entre f(n) = n! y g(n) = 2^n
# ¿Cuál crece más rápido?
# -------------------------------------------------------------
# Demostración matemática:
#   lim(n→∞) n! / 2^n
#   n!/2^n = (1/2)(2/2)(3/2)(4/2)...(n/2)
#   Para n ≥ 3, cada factor k/2 ≥ 3/2 > 1 → el producto diverge a ∞
#
# L = ∞ → 2^n = O(n!)  [n! crece MÁS rápido que 2^n]
# -------------------------------------------------------------

def ejercicio_1_3():
    print("--- Ejercicio 1.3: ¿n! o 2^n crece más rápido? ---")

    def f(n): return math.factorial(n)
    def g(n): return 2**n

    valores_n = [5, 10, 15, 20, 25]
    print(f"{'n':>5} | {'f(n)=n!':>20} | {'g(n)=2^n':>15} | {'f(n)/g(n)':>15}")
    print("-" * 65)
    for n in valores_n:
        fn, gn = f(n), g(n)
        ratio = fn / gn
        print(f"{n:>5} | {fn:>20} | {gn:>15} | {ratio:>15.2f}")

    print("\n✔ El límite de n!/2^n tiende a INFINITO")
    print("✔ Conclusión: n! crece MÁS RÁPIDO que 2^n")
    print("✔ Por el criterio del límite: 2^n = O(n!)\n")


# -------------------------------------------------------------
# Punto de entrada
# -------------------------------------------------------------
if __name__ == "__main__":
    
    print("MÓDULO 1: RIGOR MATEMÁTICO")
    
    print()
    ejercicio_1_1()
    ejercicio_1_2()
    ejercicio_1_3()

    print("Módulo 1 completado")
