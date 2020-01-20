// to make more secure the ceasar cipher to 26! use substitution mathod
// in this mathod we use a any alphabet for any one so possibility is 26!

#include<bits/stdc++.h>
using namespace std;
int main(){
    string plaintext="defend the east wall of the castle";
    //Here key length is 26 who tell us that the every alphabet replace by other alphabet
    string key="phqgiumeaylnofdxjkrcvstzwb";
    for(int i=0;i<plaintext.length();i++){
        if(plaintext[i]==' ')
            continue;
        int temp=(plaintext[i]-'a');
        cout<<key[temp];
    }
    cout<<endl;
}
// Substitution cipher is not much secure because it can be creack by using the english frequiency
// But we can guess also that if a letter is repeated then its plain text also repeat that alphabet
