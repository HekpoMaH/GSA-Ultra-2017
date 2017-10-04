#include<bits/stdc++.h>
using namespace std;
int br=0;
bool check(int a1,int a2,int a3,int a4){
    if((a1==a3&&a2!=a1&&a3!=a4&&a3!=a2)||(a2==a4&&a1!=a2&&a2!=a3&&a3!=a4)||(a1==a4&&a2!=a1&&a3!=a4&&a2!=a3))
        return false;
    return true;
}
int main(){
    for(int i=1;i<=64;i++){
        for(int j=1;j<=64;j++){
            for(int k=1;k<=64;k++){
                for(int l=1;l<=64;l++){
                    //cout<<i<<" "<<j<<" "<<k<<" "<<l<<" "<<check(i,j,k,l)<<"\n";
                    if(!check(i,j,k,l))
                        br++;
                }
            }
        }
    }
    cout<<br<<"\n";
}
