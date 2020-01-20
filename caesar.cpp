// it is monoalphabetic substitution cipher
#include<bits/stdc++.h>
using namespace std;
int main(){
  string cipher="PHHW PH DIWHU WKH WRJD SDUWB"; // cipher text to decript
  for(int i=0;i<26;i++){                        // less secure bcoz it has only 25 possibility
      for(int j=0;j<cipher.length();j++){
          if(cipher[j]!=' '){
              int temp=cipher[j]-'A';
              cout<<char((temp+i)%26+'A');
            }
          else{
              cout<<" ";
            }
        }
        cout<<endl;
    }
}
