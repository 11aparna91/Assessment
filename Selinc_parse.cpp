#include <iostream>
#include <sstream>
#include <vector>

using namespace std;


vector<string> split (const string &s, char delim) { // considerend comma(,) as delimiter
    vector<string> result;
    stringstream ss (s);
    string item;

    while (getline (ss, item, delim)) {
        result.push_back (item);
    }
    return result;
}

void parse_parm(char const *input_str, string output_buffer, int index){
    vector<string> v = split (input_str, ',');
    int j=0;
    for (auto i : v) {   //iterating through vector v
        if (j==index){        // index matched
            output_buffer=i;
            cout<<output_buffer<<endl;
            break;
        }
        j = j+ 1;
    }
}

int main() {
    string output; 
    parse_parm("abc,123,4de5", output, 1);
    return 0;
}
