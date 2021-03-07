import os
import numpy as np
import scipy.linalg as sp
import sys
import heapq

import Obj

class MeshSimplifier:
    v = []
    f = []

    # Contains list of valid edges.
    # The key represents the first vertex and the value contains a set
    # of which all vertices in the set are connected by an edge to the key vertex.
    e = None

    def __init__(self, v: list, f: list):
        self.v = v
        self.f = f
        self.build_edges_list()
        return

    # INFO: Each face only contains three edges so build an ADT representing
    # all possible edges.
    def build_edges_list(self):
        if self.e is None:
            self.e = dict()

        for face in self.f:
            # INFO: Add edge 0 to 1
            if face[0] in self.e:
                self.e[face[0]].add(face[1])
            else:
                self.e[face[0]] = {face[1]}

            # INFO: Add edge 1 to 0. Symmetrical to above.
            if face[1] in self.e:
                self.e[face[1]].add(face[0])
            else:
                self.e[face[1]] = {face[0]}

            # INFO: Add edge 0 to 2
            if face[0] in self.e:
                self.e[face[0]].add(face[2])
            else:
                self.e[face[0]] = {face[2]}

            # INFO: Add edge 2 to 0. Symmetrical to above.
            if face[2] in self.e:
                self.e[face[2]].add(face[0])
            else:
                self.e[face[2]] = {face[0]}

            # INFO: Add edge 1 to 2
            if face[1] in self.e:
                self.e[face[1]].add(face[2])
            else:
                self.e[face[1]] = {face[2]}

            # INFO: Add edge 2 to 1.  Symmetrical to above.
            if face[2] in self.e:
                self.e[face[2]].add(face[1])
            else:
                self.e[face[2]] = {face[1]}

        return

    # INFO: Each face only contains three edges so build an ADT representing
    # all possible valid edges. Valid meaning the vertices share anb edge and that
    # the norm of difference of the vertices is less then the threshold request.
    def build_valid_edges_list(self, threshold=0.0) -> list:
        valid_e = dict()
        for v1_idx in self.e:
            for v2_idx in self.e[v1_idx]:
                v1 = (v1_idx, np.array(self.v[v1_idx]))
                v2 = (v2_idx, np.array(self.v[v2_idx]))
                if self.is_valid_pair(v1, v2, threshold):
                    if v1_idx in valid_e:
                        valid_e[v1_idx].add(v2_idx)
                    else:
                        valid_e[v1_idx] = {v2_idx}
        return valid_e

    def is_valid_edge(self, vertex_a: (int, np.array), vertex_b: (int, np.array)) -> bool:
        # INFO: Check if vertex a has an edge to vertex b and vice versa.
        return (vertex_b[0] in self.e[vertex_a[0]]) and (vertex_a[0] in self.e[vertex_b[0]])

    def is_valid_pair(self, vertex_a: (int, np.array), vertex_b: (int, np.array), threshold=0.0) -> bool:
        v_norm = np.linalg.norm(vertex_a[1] - vertex_b[1])
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

        # TODO: Rewrite this to equal (p^T)(p) where p is the plane eqn vector.
        R1 = [a*a, a*b, a*c, a*d]
        R2 = [a*b, b*b, b*c, b*d]
        R3 = [a*c, b*c, c*c, c*d]
        R4 = [a*d, b*d, c*d, d*d]
        Kp = np.array([R1, R2, R3, R4])

        return Kp

    def calculate_vertex_contraction(self, Q: np.array) -> np.array:
        R1 = [Q[0][0], Q[0][1], Q[0][2], Q[0][3]]
        R2 = [Q[0][1], Q[1][1], Q[1][2], Q[1][3]]
        R3 = [Q[0][2], Q[1][2], Q[2][2], Q[2][3]]
        R4 = [0, 0, 0, 1]
        inv_M = numpy.linalg.inv(np.array([R1, R2, R3, R4]))
        V = [0, 0, 0, 1].reshape(4, 1)
        contracted_vertex = inv_M * V
        return contracted_vertex

    def simplify(self, threshold=0.0):
        # TODO: Implement.
        # TODO: Check for correctness.

        minimum_cost_pair_heap = []

        # INFO: 1. Compute Q for all faces.
        # INFO: face_plane_eqns: Key = Vertex, Value = Set of all plane eqns for that vertex.
        face_plane_eqns = dict()
        for face in self.f:
            vP = self.v[face[0]]
            vQ = self.v[face[1]]
            vR = self.v[face[2]]

            plane_eqn = self.triangle_to_plane([vP, vQ, vR])
            for i in range(0, 3):
                if face[i] in face_plane_eqns:
                    face_plane_eqns[face[i]].append(plane_eqn)
                else:
                    face_plane_eqns[face[i]] = [plane_eqn]

        # INFO: q_matrices: Key = Vertex, Value = Sum of all q matrices for that vertex.
        q_matrices = dict()
        for vertex in self.e:
            Q = np.identity(4)
            for plane_eqn in face_plane_eqns[vertex]:
                Q = Q + self.calculate_quadric_Kp(plane_eqn)
            q_matrices[vertex] = Q


        # TODO: 2. Select all valid edges.
        valid_e = self.build_valid_edges_list(threshold)
        for ve1, vlist in valid_e.items():
                for ve2 in vlist:
                    v1 = np.array(self.v[ve1])
                    v2 = np.array(self.v[ve2])
                    norm = np.linalg.norm(v1 - v2)
                    heapq.heappush(minimum_cost_pair_heap, (norm, [ve1, ve2]))

        print(minimum_cost_pair_heap)
        print(heapq.heappop(minimum_cost_pair_heap))

        # TODO: 3. Compute optimal vertex contraction for each vertex pair
        # TODO: 4.
        # TODO: 5.

        return None
