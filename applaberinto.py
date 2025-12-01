import streamlit as st
import pandas as pd
from maze_solver import (
    MAZE, START, END,
    solve_maze_bfs,
    solve_maze_dfs,
    solve_maze_astar
)

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto 🧭")

MAX_WIDTH = len(str(max(row[0] for row in MAZE)))

# Función para renderizar el laberinto
def render_maze(maze, path=None):
    if path is None:
        path = []

    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []

        row_val = row[0]

        # Asegura que todas las filas tengan el MISMO ancho
        row_str = str(row_val).zfill(MAX_WIDTH)

        for c_idx, col in enumerate(row_str):

            if (r_idx, c_idx) == START:
                display_row.append("🚀")
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")
            elif (r_idx, c_idx) in path:
                display_row.append("🔹")
            elif col == "1":
                display_row.append("⬛")
            else:
                display_row.append("⬜")

        display_maze.append("".join(display_row))

    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)



# Sidebar de controles
st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox(
    "Selecciona el algoritmo",
    ["BFS", "DFS", "A*"]
)
solve_button = st.sidebar.button("Resolver Laberinto")

# Mostrar laberinto inicial
render_maze(MAZE)

# Resolver
if solve_button:
    if algorithm == "BFS":
        path, t = solve_maze_bfs(MAZE, START, END)

    elif algorithm == "DFS":
        path, t = solve_maze_dfs(MAZE, START, END)

    elif algorithm == "A*":
        path, t = solve_maze_astar(MAZE, START, END)

    # Mostrar resultados
    if path:
        st.success(f"¡Camino encontrado con {algorithm}! Tiempo: {t:.6f} s")
        render_maze(MAZE, path)
    else:
        st.error("No se encontró camino.")
