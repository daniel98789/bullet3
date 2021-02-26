import os
import numpy as np
import scipy.linalg as sp
import sys
import Obj

class MeshSimplifier:
    a = []

    def __init__(self):
        return

    def is_valid_edge(self, model: Obj, vertex_a: (int, np.array), vertex_b: (int, np.array)) -> bool:
        # TODO(nicholas): Implement.
        # INFO: And edge is valid if va and vb are part of the same face.
        return True

    def is_valid_pair(self, model: Obj, vertex_a: (int, np.array), vertex_b: (int, np.array), threshold=0.0) -> bool:
        v_norm = np.norm(vertex_a[1] - vertex_b[1])
        return self.is_valid_edge(vertex_a, vertex_b) and (v_norm < threshold)

    def triangle_to_plane(self, tri_v) -> np.array:
        # INFO: Points that form triangle PQR.
        P = tri_v[0]
        Q = tri_v[1]
        R = tri_v[2]

        # INFO: Build matices needed to solve Ax = B.
        # A = [R1, R2, R3, R4]
        #   R1 to R3 are constraints for a, b, c and d.
        #   R4 is unique constraint that a^2 + b^2 + c^2 + 0d = 1
        # B = [1, 1, 1, 0]^T
        #   This vector is the solution coefficients to constraints above.
        #   It is always [1, 1, 1, 0].
        R1 = P + [-1]
        R2 = Q + [-1]
        R3 = R + [-1]
        R4 = [0, 0, 0, 1]
        A = np.array([R1, R2, R3, R4])
        B = np.array([0, 0, 0, 1]).reshape(4, 1)

        # INFO: Solve Ax = B, to find a, b, c, and d.
        # INFO: Since A is sqaure we can use the trivial solve() method to find
        # Ax = B.
        sol = sp.solve(A, B)
        return sol

    def calculate_quadric_Kp(self, plane_eqn: np.array) -> np.array:
        # INFO: Points that form triangle PQR.
        a = plane_eqn[0]
        b = plane_eqn[1]
        c = plane_eqn[2]
        d = plane_eqn[3]

        R1 = [a*a, a*b, a*c, a*d]
        R2 = [a*b, b*b, b*c, b*d]
        R3 = [a*c, b*c, c*c, c*d]
        R4 = [a*d, b*d, c*d, d*d]
        Kp = np.array([R1, R2, R3, R4])

        return Kp

    def evalulate_plane_vertices_against_quadric(self, tri_v):
        return

    def simplify(self, model: Obj):
        # TODO: Implement.

        # TODO: 1. Compute Q for all faces.
        # TODO: 2. Select all valid edges.
        # TODO: 3. Compute optimal vertex contraction for each vertex pair
        # TODO: 4.
        # TODO: 5.

        return None
