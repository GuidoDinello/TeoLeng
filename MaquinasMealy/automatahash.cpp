#include <sstream>
#include <iostream>
#include <unordered_map>

#define epsilon "\0"

using std::ostream;
using std::invalid_argument;
using std::string;
using std::stringstream;
using std::pair;
using std::unordered_map;
using std::make_pair;
using std::cout;
using std::endl;


typedef int estado;
typedef char sigma;
typedef string sigma_aster;
typedef char t_delta;
typedef string delta_aster;

typedef string entrada;
typedef string salida;

typedef std::pair<estado, sigma> key;
typedef std::pair<estado, sigma_aster> key_aster;

namespace std{
    template<>
    struct hash<key>{
        size_t operator()(const key& k) const {
            return hash<int>()( hash<int>()( k.first ) ^ hash<char>() (k.second));
        }
    };

    template<>
    struct hash<key_aster>{
        size_t operator()(const key_aster& k) const {
            return hash<int>()( hash<int>()( k.first ) ^ hash<string>() (k.second));
        }

    };
}

unordered_map<key, estado> deltas;
unordered_map<key, t_delta> lambdas;
unordered_map<key_aster, estado> deltas_t;
unordered_map<key_aster, delta_aster> lambdas_t;

estado delta(estado e, sigma simbolo){
    const auto it = deltas.find({e, simbolo});
    if (it != deltas.end())
        return it -> second;
    else {
        stringstream err;
        err << "ERROR: no existe delta asociado a (" << e << "," << simbolo << ")";
        throw invalid_argument(err.str());
        return 0;
    }
}
salida lambda(estado e, sigma simbolo){
    const auto it = lambdas.find({e, simbolo});
    if (it != lambdas.end())
        return string(1,it -> second);
    else {
        stringstream err;
        err << "ERROR: no existe lambda asociado a (" << e << "," << simbolo << ")";
        throw invalid_argument(err.str());
        return 0;
    }
}
estado delta_techo(estado e, sigma_aster entrada){
    if (entrada == epsilon) return e;
    else {
        sigma_aster w = entrada.substr(0,entrada.length()-1);
        sigma a = entrada[entrada.length()-1];
        return delta( delta_techo(e, w), a);
    }
}
salida lambda_techo(estado e, sigma_aster entrada){
    if (entrada == epsilon) return epsilon;
    else {
        sigma_aster w = entrada.substr(0,entrada.length()-1);
        sigma a = entrada[entrada.length()-1];
        return lambda_techo(e, w) + lambda( delta_techo(e, w), a);
    }
}

salida init(estado q0, entrada ent){
    return lambda_techo(q0, ent);
}

int main(){
    deltas = {
        {{0,'1'}, 0},
        {{0,'0'}, 1},
        {{1,'0'}, 0},
        {{1,'1'}, 1}
    };

    lambdas = {
        {{0,'1'}, 'P'},
        {{0,'0'}, 'I'},
        {{1,'0'}, 'P'},
        {{1,'1'}, 'I'}      
    };

    entrada ent = "1001";

    try {
        cout << init(0,ent) << endl;
    } 
    catch (const invalid_argument& ex){
        cout << ex.what() << endl; 
    }

}