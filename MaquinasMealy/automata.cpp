#include <iostream>

using std::ostream;
using std::string;
using std::cout;
using std::endl;

typedef string estado;
typedef string salida;
typedef string sigma;
typedef string entrada;

estado delta(estado e, sigma simbolo){
    if (e == "q0")
        if (simbolo == "1") return string("q0");
        else return string("q1");
    else
        if (simbolo == "1") return string("q1");
        else return string("q0");
}

salida lambda(estado e, sigma simbolo){
    if (e == "q0") {
        if (simbolo == "1")  return string("P");
        else if (simbolo == "0")  return string("I");
        else return string("epsilon");
    } else {
        if (simbolo == "1") return string("I");
        else if (simbolo == "0") return string("P");
        else return string("epsilon");
    }
}

estado delta_techo(estado e, sigma entrada){
    if (entrada == "\0") return e;
    else {
        string a = string(1,entrada[entrada.length()-1]);
        string w = entrada.substr(0, entrada.length()-1);
        return delta( delta_techo(e, w), a );
    }
}

salida lambda_techo(estado e, sigma entrada){
    if (entrada == "\0") return string("");
    else {
        string a = string(1,entrada[entrada.length()-1]);
        string w = entrada.substr(0, entrada.length()-1);
        return lambda_techo(e,w) + lambda( delta_techo(e,w), a );
    }
}

salida init(estado q0, entrada ent){
    return lambda_techo(q0, ent);
}

int main(){
    entrada ent = "1001";
    salida sal = init("q0", ent);
    cout << sal << endl;
}