
class c_variable(object):
    def __init__(self, line = "", nombre = "[ERROR]", valor = "[ERROR]"):
        l = line.split(" ")
        if len(l) >= 1 and l != [""]:
            self.nombre = l[0]
            self.valor = " ".join(l[1:])[:-1]
        else:
            self.nombre = nombre
            self.valor = valor

class reader(object):
    def readLines(self, conf_file):
        lines = []

        with open(conf_file, "r") as f:
            for line in f.readlines():
                l = line.split("#")[0].replace(" ","")
                if l == "" or l == "\n":
                    continue
                elif not "nv " in line:
                    continue
                else:
                    try:
                        lines.append(line.split("#")[0].split("nv ")[1])
                    except:
                        print("[Advertencia] error de sintaxis")
        return lines

    def readVariables(self, lines):
        variables = [ c_variable(line = l) for l in lines ]
        for idx, v in enumerate(variables):
            reps = 0
            for jdx, u in enumerate(variables):
                if jdx == idx:
                    break
                if u.nombre == v.nombre:
                    variables.pop(jdx)
        return variables

    def __init__(self, ejemplo_dir, nombre, ejemplo):
        self.variables = self.readVariables(self.readLines(ejemplo_dir + "/conf.LCM"))

        self.ejercicio = ["ej",".tex"]
        self.main = "main.tex"
        
        self.variables.insert(0, c_variable(nombre = "nombre", valor = nombre))
        self.variables.insert(0, c_variable(nombre = "ejemplo", valor = ejemplo))

        self.separador = '-'

            # Encuentra el valor del separador
        for v in self.variables:
            if v.nombre == "separador":
                self.separador = v.valor

        for idx, v in enumerate(self.variables):
            valor = v.valor.split(" + ")

            for i, palabra in enumerate(valor):
                if palabra[0] == "$":
                    for jdx, u in enumerate(self.variables):
                        if jdx >= idx:
                            break
                        if u.nombre == palabra[1:]:
                            valor[i] = u.valor

            v.valor = self.separador.join(valor)

            if v.nombre == "ejercicio":
                self.ejercicio = v.valor.split("<+>")
            elif v.nombre == "main":
                self.main = v.valor + ".tex"

if __name__ == '__main__':
    r = reader('/home/juamnito/Latex-Configuracion-Manual/Ejemplos/analisis-matematico-I', 'tarea1', 'analisis-matematico')
    for v in r.variables:
        print([v.nombre], [v.valor])
    print(r.main, r.ejercicio)
