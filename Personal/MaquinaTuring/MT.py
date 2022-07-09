
maquina_turing = {}

def arista(q_actual, lectura, pone, mueve, q_siguiente):
    maquina_turing[(q_actual, lectura)] = (pone, mueve, q_siguiente)


def simular(entrada, q_inicial):
    salida = entrada
    salida = "&&&&" + salida + "&&&&"

    i = 4

    q_actual = q_inicial
    while True:
        # if doesnt exist that edge then return
        print("q=", q_actual, salida[:i], salida[i], salida[i+1:], end=" ")
        if (q_actual, salida[i]) not in maquina_turing.keys():
            print("no existe key =", q_actual, salida[i])
            break
        # get the edge
        nuevo, direccion, q_actual  = maquina_turing[q_actual, salida[i]]
        print("poniendo",nuevo, "donde", salida[i], "pos", i, end=" ")
        # replace the letter
        salida = salida[:i] + nuevo + salida[i+1:]
        # move the pointer
        if direccion == 'I':
            i -= 1
        elif direccion == 'D':
            i += 1
        else:
            print("Error")
            break
        # print the new string
        print("------> q=", q_actual, salida)
    
    i=0
    while salida[i] == '&':
        print(salida[i], end="")
        i+=1
    print(" ", end="")
    while salida[i] != '&':
        print(salida[i], end="")
        i+=1
    print(" ", end="")
    while i < len(salida)-1:
        print(salida[i], end="")
        i+=1
    return ""
    

def main(entrada):
    arista('q0', '0', '0', 'D', 'q0')
    arista('q0', '1', '1', 'D', 'q0')
    arista('q0', '#', '#', 'D', 'q1')

    arista('q1', '1', 'X', 'I', 'q2')
    arista('q1', 'X', 'X', 'D', 'q1')
    arista('q1', '#', '&', 'I', 'q3')

    arista('q2', '#', '#', 'I', 'q2')
    arista('q2', 'X', 'X', 'I', 'q2')
    arista('q2', '1', '0', 'I', 'q2')
    arista('q2', '&', '1', 'D', 'q0')
    arista('q2', '0', '1', 'D', 'q0')

    arista('q3', '#', '&', 'I', 'q3')
    arista('q3', 'X', '&', 'I', 'q3')

    print(simular(entrada, 'q0'))

# write the main function entrance
if __name__ == '__main__':
    entrada = input("Ingrese la cadena a evaluar: ")
    main(entrada)



