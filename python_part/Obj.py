import os

class Obj:
    filename = ""
    v = []
    group_faces = dict()
    group_smoothing = dict()

    def __init__(self, fn):
        self.filename = os.getcwd()+fn
        return
    
    def smaller(self):
        print("FILENAME IS" + self.filename)
        with open(self.filename) as fp:
            line = fp.readline()
            last_group = None
            while line:
                vs = line.split()

                # INFO: Group: Name statements are used to organize collections of
                # elements and simplify data manipulation for operations in the model.
                if (len(vs) >= 2) and (vs[0] == "g"):
                    last_group = (vs[1])
                    self.group_faces[last_group] = []

                # INFO: Smoothing: Sets the smoothing group for the elements that follow it.
                # Not sure if needed? This may be useful if two groups have a shared egde.
                if (last_group != None) and (len(vs) == 2) and (vs[0] == "s"):
                    smoothing = int(vs[1])
                    self.group_smoothing[last_group] = smoothing

                # INFO: Vertex: Specifies a vertex by its three coordinates plus w. 
                if (len(vs) >= 3) and (vs[0] == "v"):
                    self.v.append([(float(vs[i])/100)+0.5 for i in range(1,4)])

                # INFO: Ignore vn and vt for know. Used for texture coordinations/normals
                # which a render engine would use but porbably not physics.

                # INFO: Faces: Using v, vt, and vn to represent geometric vertices, texture vertices, and vertex normals, the statement would read:
                # f v/vt/vn v/vt/vn v/vt/vn v/vt/vn
                # 3 vertices per face = triangle
                # 4 vertices per face = square
                if (len(vs) >= 1) and (vs[0] == "f"):
                    # INFO: If there is no g group specified assume a default group.
                    if last_group == None:
                        last_group = 'default'
                        self.group_faces[last_group] = []

                    # INFO: Parse and store triangle.
                    if (len(vs) == 4):
                        tri = []
                        for i in range(1,4):
                            if '/' in vs[i]:
                                tri.append(int(vs[i][:vs[i].index("/")]) - 1)
                            else:
                                tri.append(int(vs[i]) - 1)
                        self.group_faces[last_group].append(tri)

                    # INFO: Parse square, split into triangles and store triangles.
                    if (len(vs) == 5):
                        # INFO: Split into triangles for storage.
                        # TODO: Not sure if bullet proof. Test later.
                        tri_upper = []
                        tri_lower = []
                        for i in range(1,4):
                            tri_upper = None
                            if '/' in vs[i]:
                                tri_upper.append(int(vs[i][:vs[i].index("/")]) - 1)
                            else:
                                tri_upper.append(int(vs[i]) - 1)
                        for i in range(1,4):
                            tri_lower = None
                            if '/' in vs[i]:
                                tri_lower.append(int(vs[i][:vs[i].index("/")]) - 1)
                            else:
                                tri_lower.append(int(vs[i]) - 1)
                        self.group_faces[last_group].append(tri_upper)
                        self.group_faces[last_group].append(tri_lower)

                line = fp.readline()

        return self.v