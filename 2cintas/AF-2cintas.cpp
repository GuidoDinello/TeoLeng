#include <sstream>
#include <iostream>
#include <unordered_map>
#include <set>
#include <tuple>

#define epsilon "\0"

using std::invalid_argument;
using std::stringstream;
using std::ostream;
using std::string;
using std::pair;
using std::tuple;
using std::get;
using std::unordered_map;
using std::set;
using std::cout;
using std::endl;

typedef pair<int, char> key;
typedef tuple< int, string, string> key2;
namespace std{
    template<>
    struct hash<key>{
        size_t operator()(const key& k) const {
            return hash<int>()( hash<int>()( k.first ) ^ hash<char>() (k.second));
        }
    };
    template<>
    struct hash<key2>{
        size_t operator()(const key2& k) const {
            return hash<int>()( hash<int>()(get<0>(k)) ^ hash<string>() (get<1>(k)) ^ hash<string>() (get<2>(k)) );
        }
    };
}


unordered_map<pair<int, char>, int> deltas;
int delta(int e, char simbolo){
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
unordered_map< tuple< int, string, string>, int> deltas_techo;
int delta_techo(int q, string w, string z){
    if (w == epsilon && z == epsilon) return q;
    else {
        // check if key=(q,w,z) was already calculated
        const auto it = deltas_techo.find({q, w, z});
        // if it was return value
        if (it != deltas_techo.end())
            return it -> second;
        // if it wasnt, calculate it
        else {
            // q belongs to Q2
            if (q >= 3) {
                // z = a.y
                string y = z.substr(1,z.length());
                char a = z[0];

                int d = delta(q,a);
                cout << "delta(" << q << "," << a << ")= " << d << std::endl;

                // save calculation
                deltas_techo[{q, w, z}] = delta_techo(delta(q,a),w,y);

            // q belongs to Q1
            } else {
                // w = a.x
                string x = w.substr(1,w.length());
                char a = w[0];

                int d = delta(q,a);
                cout << "delta(" << q << "," << a << ")= " << d << std::endl;

                // save calculation
                deltas_techo[{q, w, z}] = delta_techo(d,x,z);

            }
            return deltas_techo[{q,w,z}];
        }
    }
}
int init(int q0, pair<string, string> ent){
    return delta_techo(q0, get<0>(ent), get<1>(ent));
}

int main(){
    // M : (Q1,Q1,Σ,δ,F,q0)

    // δ: (Q1 U Q2) x Σ -> (Q1 U Q2)
    deltas = {
        {{0,'a'}, 3},
        {{3,'a'}, 4},
        {{3,'b'}, 0},
        {{4,'c'}, 1},
        {{1,'b'}, 1},
        {{1,'c'}, 5},
        {{5,'c'}, 2},
        {{2,'c'}, 5}
    };

    // δ^: (Q1 U Q2) x Σ* x Σ* -> (Q1 U Q2)
    deltas_techo = {};

    pair<string, string> ent = {"aaabbcc","bbaccc"};   
    int q0 = 0;          

    try {
        int sol = init(q0,ent);
        cout << "δ^(" << q0 << "," << get<0>(ent) << "," << get<1>(ent) << ") = " << deltas_techo[{q0,get<0>(ent),get<1>(ent)}] << std::endl;  
    } 
    catch (const invalid_argument& ex){
        cout << ex.what() << endl; 
    }

}